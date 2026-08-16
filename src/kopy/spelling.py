"""Conservative spelling hints for Python keywords and built-ins.

KoPy never edits source automatically. Hints are advisory only.
"""

from __future__ import annotations

import builtins
import io
import keyword
import re
import tokenize
from dataclasses import dataclass
from difflib import SequenceMatcher

from .words import WORDS

_ASCII_IDENTIFIER = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_KEYWORDS = frozenset(keyword.kwlist) | frozenset(getattr(keyword, "softkwlist", ()))
_BUILTINS = frozenset(
    name
    for name in dir(builtins)
    if not name.startswith("_") and name.isidentifier()
)
_TARGETS = _KEYWORDS | _BUILTINS
_IGNORED_TOKEN_TYPES = {
    tokenize.ENCODING,
    tokenize.NL,
    tokenize.NEWLINE,
    tokenize.INDENT,
    tokenize.DEDENT,
    tokenize.COMMENT,
    tokenize.ENDMARKER,
}


@dataclass(frozen=True)
class SpellingHint:
    found: str
    suggestion: str
    line: int
    column: int
    category: str

    def format(self) -> str:
        return (
            f"{self.line}:{self.column}  # KoPy 힌트: "
            f"'{self.found}' → '{self.suggestion}' 를 입력하려고 했나요?"
        )


def _one_edit_or_transposition(a: str, b: str) -> bool:
    """Return True when strings differ by one edit or one adjacent swap."""
    if a == b or abs(len(a) - len(b)) > 1:
        return False

    if len(a) == len(b):
        diffs = [i for i, (x, y) in enumerate(zip(a, b)) if x != y]
        if len(diffs) == 1:
            return True
        if len(diffs) == 2:
            i, j = diffs
            return (
                j == i + 1
                and a[i] == b[j]
                and a[j] == b[i]
            )
        return False

    short, long = (a, b) if len(a) < len(b) else (b, a)
    i = j = mismatches = 0
    while i < len(short) and j < len(long):
        if short[i] == long[j]:
            i += 1
            j += 1
            continue
        mismatches += 1
        if mismatches > 1:
            return False
        j += 1
    return True


def _best_candidate(word: str, candidates: frozenset[str]) -> str | None:
    close = [candidate for candidate in candidates if _one_edit_or_transposition(word, candidate)]
    if not close:
        return None
    return max(close, key=lambda candidate: SequenceMatcher(None, word, candidate).ratio())


def _significant_indices(tokens: list[tokenize.TokenInfo]) -> list[int]:
    return [i for i, token in enumerate(tokens) if token.type not in _IGNORED_TOKEN_TYPES]


def find_spelling_hints(source: str) -> tuple[SpellingHint, ...]:
    """Find high-confidence English Python spelling mistakes.

    Keyword-like typos are checked anywhere except attribute access. Built-in names
    are checked only when they look like function calls, which avoids flagging most
    ordinary user variables.
    """
    reader = io.StringIO(source).readline
    try:
        tokens = list(tokenize.generate_tokens(reader))
    except (tokenize.TokenError, IndentationError):
        return ()

    significant = _significant_indices(tokens)
    position = {token_index: pos for pos, token_index in enumerate(significant)}
    hints: list[SpellingHint] = []
    seen: set[tuple[int, int, str]] = set()

    for index, token in enumerate(tokens):
        if token.type != tokenize.NAME:
            continue

        word = token.string
        if word in _TARGETS or word in WORDS or not _ASCII_IDENTIFIER.match(word):
            continue

        sig_pos = position.get(index)
        if sig_pos is None:
            continue

        prev_token = tokens[significant[sig_pos - 1]] if sig_pos > 0 else None
        next_token = (
            tokens[significant[sig_pos + 1]]
            if sig_pos + 1 < len(significant)
            else None
        )

        # Do not second-guess object.attribute names.
        if prev_token is not None and prev_token.string == ".":
            continue

        suggestion = _best_candidate(word, _KEYWORDS)
        category = "keyword"

        # For built-ins, require call syntax such as pritn(...).
        if suggestion is None and next_token is not None and next_token.string == "(":
            suggestion = _best_candidate(word, _BUILTINS)
            category = "builtin"

        if suggestion is None:
            continue

        key = (token.start[0], token.start[1], suggestion)
        if key in seen:
            continue
        seen.add(key)
        hints.append(
            SpellingHint(
                found=word,
                suggestion=suggestion,
                line=token.start[0],
                column=token.start[1] + 1,
                category=category,
            )
        )

    return tuple(hints)
