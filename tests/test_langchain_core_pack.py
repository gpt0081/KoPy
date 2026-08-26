import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class LangChainCorePackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("langchain-core")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "langchain_core")
        self.assertEqual(pack.kopy_module, "랭체인코어")

    def test_vector_store_api_translates(self):
        source = (
            "프롬 랭체인코어.다큐먼츠 임포트 도큐먼트\n"
            "프롬 랭체인코어.임베딩즈 임포트 임베딩즈\n"
            "프롬 랭체인코어.vectorstores 임포트 인메모리벡터스토어\n"
            "벡터_스토어 = 인메모리벡터스토어(embedding=embedding_model)\n"
            "벡터_스토어.add_documents(다큐먼츠=다큐먼츠)\n"
            "리절츠 = 벡터_스토어.similarity_search(쿼리, k=3)\n"
        )
        python_source = translate(source).python
        self.assertIn("from langchain_core.documents import Document", python_source)
        self.assertIn("from langchain_core.embeddings import Embeddings", python_source)
        self.assertIn("from langchain_core.vectorstores import InMemoryVectorStore", python_source)
        self.assertIn("vector_store.add_documents", python_source)
        self.assertIn("vector_store.similarity_search", python_source)

    def test_runnable_and_prompt_types_translate(self):
        source = (
            "프롬 랭체인코어.runnables 임포트 러너블람다, 러너블패스스루\n"
            "프롬 랭체인코어.prompts 임포트 프롬프트템플릿\n"
            "step = 러너블람다(func)\n"
            "prompt = 프롬프트템플릿.from_template(template)\n"
            "리절트 = step.invoke(data)\n"
        )
        python_source = translate(source).python
        self.assertIn("RunnableLambda, RunnablePassthrough", python_source)
        self.assertIn("PromptTemplate", python_source)
        self.assertIn("step.invoke(data)", python_source)
        self.assertIn("result =", python_source)

    def test_python_spellings_remain_accepted_for_rag_vocabulary(self):
        source = (
            "프롬 랭체인코어.vectorstores 임포트 인메모리벡터스토어\n"
            "vector_store = 인메모리벡터스토어(embedding=embedding_model)\n"
            "vector_store.add_documents(documents=documents)\n"
            "results = vector_store.similarity_search(query, k=2)\n"
        )
        python_source = translate(source).python
        for token in ("documents", "query", "add_documents(", "similarity_search(", "k=2"):
            self.assertIn(token, python_source)

    def test_unimported_members_are_not_global(self):
        source = "x = lib.인메모리벡터스토어(embedding=model)\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy_transliterates_known_dotted_segments_and_identifiers(self):
        source = (
            "from langchain_core.documents import Document\n"
            "from langchain_core.vectorstores import InMemoryVectorStore\n"
            "vector_store = InMemoryVectorStore(embedding=embedding_model)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 랭체인코어.다큐먼츠 임포트 도큐먼트", kopy)
        self.assertIn("프롬 랭체인코어.vectorstores 임포트 인메모리벡터스토어", kopy)
        self.assertIn("벡터_스토어 = 인메모리벡터스토어", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("랭체인코어.도큐먼트")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "Document")


if __name__ == "__main__":
    unittest.main()
