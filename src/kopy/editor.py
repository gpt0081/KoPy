"""Editor-facing data derived from KoPy's single source of truth.

This module is intentionally editor-agnostic. VS Code and future IDE clients
consume the same registry and diagnostics that the KoPy CLI/runtime use.
"""

from __future__ import annotations

import sys
from typing import Any

from . import PYTHON_BASELINE, __version__
from .education import syntax_lesson
from .spelling import find_spelling_hints
from .translator import translate
from .words import all_word_info


def word_entries() -> list[dict[str, Any]]:
    """Return the canonical KoPy registry including teaching metadata."""
    entries: list[dict[str, Any]] = []
    for info in all_word_info():
        entries.append(
            {
                "kopy": info.kopy,
                "python": info.python,
                "category": info.category,
                "description": info.description,
                "kopy_example": info.kopy_example,
                "python_example": info.python_example,
            }
        )
    return entries


def words_payload() -> dict[str, Any]:
    return {
        "schema": 2,
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
    """Return editor-friendly diagnostics using KoPy's real Core logic."""
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
        lesson = syntax_lesson(exc)
        diagnostics.append(
            {
                "severity": "error",
                "code": "syntax",
                "message": exc.msg,
                "line": line,
                "column": column,
                "end_line": end_line,
                "end_column": max(column + 1, end_column),
                "lesson_title": lesson.title,
                "lesson": lesson.explanation,
                "suggestion": lesson.suggestion,
            }
        )

    return {
        "schema": 2,
        "filename": filename,
        "ok": not diagnostics,
        "diagnostics": diagnostics,
    }
