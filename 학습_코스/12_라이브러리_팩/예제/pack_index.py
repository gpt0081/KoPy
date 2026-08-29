from kopy.packs.registry import all_packs, installed


for number, pack in enumerate(all_packs(), start=1):
    state = "설치됨" if installed(pack) else "미설치"
    print(f"{number:02d}. {pack.name}: {pack.kopy_module} → {pack.module} ({state}, API {len(pack.members)}개)")

print("전체 팩:", len(all_packs()))
