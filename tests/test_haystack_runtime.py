import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("haystack"), "haystack-ai is not installed")
class HaystackRuntimeTests(unittest.TestCase):
    def test_real_in_memory_bm25_pipeline(self):
        source = (
            "프롬 헤이스택 임포트 도큐먼트, 파이프라인\n"
            "프롬 헤이스택.document_stores.in_memory 임포트 인메모리도큐먼트스토어\n"
            "프롬 헤이스택.components.retrievers.in_memory 임포트 인메모리비엠이십오리트리버\n"
            "document_store = 인메모리도큐먼트스토어()\n"
            "document_store.write_documents([\n"
            "    도큐먼트(content='KoPy teaches Python syntax and AI libraries.'),\n"
            "    도큐먼트(content='Rubber chemistry uses sulfur vulcanization.'),\n"
            "])\n"
            "retriever = 인메모리비엠이십오리트리버(document_store=document_store, top_k=2)\n"
            "pipeline = 파이프라인()\n"
            "pipeline.add_component('retriever', retriever)\n"
            "result = pipeline.run({'retriever': {'query': 'Python KoPy'}})\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)
        documents = namespace["result"]["retriever"]["documents"]
        self.assertGreaterEqual(len(documents), 1)
        self.assertIn("KoPy", documents[0].content)
        self.assertGreater(documents[0].score, 0)


if __name__ == "__main__":
    unittest.main()
