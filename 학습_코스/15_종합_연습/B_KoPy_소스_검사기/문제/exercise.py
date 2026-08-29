from kopy.editor import diagnose_source
from kopy.translator import translate


def 검사(source: str, filename: str = "<source>") -> dict:
    # TODO: python, replacement_count, pairs, ok, diagnostics를 반환하세요.
    return {
        "python": "",
        "replacement_count": 0,
        "pairs": [],
        "ok": False,
        "diagnostics": [],
    }
