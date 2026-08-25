import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("qdrant_client"), "qdrant-client is not installed")
class QdrantRuntimeTests(unittest.TestCase):
    def test_real_in_memory_vector_query(self):
        source = (
            "프롬 큐드란트클라이언트 임포트 큐드란트클라이언트\n"
            "프롬 큐드란트클라이언트.models 임포트 벡터파람스, 디스턴스, 포인트스트럭트\n"
            "client = 큐드란트클라이언트(':memory:')\n"
            "client.크리에이트컬렉션(\n"
            "    collection_name='docs',\n"
            "    vectors_config=벡터파람스(size=2, distance=디스턴스.COSINE),\n"
            ")\n"
            "points = [\n"
            "    포인트스트럭트(id=1, vector=[1.0, 0.0], payload={'text': 'alpha'}),\n"
            "    포인트스트럭트(id=2, vector=[0.0, 1.0], payload={'text': 'beta'}),\n"
            "]\n"
            "client.upsert(collection_name='docs', points=points, wait=True)\n"
            "result = client.쿼리포인츠(\n"
            "    collection_name='docs',\n"
            "    query=[0.99, 0.01],\n"
            "    limit=2,\n"
            "    with_payload=True,\n"
            ")\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)
        result = namespace["result"]

        self.assertEqual(len(result.points), 2)
        self.assertEqual(result.points[0].id, 1)
        self.assertEqual(result.points[0].payload["text"], "alpha")
        self.assertGreater(result.points[0].score, result.points[1].score)


if __name__ == "__main__":
    unittest.main()
