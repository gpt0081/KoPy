"""Editor-facing data derived from KoPy's single source of truth.

This module is intentionally editor-agnostic. VS Code and future IDE clients
consume the same word registry and diagnostics that the KoPy CLI/runtime use.
"""

from __future__ import annotations

import builtins
import keyword
import sys
from typing import Any

from . import PYTHON_BASELINE, __version__
from .spelling import find_spelling_hints
from .translator import translate
from .words import WORDS

_BUILTINS = frozenset(
    name for name in dir(builtins) if not name.startswith("_") and name.isidentifier()
)
_KEYWORDS = frozenset(keyword.kwlist) | frozenset(getattr(keyword, "softkwlist", ()))
_CONSTANTS = frozenset({"True", "False", "None"})


def _category(python_name: str) -> str:
    if python_name in _CONSTANTS:
        return "constant"
    if python_name in _KEYWORDS:
        return "keyword"
    if python_name in _BUILTINS:
        return "builtin"
    return "name"


def word_entries() -> list[dict[str, str]]:
    """Return the canonical KoPy transliteration registry for editor clients."""
    return [
        {
            "kopy": korean,
            "python": python_name,
            "category": _category(python_name),
        }
        for korean, python_name in WORDS.items()
    ]


def words_payload() -> dict[str, Any]:
    return {
        "schema": 1,
        "kopy_version": __version__,
        "python_baseline": PYTHON_BASELINE,
        "words": word_entries(),
    }


def info_payload() -> dict[str, Any]:
    return {
        "schema": 1,
        "kopy_version": __version__,
        "python_baseline": PYTHON_BASELINE,
        "runtime_python": ".".join(str(part) for part in sys.version_info[:3]),
    }


def diagnose_source(source: str, filename: str = "<stdin>") -> dict[str, Any]:
    """Return editor-friendly diagnostics using KoPy's real spelling/translator logic."""
    diagnostics: list[dict[str, Any]] = []

    for hint in find_spelling_hints(source):
        diagnostics.append(
            {
                "severity": "warning",
                "code": "spelling",
                "message": f"'{hint.found}' → '{hint.suggestion}' 를 입력하려고 했나요?",
                "line": hint.line,
                "column": hint.column,
                "end_line": hint.line,
                "end_column": hint.column + len(hint.found),
                "found": hint.found,
                "suggestion": hint.suggestion,
                "category": hint.category,
            }
        )

    try:
        translated = translate(source).python
        compile(translated, filename, "exec")
    except SyntaxError as exc:
        line = exc.lineno or 1
        column = exc.offset or 1
        end_line = getattr(exc, "end_lineno", None) or line
        end_column = getattr(exc, "end_offset", None) or (column + 1)
        diagnostics.append(
            {
                "severity": "error",
                "code": "syntax",
                "message": exc.msg,
                "line": line,
                "column": column,
                "end_line": end_line,
                "end_column": max(column + 1, end_column),
            }
        )

    return {
        "schema": 1,
        "filename": filename,
        "ok": not diagnostics,
        "diagnostics": diagnostics,
    }
