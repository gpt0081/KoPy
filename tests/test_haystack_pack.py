import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class HaystackPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("haystack-ai")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "haystack")
        self.assertEqual(pack.kopy_module, "헤이스택")

    def test_pipeline_api_translates(self):
        source = (
            "프롬 헤이스택 임포트 도큐먼트, 파이프라인\n"
            "프롬 헤이스택.document_stores.in_memory 임포트 인메모리도큐먼트스토어\n"
            "프롬 헤이스택.components.retrievers.in_memory 임포트 인메모리비엠이십오리트리버\n"
            "document_store = 인메모리도큐먼트스토어()\n"
            "document_store.write_documents([도큐먼트(content='alpha')])\n"
            "retriever = 인메모리비엠이십오리트리버(document_store=document_store)\n"
            "pipeline = 파이프라인()\n"
            "pipeline.add_component('retriever', retriever)\n"
            "result = pipeline.run({'retriever': {'query': query}})\n"
        )
        python_source = translate(source).python
        self.assertIn("from haystack import Document, Pipeline", python_source)
        self.assertIn("from haystack.document_stores.in_memory import InMemoryDocumentStore", python_source)
        self.assertIn("from haystack.components.retrievers.in_memory import InMemoryBM25Retriever", python_source)
        self.assertIn("document_store.write_documents", python_source)
        self.assertIn("pipeline.add_component", python_source)
        self.assertIn("pipeline.run", python_source)

    def test_transferable_search_vocabulary_stays_python(self):
        source = "프롬 헤이스택 임포트 파이프라인\npipeline = 파이프라인()\npipeline.add_component(name, retriever)\nresult = pipeline.run(data)\n"
        python_source = translate(source).python
        for token in ("pipeline", "retriever", "add_component(", "run("):
            self.assertIn(token, python_source)

    def test_unimported_members_are_not_global(self):
        source = "x = lib.인메모리비엠이십오리트리버(store)\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy(self):
        source = (
            "from haystack import Document, Pipeline\n"
            "from haystack.document_stores.in_memory import InMemoryDocumentStore\n"
            "document_store = InMemoryDocumentStore()\n"
            "pipeline = Pipeline()\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 헤이스택 임포트 도큐먼트, 파이프라인", kopy)
        self.assertIn("프롬 헤이스택.document_stores.in_memory 임포트 인메모리도큐먼트스토어", kopy)
        self.assertIn("document_store = 인메모리도큐먼트스토어()", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("헤이스택.파이프라인")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "Pipeline")


if __name__ == "__main__":
    unittest.main()
