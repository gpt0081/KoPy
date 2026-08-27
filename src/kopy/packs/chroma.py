"""Official Chroma library pack for KoPy.

Chroma client, collection-management, and collection data operations are
transliterated only while the Chroma namespace is active. This avoids ambiguous
global translations while keeping KoPy's default transliteration principle.
"""

from __future__ import annotations

from .base import LibraryPack


CHROMA_PACK = LibraryPack(
    name="chroma",
    module="chromadb",
    kopy_module="크로마",
    preferred_aliases=("chroma", "chromadb"),
    description="Chroma 로컬·서버 벡터DB client와 collection 관리 API 팩",
    members={
        "클라이언트": "Client",
        "퍼시스턴트클라이언트": "PersistentClient",
        "에이치티티피클라이언트": "HttpClient",
        "어싱크에이치티티피클라이언트": "AsyncHttpClient",
        "크리에이트컬렉션": "create_collection",
        "겟컬렉션": "get_collection",
        "겟오어크리에이트컬렉션": "get_or_create_collection",
        "딜리트컬렉션": "delete_collection",
        "리스트컬렉션즈": "list_collections",
        "카운트컬렉션즈": "count_collections",
        "하트비트": "heartbeat",
        "겟버전": "get_version",
        "애드": "add",
        "쿼리": "query",
        "업서트": "upsert",
        "겟": "get",
        "업데이트": "update",
        "딜리트": "delete",
        "카운트": "count",
    },
    member_descriptions={
        "Client": "별도 서버 없이 메모리에서 실행하는 Chroma client를 생성합니다.",
        "PersistentClient": "로컬 경로에 collection과 vector 데이터를 지속 저장하는 client입니다.",
        "HttpClient": "실행 중인 Chroma 서버에 HTTP로 연결하는 동기 client입니다.",
        "AsyncHttpClient": "실행 중인 Chroma 서버에 연결하는 비동기 client입니다.",
        "create_collection": "새 Chroma collection을 생성합니다.",
        "get_or_create_collection": "collection이 있으면 가져오고 없으면 생성합니다.",
        "list_collections": "현재 database의 collection 목록을 반환합니다.",
        "add": "문서, ID, 임베딩을 collection에 추가합니다.",
        "query": "query embedding으로 collection을 검색합니다.",
        "upsert": "ID 기준으로 데이터를 추가하거나 갱신합니다.",
    },
    examples={
        "Client": (
            "임포트 크로마 애즈 chroma\nclient = chroma.클라이언트()",
            "import chromadb as chroma\nclient = chroma.Client()",
        ),
        "create_collection": (
            "collection = client.크리에이트컬렉션(name='docs', embedding_function=None)",
            "collection = client.create_collection(name='docs', embedding_function=None)",
        ),
        "query": (
            "collection.애드(ids=ids, embeddings=임베딩즈, documents=다큐먼츠)\n리절트 = collection.쿼리(query_embeddings=query_embeddings, n_results=2)",
            "collection.add(ids=ids, embeddings=embeddings, documents=documents)\nresult = collection.query(query_embeddings=query_embeddings, n_results=2)",
        ),
    },
)
