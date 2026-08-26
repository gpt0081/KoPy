"""Official USearch vector-search library pack for KoPy.

USearch is a compact local approximate-nearest-neighbor engine. The pack
transliterates USearch-specific public types while intentionally preserving
transferable vector-search vocabulary such as ``add()``, ``search()``,
``query``, ``vectors``, and tuning keyword arguments in upstream Python form.
"""

from __future__ import annotations

from .base import LibraryPack


USEARCH_PACK = LibraryPack(
    name="usearch",
    module="usearch",
    kopy_module="유서치",
    preferred_aliases=("usearch",),
    description="로컬 근사 최근접 이웃·벡터 인덱싱·고속 유사도 검색용 USearch 팩",
    members={
        "인덱스": "Index",
        "인덱스들": "Indexes",
        "인덱스드키즈": "IndexedKeys",
        "매치": "Match",
        "매치즈": "Matches",
        "배치매치즈": "BatchMatches",
        "컴파일드메트릭": "CompiledMetric",
        "클러스터링": "Clustering",
        "케이민즈": "kmeans",
    },
    member_descriptions={
        "Index": "dense vector를 저장하고 approximate nearest-neighbor 검색을 수행하는 USearch 인덱스입니다.",
        "Indexes": "여러 USearch 인덱스를 묶어 검색하거나 병합합니다.",
        "IndexedKeys": "인덱스에 저장된 key들의 view를 제공합니다.",
        "Match": "단일 검색 결과의 key와 distance를 담습니다.",
        "Matches": "단일 query 검색 결과의 key와 distance를 담습니다.",
        "BatchMatches": "여러 query의 배치 검색 결과를 담습니다.",
        "CompiledMetric": "USearch에서 사용할 사용자 정의 compiled distance metric을 표현합니다.",
        "Clustering": "USearch 인덱스 기반 clustering 결과를 표현합니다.",
        "kmeans": "벡터 집합에 k-means clustering을 수행합니다.",
    },
    examples={
        "Index": (
            "프롬 유서치.index 임포트 인덱스\nindex = 인덱스(ndim=384, metric='cos')",
            "from usearch.index import Index\nindex = Index(ndim=384, metric='cos')",
        ),
        "Matches": (
            "프롬 유서치.index 임포트 매치즈\nmatches: 매치즈 = index.search(query, 5)",
            "from usearch.index import Matches\nmatches: Matches = index.search(query, 5)",
        ),
    },
)
