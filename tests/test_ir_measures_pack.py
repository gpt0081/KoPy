import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class IrMeasuresPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("ir-measures")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "ir_measures")
        self.assertEqual(pack.kopy_module, "아이알메저스")

    def test_ir_measures_entry_points_translate(self):
        source = (
            "프롬 아이알메저스 임포트 캘크어그리게이트, 파스메저, 큐렐, 스코어드독, nDCG, P, RR\n"
            "metric = 파스메저('nDCG@10')\n"
            "qrel = 큐렐('q1', 'd1', 1)\n"
            "doc = 스코어드독('q1', 'd1', 2.0)\n"
            "scores = 캘크어그리게이트([nDCG@10, P@5, RR], qrels, run)\n"
        )
        python_source = translate(source).python
        self.assertIn("from ir_measures import calc_aggregate, parse_measure, Qrel, ScoredDoc, nDCG, P, RR", python_source)
        self.assertIn("metric = parse_measure('nDCG@10')", python_source)
        self.assertIn("qrel = Qrel('q1', 'd1', 1)", python_source)
        self.assertIn("doc = ScoredDoc('q1', 'd1', 2.0)", python_source)
        self.assertIn("calc_aggregate([nDCG@10, P@5, RR], qrels, run)", python_source)

    def test_standard_ir_vocabulary_remains_python(self):
        source = (
            "프롬 아이알메저스 임포트 캘크어그리게이트, nDCG, P, RR\n"
            "metrics = 캘크어그리게이트([nDCG@10, P@5, RR], qrels, run)\n"
        )
        python_source = translate(source).python
        for token in ("qrels", "run", "nDCG@10", "P@5", "RR"):
            self.assertIn(token, python_source)

    def test_unimported_words_are_not_global(self):
        source = "metrics = lib.캘크어그리게이트(measures, qrels, run)\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy_preserves_metric_symbols(self):
        source = (
            "from ir_measures import calc_aggregate, parse_measure, nDCG, P, RR\n"
            "metric = parse_measure('nDCG@10')\n"
            "scores = calc_aggregate([nDCG@10, P@5, RR], qrels, run)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 아이알메저스 임포트 캘크어그리게이트, 파스메저, nDCG, P, RR", kopy)
        self.assertIn("파스메저('nDCG@10')", kopy)
        self.assertIn("캘크어그리게이트([nDCG@10, P@5, RR], qrels, run)", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("아이알메저스.캘크어그리게이트")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "calc_aggregate")


if __name__ == "__main__":
    unittest.main()
