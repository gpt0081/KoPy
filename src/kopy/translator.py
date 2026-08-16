"""Token-safe KoPy -> Python translation."""

from __future__ import annotations

import io
import tokenize
from dataclasses import dataclass

from .words import WORDS


@dataclass(frozen=True)
class Translation:
    source: str
    python: str
    replacements: tuple[tuple[str, str, int, int], ...]


def translate(source: str) -> Translation:
    """Translate KoPy NAME tokens to Python while preserving strings/comments.

    English Python source passes through unchanged except for harmless formatting
    normalization performed by ``tokenize.untokenize``.
    """
    tokens: list[tokenize.TokenInfo] = []
    replacements: list[tuple[str, str, int, int]] = []
    reader = io.StringIO(source).readline

    for token in tokenize.generate_tokens(reader):
        if token.type == tokenize.NAME and token.string in WORDS:
            replacement = WORDS[token.string]
            replacements.append(
                (token.string, replacement, token.start[0], token.start[1] + 1)
            )
            token = tokenize.TokenInfo(
                token.type,
                replacement,
                token.start,
                token.end,
                token.line,
            )
        tokens.append(token)

    return Translation(
        source=source,
        python=tokenize.untokenize(tokens),
        replacements=tuple(replacements),
    )
