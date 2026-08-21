"""KoPy library-pack support.

Library packs extend KoPy transliteration beyond Python's built-in vocabulary
without polluting the global core word registry.
"""

from .base import LibraryPack, PackMemberInfo
from .registry import all_packs, pack_by_name, pack_by_prefix

__all__ = [
    "LibraryPack",
    "PackMemberInfo",
    "all_packs",
    "pack_by_name",
    "pack_by_prefix",
]
