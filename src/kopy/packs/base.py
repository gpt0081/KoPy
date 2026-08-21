"""Data model for KoPy library packs."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class PackMemberInfo:
    kopy: str
    python: str
    description: str
    kopy_example: str | None = None
    python_example: str | None = None


@dataclass(frozen=True)
class LibraryPack:
    """A namespace-scoped transliteration pack for a Python library.

    ``members`` maps KoPy spellings to Python attributes or imported names.
    The mapping is intentionally namespace-scoped instead of being merged into
    KoPy's global WORDS dictionary, preventing cross-library collisions.
    """

    name: str
    module: str
    kopy_module: str
    description: str
    members: dict[str, str]
    preferred_aliases: tuple[str, ...] = ()
    member_descriptions: dict[str, str] = field(default_factory=dict)
    examples: dict[str, tuple[str, str]] = field(default_factory=dict)

    @property
    def python_to_kopy(self) -> dict[str, str]:
        return {python_name: kopy for kopy, python_name in self.members.items()}

    @property
    def prefixes(self) -> frozenset[str]:
        return frozenset({self.name, self.module, self.kopy_module, *self.preferred_aliases})

    def python_for(self, kopy_name: str) -> str | None:
        return self.members.get(kopy_name)

    def kopy_for(self, python_name: str) -> str | None:
        return self.python_to_kopy.get(python_name)

    def member_info(self, word: str) -> PackMemberInfo | None:
        if word in self.members:
            kopy = word
            python_name = self.members[word]
        else:
            kopy = self.python_to_kopy.get(word)
            if kopy is None:
                return None
            python_name = word

        examples = self.examples.get(python_name)
        return PackMemberInfo(
            kopy=kopy,
            python=python_name,
            description=self.member_descriptions.get(
                python_name,
                f"{self.module}.{python_name} API를 KoPy 음역으로 사용할 수 있습니다.",
            ),
            kopy_example=examples[0] if examples else None,
            python_example=examples[1] if examples else None,
        )
