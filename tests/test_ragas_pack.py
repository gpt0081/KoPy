import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class RagasPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("ragas")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "ragas")
        self.assertEqual(pack.kopy_module, "라가스")

    def test_dataset_api_translates(self):
        source = (
            "프롬 라가스 임포트 이밸류에이션데이터셋, 싱글턴샘플\n"
            "sample = 싱글턴샘플(user_input=쿼리, 리스폰스=리스폰스, 레퍼런스=레퍼런스, retrieved_contexts=contexts)\n"
            "dataset = 이밸류에이션데이터셋(samples=[sample])\n"
        )
        python_source = translate(source).python
        self.assertIn("from ragas import EvaluationDataset, SingleTurnSample", python_source)
        self.assertIn("SingleTurnSample(user_input=query, response=response, reference=reference, retrieved_contexts=contexts)", python_source)
        self.assertIn("EvaluationDataset(samples=[sample])", python_source)

    def test_collections_metric_dotted_path_stays_python_native(self):
        source = (
            "프롬 라가스.metrics.collections 임포트 논엘엘엠스트링시밀래리티, 디스턴스메저\n"
            "메트릭 = 논엘엘엠스트링시밀래리티(distance_measure=디스턴스메저.LEVENSHTEIN)\n"
            "리절트 = 메트릭.score(레퍼런스=레퍼런스, 리스폰스=리스폰스)\n"
        )
        python_source = translate(source).python
        self.assertIn("from ragas.metrics.collections import NonLLMStringSimilarity, DistanceMeasure", python_source)
        self.assertIn("metric = NonLLMStringSimilarity(distance_measure=DistanceMeasure.LEVENSHTEIN)", python_source)
        self.assertIn("result = metric.score(reference=reference, response=response)", python_source)

    def test_python_spellings_remain_accepted(self):
        source = (
            "프롬 라가스 임포트 싱글턴샘플\n"
            "sample = 싱글턴샘플(user_input=query, response=response, reference=reference, retrieved_contexts=contexts)\n"
            "result = evaluate(dataset=dataset, metrics=metrics)\n"
        )
        python_source = translate(source).python
        for token in ("user_input=", "response=", "reference=", "retrieved_contexts=", "evaluate(", "metrics="):
            self.assertIn(token, python_source)

    def test_unimported_members_are_not_global(self):
        source = "메트릭 = lib.논엘엘엠스트링시밀래리티()\n"
        translated = translate(source).python
        self.assertEqual(translated, "metric = lib.논엘엘엠스트링시밀래리티()\n")

    def test_python_to_kopy(self):
        source = (
            "from ragas.metrics.collections import NonLLMStringSimilarity, DistanceMeasure\n"
            "metric = NonLLMStringSimilarity(distance_measure=DistanceMeasure.LEVENSHTEIN)\n"
            "result = metric.score(reference=reference, response=response)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 라가스.metrics.collections 임포트 논엘엘엠스트링시밀래리티, 디스턴스메저", kopy)
        self.assertIn("메트릭 = 논엘엘엠스트링시밀래리티(distance_measure=디스턴스메저.LEVENSHTEIN)", kopy)
        self.assertIn("리절트 = 메트릭.score(레퍼런스=레퍼런스, 리스폰스=리스폰스)", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("라가스.논엘엘엠스트링시밀래리티")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "NonLLMStringSimilarity")


if __name__ == "__main__":
    unittest.main()
