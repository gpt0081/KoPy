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
            "인덱스 = faiss.인덱스플랫엘2(384)\n"
            "faiss.노멀라이즈엘2(임베딩즈)\n"
            "factory = faiss.인덱스팩토리(384, 'Flat')\n"
        )
        python_source = translate(source).python
        self.assertIn("import faiss as faiss", python_source)
        self.assertIn("index = faiss.IndexFlatL2(384)", python_source)
        self.assertIn("faiss.normalize_L2(embeddings)", python_source)
        self.assertIn("faiss.index_factory(384, 'Flat')", python_source)

    def test_generic_index_methods_stay_upstream_python(self):
        source = (
            "임포트 파이스 애즈 faiss\n"
            "인덱스 = faiss.인덱스플랫엘2(4)\n"
            "인덱스.add(vectors)\n"
            "디스턴시즈, 인디시즈 = 인덱스.search(쿼리, 2)\n"
        )
        python_source = translate(source).python
        self.assertIn("index.add(vectors)", python_source)
        self.assertIn("distances, indices = index.search(query, 2)", python_source)

    def test_unimported_faiss_words_are_not_pack_global(self):
        source = "인덱스 = faiss.인덱스플랫엘2(4)\n"
        python_source = translate(source).python
        self.assertIn("index = faiss.인덱스플랫엘2(4)", python_source)

    def test_python_to_kopy(self):
        source = (
            "import faiss\n"
            "index = faiss.IndexFlatIP(768)\n"
            "faiss.normalize_L2(embeddings)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 파이스", kopy)
        self.assertIn("인덱스 = 파이스.인덱스플랫아이피", kopy)
        self.assertIn("파이스.노멀라이즈엘2(임베딩즈)", kopy)

    def test_python_alias_is_preserved(self):
        source = (
            "import faiss as fx\n"
            "index = fx.IndexFlatL2(4)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 파이스 애즈 fx", kopy)
        self.assertIn("인덱스 = fx.인덱스플랫엘2(4)", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("파이스.인덱스플랫엘2")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "IndexFlatL2")


if __name__ == "__main__":
    unittest.main()
