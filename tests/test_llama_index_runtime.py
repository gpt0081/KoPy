import unittest

from kopy.translator import translate


class LlamaIndexRuntimeTests(unittest.TestCase):
    def test_real_vector_index_and_retriever(self):
        source = (
            "프롬 라마인덱스.core 임포트 도큐먼트, 벡터스토어인덱스, 목임베딩\n"
            "documents = [\n"
            "    도큐먼트(text='KoPy teaches Python through transliteration.'),\n"
            "    도큐먼트(text='LlamaIndex composes retrieval augmented generation pipelines.'),\n"
            "]\n"
            "index = 벡터스토어인덱스.from_documents(\n"
            "    documents,\n"
            "    embed_model=목임베딩(embed_dim=8),\n"
            "    show_progress=False,\n"
            ")\n"
            "retriever = index.as_retriever(similarity_top_k=2)\n"
            "nodes = retriever.retrieve('KoPy RAG')\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)

        nodes = namespace["nodes"]
        self.assertEqual(len(nodes), 2)
        texts = {node.node.get_content() for node in nodes}
        self.assertEqual(
            texts,
            {
                "KoPy teaches Python through transliteration.",
                "LlamaIndex composes retrieval augmented generation pipelines.",
            },
        )
        self.assertTrue(all(node.score is not None for node in nodes))


if __name__ == "__main__":
    unittest.main()
