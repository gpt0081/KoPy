"""Command-line interface for KoPy."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import PYTHON_BASELINE, __version__
from .config import set_spelling_enabled, spelling_enabled
from .runtime import read_source, run_file
from .spelling import find_spelling_hints
from .translator import translate

_COMMANDS = {"run", "check", "translate", "learn", "spelling", "version"}


def _configure_utf8_console() -> None:
    """Make Korean CLI output safe on Windows and frozen executables."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is None:
            continue
        try:
            reconfigure(encoding="utf-8", errors="replace")
        except (OSError, ValueError):
            pass


def _add_spelling_option(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--spelling",
        action=argparse.BooleanOptionalAction,
        default=None,
        help="이번 실행에서 스펠링 힌트를 켜거나 끕니다.",
    )


def _resolve_spelling(value: bool | None) -> bool:
    return spelling_enabled() if value is None else value


def _print_hints(source: str, enabled: bool) -> None:
    if not enabled:
        return
    for hint in find_spelling_hints(source):
        print(hint.format(), file=sys.stderr)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="kopy",
        description="KoPy - Python 문법을 그대로 배우는 한글 음역 호환 레이어",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    run_parser = sub.add_parser("run", help="KoPy/Python 파일을 실행합니다.")
    _add_spelling_option(run_parser)
    run_parser.add_argument("file", help="실행할 .kpy 또는 .py 파일")
    run_parser.add_argument("script_args", nargs=argparse.REMAINDER, help="스크립트에 전달할 인자")

    check_parser = sub.add_parser("check", help="실행하지 않고 문법을 검사합니다.")
    _add_spelling_option(check_parser)
    check_parser.add_argument("file")

    translate_parser = sub.add_parser("translate", help="KoPy를 표준 Python 코드로 변환해 보여줍니다.")
    translate_parser.add_argument("file")

    learn_parser = sub.add_parser("learn", help="사용한 KoPy 단어와 실제 Python 표현을 함께 보여줍니다.")
    learn_parser.add_argument("file")

    spelling_parser = sub.add_parser("spelling", help="기본 스펠링 힌트 설정을 변경합니다.")
    spelling_parser.add_argument("state", choices=("on", "off", "status"))

    sub.add_parser("version", help="KoPy와 기준 Python 버전을 표시합니다.")
    return parser


def _normalize_argv(argv: list[str]) -> list[str]:
    # `kopy hello.kpy` is shorthand for `kopy run hello.kpy`.
    if argv and argv[0] not in _COMMANDS and not argv[0].startswith("-"):
        return ["run", *argv]
    return argv


def _cmd_run(args: argparse.Namespace) -> int:
    enabled = _resolve_spelling(args.spelling)
    source = read_source(args.file)
    _print_hints(source, enabled)

    script_args = list(args.script_args)
    if script_args and script_args[0] == "--":
        script_args = script_args[1:]

    # Hints were already emitted before execution, so avoid scanning twice.
    run_file(args.file, spelling=False, script_args=script_args)
    return 0


def _cmd_check(args: argparse.Namespace) -> int:
    enabled = _resolve_spelling(args.spelling)
    source = read_source(args.file)
    _print_hints(source, enabled)
    translation = translate(source)
    compile(translation.python, str(Path(args.file)), "exec")
    print(f"KoPy 검사 완료: {args.file}")
    return 0


def _cmd_translate(args: argparse.Namespace) -> int:
    source = read_source(args.file)
    print(translate(source).python, end="")
    return 0


def _cmd_learn(args: argparse.Namespace) -> int:
    source = read_source(args.file)
    result = translate(source)

    print("[KoPy → Python 대응]")
    seen: set[tuple[str, str]] = set()
    if not result.replacements:
        print("사용된 한글 음역 토큰이 없습니다. 이 파일은 일반 Python으로 그대로 실행됩니다.")
    else:
        for korean, english, line, column in result.replacements:
            pair = (korean, english)
            if pair in seen:
                continue
            seen.add(pair)
            print(f"{korean:<12} → {english:<12} (처음 사용: {line}:{column})")

    print("\n[표준 Python 변환 결과]")
    print(result.python, end="")
    return 0


def _cmd_spelling(args: argparse.Namespace) -> int:
    if args.state == "status":
        print("ON" if spelling_enabled() else "OFF")
        return 0

    enabled = args.state == "on"
    set_spelling_enabled(enabled)
    print(f"KoPy 스펠링 힌트: {'ON' if enabled else 'OFF'}")
    return 0


def _cmd_version() -> int:
    runtime = ".".join(str(part) for part in sys.version_info[:3])
    print(f"KoPy {__version__}")
    print(f"기준 Python: {PYTHON_BASELINE}")
    print(f"현재 실행 Python: {runtime}")
    return 0


def main(argv: list[str] | None = None) -> int:
    _configure_utf8_console()
    raw_argv = list(sys.argv[1:] if argv is None else argv)
    parser = _build_parser()
    args = parser.parse_args(_normalize_argv(raw_argv))

    try:
        if args.command == "run":
            return _cmd_run(args)
        if args.command == "check":
            return _cmd_check(args)
        if args.command == "translate":
            return _cmd_translate(args)
        if args.command == "learn":
            return _cmd_learn(args)
        if args.command == "spelling":
            return _cmd_spelling(args)
        if args.command == "version":
            return _cmd_version()
    except FileNotFoundError as exc:
        print(f"KoPy 오류: 파일을 찾을 수 없습니다: {exc.filename}", file=sys.stderr)
        return 2
    except PermissionError as exc:
        print(f"KoPy 오류: 파일을 읽을 권한이 없습니다: {exc.filename}", file=sys.stderr)
        return 2
    except SyntaxError as exc:
        location = f"{exc.filename}:{exc.lineno}:{exc.offset}" if exc.filename else "문법"
        print(f"KoPy 문법 오류 [{location}] {exc.msg}", file=sys.stderr)
        if exc.text:
            print(exc.text.rstrip(), file=sys.stderr)
        return 1

    parser.error("알 수 없는 명령입니다.")
    return 2
