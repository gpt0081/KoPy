import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("bm25s"), "bm25s is not installed")
class BM25SRuntimeTests(unittest.TestCase):
    def test_real_lexical_retrieval(self):
        source = (
            "임포트 비엠이십오에스 애즈 bm25s\n"
            "corpus = [\n"
            "    'machine learning uses data',\n"
            "    'rubber chemistry uses vulcanization additives',\n"
            "    'vector search retrieves documents',\n"
            "]\n"
            "corpus_tokens = bm25s.토크나이즈(corpus, show_progress=False)\n"
            "retriever = bm25s.비엠이십오(corpus=corpus)\n"
            "retriever.index(corpus_tokens, show_progress=False)\n"
            "query = 'rubber vulcanization'\n"
            "query_tokens = bm25s.토크나이즈([query], show_progress=False)\n"
            "results = retriever.retrieve(query_tokens, k=2, show_progress=False)\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)
        results = namespace["results"]

        self.assertEqual(results.documents.shape, (1, 2))
        self.assertEqual(results.scores.shape, (1, 2))
        self.assertEqual(results.documents[0][0], "rubber chemistry uses vulcanization additives")
        self.assertGreaterEqual(results.scores[0][0], results.scores[0][1])


if __name__ == "__main__":
    unittest.main()
