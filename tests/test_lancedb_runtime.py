import importlib.util
import tempfile
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("lancedb"), "lancedb is not installed")
class LanceDBRuntimeTests(unittest.TestCase):
    def test_real_local_vector_search(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            source = (
                "임포트 랜스디비 애즈 lancedb\n"
                "db = lancedb.connect(path)\n"
                "table = db.create_table(\n"
                "    'docs',\n"
                "    data=[\n"
                "        {'id': 'alpha', 'vector': [1.0, 0.0], 'text': 'alpha document'},\n"
                "        {'id': 'beta', 'vector': [0.0, 1.0], 'text': 'beta document'},\n"
                "    ],\n"
                "    mode='overwrite',\n"
                ")\n"
                "query = [0.99, 0.01]\n"
                "results = table.search(query).limit(2).to_list()\n"
            )
            namespace = {"path": tmpdir}
            exec(translate(source).python, namespace)
            results = namespace["results"]

        self.assertEqual(results[0]["id"], "alpha")
        self.assertEqual(results[0]["text"], "alpha document")
        self.assertEqual(len(results), 2)
        self.assertLess(results[0]["_distance"], results[1]["_distance"])


if __name__ == "__main__":
    unittest.main()
