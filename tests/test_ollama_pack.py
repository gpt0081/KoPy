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
            "에스디케이 = 클라이언트(호스트='http://localhost:11434', 타임아웃=1.0)\n"
            "리스폰스 = 챗(모델='gemma3', 메시지즈=[{'role': 'user', 'content': '안녕'}], 스트림=펄스, 킵_얼라이브='5m')\n"
            "벡터 = 임베드(모델='embeddinggemma', 인풋='KoPy')\n"
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
        self.assertIn("어싱크클라이언트(호스트='http://localhost:11434', 타임아웃=2.0)", result)
        self.assertIn("챗(모델='gemma3', 메시지즈=[], 스트림=트루, 옵션즈={'temperature': 0.1})", result)

    def test_ollama_names_are_namespace_scoped(self):
        result = translate(
            "메시지즈 = []\n킵_얼라이브 = '5m'\n리스폰스 = 챗(메시지즈=메시지즈, 킵_얼라이브=킵_얼라이브)\n"
        ).python
        self.assertIn("메시지즈 = []", result)
        self.assertIn("킵_얼라이브 = '5m'", result)
        self.assertIn("챗(메시지즈=메시지즈, 킵_얼라이브=킵_얼라이브)", result)

    def test_ollama_keywords_translate_only_at_call_keywords(self):
        source = (
            "프롬 올라마 임포트 챗\n"
            "메시지즈 = []\n"
            "킵_얼라이브 = '10m'\n"
            "리스폰스 = 챗(메시지즈=메시지즈, 킵_얼라이브=킵_얼라이브)\n"
        )
        result = translate(source).python
        self.assertIn("메시지즈 = []", result)
        self.assertIn("킵_얼라이브 = '10m'", result)
        self.assertIn("chat(messages=메시지즈, keep_alive=킵_얼라이브)", result)

        reverse = to_kopy(
            "from ollama import chat\n"
            "messages = []\n"
            "keep_alive = '10m'\n"
            "response = chat(messages=messages, keep_alive=keep_alive)\n"
        ).kopy
        self.assertIn("messages = []", reverse)
        self.assertIn("keep_alive = '10m'", reverse)
        self.assertIn("챗(메시지즈=messages, 킵_얼라이브=keep_alive)", reverse)


if __name__ == "__main__":
    unittest.main()
