"""Token-safe translation between KoPy and Python."""

from __future__ import annotations

import io
import tokenize
from dataclasses import dataclass

from .words import PY_TO_KO, WORDS


@dataclass(frozen=True)
class Translation:
    source: str
    python: str
    replacements: tuple[tuple[str, str, int, int], ...]


@dataclass(frozen=True)
class ReverseTranslation:
    source: str
    kopy: str
    replacements: tuple[tuple[str, str, int, int], ...]


def _replace_names(source: str, mapping: dict[str, str]) -> tuple[str, tuple[tuple[str, str, int, int], ...]]:
    tokens: list[tokenize.TokenInfo] = []
    replacements: list[tuple[str, str, int, int]] = []
    reader = io.StringIO(source).readline

    for token in tokenize.generate_tokens(reader):
        if token.type == tokenize.NAME and token.string in mapping:
            replacement = mapping[token.string]
            replacements.append((token.string, replacement, token.start[0], token.start[1] + 1))
            token = tokenize.TokenInfo(
                token.type,
                replacement,
                token.start,
                token.end,
                token.line,
            )
        tokens.append(token)

    return tokenize.untokenize(tokens), tuple(replacements)


def translate(source: str) -> Translation:
    """Translate KoPy NAME tokens to Python while preserving strings/comments."""
    python_source, replacements = _replace_names(source, WORDS)
    return Translation(source=source, python=python_source, replacements=replacements)


def to_kopy(source: str) -> ReverseTranslation:
    """Translate registered Python NAME tokens to KoPy.

    Strings, comments and attribute names remain token-safe. The conversion is
    intentionally mechanical and reversible for registered names.
    """
    kopy_source, replacements = _replace_names(source, PY_TO_KO)
    return ReverseTranslation(source=source, kopy=kopy_source, replacements=replacements)
