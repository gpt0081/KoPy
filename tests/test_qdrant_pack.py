import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class QdrantPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("qdrant-client")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "qdrant_client")
        self.assertEqual(pack.kopy_module, "큐드란트")

    def test_dotted_model_imports_translate(self):
        source = (
            "프롬 큐드란트 임포트 큐드란트클라이언트\n"
            "프롬 큐드란트.models 임포트 벡터파람스, 디스턴스, 포인트스트럭트\n"
            "클라이언트 = 큐드란트클라이언트(':memory:')\n"
            "config = 벡터파람스(size=4, distance=디스턴스.COSINE)\n"
            "point = 포인트스트럭트(id=1, vector=[1.0, 0.0, 0.0, 0.0])\n"
        )
        python_source = translate(source).python
        self.assertIn("from qdrant_client import QdrantClient", python_source)
        self.assertIn("from qdrant_client.models import VectorParams, Distance, PointStruct", python_source)
        self.assertIn("client = QdrantClient(':memory:')", python_source)
        self.assertIn("VectorParams(size=4, distance=Distance.COSINE)", python_source)
        self.assertIn("PointStruct(id=1, vector=[1.0, 0.0, 0.0, 0.0])", python_source)

    def test_qdrant_specific_client_methods_translate(self):
        source = (
            "프롬 큐드란트 임포트 큐드란트클라이언트\n"
            "클라이언트 = 큐드란트클라이언트(':memory:')\n"
            "클라이언트.크리에이트컬렉션(collection_name='docs', vectors_config=config)\n"
            "리절트 = 클라이언트.쿼리포인츠(collection_name='docs', 쿼리=쿼리, limit=3)\n"
        )
        python_source = translate(source).python
        self.assertIn("client.create_collection(collection_name='docs', vectors_config=config)", python_source)
        self.assertIn("result = client.query_points(collection_name='docs', query=query, limit=3)", python_source)

    def test_generic_database_search_methods_remain_python(self):
        source = (
            "프롬 큐드란트 임포트 큐드란트클라이언트\n"
            "클라이언트 = 큐드란트클라이언트(':memory:')\n"
            "클라이언트.upsert(collection_name='docs', points=points)\n"
            "클라이언트.scroll(collection_name='docs', limit=10)\n"
            "클라이언트.retrieve(collection_name='docs', ids=[1])\n"
        )
        python_source = translate(source).python
        for token in ("client.upsert(", "client.scroll(", "client.retrieve("):
            self.assertIn(token, python_source)

    def test_unimported_qdrant_words_are_not_global(self):
        source = "client.쿼리포인츠(collection_name='docs', 쿼리=쿼리)\n"
        self.assertEqual(translate(source).python, "client.쿼리포인츠(collection_name='docs', query=query)\n")

    def test_python_to_kopy_transliterates_query_vocabulary(self):
        source = (
            "from qdrant_client import QdrantClient\n"
            "from qdrant_client.models import VectorParams, Distance\n"
            "client = QdrantClient(':memory:')\n"
            "client.create_collection(collection_name='docs', vectors_config=VectorParams(size=4, distance=Distance.COSINE))\n"
            "client.upsert(collection_name='docs', points=points)\n"
            "result = client.query_points(collection_name='docs', query=query, limit=3)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 큐드란트 임포트 큐드란트클라이언트", kopy)
        self.assertIn("프롬 큐드란트.models 임포트 벡터파람스, 디스턴스", kopy)
        self.assertIn("클라이언트.크리에이트컬렉션(", kopy)
        self.assertIn("클라이언트.upsert(", kopy)
        self.assertIn("리절트 = 클라이언트.쿼리포인츠(", kopy)
        self.assertIn("쿼리=쿼리", kopy)
        for token in ("collection_name=", "vectors_config=", "limit="):
            self.assertIn(token, kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("큐드란트.쿼리포인츠")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "query_points")


if __name__ == "__main__":
    unittest.main()
