import unittest

from kopy.packs.registry import pack_by_name
from kopy.translator import to_kopy, translate


class LiteLLMPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("litellm")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.kopy_module, "라이트엘엘엠")

    def test_translate_core_litellm_api(self):
        source = (
            "프롬 라이트엘엘엠 임포트 컴플리션, 임베딩, 라우터\n"
            "리스폰스 = 컴플리션(모델='openai/gpt-5-mini', messages=[])\n"
            "벡터 = 임베딩(모델='text-embedding-3-small', input=['KoPy'])\n"
            "라우터객체 = 라우터(model_list=[])\n"
        )
        result = translate(source).python
        self.assertIn("from litellm import completion, embedding, Router", result)
        self.assertIn("completion(model='openai/gpt-5-mini', messages=[])", result)
        self.assertIn("embedding(model='text-embedding-3-small', input=['KoPy'])", result)
        self.assertIn("Router(model_list=[])", result)

    def test_reverse_translate_uses_canonical_litellm_spellings(self):
        source = (
            "from litellm import acompletion, aembedding, image_generation, transcription, ModelResponse\n"
            "response = acompletion(model='openai/gpt-5-mini', messages=[])\n"
        )
        result = to_kopy(source).kopy
        self.assertIn(
            "프롬 라이트엘엘엠 임포트 에이컴플리션, 에이임베딩, 이미지_제너레이션, 트랜스크립션, 모델리스폰스",
            result,
        )
        self.assertIn("에이컴플리션(모델='openai/gpt-5-mini', messages=[])", result)

    def test_litellm_names_are_namespace_scoped(self):
        result = translate(
            "컴플리션 = '사용자 값'\n"
            "리스폰스 = 컴플리션(모델='local', messages=[])\n"
        ).python
        self.assertIn("컴플리션 = '사용자 값'", result)
        self.assertIn("컴플리션(model='local', messages=[])", result)

    def test_import_does_not_rewrite_unrelated_call_keywords(self):
        source = (
            "프롬 라이트엘엘엠 임포트 컴플리션\n"
            "def 재시도(메시지즈, 타임아웃=논):\n"
            "    리턴 메시지즈\n"
            "결과 = 재시도(메시지즈=[], 타임아웃=1)\n"
            "리스폰스 = 컴플리션(모델='openai/gpt-5-mini', messages=[])\n"
        )
        result = translate(source).python
        self.assertIn("재시도(메시지즈=[], 타임아웃=1)", result)
        self.assertIn("completion(model='openai/gpt-5-mini', messages=[])", result)

    def test_keyword_arguments_are_not_pack_global(self):
        pack = pack_by_name("litellm")
        self.assertEqual(pack.keyword_arguments, {})


if __name__ == "__main__":
    unittest.main()
