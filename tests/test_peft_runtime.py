import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("peft"), "PEFT is not installed")
@unittest.skipUnless(importlib.util.find_spec("transformers"), "Transformers is not installed")
@unittest.skipUnless(importlib.util.find_spec("torch"), "PyTorch is not installed")
class PeftRuntimeTests(unittest.TestCase):
    def test_kopy_peft_tiny_bert_lora_forward(self):
        source = (
            "프롬 트랜스포머스 임포트 버트컨피그, 버트모델\n"
            "프롬 페프트 임포트 로라컨피그, 겟페프트모델\n"
            "임포트 토치\n"
            "기본설정 = 버트컨피그(vocab_size=32, hidden_size=16, num_hidden_layers=1, num_attention_heads=2, intermediate_size=32)\n"
            "기본모델 = 버트모델(기본설정)\n"
            "로라설정 = 로라컨피그(r=2, lora_alpha=4, target_modules=['query', 'value'], lora_dropout=0.0)\n"
            "모델 = 겟페프트모델(기본모델, 로라설정)\n"
            "입력아이디 = 토치.텐서([[1, 2, 3, 4]])\n"
            "출력 = 모델(input_ids=입력아이디)\n"
            "모양 = 튜플(출력.last_hidden_state.셰이프)\n"
            "학습가능 = 썸(p.numel() 포 p 인 모델.파라미터스() 이프 p.requires_grad)\n"
            "전체 = 썸(p.numel() 포 p 인 모델.파라미터스())\n"
        )
        namespace: dict[str, object] = {}
        exec(compile(translate(source).python, "<kopy-peft-smoke>", "exec"), namespace)
        self.assertEqual(namespace["모양"], (1, 4, 16))
        self.assertGreater(namespace["학습가능"], 0)
        self.assertLess(namespace["학습가능"], namespace["전체"])


if __name__ == "__main__":
    unittest.main()
