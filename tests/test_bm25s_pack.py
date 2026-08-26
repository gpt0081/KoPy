import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class BM25SPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("bm25s")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "bm25s")
        self.assertEqual(pack.kopy_module, "비엠25에스")

    def test_bm25_and_tokenize_translate(self):
        source = (
            "임포트 비엠25에스 애즈 bm25s\n"
            "코퍼스_토큰즈 = bm25s.토크나이즈(코퍼스, show_progress=False)\n"
            "리트리버 = bm25s.비엠25(코퍼스=코퍼스)\n"
            "리트리버.index(코퍼스_토큰즈, show_progress=False)\n"
            "쿼리_토큰즈 = bm25s.토크나이즈([쿼리], show_progress=False)\n"
            "리절츠 = 리트리버.retrieve(쿼리_토큰즈, k=2, show_progress=False)\n"
        )
        python_source = translate(source).python
        self.assertIn("import bm25s", python_source)
        self.assertIn("corpus_tokens = bm25s.tokenize(corpus, show_progress=False)", python_source)
        self.assertIn("retriever = bm25s.BM25(corpus=corpus)", python_source)
        self.assertIn("retriever.index(corpus_tokens, show_progress=False)", python_source)
        self.assertIn("retriever.retrieve(query_tokens, k=2, show_progress=False)", python_source)

    def test_stable_retrieval_parameters_remain_python(self):
        source = (
            "임포트 비엠25에스 애즈 bm25s\n"
            "리트리버 = bm25s.비엠25(코퍼스=코퍼스)\n"
            "리트리버.index(코퍼스_토큰즈)\n"
            "리절츠 = 리트리버.retrieve(쿼리_토큰즈, k=3)\n"
        )
        python_source = translate(source).python
        for token in ("retriever.index(", "retriever.retrieve(", "corpus=", "k="):
            self.assertIn(token, python_source)

    def test_unimported_bm25s_words_are_not_pack_global(self):
        source = "리트리버 = lib.비엠25()\n"
        python_source = translate(source).python
        self.assertIn("retriever = lib.비엠25()", python_source)

    def test_python_to_kopy_transliterates_common_identifiers(self):
        source = (
            "import bm25s\n"
            "corpus_tokens = bm25s.tokenize(corpus, show_progress=False)\n"
            "retriever = bm25s.BM25(corpus=corpus)\n"
            "retriever.index(corpus_tokens, show_progress=False)\n"
            "results = retriever.retrieve(query_tokens, k=2, show_progress=False)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 비엠25에스", kopy)
        self.assertIn("비엠25에스.토크나이즈(코퍼스, show_progress=펄스)", kopy)
        self.assertIn("리트리버 = 비엠25에스.비엠25(코퍼스=코퍼스)", kopy)
        self.assertIn("리트리버.index(", kopy)
        self.assertIn("리트리버.retrieve(", kopy)
        self.assertIn("k=2", kopy)
        self.assertIn("show_progress=펄스", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("비엠25에스.비엠25")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "BM25")


if __name__ == "__main__":
    unittest.main()
