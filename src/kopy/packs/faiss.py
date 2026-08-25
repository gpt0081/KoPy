"""Official FAISS library pack for KoPy.

FAISS is the first KoPy vector-search pack.  The pack intentionally translates
recognisable FAISS class/function names while leaving generic index methods such
as ``add`` and ``search`` in upstream Python form.  That avoids ambiguous
attribute translations and helps learners transfer directly to real FAISS/RAG
examples.
"""

from __future__ import annotations

from .base import LibraryPack


FAISS_PACK = LibraryPack(
    name="faiss",
    module="faiss",
    kopy_module="파이스",
    preferred_aliases=("faiss",),
    description="벡터 유사도 검색·최근접 이웃 인덱스·벡터 정규화용 FAISS 팩",
    members={
        "인덱스플랫엘투": "IndexFlatL2",
        "인덱스플랫아이피": "IndexFlatIP",
        "인덱스아이디맵": "IndexIDMap",
        "인덱스아이디맵투": "IndexIDMap2",
        "인덱스아이브이에프플랫": "IndexIVFFlat",
        "인덱스에이치엔에스더블유플랫": "IndexHNSWFlat",
        "인덱스스칼라퀀타이저": "IndexScalarQuantizer",
        "인덱스피큐": "IndexPQ",
        "노멀라이즈엘투": "normalize_L2",
        "인덱스팩토리": "index_factory",
        "라이트인덱스": "write_index",
        "리드인덱스": "read_index",
        "클론인덱스": "clone_index",
        "벡터투어레이": "vector_to_array",
        "어레이투벡터": "copy_array_to_vector",
    },
    member_descriptions={
        "IndexFlatL2": "정확한 L2(유클리드) 최근접 이웃 검색 인덱스입니다.",
        "IndexFlatIP": "내적 기반 정확 검색 인덱스입니다. 정규화 벡터에서는 cosine 검색에 활용할 수 있습니다.",
        "IndexIDMap": "기본 인덱스에 사용자 지정 벡터 ID를 매핑합니다.",
        "IndexIVFFlat": "학습 가능한 inverted-file 기반 근사 최근접 이웃 인덱스입니다.",
        "IndexHNSWFlat": "HNSW 그래프 기반 근사 최근접 이웃 인덱스입니다.",
        "normalize_L2": "벡터 행을 L2 정규화합니다.",
        "index_factory": "문자열 factory 설명으로 FAISS 인덱스를 생성합니다.",
        "write_index": "FAISS 인덱스를 파일로 저장합니다.",
        "read_index": "저장된 FAISS 인덱스를 읽습니다.",
    },
    examples={
        "IndexFlatL2": (
            "임포트 파이스 애즈 faiss\nindex = faiss.인덱스플랫엘투(384)",
            "import faiss\nindex = faiss.IndexFlatL2(384)",
        ),
        "normalize_L2": (
            "faiss.노멀라이즈엘투(embeddings)",
            "faiss.normalize_L2(embeddings)",
        ),
        "index_factory": (
            "index = faiss.인덱스팩토리(384, 'Flat')",
            "index = faiss.index_factory(384, 'Flat')",
        ),
    },
)
