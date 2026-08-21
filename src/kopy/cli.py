"""Command-line interface for KoPy."""

from __future__ import annotations

import argparse
import json
import sys
from difflib import get_close_matches
from pathlib import Path

from . import PYTHON_BASELINE, __version__
from .config import set_spelling_enabled, spelling_enabled
from .editor import diagnose_source, info_payload, words_payload
from .education import explain_source, syntax_lesson
from .packs.registry import (
    pack_by_name,
    pack_members_payload,
    packs_payload,
    resolve_pack_member,
)
from .runtime import read_source, run_file
from .spelling import SpellingHint, find_spelling_hints
from .translator import to_kopy, translate
from .words import PY_TO_KO, WORDS, info_for

_COMMANDS = {
    "run", "check", "translate", "learn", "spelling", "version",
    "words", "diagnose", "info", "help", "to-kopy", "convert-python", "explain",
    "packs", "libraries",
}


def _configure_utf8_console() -> None:
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


def _collect_hints(source: str, enabled: bool) -> tuple[SpellingHint, ...]:
    return find_spelling_hints(source) if enabled else ()


def _print_hints(hints: tuple[SpellingHint, ...]) -> None:
    for hint in hints:
        print(hint.format(), file=sys.stderr)


def _print_spelling_stop_message() -> None:
    print("", file=sys.stderr)
    print("KoPy: 영문 스펠링 오류가 의심되어 실행을 중단했습니다.", file=sys.stderr)
    print("코드를 수정한 뒤 다시 실행하세요.", file=sys.stderr)
    print("검사를 무시하고 실행하려면 --no-spelling 옵션을 사용하거나", file=sys.stderr)
    print("'kopy spelling off'로 기본 스펠링 검사를 끌 수 있습니다.", file=sys.stderr)


def _print_json(payload: object) -> None:
    print(json.dumps(payload, ensure_ascii=False, separators=(",", ":")))


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="kopy",
        description="KoPy - Python 문법을 그대로 배우는 한글 음역 호환/학습 레이어",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    run_parser = sub.add_parser("run", help="KoPy/Python 파일을 실행합니다.")
    _add_spelling_option(run_parser)
    run_parser.add_argument("file", help="실행할 .kpy 또는 .py 파일")
    run_parser.add_argument("script_args", nargs=argparse.REMAINDER, help="스크립트에 전달할 인자")

    check_parser = sub.add_parser("check", help="실행하지 않고 문법을 검사합니다.")
    _add_spelling_option(check_parser)
    check_parser.add_argument("file")

    translate_parser = sub.add_parser("translate", help="KoPy를 표준 Python 코드로 변환합니다.")
    translate_parser.add_argument("file")

    reverse_parser = sub.add_parser(
        "to-kopy",
        aliases=["convert-python"],
        help="Python 코드를 KoPy 학습 표현으로 변환합니다.",
    )
    reverse_parser.add_argument("file")
    reverse_parser.add_argument("-o", "--output", help="변환 결과를 저장할 파일. 생략하면 화면에 출력합니다.")

    help_parser = sub.add_parser("help", help="KoPy 단어 또는 라이브러리 API를 설명합니다.")
    help_parser.add_argument("word", help="예: 프린트, print, np.어레이, numpy.array")

    explain_parser = sub.add_parser("explain", help="코드를 실행하지 않고 흐름을 한국어로 설명합니다.")
    explain_parser.add_argument("file")

    learn_parser = sub.add_parser("learn", help="사용한 KoPy 단어와 Python 표현을 함께 보여줍니다.")
    learn_parser.add_argument("file")

    spelling_parser = sub.add_parser("spelling", help="기본 스펠링 힌트 설정을 변경합니다.")
    spelling_parser.add_argument("state", choices=("on", "off", "status"))

    words_parser = sub.add_parser("words", help="KoPy의 공식 Core 단어 등록부를 표시합니다.")
    words_parser.add_argument("--json", action="store_true", help="편집기용 JSON으로 출력합니다.")

    packs_parser = sub.add_parser(
        "packs",
        aliases=["libraries"],
        help="KoPy 라이브러리 팩과 설치 상태를 표시합니다.",
    )
    packs_parser.add_argument("name", nargs="?", help="상세히 볼 팩 이름. 예: numpy")
    packs_parser.add_argument("--json", action="store_true", help="JSON으로 출력합니다.")

    diagnose_parser = sub.add_parser("diagnose", help="KoPy Core 규칙으로 편집기용 진단을 생성합니다.")
    diagnose_parser.add_argument("file", nargs="?", help="검사할 .kpy/.py 파일")
    diagnose_parser.add_argument("--stdin", action="store_true", help="파일 대신 표준 입력 소스를 검사합니다.")
    diagnose_parser.add_argument("--json", action="store_true", help="편집기용 JSON으로 출력합니다.")

    info_parser = sub.add_parser("info", help="KoPy 런타임 정보를 표시합니다.")
    info_parser.add_argument("--json", action="store_true", help="편집기용 JSON으로 출력합니다.")

    sub.add_parser("version", help="KoPy와 기준 Python 버전을 표시합니다.")
    return parser


def _normalize_argv(argv: list[str]) -> list[str]:
    if argv and argv[0] not in _COMMANDS and not argv[0].startswith("-"):
        return ["run", *argv]
    return argv


def _cmd_run(args: argparse.Namespace) -> int:
    enabled = _resolve_spelling(args.spelling)
    source = read_source(args.file)
    hints = _collect_hints(source, enabled)
    _print_hints(hints)
    if hints:
        _print_spelling_stop_message()
        return 1

    compile(translate(source).python, str(Path(args.file)), "exec")
    script_args = list(args.script_args)
    if script_args and script_args[0] == "--":
        script_args = script_args[1:]
    run_file(args.file, spelling=False, script_args=script_args)
    return 0


def _cmd_check(args: argparse.Namespace) -> int:
    enabled = _resolve_spelling(args.spelling)
    source = read_source(args.file)
    hints = _collect_hints(source, enabled)
    _print_hints(hints)
    compile(translate(source).python, str(Path(args.file)), "exec")
    if hints:
        print(f"KoPy 검사: 스펠링 오류 의심 {len(hints)}개", file=sys.stderr)
        return 1
    print(f"KoPy 검사 완료: {args.file}")
    return 0


def _cmd_translate(args: argparse.Namespace) -> int:
    print(translate(read_source(args.file)).python, end="")
    return 0


def _cmd_to_kopy(args: argparse.Namespace) -> int:
    result = to_kopy(read_source(args.file)).kopy
    if args.output:
        Path(args.output).write_text(result, encoding="utf-8")
        print(f"KoPy 변환 완료: {args.output}")
    else:
        print(result, end="")
    return 0


def _resolve_help_word(word: str) -> str | None:
    if word in WORDS:
        return word
    return PY_TO_KO.get(word)


def _cmd_help(args: argparse.Namespace) -> int:
    pack_match = resolve_pack_member(args.word)
    if pack_match is not None:
        pack, info = pack_match
        alias = pack.preferred_aliases[0] if pack.preferred_aliases else pack.module
        print(f"{alias}.{info.kopy} → Python {pack.module}.{info.python}")
        print(f"팩: {pack.name}")
        print(f"설명: {info.description}")
        if info.kopy_example:
            print("\nKoPy 예제:")
            print(info.kopy_example)
        if info.python_example:
            print("\nPython 예제:")
            print(info.python_example)
        return 0

    kopy_word = _resolve_help_word(args.word)
    if kopy_word is None:
        candidates = list(WORDS) + list(PY_TO_KO)
        matches = get_close_matches(args.word, candidates, n=3, cutoff=0.5)
        print(f"KoPy 도움말: '{args.word}' 단어를 찾지 못했습니다.", file=sys.stderr)
        if matches:
            print("비슷한 Core 단어: " + ", ".join(matches), file=sys.stderr)
        print("라이브러리 API는 'kopy help np.어레이'처럼 조회할 수 있습니다.", file=sys.stderr)
        return 1

    info = info_for(kopy_word)
    if info is None:
        return 1
    print(f"{info.kopy} → Python {info.python}")
    print(f"분류: {info.category}")
    print(f"설명: {info.description}")
    if info.kopy_example:
        print("\nKoPy 예제:")
        print(info.kopy_example)
    if info.python_example:
        print("\nPython 예제:")
        print(info.python_example)
    return 0


def _cmd_packs(args: argparse.Namespace) -> int:
    if args.name:
        pack = pack_by_name(args.name)
        if pack is None:
            print(f"KoPy 팩 오류: '{args.name}' 팩을 찾지 못했습니다.", file=sys.stderr)
            return 1
        payload = pack_members_payload(pack)
        if args.json:
            _print_json(payload)
            return 0
        state = "설치됨" if payload["installed"] else "Python 라이브러리 미설치"
        print(f"[{pack.name}] {pack.kopy_module} → {pack.module}")
        print(f"상태: {state}")
        print(f"설명: {pack.description}")
        print(f"등록 API: {len(payload['members'])}개")
        for item in payload["members"]:
            print(f"  {item['kopy']:<18} → {item['python']:<22} {item['description']}")
        return 0

    payload = packs_payload()
    if args.json:
        _print_json(payload)
        return 0
    print("[KoPy 라이브러리 팩]")
    for item in payload["packs"]:
        state = "✅ 설치됨" if item["installed"] else "○ 라이브러리 미설치"
        print(
            f"{item['name']:<12} {state}  "
            f"{item['kopy_module']} → {item['module']}  API {item['member_count']}개"
        )
    return 0


def _cmd_explain(args: argparse.Namespace) -> int:
    source = read_source(args.file)
    print(f"[KoPy 코드 설명: {args.file}]")
    for index, step in enumerate(explain_source(source, str(Path(args.file))), start=1):
        print(f"{index}. {step}")
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
            print(f"{korean:<16} → {english:<18} (처음 사용: {line}:{column})")
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


def _cmd_words(args: argparse.Namespace) -> int:
    payload = words_payload()
    if args.json:
        _print_json(payload)
        return 0
    for entry in payload["words"]:
        print(f"{entry['kopy']:<18} → {entry['python']:<22} [{entry['category']}] {entry['description']}")
    return 0


def _cmd_diagnose(args: argparse.Namespace) -> int:
    if args.stdin:
        source = sys.stdin.read()
        filename = args.file or "<stdin>"
    else:
        if not args.file:
            raise ValueError("diagnose에는 파일 경로 또는 --stdin이 필요합니다.")
        source = read_source(args.file)
        filename = str(Path(args.file))
    payload = diagnose_source(source, filename)
    if args.json:
        _print_json(payload)
    else:
        for item in payload["diagnostics"]:
            print(f"{item['line']}:{item['column']} [{item['severity']}] {item['message']}")
            if item.get("lesson"):
                print(f"  학습 힌트: {item['lesson']}")
            if item.get("suggestion"):
                print(f"  수정 제안: {item['suggestion']}")
        if payload["ok"]:
            print("KoPy 진단 완료: 문제 없음")
    return 0 if payload["ok"] else 1


def _cmd_info(args: argparse.Namespace) -> int:
    payload = info_payload()
    if args.json:
        _print_json(payload)
        return 0
    print(f"KoPy {payload['kopy_version']}")
    print(f"기준 Python: {payload['python_baseline']}")
    print(f"현재 실행 Python: {payload['runtime_python']}")
    return 0


def _cmd_version() -> int:
    runtime = ".".join(str(part) for part in sys.version_info[:3])
    print(f"KoPy {__version__}")
    print(f"기준 Python: {PYTHON_BASELINE}")
    print(f"현재 실행 Python: {runtime}")
    return 0


def _print_syntax_lesson(exc: SyntaxError) -> None:
    lesson = syntax_lesson(exc)
    location = f"{exc.filename}:{exc.lineno}:{exc.offset}" if exc.filename else "문법"
    print(f"KoPy 문법 오류 [{location}] {exc.msg}", file=sys.stderr)
    if exc.text:
        print(exc.text.rstrip(), file=sys.stderr)
    print(f"학습 힌트: {lesson.title}", file=sys.stderr)
    print(lesson.explanation, file=sys.stderr)
    if lesson.suggestion:
        print(f"수정 제안: {lesson.suggestion}", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    _configure_utf8_console()
    raw_argv = list(sys.argv[1:] if argv is None else argv)
    parser = _build_parser()
    args = parser.parse_args(_normalize_argv(raw_argv))

    try:
        if args.command == "run": return _cmd_run(args)
        if args.command == "check": return _cmd_check(args)
        if args.command == "translate": return _cmd_translate(args)
        if args.command in {"to-kopy", "convert-python"}: return _cmd_to_kopy(args)
        if args.command == "help": return _cmd_help(args)
        if args.command in {"packs", "libraries"}: return _cmd_packs(args)
        if args.command == "explain": return _cmd_explain(args)
        if args.command == "learn": return _cmd_learn(args)
        if args.command == "spelling": return _cmd_spelling(args)
        if args.command == "words": return _cmd_words(args)
        if args.command == "diagnose": return _cmd_diagnose(args)
        if args.command == "info": return _cmd_info(args)
        if args.command == "version": return _cmd_version()
    except FileNotFoundError as exc:
        print(f"KoPy 오류: 파일을 찾을 수 없습니다: {exc.filename}", file=sys.stderr)
        return 2
    except PermissionError as exc:
        print(f"KoPy 오류: 파일을 읽을 권한이 없습니다: {exc.filename}", file=sys.stderr)
        return 2
    except SyntaxError as exc:
        _print_syntax_lesson(exc)
        return 1
    except ValueError as exc:
        print(f"KoPy 오류: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:
        print(f"KoPy 실행 오류 [{type(exc).__name__}]: {exc}", file=sys.stderr)
        return 1

    parser.error("알 수 없는 명령입니다.")
    return 2
