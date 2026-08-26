import unittest

from kopy.translator import to_kopy, translate


class PeftPackTests(unittest.TestCase):
    def test_translate_lora_api(self):
        source = (
            "프롬 페프트 임포트 로라컨피그, 겟페프트모델\n"
            "설정 = 로라컨피그(r=8, lora_alpha=16, target_modules=['query', 'value'])\n"
            "모델 = 겟페프트모델(모델, 설정)\n"
            "병합 = 모델.머지앤언로드()\n"
        )
        result = translate(source).python
        self.assertIn("from peft import LoraConfig, get_peft_model", result)
        self.assertIn("설정 = LoraConfig", result)
        self.assertIn("model = get_peft_model(model, 설정)", result)
        self.assertIn("model.merge_and_unload()", result)

    def test_reverse_translate_peft_api(self):
        source = (
            "from peft import PeftModel, LoraConfig\n"
            "config = LoraConfig(r=4)\n"
            "model = model.set_adapter('default')\n"
        )
        result = to_kopy(source).kopy
        self.assertIn("프롬 페프트 임포트 페프트모델, 로라컨피그", result)
        self.assertIn("로라컨피그(r=4)", result)
        self.assertIn("모델 = 모델.셋어댑터('default')", result)


if __name__ == "__main__":
    unittest.main()
