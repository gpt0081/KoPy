import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class FastEmbedPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("fastembed")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "fastembed")
        self.assertEqual(pack.kopy_module, "패스트임베드")

    def test_top_level_embedding_api_translates(self):
        source = (
            "프롬 패스트임베드 임포트 텍스트임베딩, 스파스텍스트임베딩\n"
            "model = 텍스트임베딩(model_name='BAAI/bge-small-en-v1.5')\n"
            "sparse_model = 스파스텍스트임베딩(model_name='Qdrant/bm25')\n"
            "embeddings = list(model.embed(documents))\n"
        )
        python_source = translate(source).python
        self.assertIn("from fastembed import TextEmbedding, SparseTextEmbedding", python_source)
        self.assertIn("model = TextEmbedding(model_name='BAAI/bge-small-en-v1.5')", python_source)
        self.assertIn("sparse_model = SparseTextEmbedding(model_name='Qdrant/bm25')", python_source)
        self.assertIn("model.embed(documents)", python_source)

    def test_cross_encoder_dotted_submodule_path_stays_python_native(self):
        source = (
            "프롬 패스트임베드.rerank.cross_encoder 임포트 텍스트크로스인코더\n"
            "reranker = 텍스트크로스인코더(model_name='Xenova/ms-marco-MiniLM-L-6-v2')\n"
            "scores = list(reranker.rerank(query, documents))\n"
        )
        python_source = translate(source).python
        self.assertIn("from fastembed.rerank.cross_encoder import TextCrossEncoder", python_source)
        self.assertIn("TextCrossEncoder(model_name='Xenova/ms-marco-MiniLM-L-6-v2')", python_source)
        self.assertIn("reranker.rerank(query, documents)", python_source)

    def test_transferable_retrieval_vocabulary_remains_python(self):
        source = (
            "프롬 패스트임베드.rerank.cross_encoder 임포트 텍스트크로스인코더\n"
            "reranker = 텍스트크로스인코더(model_name=model_name)\n"
            "scores = list(reranker.rerank(query, documents))\n"
        )
        python_source = translate(source).python
        for token in ("model_name=", "scores", "query", "documents", ".rerank("):
            self.assertIn(token, python_source)

    def test_unimported_members_are_not_global(self):
        source = "model = lib.텍스트임베딩(model_name='x')\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy(self):
        source = (
            "from fastembed.rerank.cross_encoder import TextCrossEncoder\n"
            "reranker = TextCrossEncoder(model_name='Xenova/ms-marco-MiniLM-L-6-v2')\n"
            "scores = list(reranker.rerank(query, documents))\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 패스트임베드.rerank.cross_encoder 임포트 텍스트크로스인코더", kopy)
        self.assertIn("텍스트크로스인코더(model_name='Xenova/ms-marco-MiniLM-L-6-v2')", kopy)
        self.assertIn("reranker.rerank(query, documents)", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("패스트임베드.텍스트크로스인코더")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "TextCrossEncoder")


if __name__ == "__main__":
    unittest.main()
