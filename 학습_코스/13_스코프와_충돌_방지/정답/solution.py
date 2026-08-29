from kopy.translator import translate


def 스코프_상태() -> dict[str, bool]:
    imported = translate("임포트 넘파이 애즈 np\n값 = np.어레이([1, 2])\n").python
    unimported = translate("값 = np.어레이([1, 2])\n").python
    peft_call = translate(
        "프롬 페프트 임포트 로라컨피그\n설정 = 로라컨피그(로라_알파=16)\n"
    ).python
    unrelated_call = translate(
        "프롬 페프트 임포트 로라컨피그\n값 = 다른함수(로라_알파=16)\n"
    ).python
    return {
        "pack_import_activates": "np.array" in imported,
        "no_import_preserves": "np.어레이" in unimported,
        "call_keyword_translates": "lora_alpha=16" in peft_call,
        "callee_specific": "로라_알파=16" in unrelated_call,
    }
