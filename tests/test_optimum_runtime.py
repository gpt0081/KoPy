import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("optimum"), "Optimum is not installed")
class OptimumRuntimeTests(unittest.TestCase):
    def test_kopy_optimum_tasks_manager_executes(self):
        source = (
            "프롬 옵티멈.exporters.tasks 임포트 태스크매니저\n"
            "태스크들 = 태스크매니저.겟올태스크스()\n"
            "모델클래스 = 태스크매니저.겟모델클래스포태스크('text-classification')\n"
            "정규화 = 태스크매니저.맵프롬시노님('sentiment-analysis')\n"
        )
        namespace: dict[str, object] = {}
        python_source = translate(source).python
        exec(compile(python_source, "<kopy-optimum-smoke>", "exec"), namespace)

        self.assertIn("text-classification", namespace["태스크들"])
        self.assertEqual(namespace["모델클래스"].__name__, "AutoModelForSequenceClassification")
        self.assertEqual(namespace["정규화"], "text-classification")


if __name__ == "__main__":
    unittest.main()
