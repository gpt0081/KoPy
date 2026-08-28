import unittest

from kopy.translator import to_kopy, translate


class PeftPackTests(unittest.TestCase):
    def test_translate_canonical_lora_api(self):
        source = (
            "프롬 페프트 임포트 로라컨피그, 겟_페프트_모델\n"
            "설정 = 로라컨피그(r=8, 로라_알파=16, 타깃_모듈즈=['query', 'value'], 로라_드롭아웃=0.05, 바이어스='none', 인퍼런스_모드=펄스)\n"
            "모델 = 겟_페프트_모델(모델, 설정)\n"
            "모델 = 모델.머지_앤드_언로드()\n"
        )
        result = translate(source).python
        self.assertIn("from peft import LoraConfig, get_peft_model", result)
        self.assertIn(
            "설정 = LoraConfig(r=8, lora_alpha=16, target_modules=['query', 'value'], lora_dropout=0.05, bias='none', inference_mode=False)",
            result,
        )
        self.assertIn("model = get_peft_model(model, 설정)", result)
        self.assertIn("model = model.merge_and_unload()", result)

    def test_reverse_translate_uses_canonical_peft_api(self):
        source = (
            "from peft import PeftModel, LoraConfig, IA3Config\n"
            "config = LoraConfig(r=4, lora_alpha=8, target_modules=['query'], task_type='FEATURE_EXTRACTION', lora_dropout=0.1, bias='none', inference_mode=False)\n"
            "model = model.set_adapter('default')\n"
            "model = model.merge_and_unload()\n"
        )
        result = to_kopy(source).kopy
        self.assertIn("프롬 페프트 임포트 페프트모델, 로라컨피그, 아이에이3컨피그", result)
        self.assertIn(
            "로라컨피그(r=4, 로라_알파=8, 타깃_모듈즈=['query'], 태스크_타입='FEATURE_EXTRACTION', 로라_드롭아웃=0.1, 바이어스='none', 인퍼런스_모드=펄스)",
            result,
        )
        self.assertIn("모델 = 모델.셋_어댑터('default')", result)
        self.assertIn("모델 = 모델.머지_앤드_언로드()", result)
        self.assertNotIn("아이에이쓰리컨피그", result)

    def test_legacy_compact_spellings_still_translate(self):
        source = (
            "프롬 페프트 임포트 겟페프트모델, 아이에이쓰리컨피그\n"
            "모델 = 겟페프트모델(모델, 설정)\n"
            "모델 = 모델.셋어댑터('default')\n"
        )
        result = translate(source).python
        self.assertIn("from peft import get_peft_model, IA3Config", result)
        self.assertIn("model = get_peft_model(model, 설정)", result)
        self.assertIn("model = model.set_adapter('default')", result)

    def test_peft_member_spellings_are_namespace_scoped(self):
        result = translate(
            "로라_알파 = 16\n타깃_모듈즈 = []\n바이어스 = 'none'\n인퍼런스_모드 = 펄스\n모델 = 모델.머지_앤드_언로드()\n"
        ).python
        self.assertIn("로라_알파 = 16", result)
        self.assertIn("타깃_모듈즈 = []", result)
        self.assertIn("바이어스 = 'none'", result)
        self.assertIn("인퍼런스_모드 = False", result)
        self.assertIn("model = model.머지_앤드_언로드()", result)

    def test_peft_keyword_spellings_only_translate_at_call_keywords(self):
        source = (
            "프롬 페프트 임포트 로라컨피그\n"
            "로라_알파 = 99\n"
            "바이어스 = 'all'\n"
            "인퍼런스_모드 = 펄스\n"
            "설정 = 로라컨피그(로라_알파=8, 바이어스='none', 인퍼런스_모드=트루)\n"
        )
        result = translate(source).python
        self.assertIn("로라_알파 = 99", result)
        self.assertIn("바이어스 = 'all'", result)
        self.assertIn("인퍼런스_모드 = False", result)
        self.assertIn("LoraConfig(lora_alpha=8, bias='none', inference_mode=True)", result)

        reverse = to_kopy(
            "from peft import LoraConfig\n"
            "lora_alpha = 99\n"
            "bias = 'all'\n"
            "inference_mode = False\n"
            "config = LoraConfig(lora_alpha=8, bias='none', inference_mode=True)\n"
        ).kopy
        self.assertIn("lora_alpha = 99", reverse)
        self.assertIn("bias = 'all'", reverse)
        self.assertIn("inference_mode = 펄스", reverse)
        self.assertIn("로라컨피그(로라_알파=8, 바이어스='none', 인퍼런스_모드=트루)", reverse)

    def test_rank_r_remains_untranslated_because_it_is_ambiguous(self):
        source = "프롬 페프트 임포트 로라컨피그\n설정 = 로라컨피그(r=8, 로라_알파=16)\n"
        result = translate(source).python
        self.assertIn("LoraConfig(r=8, lora_alpha=16)", result)


if __name__ == "__main__":
    unittest.main()
