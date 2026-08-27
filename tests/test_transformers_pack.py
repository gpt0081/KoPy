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
            "입력값 = 토크나이저('안녕', 리턴_텐서즈='pt')\n"
            "출력 = 모델.제너레이트(**입력값)\n"
            "텍스트 = 토크나이저.배치디코드(출력)\n"
            "제너레이터 = 파이프라인('text-generation', 모델=모델, 토크나이저=토크나이저)\n"
        )
        python_source = translate(source).python
        self.assertIn(
            "from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline",
            python_source,
        )
        self.assertIn("AutoTokenizer.from_pretrained", python_source)
        self.assertIn("AutoModelForCausalLM.from_pretrained", python_source)
        self.assertIn("return_tensors='pt'", python_source)
        self.assertIn(".generate(**", python_source)
        self.assertIn(".batch_decode(", python_source)
        self.assertIn("pipeline('text-generation', model=model, tokenizer=tokenizer)", python_source)

    def test_bert_config_keywords_translate_and_preserve_digits(self):
        source = (
            "프롬 트랜스포머스 임포트 버트컨피그, 버트모델\n"
            "컨피그 = 버트컨피그(보캡_사이즈=32, 히든_사이즈=16, 넘_히든_레이어즈=1, "
            "넘_어텐션_헤즈=2, 인터미디어트_사이즈=32)\n"
            "인풋_아이디즈 = 텐서\n"
            "출력 = 버트모델(컨피그)(인풋_아이디즈=인풋_아이디즈)\n"
        )
        python_source = translate(source).python
        self.assertIn("vocab_size=32", python_source)
        self.assertIn("hidden_size=16", python_source)
        self.assertIn("num_hidden_layers=1", python_source)
        self.assertIn("num_attention_heads=2", python_source)
        self.assertIn("intermediate_size=32", python_source)
        self.assertIn("input_ids=input_ids", python_source)

    def test_reverse_translation(self):
        source = (
            "from transformers import AutoTokenizer, AutoModelForCausalLM\n"
            "tokenizer = AutoTokenizer.from_pretrained('local-model')\n"
            "model = AutoModelForCausalLM.from_pretrained('local-model')\n"
            "input_ids = tokenizer('hello', return_tensors='pt').input_ids\n"
            "output_ids = model.generate(input_ids=input_ids)\n"
            "text = tokenizer.decode(output_ids[0])\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 트랜스포머스 임포트 오토토크나이저, 오토모델포코절엘엠", kopy)
        self.assertIn("토크나이저 = 오토토크나이저.프롬프리트레인드", kopy)
        self.assertIn("리턴_텐서즈='pt'", kopy)
        self.assertIn("인풋_아이디즈", kopy)
        self.assertIn("아웃풋_아이디즈", kopy)
        self.assertIn(".제너레이트(", kopy)
        self.assertIn(".디코드(", kopy)

    def test_digits_stay_digits_in_gpt2_names(self):
        kopy = to_kopy("from transformers import GPT2Config, GPT2LMHeadModel\n").kopy
        self.assertIn("지피티2컨피그", kopy)
        self.assertIn("지피티2엘엠헤드모델", kopy)
        self.assertNotIn("지피티투", kopy)

    def test_help_term_resolves(self):
        resolved = resolve_pack_member("트랜스포머스.오토토크나이저")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "AutoTokenizer")


if __name__ == "__main__":
    unittest.main()
