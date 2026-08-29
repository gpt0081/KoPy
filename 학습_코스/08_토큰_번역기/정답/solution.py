from kopy.translator import translate


def 변환된_이름들(source: str) -> list[tuple[str, str]]:
    return [(before, after) for before, after, _line, _column in translate(source).replacements]
