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
            "프롬 페프트 임포트 로라컨피그, 겟_페프트_모델\n"
            "임포트 토치\n"
            "기본설정 = 버트컨피그(보캡_사이즈=32, 히든_사이즈=16, 넘_히든_레이어즈=1, 넘_어텐션_헤즈=2, 인터미디어트_사이즈=32)\n"
            "기본모델 = 버트모델(기본설정)\n"
            "로라설정 = 로라컨피그(r=2, 로라_알파=4, 타깃_모듈즈=['query', 'value'], 로라_드롭아웃=0.0)\n"
            "모델 = 겟_페프트_모델(기본모델, 로라설정)\n"
            "인풋_아이디즈 = 토치.텐서([[1, 2, 3, 4]])\n"
            "출력 = 모델(인풋_아이디즈=인풋_아이디즈)\n"
            "모양 = 튜플(출력.last_hidden_state.셰이프)\n"
            "학습가능 = 썸(p.numel() 포 p 인 모델.파라미터스() 이프 p.requires_grad)\n"
            "전체 = 썸(p.numel() 포 p 인 모델.파라미터스())\n"
        )
        namespace: dict[str, object] = {}
        exec(compile(translate(source).python, "<kopy-peft-smoke>", "exec"), namespace)
        self.assertEqual(namespace["모양"], (1, 4, 16))
        self.assertGreater(namespace["학습가능"], 0)
        self.assertLess(namespace["학습가능"], namespace["전체"])

    def test_real_lora_config_accepts_phase4_keywords(self):
        source = (
            "프롬 페프트 임포트 로라컨피그\n"
            "설정 = 로라컨피그("
            "r=4, 로라_알파=8, 타깃_모듈즈=['query', 'value'], "
            "익스클루드_모듈즈=['classifier'], 레이어즈_투_트랜스폼=[0], "
            "레이어즈_패턴='layers', 랭크_패턴={'query': 2}, "
            "알파_패턴={'query': 4}, 유즈_도라=펄스)\n"
        )
        namespace: dict[str, object] = {}
        exec(compile(translate(source).python, "<kopy-peft-config>", "exec"), namespace)
        config = namespace["설정"]
        self.assertEqual(config.r, 4)
        self.assertEqual(config.lora_alpha, 8)
        self.assertEqual(config.target_modules, {"query", "value"})
        self.assertEqual(config.exclude_modules, {"classifier"})
        self.assertEqual(config.layers_to_transform, [0])
        self.assertEqual(config.layers_pattern, "layers")
        self.assertEqual(config.rank_pattern, {"query": 2})
        self.assertEqual(config.alpha_pattern, {"query": 4})
        self.assertFalse(config.use_dora)


if __name__ == "__main__":
    unittest.main()
