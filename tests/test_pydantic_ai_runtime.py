import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("pydantic_ai"), "pydantic-ai is not installed")
class PydanticAIRuntimeTests(unittest.TestCase):
    def test_real_exports_are_available_without_provider_credentials(self):
        import pydantic_ai

        for name in (
            "Agent",
            "RunContext",
            "Tool",
            "ModelRetry",
            "UsageLimits",
            "AgentRunResult",
            "BinaryContent",
            "ImageUrl",
            "ToolOutput",
            "NativeOutput",
            "PromptedOutput",
            "TextOutput",
            "WebSearchTool",
            "CodeExecutionTool",
            "Embedder",
        ):
            self.assertTrue(hasattr(pydantic_ai, name), name)

        limits = pydantic_ai.UsageLimits(request_limit=3)
        self.assertEqual(limits.request_limit, 3)

    def test_translated_imports_resolve_against_real_library(self):
        source = (
            "프롬 파이댄틱에이아이 임포트 에이전트, 런컨텍스트, 툴, 모델리트라이, 유세이지리밋츠\n"
            "에이전트타입 = 에이전트\n"
            "컨텍스트타입 = 런컨텍스트\n"
            "툴타입 = 툴\n"
            "리트라이타입 = 모델리트라이\n"
            "리밋츠 = 유세이지리밋츠(request_limit=2)\n"
        )
        namespace: dict[str, object] = {}
        exec(compile(translate(source).python, "<kopy-pydantic-ai-runtime>", "exec"), namespace)

        self.assertTrue(isinstance(namespace["에이전트타입"], type))
        self.assertTrue(isinstance(namespace["컨텍스트타입"], type))
        self.assertTrue(isinstance(namespace["툴타입"], type))
        self.assertTrue(issubclass(namespace["리트라이타입"], Exception))
        self.assertEqual(namespace["리밋츠"].request_limit, 2)


if __name__ == "__main__":
    unittest.main()
