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
            "프롬 헤이스택.components.retrievers.in_memory 임포트 인메모리비엠25리트리버\n"
            "다큐먼트_스토어 = 인메모리도큐먼트스토어()\n"
            "다큐먼트_스토어.write_documents([도큐먼트(content='alpha')])\n"
            "리트리버 = 인메모리비엠25리트리버(다큐먼트_스토어=다큐먼트_스토어, top_k=2)\n"
            "pipeline = 파이프라인()\n"
            "pipeline.add_component('retriever', 리트리버)\n"
            "리절트 = pipeline.run({'retriever': {'query': 쿼리}})\n"
        )
        python_source = translate(source).python
        self.assertIn("from haystack import Document, Pipeline", python_source)
        self.assertIn("from haystack.document_stores.in_memory import InMemoryDocumentStore", python_source)
        self.assertIn("from haystack.components.retrievers.in_memory import InMemoryBM25Retriever", python_source)
        self.assertIn("document_store = InMemoryDocumentStore()", python_source)
        self.assertIn("retriever = InMemoryBM25Retriever(document_store=document_store, top_k=2)", python_source)
        self.assertIn("pipeline.add_component", python_source)
        self.assertIn("pipeline.run", python_source)

    def test_top_k_remains_python_as_teaching_convention(self):
        source = (
            "프롬 헤이스택.components.retrievers.in_memory 임포트 인메모리비엠25리트리버\n"
            "리트리버 = 인메모리비엠25리트리버(다큐먼트_스토어=다큐먼트_스토어, top_k=2)\n"
        )
        python_source = translate(source).python
        self.assertIn("document_store=document_store", python_source)
        self.assertIn("top_k=2", python_source)

    def test_unimported_members_are_not_pack_global(self):
        source = "x = lib.인메모리비엠25리트리버(store)\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy_transliterates_common_identifiers(self):
        source = (
            "from haystack import Document, Pipeline\n"
            "from haystack.document_stores.in_memory import InMemoryDocumentStore\n"
            "document_store = InMemoryDocumentStore()\n"
            "retriever = object()\n"
            "query = 'KoPy'\n"
            "pipeline = Pipeline()\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 헤이스택 임포트 도큐먼트, 파이프라인", kopy)
        self.assertIn("프롬 헤이스택.document_stores.in_memory 임포트 인메모리도큐먼트스토어", kopy)
        self.assertIn("다큐먼트_스토어 = 인메모리도큐먼트스토어()", kopy)
        self.assertIn("리트리버 = 오브젝트()", kopy)
        self.assertIn("쿼리 = 'KoPy'", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("헤이스택.인메모리비엠25리트리버")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "InMemoryBM25Retriever")


if __name__ == "__main__":
    unittest.main()
