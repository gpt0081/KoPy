import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class TransformersPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("transformers")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "transformers")
        self.assertEqual(pack.kopy_module, "트랜스포머스")

    def test_auto_model_tokenizer_generation_and_pipeline_translate(self):
        source = (
            "프롬 트랜스포머스 임포트 오토토크나이저, 오토모델포코절엘엠, 파이프라인\n"
            "토크나이저 = 오토토크나이저.프롬프리트레인드('local-model')\n"
            "모델 = 오토모델포코절엘엠.프롬프리트레인드('local-model')\n"
            "입력값 = 토크나이저('안녕', return_tensors='pt')\n"
            "출력 = 모델.제너레이트(**입력값)\n"
            "텍스트 = 토크나이저.배치디코드(출력)\n"
            "생성기 = 파이프라인('text-generation', model=모델, tokenizer=토크나이저)\n"
        )
        python_source = translate(source).python
        self.assertIn(
            "from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline",
            python_source,
        )
        self.assertIn("AutoTokenizer.from_pretrained", python_source)
        self.assertIn("AutoModelForCausalLM.from_pretrained", python_source)
        self.assertIn(".generate(**", python_source)
        self.assertIn(".batch_decode(", python_source)
        self.assertIn("pipeline('text-generation'", python_source)

    def test_reverse_translation(self):
        source = (
            "from transformers import AutoTokenizer, AutoModelForCausalLM\n"
            "tokenizer = AutoTokenizer.from_pretrained('local-model')\n"
            "model = AutoModelForCausalLM.from_pretrained('local-model')\n"
            "outputs = model.generate(input_ids)\n"
            "text = tokenizer.decode(outputs[0])\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 트랜스포머스 임포트 오토토크나이저, 오토모델포코절엘엠", kopy)
        self.assertIn(".프롬프리트레인드", kopy)
        self.assertIn(".제너레이트(", kopy)
        self.assertIn(".디코드(", kopy)

    def test_help_term_resolves(self):
        resolved = resolve_pack_member("트랜스포머스.오토토크나이저")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "AutoTokenizer")


if __name__ == "__main__":
    unittest.main()
