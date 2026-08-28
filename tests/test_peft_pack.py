import unittest

from kopy.translator import to_kopy, translate


class PeftPackTests(unittest.TestCase):
    def test_translate_canonical_lora_api(self):
        source = (
            "프롬 페프트 임포트 로라컨피그, 겟_페프트_모델\n"
            "설정 = 로라컨피그(r=8, 로라_알파=16, 타깃_모듈즈=['query', 'value'], 로라_드롭아웃=0.05, 바이어스='none', 인퍼런스_모드=펄스, 모듈즈_투_세이브=['classifier'], 팬_인_팬_아웃=펄스, 유즈_알에스로라=트루, 이니트_로라_웨이츠=트루)\n"
            "모델 = 겟_페프트_모델(모델, 설정)\n"
            "모델 = 모델.머지_앤드_언로드()\n"
        )
        result = translate(source).python
        self.assertIn("from peft import LoraConfig, get_peft_model", result)
        self.assertIn(
            "설정 = LoraConfig(r=8, lora_alpha=16, target_modules=['query', 'value'], lora_dropout=0.05, bias='none', inference_mode=False, modules_to_save=['classifier'], fan_in_fan_out=False, use_rslora=True, init_lora_weights=True)",
            result,
        )
        self.assertIn("model = get_peft_model(model, 설정)", result)
        self.assertIn("model = model.merge_and_unload()", result)

    def test_reverse_translate_uses_canonical_peft_api(self):
        source = (
            "from peft import PeftModel, LoraConfig, IA3Config\n"
            "config = LoraConfig(r=4, lora_alpha=8, target_modules=['query'], task_type='FEATURE_EXTRACTION', lora_dropout=0.1, bias='none', inference_mode=False, modules_to_save=['classifier'], fan_in_fan_out=False, use_rslora=True, init_lora_weights=True)\n"
            "model = model.set_adapter('default')\n"
            "model = model.merge_and_unload()\n"
        )
        result = to_kopy(source).kopy
        self.assertIn("프롬 페프트 임포트 페프트모델, 로라컨피그, 아이에이3컨피그", result)
        self.assertIn(
            "로라컨피그(r=4, 로라_알파=8, 타깃_모듈즈=['query'], 태스크_타입='FEATURE_EXTRACTION', 로라_드롭아웃=0.1, 바이어스='none', 인퍼런스_모드=펄스, 모듈즈_투_세이브=['classifier'], 팬_인_팬_아웃=펄스, 유즈_알에스로라=트루, 이니트_로라_웨이츠=트루)",
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
            "로라_알파 = 16\n타깃_모듈즈 = []\n바이어스 = 'none'\n인퍼런스_모드 = 펄스\n모듈즈_투_세이브 = []\n팬_인_팬_아웃 = 펄스\n유즈_알에스로라 = 펄스\n이니트_로라_웨이츠 = 트루\n모델 = 모델.머지_앤드_언로드()\n"
        ).python
        self.assertIn("로라_알파 = 16", result)
        self.assertIn("타깃_모듈즈 = []", result)
        self.assertIn("바이어스 = 'none'", result)
        self.assertIn("인퍼런스_모드 = False", result)
        self.assertIn("모듈즈_투_세이브 = []", result)
        self.assertIn("팬_인_팬_아웃 = False", result)
        self.assertIn("유즈_알에스로라 = False", result)
        self.assertIn("이니트_로라_웨이츠 = True", result)
        self.assertIn("model = model.머지_앤드_언로드()", result)

    def test_peft_keyword_spellings_only_translate_at_call_keywords(self):
        source = (
            "프롬 페프트 임포트 로라컨피그\n"
            "로라_알파 = 99\n"
            "바이어스 = 'all'\n"
            "인퍼런스_모드 = 펄스\n"
            "모듈즈_투_세이브 = ['head']\n"
            "팬_인_팬_아웃 = 트루\n"
            "유즈_알에스로라 = 펄스\n"
            "이니트_로라_웨이츠 = 펄스\n"
            "설정 = 로라컨피그(로라_알파=8, 바이어스='none', 인퍼런스_모드=트루, 모듈즈_투_세이브=['classifier'], 팬_인_팬_아웃=펄스, 유즈_알에스로라=트루, 이니트_로라_웨이츠=트루)\n"
        )
        result = translate(source).python
        self.assertIn("로라_알파 = 99", result)
        self.assertIn("바이어스 = 'all'", result)
        self.assertIn("인퍼런스_모드 = False", result)
        self.assertIn("모듈즈_투_세이브 = ['head']", result)
        self.assertIn("팬_인_팬_아웃 = True", result)
        self.assertIn("유즈_알에스로라 = False", result)
        self.assertIn("이니트_로라_웨이츠 = False", result)
        self.assertIn("LoraConfig(lora_alpha=8, bias='none', inference_mode=True, modules_to_save=['classifier'], fan_in_fan_out=False, use_rslora=True, init_lora_weights=True)", result)

        reverse = to_kopy(
            "from peft import LoraConfig\n"
            "lora_alpha = 99\n"
            "bias = 'all'\n"
            "inference_mode = False\n"
            "modules_to_save = ['head']\n"
            "fan_in_fan_out = True\n"
            "use_rslora = False\n"
            "init_lora_weights = False\n"
            "config = LoraConfig(lora_alpha=8, bias='none', inference_mode=True, modules_to_save=['classifier'], fan_in_fan_out=False, use_rslora=True, init_lora_weights=True)\n"
        ).kopy
        self.assertIn("lora_alpha = 99", reverse)
        self.assertIn("bias = 'all'", reverse)
        self.assertIn("inference_mode = 펄스", reverse)
        self.assertIn("modules_to_save = ['head']", reverse)
        self.assertIn("fan_in_fan_out = 트루", reverse)
        self.assertIn("use_rslora = 펄스", reverse)
        self.assertIn("init_lora_weights = 펄스", reverse)
        self.assertIn("로라컨피그(로라_알파=8, 바이어스='none', 인퍼런스_모드=트루, 모듈즈_투_세이브=['classifier'], 팬_인_팬_아웃=펄스, 유즈_알에스로라=트루, 이니트_로라_웨이츠=트루)", reverse)

    def test_rank_r_remains_untranslated_because_it_is_ambiguous(self):
        source = "프롬 페프트 임포트 로라컨피그\n설정 = 로라컨피그(r=8, 로라_알파=16)\n"
        result = translate(source).python
        self.assertIn("LoraConfig(r=8, lora_alpha=16)", result)


if __name__ == "__main__":
    unittest.main()