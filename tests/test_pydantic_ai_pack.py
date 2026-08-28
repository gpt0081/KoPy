import unittest

from kopy.packs.registry import pack_by_name
from kopy.translator import to_kopy, translate


class PydanticAIPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("pydantic-ai")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.kopy_module, "파이댄틱에이아이")

    def test_translate_core_pydantic_ai_api(self):
        source = (
            "프롬 파이댄틱에이아이 임포트 에이전트, 런컨텍스트, 툴, 모델리트라이, 유세이지리밋츠\n"
            "에이전트객체 = 에이전트('test', system_prompt='KoPy')\n"
            "리밋츠 = 유세이지리밋츠(request_limit=3)\n"
        )
        result = translate(source).python
        self.assertIn(
            "from pydantic_ai import Agent, RunContext, Tool, ModelRetry, UsageLimits",
            result,
        )
        self.assertIn("Agent('test', system_prompt='KoPy')", result)
        self.assertIn("UsageLimits(request_limit=3)", result)

    def test_reverse_translate_uses_canonical_spellings(self):
        source = (
            "from pydantic_ai import Agent, RunContext, ModelRetry, ToolOutput, WebSearchTool\n"
            "agent = Agent('test', system_prompt='KoPy')\n"
        )
        result = to_kopy(source).kopy
        self.assertIn(
            "프롬 파이댄틱에이아이 임포트 에이전트, 런컨텍스트, 모델리트라이, 툴아웃풋, 웹서치툴",
            result,
        )
        self.assertIn("에이전트('test', system_prompt='KoPy')", result)

    def test_names_are_namespace_scoped(self):
        result = translate(
            "에이전트 = '사용자 값'\n"
            "결과 = 에이전트('local')\n"
        ).python
        self.assertIn("에이전트 = '사용자 값'", result)
        self.assertIn("에이전트('local')", result)

    def test_import_does_not_rewrite_unrelated_call_keywords(self):
        source = (
            "프롬 파이댄틱에이아이 임포트 에이전트\n"
            "def 실행(시스템_프롬프트, 리퀘스트_리밋=논):\n"
            "    리턴 시스템_프롬프트\n"
            "결과 = 실행(시스템_프롬프트='x', 리퀘스트_리밋=1)\n"
            "에이전트객체 = 에이전트('test', system_prompt='KoPy')\n"
        )
        result = translate(source).python
        self.assertIn("실행(시스템_프롬프트='x', 리퀘스트_리밋=1)", result)
        self.assertIn("Agent('test', system_prompt='KoPy')", result)

    def test_keyword_arguments_are_not_pack_global(self):
        pack = pack_by_name("pydantic-ai")
        self.assertEqual(pack.keyword_arguments, {})


if __name__ == "__main__":
    unittest.main()
