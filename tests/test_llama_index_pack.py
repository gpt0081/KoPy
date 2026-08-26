import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class LlamaIndexPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("llama-index-core")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "llama_index")
        self.assertEqual(pack.kopy_module, "라마인덱스")

    def test_core_rag_api_translates(self):
        source = (
            "프롬 라마인덱스.core 임포트 도큐먼트, 벡터스토어인덱스, 목임베딩\n"
            "documents = [도큐먼트(text='alpha')]\n"
            "index = 벡터스토어인덱스.from_documents(documents, embed_model=목임베딩(embed_dim=8))\n"
            "retriever = index.as_retriever(similarity_top_k=1)\n"
            "nodes = retriever.retrieve(query)\n"
        )
        python_source = translate(source).python
        self.assertIn("from llama_index.core import Document, VectorStoreIndex, MockEmbedding", python_source)
        self.assertIn("Document(text='alpha')", python_source)
        self.assertIn("VectorStoreIndex.from_documents(documents, embed_model=MockEmbedding(embed_dim=8))", python_source)
        self.assertIn("index.as_retriever(similarity_top_k=1)", python_source)
        self.assertIn("retriever.retrieve(query)", python_source)

    def test_dotted_submodule_path_stays_python_native(self):
        source = (
            "프롬 라마인덱스.core.node_parser 임포트 센텐스스플리터\n"
            "splitter = 센텐스스플리터(chunk_size=128, chunk_overlap=16)\n"
        )
        python_source = translate(source).python
        self.assertIn("from llama_index.core.node_parser import SentenceSplitter", python_source)
        self.assertIn("SentenceSplitter(chunk_size=128, chunk_overlap=16)", python_source)

    def test_transferable_rag_vocabulary_remains_python(self):
        source = (
            "프롬 라마인덱스.core 임포트 벡터스토어인덱스\n"
            "index = 벡터스토어인덱스.from_documents(documents, show_progress=False)\n"
            "retriever = index.as_retriever(similarity_top_k=3)\n"
            "nodes = retriever.retrieve(query)\n"
        )
        python_source = translate(source).python
        for token in ("documents", "index", "retriever", "query", "from_documents(", "as_retriever(", "retrieve(", "similarity_top_k="):
            self.assertIn(token, python_source)

    def test_unimported_members_are_not_global(self):
        source = "index = lib.벡터스토어인덱스(nodes)\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy(self):
        source = (
            "from llama_index.core import Document, VectorStoreIndex, MockEmbedding\n"
            "documents = [Document(text='alpha')]\n"
            "index = VectorStoreIndex.from_documents(documents, embed_model=MockEmbedding(embed_dim=8))\n"
            "retriever = index.as_retriever(similarity_top_k=1)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 라마인덱스.core 임포트 도큐먼트, 벡터스토어인덱스, 목임베딩", kopy)
        self.assertIn("도큐먼트(text='alpha')", kopy)
        self.assertIn("벡터스토어인덱스.from_documents", kopy)
        self.assertIn("index.as_retriever(similarity_top_k=1)", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("라마인덱스.벡터스토어인덱스")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "VectorStoreIndex")


if __name__ == "__main__":
    unittest.main()
