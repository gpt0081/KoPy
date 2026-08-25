import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("chromadb"), "chromadb is not installed")
class ChromaRuntimeTests(unittest.TestCase):
    def test_real_in_memory_vector_query(self):
        source = (
            "임포트 크로마 애즈 chroma\n"
            "client = chroma.클라이언트()\n"
            "collection = client.크리에이트컬렉션(name='docs', embedding_function=None)\n"
            "collection.add(\n"
            "    ids=['alpha', 'beta'],\n"
            "    embeddings=[[1.0, 0.0], [0.0, 1.0]],\n"
            "    documents=['alpha document', 'beta document'],\n"
            "    metadatas=[{'kind': 'a'}, {'kind': 'b'}],\n"
            ")\n"
            "result = collection.query(\n"
            "    query_embeddings=[[0.99, 0.01]],\n"
            "    n_results=2,\n"
            "    include=['documents', 'metadatas', 'distances'],\n"
            ")\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)
        result = namespace["result"]

        self.assertEqual(result["ids"][0][0], "alpha")
        self.assertEqual(result["documents"][0][0], "alpha document")
        self.assertEqual(result["metadatas"][0][0]["kind"], "a")
        self.assertLess(result["distances"][0][0], result["distances"][0][1])


if __name__ == "__main__":
    unittest.main()
