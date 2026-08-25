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
            "client = chroma.클라이언트()\n"
            "collection = client.크리에이트컬렉션(name='docs', embedding_function=None)\n"
            "same = client.겟오어크리에이트컬렉션(name='docs', embedding_function=None)\n"
            "items = client.리스트컬렉션즈()\n"
        )
        python_source = translate(source).python
        self.assertIn("import chromadb as chroma", python_source)
        self.assertIn("client = chroma.Client()", python_source)
        self.assertIn("client.create_collection(name='docs', embedding_function=None)", python_source)
        self.assertIn("client.get_or_create_collection(name='docs', embedding_function=None)", python_source)
        self.assertIn("client.list_collections()", python_source)

    def test_generic_retrieval_methods_remain_python(self):
        source = (
            "임포트 크로마 애즈 chroma\n"
            "client = chroma.클라이언트()\n"
            "collection = client.크리에이트컬렉션(name='docs', embedding_function=None)\n"
            "collection.add(ids=ids, embeddings=embeddings, documents=documents)\n"
            "result = collection.query(query_embeddings=query_embeddings, n_results=2)\n"
            "collection.upsert(ids=ids, embeddings=embeddings)\n"
            "records = collection.get(ids=ids)\n"
        )
        python_source = translate(source).python
        for token in ("collection.add(", "collection.query(", "collection.upsert(", "collection.get("):
            self.assertIn(token, python_source)
        for token in ("ids=", "embeddings=", "documents=", "query_embeddings=", "n_results="):
            self.assertIn(token, python_source)

    def test_unimported_chroma_words_are_not_global(self):
        source = "client.크리에이트컬렉션(name='docs')\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy_preserves_retrieval_vocabulary(self):
        source = (
            "import chromadb as chroma\n"
            "client = chroma.Client()\n"
            "collection = client.create_collection(name='docs', embedding_function=None)\n"
            "collection.add(ids=ids, embeddings=embeddings, documents=documents)\n"
            "result = collection.query(query_embeddings=query_embeddings, n_results=2)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 크로마 애즈 chroma", kopy)
        self.assertIn("client = chroma.클라이언트()", kopy)
        self.assertIn("client.크리에이트컬렉션(", kopy)
        self.assertIn("collection.add(", kopy)
        self.assertIn("collection.query(", kopy)
        for token in ("ids=", "embeddings=", "documents=", "query_embeddings=", "n_results="):
            self.assertIn(token, kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("크로마.퍼시스턴트클라이언트")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "PersistentClient")


if __name__ == "__main__":
    unittest.main()
