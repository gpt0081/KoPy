import unittest

from kopy.translator import translate


class OpenAIAgentsRuntimeTests(unittest.TestCase):
    def test_real_library_exports_and_objects(self):
        from agents import Agent, RunConfig, RunContextWrapper, RunResult, RunState, Runner, function_tool

        self.assertTrue(callable(Agent))
        self.assertTrue(callable(Runner.run_sync))
        self.assertTrue(callable(function_tool))
        self.assertIsNotNone(RunContextWrapper)
        self.assertIsNotNone(RunResult)
        self.assertIsNotNone(RunState)
        self.assertIsInstance(RunConfig(), RunConfig)
        agent = Agent(name="Assistant", instructions="KoPy runtime smoke test")
        self.assertEqual(agent.name, "Assistant")

    def test_translated_code_executes_without_api_call(self):
        source = (
            "프롬 에이전츠 임포트 에이전트, 런컨피그\n"
            "도우미 = 에이전트(name='Assistant', instructions='KoPy')\n"
            "설정 = 런컨피그()\n"
        )
        python_source = translate(source).python
        scope = {}
        exec(python_source, scope, scope)
        self.assertEqual(scope["도우미"].name, "Assistant")


if __name__ == "__main__":
    unittest.main()
