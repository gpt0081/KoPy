from kopy.packs.registry import all_packs, installed


def 팩_통계() -> dict:
    packs = all_packs()
    return {
        "count": len(packs),
        "names": sorted(pack.name for pack in packs),
        "member_count": sum(len(pack.members) for pack in packs),
        "installed": sorted(pack.name for pack in packs if installed(pack)),
    }
