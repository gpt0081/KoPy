import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class RanxPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("ranx")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "ranx")
        self.assertEqual(pack.kopy_module, "랜엑스")

    def test_run_qrels_and_fuse_translate(self):
        source = (
            "프롬 랜엑스 임포트 큐렐즈, 런, 퓨즈\n"
            "qrels = 큐렐즈(qrels_dict)\n"
            "dense_run = 런(dense_scores, name='dense')\n"
            "lexical_run = 런(lexical_scores, name='bm25')\n"
            "hybrid_run = 퓨즈(runs=[dense_run, lexical_run], method='rrf')\n"
        )
        python_source = translate(source).python
        self.assertIn("from ranx import Qrels, Run, fuse", python_source)
        self.assertIn("qrels = Qrels(qrels_dict)", python_source)
        self.assertIn("dense_run = Run(dense_scores, name='dense')", python_source)
        self.assertIn("fuse(runs=[dense_run, lexical_run], method='rrf')", python_source)

    def test_generic_ir_vocabulary_remains_python(self):
        source = (
            "프롬 랜엑스 임포트 런, 퓨즈\n"
            "dense_run = 런(dense_scores, name='dense')\n"
            "hybrid_run = 퓨즈(runs=[dense_run, lexical_run], norm='min-max', method='sum')\n"
            "score = evaluate(qrels, hybrid_run, 'ndcg@3')\n"
        )
        python_source = translate(source).python
        for token in ("runs=", "norm=", "method=", "evaluate(", "qrels", "hybrid_run"):
            self.assertIn(token, python_source)

    def test_unimported_ranx_words_are_not_global(self):
        source = "combined = lib.퓨즈(runs=runs)\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy_preserves_ir_vocabulary(self):
        source = (
            "from ranx import Qrels, Run, fuse\n"
            "qrels = Qrels(qrels_dict)\n"
            "dense_run = Run(dense_scores, name='dense')\n"
            "hybrid_run = fuse(runs=[dense_run, lexical_run], method='rrf')\n"
            "score = evaluate(qrels, hybrid_run, 'ndcg@3')\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 랜엑스 임포트 큐렐즈, 런, 퓨즈", kopy)
        self.assertIn("큐렐즈(qrels_dict)", kopy)
        self.assertIn("런(dense_scores, name='dense')", kopy)
        self.assertIn("퓨즈(runs=[dense_run, lexical_run], method='rrf')", kopy)
        self.assertIn("evaluate(qrels, hybrid_run", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("랜엑스.퓨즈")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "fuse")


if __name__ == "__main__":
    unittest.main()
