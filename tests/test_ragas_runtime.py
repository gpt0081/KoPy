import importlib.util
import os
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("ragas"), "ragas is not installed")
class RagasRuntimeTests(unittest.TestCase):
    def test_real_dataset_and_non_llm_metric(self):
        os.environ.setdefault("RAGAS_DO_NOT_TRACK", "true")
        source = (
            "프롬 라가스 임포트 이밸류에이션데이터셋, 싱글턴샘플\n"
            "프롬 라가스.metrics.collections 임포트 논엘엘엠스트링시밀래리티, 디스턴스메저\n"
            "sample = 싱글턴샘플(user_input='Where is the Eiffel Tower?', response='The Eiffel Tower is in Paris.', reference='The Eiffel Tower is in Paris.', retrieved_contexts=['The Eiffel Tower is located in Paris.'])\n"
            "dataset = 이밸류에이션데이터셋(samples=[sample])\n"
            "metric = 논엘엘엠스트링시밀래리티(distance_measure=디스턴스메저.LEVENSHTEIN)\n"
            "result = metric.score(reference=sample.reference, response=sample.response)\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)

        dataset = namespace["dataset"]
        sample = namespace["sample"]
        result = namespace["result"]

        self.assertEqual(len(dataset.samples), 1)
        self.assertEqual(sample.user_input, "Where is the Eiffel Tower?")
        self.assertEqual(sample.retrieved_contexts, ["The Eiffel Tower is located in Paris."])
        self.assertAlmostEqual(float(result.value), 1.0, places=6)


if __name__ == "__main__":
    unittest.main()
