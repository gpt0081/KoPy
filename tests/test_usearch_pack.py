import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class USearchPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("usearch")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "usearch")
        self.assertEqual(pack.kopy_module, "유서치")

    def test_usearch_types_translate(self):
        source = (
            "프롬 유서치.index 임포트 인덱스, 매치즈\n"
            "index = 인덱스(ndim=3, metric='cos', dtype='f32')\n"
            "matches: 매치즈 = index.search(query, 2)\n"
        )
        python_source = translate(source).python
        self.assertIn("from usearch.index import Index, Matches", python_source)
        self.assertIn("Index(ndim=3, metric='cos', dtype='f32')", python_source)
        self.assertIn("index.search(query, 2)", python_source)

    def test_generic_vector_search_vocabulary_stays_python(self):
        source = (
            "프롬 유서치.index 임포트 인덱스\n"
            "index = 인덱스(ndim=3)\n"
            "index.add(keys, vectors)\n"
            "matches = index.search(query, 5)\n"
        )
        python_source = translate(source).python
        self.assertIn("index.add(keys, vectors)", python_source)
        self.assertIn("index.search(query, 5)", python_source)

    def test_unimported_words_are_not_global(self):
        source = "index = 유서치.인덱스(ndim=3)\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy_preserves_dotted_module(self):
        source = (
            "from usearch.index import Index\n"
            "index = Index(ndim=4, metric='cos')\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 유서치.index 임포트 인덱스", kopy)
        self.assertIn("인덱스(ndim=4, metric='cos')", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("유서치.인덱스")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "Index")


if __name__ == "__main__":
    unittest.main()
