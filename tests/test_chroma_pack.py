import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class ChromaPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("chroma")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "chromadb")
        self.assertEqual(pack.kopy_module, "크로마")

    def test_client_and_collection_management_translate(self):
        source = (
            "임포트 크로마 애즈 chroma\n"
            "클라이언트 = chroma.클라이언트()\n"
            "컬렉션 = 클라이언트.크리에이트컬렉션(name='docs', embedding_function=None)\n"
            "세임 = 클라이언트.겟오어크리에이트컬렉션(name='docs', embedding_function=None)\n"
            "아이템즈 = 클라이언트.리스트컬렉션즈()\n"
        )
        python_source = translate(source).python
        self.assertIn("import chromadb as chroma", python_source)
        self.assertIn("클라이언트 = chroma.Client()", python_source)
        self.assertIn("클라이언트.create_collection(name='docs', embedding_function=None)", python_source)
        self.assertIn("클라이언트.get_or_create_collection(name='docs', embedding_function=None)", python_source)
        self.assertIn("클라이언트.list_collections()", python_source)

    def test_collection_data_methods_translate_in_chroma_scope(self):
        source = (
            "임포트 크로마 애즈 chroma\n"
            "컬렉션.애드(ids=ids, embeddings=임베딩즈, documents=다큐먼츠)\n"
            "리절트 = 컬렉션.쿼리(query_embeddings=query_embeddings, n_results=2)\n"
            "컬렉션.업서트(ids=ids, embeddings=임베딩즈)\n"
            "레코즈 = 컬렉션.겟(ids=ids)\n"
        )
        python_source = translate(source).python
        self.assertIn("컬렉션.add(", python_source)
        self.assertIn("컬렉션.query(", python_source)
        self.assertIn("컬렉션.upsert(", python_source)
        self.assertIn("컬렉션.get(", python_source)
        self.assertIn("embeddings=embeddings", python_source)
        self.assertIn("documents=documents", python_source)

    def test_unimported_chroma_methods_are_not_global(self):
        source = "컬렉션.업서트(ids=ids)\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy_transliterates_collection_methods(self):
        source = (
            "import chromadb as chroma\n"
            "collection.add(ids=ids, embeddings=embeddings, documents=documents)\n"
            "result = collection.query(query_embeddings=query_embeddings, n_results=2)\n"
            "collection.upsert(ids=ids, embeddings=embeddings)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 크로마 애즈 chroma", kopy)
        self.assertIn("collection.애드(", kopy)
        self.assertIn("collection.쿼리(", kopy)
        self.assertIn("collection.업서트(", kopy)
        self.assertIn("리절트 =", kopy)
        self.assertIn("임베딩즈=임베딩즈", kopy)
        self.assertIn("다큐먼츠=다큐먼츠", kopy)
        for token in ("ids=", "query_embeddings=", "n_results="):
            self.assertIn(token, kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("크로마.업서트")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "upsert")


if __name__ == "__main__":
    unittest.main()
