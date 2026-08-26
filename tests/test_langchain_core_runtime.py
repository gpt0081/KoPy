import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("langchain_core"), "langchain-core is not installed")
class LangChainCoreRuntimeTests(unittest.TestCase):
    def test_real_in_memory_vector_search(self):
        source = (
            "프롬 랭체인코어.documents 임포트 도큐먼트\n"
            "프롬 랭체인코어.embeddings 임포트 임베딩즈\n"
            "프롬 랭체인코어.vectorstores 임포트 인메모리벡터스토어\n"
            "class DemoEmbeddings(임베딩즈):\n"
            "    def embed_documents(self, texts):\n"
            "        return [self.embed_query(text) for text in texts]\n"
            "    def embed_query(self, text):\n"
            "        lowered = text.lower()\n"
            "        if 'python' in lowered or 'kopy' in lowered:\n"
            "            return [1.0, 0.0]\n"
            "        return [0.0, 1.0]\n"
            "documents = [\n"
            "    도큐먼트(page_content='KoPy teaches Python syntax.'),\n"
            "    도큐먼트(page_content='Rubber chemistry uses sulfur vulcanization.'),\n"
            "]\n"
            "vector_store = 인메모리벡터스토어(embedding=DemoEmbeddings())\n"
            "vector_store.add_documents(documents=documents)\n"
            "results = vector_store.similarity_search('Python KoPy', k=1)\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)
        results = namespace["results"]
        self.assertEqual(len(results), 1)
        self.assertIn("KoPy", results[0].page_content)


if __name__ == "__main__":
    unittest.main()
