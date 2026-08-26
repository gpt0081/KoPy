import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class TantivyPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("tantivy")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "tantivy")
        self.assertEqual(pack.kopy_module, "탄티비")

    def test_tantivy_types_translate(self):
        source = (
            "임포트 탄티비\n"
            "builder = 탄티비.스키마빌더()\n"
            "schema = builder.build()\n"
            "index = 탄티비.인덱스(schema)\n"
            "doc = 탄티비.도큐먼트()\n"
        )
        python_source = translate(source).python
        self.assertIn("import tantivy", python_source)
        self.assertIn("tantivy.SchemaBuilder()", python_source)
        self.assertIn("tantivy.Index(schema)", python_source)
        self.assertIn("tantivy.Document()", python_source)

    def test_generic_search_vocabulary_stays_python(self):
        source = (
            "임포트 탄티비\n"
            "index = 탄티비.인덱스(schema)\n"
            "writer = index.writer()\n"
            "writer.add_document(doc)\n"
            "writer.commit()\n"
            "searcher = index.searcher()\n"
            "query = index.parse_query('python', ['body'])\n"
            "results = searcher.search(query, 5)\n"
        )
        python_source = translate(source).python
        self.assertIn("writer = index.writer()", python_source)
        self.assertIn("writer.add_document(doc)", python_source)
        self.assertIn("writer.commit()", python_source)
        self.assertIn("query = index.parse_query('python', ['body'])", python_source)
        self.assertIn("results = searcher.search(query, 5)", python_source)

    def test_unimported_words_are_not_global(self):
        source = "index = 탄티비.인덱스(schema)\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy_preserves_search_methods(self):
        source = (
            "import tantivy\n"
            "builder = tantivy.SchemaBuilder()\n"
            "index = tantivy.Index(schema)\n"
            "results = index.searcher().search(query, 3)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 탄티비", kopy)
        self.assertIn("탄티비.스키마빌더()", kopy)
        self.assertIn("탄티비.인덱스(schema)", kopy)
        self.assertIn(".search(query, 3)", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("탄티비.스키마빌더")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "SchemaBuilder")


if __name__ == "__main__":
    unittest.main()
