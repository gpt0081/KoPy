import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class FaissPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("faiss")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "faiss")
        self.assertEqual(pack.kopy_module, "파이스")

    def test_faiss_specific_members_translate(self):
        source = (
            "임포트 파이스 애즈 faiss\n"
            "index = faiss.인덱스플랫엘투(384)\n"
            "faiss.노멀라이즈엘투(embeddings)\n"
            "factory = faiss.인덱스팩토리(384, 'Flat')\n"
        )
        python_source = translate(source).python
        self.assertIn("import faiss as faiss", python_source)
        self.assertIn("faiss.IndexFlatL2(384)", python_source)
        self.assertIn("faiss.normalize_L2(embeddings)", python_source)
        self.assertIn("faiss.index_factory(384, 'Flat')", python_source)

    def test_generic_index_methods_remain_upstream_python(self):
        source = (
            "임포트 파이스 애즈 faiss\n"
            "index = faiss.인덱스플랫엘투(4)\n"
            "index.add(vectors)\n"
            "distances, indices = index.search(query, 2)\n"
        )
        python_source = translate(source).python
        self.assertIn("index.add(vectors)", python_source)
        self.assertIn("index.search(query, 2)", python_source)

    def test_unimported_faiss_words_are_not_global(self):
        source = "index = faiss.인덱스플랫엘투(4)\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy(self):
        source = (
            "import faiss\n"
            "index = faiss.IndexFlatIP(768)\n"
            "faiss.normalize_L2(embeddings)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 파이스", kopy)
        self.assertIn("파이스.인덱스플랫아이피", kopy)
        self.assertIn("파이스.노멀라이즈엘투", kopy)

    def test_python_alias_is_preserved_for_transfer_learning(self):
        source = (
            "import faiss as fx\n"
            "index = fx.IndexFlatL2(4)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 파이스 애즈 fx", kopy)
        self.assertIn("fx.인덱스플랫엘투(4)", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("파이스.인덱스플랫엘투")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "IndexFlatL2")


if __name__ == "__main__":
    unittest.main()
