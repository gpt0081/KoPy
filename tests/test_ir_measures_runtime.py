import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("ir_measures"), "ir-measures is not installed")
class IrMeasuresRuntimeTests(unittest.TestCase):
    def test_real_retrieval_metrics(self):
        source = (
            "프롬 아이알메저스 임포트 캘크어그리게이트, 파스메저, nDCG, P, RR\n"
            "qrels = {'q1': {'d1': 1, 'd2': 0}}\n"
            "run = {'q1': {'d1': 2.0, 'd2': 1.0}}\n"
            "metrics = 캘크어그리게이트([nDCG@2, P@1, RR], qrels, run)\n"
            "parsed = 파스메저('nDCG@2')\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)

        metrics = namespace["metrics"]
        values = {str(measure): float(value) for measure, value in metrics.items()}
        self.assertAlmostEqual(values["nDCG@2"], 1.0, places=6)
        self.assertAlmostEqual(values["P@1"], 1.0, places=6)
        self.assertAlmostEqual(values["RR"], 1.0, places=6)
        self.assertEqual(str(namespace["parsed"]), "nDCG@2")


if __name__ == "__main__":
    unittest.main()
