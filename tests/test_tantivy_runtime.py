import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("tantivy"), "tantivy is not installed")
class TantivyRuntimeTests(unittest.TestCase):
    def test_real_in_memory_full_text_search(self):
        source = (
            "임포트 탄티비\n"
            "builder = 탄티비.스키마빌더()\n"
            "builder.add_text_field('title', stored=True)\n"
            "builder.add_text_field('body', stored=True)\n"
            "schema = builder.build()\n"
            "index = 탄티비.인덱스(schema)\n"
            "writer = index.writer(heap_size=15_000_000, num_threads=1)\n"
            "doc1 = 탄티비.도큐먼트()\n"
            "doc1.add_text('title', 'KoPy Python learning')\n"
            "doc1.add_text('body', 'KoPy teaches Python syntax and machine learning libraries')\n"
            "writer.add_document(doc1)\n"
            "doc2 = 탄티비.도큐먼트()\n"
            "doc2.add_text('title', 'Weather report')\n"
            "doc2.add_text('body', 'Rain and wind are expected tomorrow')\n"
            "writer.add_document(doc2)\n"
            "writer.commit()\n"
            "index.reload()\n"
            "searcher = index.searcher()\n"
            "query = index.parse_query('Python KoPy', ['title', 'body'])\n"
            "results = searcher.search(query, 2)\n"
            "score, address = results.hits[0]\n"
            "best_doc = searcher.doc(address)\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)
        results = namespace["results"]
        best_doc = namespace["best_doc"]
        score = namespace["score"]

        self.assertGreaterEqual(len(results.hits), 1)
        self.assertGreater(float(score), 0.0)
        self.assertEqual(best_doc.get_first("title"), "KoPy Python learning")
        self.assertIn("Python", best_doc.get_first("body"))


if __name__ == "__main__":
    unittest.main()
