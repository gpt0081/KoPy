import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("ranx"), "ranx is not installed")
class RanxRuntimeTests(unittest.TestCase):
    def test_real_hybrid_rank_fusion_and_evaluation(self):
        source = (
            "프롬 랜엑스 임포트 큐렐즈, 런, 퓨즈, evaluate\n"
            "qrels = 큐렐즈({'q1': {'d2': 1}})\n"
            "dense_run = 런({'q1': {'d1': 0.9, 'd2': 0.8, 'd3': 0.1}}, name='dense')\n"
            "lexical_run = 런({'q1': {'d2': 3.0, 'd1': 2.0, 'd3': 0.1}}, name='bm25')\n"
            "hybrid_run = 퓨즈(\n"
            "    runs=[dense_run, lexical_run],\n"
            "    norm='min-max',\n"
            "    method='sum',\n"
            ")\n"
            "ndcg_at_1 = evaluate(qrels, hybrid_run, 'ndcg@1')\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)

        self.assertAlmostEqual(float(namespace["ndcg_at_1"]), 1.0, places=6)
        hybrid_run = namespace["hybrid_run"]
        # ranx maps method='sum' to its CombSUM implementation, whose default
        # Run name is 'comb_sum'. Verify the real library behavior rather than
        # assuming the method selector is copied into Run.name.
        self.assertEqual(hybrid_run.name, "comb_sum")


if __name__ == "__main__":
    unittest.main()
