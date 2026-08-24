"""Registry for built-in KoPy library packs."""

from __future__ import annotations

import importlib.util
from dataclasses import asdict
from typing import Any

from .accelerate import ACCELERATE_PACK
from .base import LibraryPack, PackMemberInfo
from .datasets import DATASETS_PACK
from .numpy import NUMPY_PACK
from .onnxruntime import ONNXRUNTIME_PACK
from .optimum import OPTIMUM_PACK
from .pandas import PANDAS_PACK
from .peft import PEFT_PACK
from .safetensors import SAFETENSORS_PACK
from .sklearn import SKLEARN_PACK
from .tokenizers import TOKENIZERS_PACK
from .torch import TORCH_PACK
from .transformers import TRANSFORMERS_PACK

_BUILTIN_PACKS: tuple[LibraryPack, ...] = (
    NUMPY_PACK, PANDAS_PACK, SKLEARN_PACK, TORCH_PACK, TRANSFORMERS_PACK,
    DATASETS_PACK, TOKENIZERS_PACK, ACCELERATE_PACK, PEFT_PACK,
    ONNXRUNTIME_PACK, SAFETENSORS_PACK, OPTIMUM_PACK,
)


def all_packs() -> tuple[LibraryPack, ...]:
    return _BUILTIN_PACKS


def pack_by_name(name: str) -> LibraryPack | None:
    lowered = name.casefold()
    for pack in _BUILTIN_PACKS:
        if lowered in {pack.name.casefold(), pack.module.casefold(), pack.kopy_module.casefold()}:
            return pack
    return None


def pack_by_prefix(prefix: str) -> LibraryPack | None:
    lowered = prefix.casefold()
    for pack in _BUILTIN_PACKS:
        if any(lowered == item.casefold() for item in pack.prefixes):
            return pack
    return None


def installed(pack: LibraryPack) -> bool:
    try:
        return importlib.util.find_spec(pack.module) is not None
    except (ImportError, ModuleNotFoundError, ValueError):
        return False


def packs_payload() -> dict[str, Any]:
    return {"schema": 1, "packs": [{"name": pack.name, "module": pack.module, "kopy_module": pack.kopy_module, "preferred_aliases": list(pack.preferred_aliases), "description": pack.description, "installed": installed(pack), "member_count": len(pack.members)} for pack in _BUILTIN_PACKS]}


def resolve_pack_member(term: str) -> tuple[LibraryPack, PackMemberInfo] | None:
    if "." not in term:
        return None
    prefix, member = term.split(".", 1)
    pack = pack_by_prefix(prefix)
    if pack is None:
        return None
    info = pack.member_info(member)
    if info is None:
        return None
    return pack, info


def pack_members_payload(pack: LibraryPack) -> dict[str, Any]:
    members = []
    for kopy, python_name in pack.members.items():
        info = pack.member_info(kopy)
        if info is not None:
            members.append(asdict(info))
    return {"schema": 1, "name": pack.name, "module": pack.module, "kopy_module": pack.kopy_module, "description": pack.description, "installed": installed(pack), "members": members}
