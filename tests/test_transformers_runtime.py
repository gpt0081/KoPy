import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("transformers"), "Transformers is not installed")
@unittest.skipUnless(importlib.util.find_spec("torch"), "PyTorch is not installed")
class TransformersRuntimeTests(unittest.TestCase):
    def test_kopy_transformers_bert_forward_executes_offline(self):
        source = (
            "프롬 트랜스포머스 임포트 버트컨피그, 버트모델\n"
            "임포트 토치\n"
            "컨피그 = 버트컨피그(vocab_size=32, hidden_size=16, num_hidden_layers=1, "
            "num_attention_heads=2, intermediate_size=32)\n"
            "모델 = 버트모델(컨피그)\n"
            "모델.이밸()\n"
            "입력아이디 = 토치.텐서([[1, 2, 3, 4]])\n"
            "출력 = 모델(input_ids=입력아이디)\n"
            "히든 = 출력.라스트히든스테이트\n"
            "모양 = 히든.셰이프\n"
        )
        namespace: dict[str, object] = {}
        exec(compile(translate(source).python, "<kopy-transformers-smoke>", "exec"), namespace)
        self.assertEqual(tuple(namespace["모양"]), (1, 4, 16))


if __name__ == "__main__":
    unittest.main()
