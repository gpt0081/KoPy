import unittest

from kopy.packs.registry import pack_by_name
from kopy.translator import to_kopy, translate


class OpenAIAgentsPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("openai-agents")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "agents")
        self.assertEqual(pack.kopy_module, "에이전츠")

    def test_translate_core_agents_api(self):
        source = (
            "프롬 에이전츠 임포트 에이전트, 러너, 런컨피그, 펑션_툴\n"
            "도우미 = 에이전트(name='Assistant', instructions='KoPy')\n"
            "설정 = 런컨피그()\n"
        )
        result = translate(source).python
        self.assertIn("from agents import Agent, Runner, RunConfig, function_tool", result)
        self.assertIn("Agent(name='Assistant', instructions='KoPy')", result)
        self.assertIn("RunConfig()", result)

    def test_reverse_translate_uses_canonical_spellings(self):
        source = (
            "from agents import Agent, Runner, RunContextWrapper, RunState, function_tool\n"
            "assistant = Agent(name='Assistant', instructions='KoPy')\n"
        )
        result = to_kopy(source).kopy
        self.assertIn(
            "프롬 에이전츠 임포트 에이전트, 러너, 런컨텍스트래퍼, 런스테이트, 펑션_툴",
            result,
        )
        self.assertIn("에이전트(네임='Assistant', instructions='KoPy')", result)

    def test_names_are_namespace_scoped(self):
        result = translate(
            "에이전트 = '사용자 값'\n"
            "러너 = lambda 값: 값\n"
            "결과 = 러너(에이전트)\n"
        ).python
        self.assertIn("에이전트 = '사용자 값'", result)
        self.assertIn("결과 = 러너(에이전트)", result)

    def test_import_does_not_rewrite_unrelated_call_keywords(self):
        source = (
            "프롬 에이전츠 임포트 에이전트\n"
            "def 실행(커스텀옵션, 인스트럭션즈=논, 툴즈=논):\n"
            "    리턴 커스텀옵션\n"
            "결과 = 실행(커스텀옵션='x', 인스트럭션즈='y', 툴즈=[])\n"
            "도우미 = 에이전트(name='Assistant', instructions='KoPy')\n"
        )
        result = translate(source).python
        self.assertIn("실행(커스텀옵션='x', 인스트럭션즈='y', 툴즈=[])", result)
        self.assertIn("Agent(name='Assistant', instructions='KoPy')", result)

    def test_keyword_arguments_are_not_pack_global(self):
        pack = pack_by_name("openai-agents")
        self.assertEqual(pack.keyword_arguments, {})


if __name__ == "__main__":
    unittest.main()
