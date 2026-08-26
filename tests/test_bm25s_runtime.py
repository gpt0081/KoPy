import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("bm25s"), "bm25s is not installed")
class BM25SRuntimeTests(unittest.TestCase):
    def test_real_lexical_retrieval(self):
        source = (
            "임포트 비엠25에스 애즈 bm25s\n"
            "코퍼스 = [\n"
            "    'machine learning uses data',\n"
            "    'rubber chemistry uses vulcanization additives',\n"
            "    'vector search retrieves documents',\n"
            "]\n"
            "코퍼스_토큰즈 = bm25s.토크나이즈(코퍼스, show_progress=False)\n"
            "리트리버 = bm25s.비엠25(코퍼스=코퍼스)\n"
            "리트리버.index(코퍼스_토큰즈, show_progress=False)\n"
            "쿼리 = 'rubber vulcanization'\n"
            "쿼리_토큰즈 = bm25s.토크나이즈([쿼리], show_progress=False)\n"
            "리절츠 = 리트리버.retrieve(쿼리_토큰즈, k=2, show_progress=False)\n"
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
