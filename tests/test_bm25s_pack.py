import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class BM25SPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("bm25s")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "bm25s")
        self.assertEqual(pack.kopy_module, "비엠이십오에스")

    def test_bm25_and_tokenize_translate(self):
        source = (
            "임포트 비엠이십오에스 애즈 bm25s\n"
            "corpus_tokens = bm25s.토크나이즈(corpus, show_progress=False)\n"
            "retriever = bm25s.비엠이십오(corpus=corpus)\n"
            "retriever.index(corpus_tokens, show_progress=False)\n"
            "query_tokens = bm25s.토크나이즈([query], show_progress=False)\n"
            "results = retriever.retrieve(query_tokens, k=2, show_progress=False)\n"
        )
        python_source = translate(source).python
        self.assertIn("import bm25s", python_source)
        self.assertIn("bm25s.tokenize(corpus, show_progress=False)", python_source)
        self.assertIn("bm25s.BM25(corpus=corpus)", python_source)
        self.assertIn("retriever.index(corpus_tokens, show_progress=False)", python_source)
        self.assertIn("retriever.retrieve(query_tokens, k=2, show_progress=False)", python_source)

    def test_generic_retrieval_vocabulary_remains_python(self):
        source = (
            "임포트 비엠이십오에스 애즈 bm25s\n"
            "retriever = bm25s.비엠이십오(corpus=corpus)\n"
            "retriever.index(corpus_tokens)\n"
            "results = retriever.retrieve(query_tokens, k=3)\n"
            "documents = results.documents\n"
            "scores = results.scores\n"
        )
        python_source = translate(source).python
        for token in ("retriever.index(", "retriever.retrieve(", "corpus=", "k=", ".documents", ".scores"):
            self.assertIn(token, python_source)

    def test_unimported_bm25s_words_are_not_global(self):
        source = "retriever = lib.비엠이십오()\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy_preserves_retrieval_vocabulary(self):
        source = (
            "import bm25s\n"
            "corpus_tokens = bm25s.tokenize(corpus, show_progress=False)\n"
            "retriever = bm25s.BM25(corpus=corpus)\n"
            "retriever.index(corpus_tokens, show_progress=False)\n"
            "results = retriever.retrieve(query_tokens, k=2, show_progress=False)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 비엠이십오에스", kopy)
        self.assertIn("bm25s.토크나이즈(corpus, show_progress=False)", kopy)
        self.assertIn("bm25s.비엠이십오(corpus=corpus)", kopy)
        self.assertIn("retriever.index(", kopy)
        self.assertIn("retriever.retrieve(", kopy)
        self.assertIn("k=2", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("비엠이십오에스.비엠이십오")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "BM25")


if __name__ == "__main__":
    unittest.main()
