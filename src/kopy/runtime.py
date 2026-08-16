"""KoPy execution and validation helpers."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from .spelling import SpellingHint, find_spelling_hints
from .translator import Translation, translate


def read_source(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def analyze_source(source: str, *, spelling: bool = True) -> tuple[Translation, tuple[SpellingHint, ...]]:
    hints = find_spelling_hints(source) if spelling else ()
    translation = translate(source)
    return translation, hints


def compile_source(source: str, filename: str, *, spelling: bool = True):
    translation, hints = analyze_source(source, spelling=spelling)
    code = compile(translation.python, filename, "exec")
    return code, translation, hints


def run_file(path: str | Path, *, spelling: bool = True, script_args: list[str] | None = None) -> tuple[Translation, tuple[SpellingHint, ...]]:
    file_path = Path(path)
    source = read_source(file_path)
    code, translation, hints = compile_source(source, str(file_path), spelling=spelling)

    old_argv = sys.argv[:]
    sys.argv = [str(file_path), *(script_args or [])]
    globals_dict: dict[str, Any] = {
        "__name__": "__main__",
        "__file__": str(file_path),
        "__package__": None,
        "__cached__": None,
    }
    try:
        exec(code, globals_dict, globals_dict)
    finally:
        sys.argv = old_argv

    return translation, hints
