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
            "인덱스 = 인덱스(ndim=3, 메트릭='cos', 디타입='f32')\n"
            "matches: 매치즈 = 인덱스.search(쿼리, 2)\n"
        )
        python_source = translate(source).python
        self.assertIn("from usearch.index import Index, Matches", python_source)
        self.assertIn("index = Index(ndim=3, metric='cos', dtype='f32')", python_source)
        self.assertIn("index.search(query, 2)", python_source)

    def test_common_vector_search_identifiers_translate(self):
        source = (
            "프롬 유서치.index 임포트 인덱스\n"
            "인덱스 = 인덱스(ndim=3)\n"
            "인덱스.add(keys, vectors)\n"
            "matches = 인덱스.search(쿼리, 5)\n"
        )
        python_source = translate(source).python
        self.assertIn("index.add(keys, vectors)", python_source)
        self.assertIn("index.search(query, 5)", python_source)

    def test_unimported_pack_name_stays_scoped_but_common_index_translates(self):
        source = "인덱스 = 유서치.인덱스(ndim=3)\n"
        self.assertEqual(translate(source).python, "index = 유서치.index(ndim=3)\n")

    def test_python_to_kopy_preserves_dotted_module_and_round_trips(self):
        source = (
            "from usearch.index import Index\n"
            "index = Index(ndim=4, metric='cos')\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 유서치.index 임포트 인덱스", kopy)
        self.assertIn("인덱스 = 인덱스(ndim=4, 메트릭='cos')", kopy)
        self.assertEqual(translate(kopy).python, source)

    def test_help_resolution(self):
        resolved = resolve_pack_member("유서치.인덱스")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "Index")


if __name__ == "__main__":
    unittest.main()
