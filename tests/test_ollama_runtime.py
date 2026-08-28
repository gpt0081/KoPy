import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("ollama"), "ollama is not installed")
class OllamaRuntimeTests(unittest.TestCase):
    def test_real_client_and_message_types_without_server(self):
        source = (
            "프롬 올라마 임포트 클라이언트, 메시지, 옵션즈\n"
            "에스디케이 = 클라이언트(호스트='http://127.0.0.1:11434', 타임아웃=1.0)\n"
            "메시지객체 = 메시지(role='user', content='KoPy')\n"
            "옵션객체 = 옵션즈(temperature=0.2)\n"
        )
        namespace: dict[str, object] = {}
        exec(compile(translate(source).python, "<kopy-ollama-runtime>", "exec"), namespace)

        client = namespace["에스디케이"]
        message = namespace["메시지객체"]
        options = namespace["옵션객체"]
        self.assertTrue(callable(client.chat))
        self.assertTrue(callable(client.generate))
        self.assertTrue(callable(client.embed))
        self.assertEqual(message.role, "user")
        self.assertEqual(message.content, "KoPy")
        self.assertAlmostEqual(options.temperature, 0.2)

    def test_exported_top_level_functions_exist(self):
        import ollama

        for name in ("chat", "generate", "embed", "pull", "show", "ps", "web_search", "web_fetch"):
            self.assertTrue(callable(getattr(ollama, name)))


if __name__ == "__main__":
    unittest.main()
