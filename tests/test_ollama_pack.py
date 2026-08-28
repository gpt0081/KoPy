import unittest

from kopy.packs.registry import pack_by_name
from kopy.translator import to_kopy, translate


class OllamaPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("ollama")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.kopy_module, "올라마")

    def test_translate_core_ollama_api(self):
        source = (
            "프롬 올라마 임포트 클라이언트, 챗, 임베드\n"
            "에스디케이 = 클라이언트(host='http://localhost:11434', timeout=1.0)\n"
            "리스폰스 = 챗(model='gemma3', messages=[{'role': 'user', 'content': '안녕'}], stream=펄스, keep_alive='5m')\n"
            "벡터 = 임베드(model='embeddinggemma', input='KoPy')\n"
        )
        result = translate(source).python
        self.assertIn("from ollama import Client, chat, embed", result)
        self.assertIn("Client(host='http://localhost:11434', timeout=1.0)", result)
        self.assertIn("chat(model='gemma3', messages=[{'role': 'user', 'content': '안녕'}], stream=False, keep_alive='5m')", result)
        self.assertIn("embed(model='embeddinggemma', input='KoPy')", result)

    def test_reverse_translate_uses_canonical_ollama_spellings(self):
        source = (
            "from ollama import AsyncClient, ChatResponse, ResponseError, chat, web_search\n"
            "sdk = AsyncClient(host='http://localhost:11434', timeout=2.0)\n"
            "response = chat(model='gemma3', messages=[], stream=True, options={'temperature': 0.1})\n"
        )
        result = to_kopy(source).kopy
        self.assertIn("프롬 올라마 임포트 어싱크클라이언트, 챗리스폰스, 리스폰스에러, 챗, 웹_서치", result)
        self.assertIn("어싱크클라이언트(host='http://localhost:11434', timeout=2.0)", result)
        self.assertIn("챗(model='gemma3', messages=[], stream=트루, options={'temperature': 0.1})", result)

    def test_ollama_names_are_namespace_scoped(self):
        result = translate(
            "메시지즈 = []\n킵_얼라이브 = '5m'\n리스폰스 = 챗(messages=메시지즈, keep_alive=킵_얼라이브)\n"
        ).python
        self.assertIn("메시지즈 = []", result)
        self.assertIn("킵_얼라이브 = '5m'", result)
        self.assertIn("챗(messages=메시지즈, keep_alive=킵_얼라이브)", result)

    def test_ollama_import_does_not_rewrite_unrelated_call_keywords(self):
        source = (
            "프롬 올라마 임포트 챗\n"
            "def 재시도(타임아웃, 헤더즈=논):\n"
            "    리턴 타임아웃\n"
            "결과 = 재시도(타임아웃=1, 헤더즈={'x': 'y'})\n"
            "리스폰스 = 챗(model='gemma3', messages=[])\n"
        )
        result = translate(source).python
        self.assertIn("def 재시도(타임아웃, 헤더즈=None):", result)
        self.assertIn("재시도(타임아웃=1, 헤더즈={'x': 'y'})", result)
        self.assertIn("chat(model='gemma3', messages=[])", result)

    def test_ollama_keyword_arguments_remain_python_for_now(self):
        pack = pack_by_name("ollama")
        self.assertEqual(pack.keyword_arguments, {})


if __name__ == "__main__":
    unittest.main()
