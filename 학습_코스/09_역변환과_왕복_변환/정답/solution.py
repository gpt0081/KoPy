from kopy.translator import to_kopy, translate


def 왕복(source: str) -> tuple[str, str, bool]:
    kopy = to_kopy(source).kopy
    restored = translate(kopy).python
    return kopy, restored, restored == source
