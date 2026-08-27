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
        )
        python_source = translate(source).python
        self.assertIn("import chromadb as chroma", python_source)
        self.assertIn("client = chroma.Client()", python_source)
        self.assertIn("collection = client.create_collection(name='docs', embedding_function=None)", python_source)

    def test_collection_data_methods_translate_in_chroma_scope(self):
        source = (
            "임포트 크로마 애즈 chroma\n"
            "컬렉션.애드(ids=아이디즈, embeddings=임베딩즈, documents=다큐먼츠)\n"
            "리절트 = 컬렉션.쿼리(query_embeddings=쿼리_임베딩즈, n_results=2)\n"
            "컬렉션.업서트(ids=아이디즈, embeddings=임베딩즈)\n"
            "레코즈 = 컬렉션.겟(ids=아이디즈)\n"
        )
        python_source = translate(source).python
        self.assertIn("collection.add(ids=ids, embeddings=embeddings, documents=documents)", python_source)
        self.assertIn("result = collection.query(query_embeddings=query_embeddings, n_results=2)", python_source)
        self.assertIn("collection.upsert(ids=ids, embeddings=embeddings)", python_source)
        self.assertIn("records = collection.get(ids=ids)", python_source)

    def test_unimported_chroma_methods_are_not_global(self):
        source = "컬렉션.업서트(ids=아이디즈)\n"
        python_source = translate(source).python
        self.assertIn("collection.업서트(ids=ids)", python_source)

    def test_python_to_kopy_transliterates_collection_methods(self):
        source = (
            "import chromadb as chroma\n"
            "client = chroma.Client()\n"
            "collection = client.create_collection(name='docs', embedding_function=None)\n"
            "collection.add(ids=ids, embeddings=embeddings, documents=documents)\n"
            "result = collection.query(query_embeddings=query_embeddings, n_results=2)\n"
            "collection.upsert(ids=ids, embeddings=embeddings)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 크로마 애즈 chroma", kopy)
        self.assertIn("클라이언트 = chroma.클라이언트()", kopy)
        self.assertIn("컬렉션 = 클라이언트.크리에이트컬렉션(", kopy)
        self.assertIn("컬렉션.애드(", kopy)
        self.assertIn("컬렉션.쿼리(", kopy)
        self.assertIn("컬렉션.업서트(", kopy)
        self.assertIn("리절트 =", kopy)
        self.assertIn("아이디즈=아이디즈", kopy)
        self.assertIn("임베딩즈=임베딩즈", kopy)
        self.assertIn("다큐먼츠=다큐먼츠", kopy)
        self.assertIn("쿼리_임베딩즈=쿼리_임베딩즈", kopy)
        self.assertIn("n_results=2", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("크로마.업서트")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "upsert")


if __name__ == "__main__":
    unittest.main()
