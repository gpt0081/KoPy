import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("litellm"), "litellm is not installed")
class LiteLLMRuntimeTests(unittest.TestCase):
    def test_real_exports_are_available_without_provider_credentials(self):
        import litellm

        for name in (
            "completion",
            "acompletion",
            "embedding",
            "aembedding",
            "image_generation",
            "transcription",
            "Router",
            "ModelResponse",
        ):
            self.assertTrue(hasattr(litellm, name), name)

        self.assertTrue(callable(litellm.completion))
        self.assertTrue(callable(litellm.acompletion))
        self.assertTrue(callable(litellm.embedding))
        self.assertTrue(callable(litellm.Router))

    def test_translated_imports_resolve_against_real_library(self):
        source = (
            "프롬 라이트엘엘엠 임포트 컴플리션, 임베딩, 라우터, 모델리스폰스\n"
            "호출가능 = 컴플리션\n"
            "임베딩호출 = 임베딩\n"
            "라우터타입 = 라우터\n"
            "리스폰스타입 = 모델리스폰스\n"
        )
        namespace: dict[str, object] = {}
        exec(compile(translate(source).python, "<kopy-litellm-runtime>", "exec"), namespace)

        self.assertTrue(callable(namespace["호출가능"]))
        self.assertTrue(callable(namespace["임베딩호출"]))
        self.assertTrue(callable(namespace["라우터타입"]))
        self.assertTrue(isinstance(namespace["리스폰스타입"], type))


if __name__ == "__main__":
    unittest.main()
