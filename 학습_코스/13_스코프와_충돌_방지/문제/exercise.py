from kopy.translator import translate


def 스코프_상태() -> dict[str, bool]:
    # TODO: 네 사례를 번역해 현재 동작을 불리언으로 보고하세요.
    return {
        "pack_import_activates": False,
        "no_import_preserves": False,
        "call_keyword_translates": False,
        "callee_specific": False,
    }
