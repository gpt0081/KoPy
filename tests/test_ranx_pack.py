import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class RanxPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("ranx")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "ranx")
        self.assertEqual(pack.kopy_module, "랜엑스")

    def test_run_qrels_fuse_and_evaluate_translate(self):
        source = (
            "프롬 랜엑스 임포트 큐렐즈, 런, 퓨즈, 이밸류에이트\n"
            "큐렐즈 = 큐렐즈(qrels_dict)\n"
            "덴스_런 = 런(dense_scores, 네임='dense')\n"
            "렉시컬_런 = 런(lexical_scores, 네임='bm25')\n"
            "하이브리드_런 = 퓨즈(런즈=[덴스_런, 렉시컬_런], 메서드='rrf')\n"
            "스코어 = 이밸류에이트(큐렐즈, 하이브리드_런, 'ndcg@3')\n"
        )
        python_source = translate(source).python
        self.assertIn("from ranx import Qrels, Run, fuse, evaluate", python_source)
        self.assertIn("qrels = Qrels(qrels_dict)", python_source)
        self.assertIn("dense_run = Run(dense_scores, name='dense')", python_source)
        self.assertIn("fuse(runs=[dense_run, lexical_run], method='rrf')", python_source)
        self.assertIn("score = evaluate(qrels, hybrid_run, 'ndcg@3')", python_source)

    def test_ir_signature_vocabulary_is_transliterated(self):
        source = (
            "프롬 랜엑스 임포트 런, 퓨즈\n"
            "덴스_런 = 런(dense_scores, 네임='dense')\n"
            "하이브리드_런 = 퓨즈(런즈=[덴스_런, 렉시컬_런], 노름='min-max', 메서드='sum')\n"
        )
        python_source = translate(source).python
        for token in ("runs=", "norm=", "method=", "dense_run", "hybrid_run"):
            self.assertIn(token, python_source)

    def test_unimported_ranx_words_are_not_global(self):
        source = "combined = lib.퓨즈(런즈=런즈)\n"
        translated = translate(source).python
        self.assertIn("lib.퓨즈", translated)
        self.assertIn("runs=runs", translated)

    def test_python_to_kopy_transliterates_ir_vocabulary(self):
        source = (
            "from ranx import Qrels, Run, fuse, evaluate\n"
            "qrels = Qrels(qrels_dict)\n"
            "dense_run = Run(dense_scores, name='dense')\n"
            "hybrid_run = fuse(runs=[dense_run, lexical_run], method='rrf')\n"
            "score = evaluate(qrels, hybrid_run, 'ndcg@3')\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 랜엑스 임포트 큐렐즈, 런, 퓨즈, 이밸류에이트", kopy)
        self.assertIn("큐렐즈 = 큐렐즈(qrels_dict)", kopy)
        self.assertIn("덴스_런 = 런(dense_scores, 네임='dense')", kopy)
        self.assertIn("하이브리드_런 = 퓨즈(런즈=[덴스_런, 렉시컬_런], 메서드='rrf')", kopy)
        self.assertIn("스코어 = 이밸류에이트(큐렐즈, 하이브리드_런", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("랜엑스.이밸류에이트")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "evaluate")


if __name__ == "__main__":
    unittest.main()
