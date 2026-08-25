"""Official Qdrant Client library pack for KoPy.

The pack focuses on Qdrant-specific client operations and model types while
leaving generic database/search verbs such as ``upsert``, ``scroll``,
``retrieve``, and keyword arguments in upstream Python form. This keeps the
pack namespace-scoped and preserves transferable vector-database vocabulary.
"""

from __future__ import annotations

from .base import LibraryPack


QDRANT_PACK = LibraryPack(
    name="qdrant-client",
    module="qdrant_client",
    kopy_module="큐드란트클라이언트",
    preferred_aliases=("qdrant", "qdrant-client", "qdrant_client"),
    description="Qdrant 벡터DB collection·point·query·filter API용 클라이언트 팩",
    members={
        "큐드란트클라이언트": "QdrantClient",
        "어싱크큐드란트클라이언트": "AsyncQdrantClient",
        "크리에이트컬렉션": "create_collection",
        "딜리트컬렉션": "delete_collection",
        "겟컬렉션": "get_collection",
        "겟컬렉션즈": "get_collections",
        "컬렉션이그지스츠": "collection_exists",
        "쿼리포인츠": "query_points",
        "쿼리배치포인츠": "query_batch_points",
        "벡터파람스": "VectorParams",
        "스파스벡터파람스": "SparseVectorParams",
        "스파스벡터": "SparseVector",
        "포인트스트럭트": "PointStruct",
        "디스턴스": "Distance",
        "필드컨디션": "FieldCondition",
        "매치밸류": "MatchValue",
        "필터": "Filter",
        "레인지": "Range",
        "네임드벡터": "NamedVector",
    },
    member_descriptions={
        "QdrantClient": "Qdrant 서버 또는 로컬 in-memory/on-disk 저장소에 연결하는 동기 클라이언트입니다.",
        "AsyncQdrantClient": "Qdrant API의 비동기 클라이언트입니다.",
        "create_collection": "벡터 크기와 distance 설정으로 collection을 생성합니다.",
        "query_points": "벡터·point ID·query object를 이용해 nearest-neighbor 검색을 수행합니다.",
        "VectorParams": "collection dense vector의 차원과 distance를 정의합니다.",
        "SparseVectorParams": "sparse vector collection 설정을 정의합니다.",
        "PointStruct": "ID, vector, payload를 함께 저장하는 Qdrant point 구조입니다.",
        "Filter": "payload 조건을 결합하는 Qdrant filter 모델입니다.",
    },
    examples={
        "QdrantClient": (
            "프롬 큐드란트클라이언트 임포트 큐드란트클라이언트\nclient = 큐드란트클라이언트(':memory:')",
            "from qdrant_client import QdrantClient\nclient = QdrantClient(':memory:')",
        ),
        "VectorParams": (
            "프롬 큐드란트클라이언트.models 임포트 벡터파람스, 디스턴스\nconfig = 벡터파람스(size=384, distance=디스턴스.COSINE)",
            "from qdrant_client.models import VectorParams, Distance\nconfig = VectorParams(size=384, distance=Distance.COSINE)",
        ),
        "query_points": (
            "result = client.쿼리포인츠(collection_name='docs', query=query, limit=5)",
            "result = client.query_points(collection_name='docs', query=query, limit=5)",
        ),
    },
)
