"""Official BM25S lexical-search library pack for KoPy.

BM25S-specific entry points and its retrieval workflow methods are transliterated
only while the BM25S namespace is active. Shared identifiers use KoPy's common
educational vocabulary. Numeric fragments remain digits: BM25S -> 비엠25에스.
"""

from __future__ import annotations

from .base import LibraryPack


BM25S_PACK = LibraryPack(
    name="bm25s",
    module="bm25s",
    kopy_module="비엠25에스",
    preferred_aliases=("bm25s", "bm25"),
    description="BM25 lexical search를 위한 토큰화·BM25 retriever API 팩",
    members={
        "비엠25": "BM25",
        "토크나이즈": "tokenize",
        "리절츠": "Results",
        "겟유니크토큰즈": "get_unique_tokens",
        "인덱스": "index",
        "리트리브": "retrieve",
        "세이브": "save",
        "로드": "load",
    },
    member_descriptions={
        "BM25": "BM25 sparse lexical retriever를 생성합니다.",
        "tokenize": "문서와 query를 BM25S가 사용할 token 표현으로 변환합니다.",
        "Results": "retrieve 결과의 documents와 scores를 담는 결과 타입입니다.",
        "get_unique_tokens": "tokenized corpus에서 고유 token 집합을 계산합니다.",
        "index": "토큰화된 corpus를 BM25 검색 인덱스로 구축합니다.",
        "retrieve": "토큰화된 query로 상위 문서와 점수를 검색합니다.",
    },
    examples={
        "BM25": (
            "임포트 비엠25에스 애즈 bm25s\n리트리버 = bm25s.비엠25(코퍼스=코퍼스)",
            "import bm25s\nretriever = bm25s.BM25(corpus=corpus)",
        ),
        "tokenize": (
            "코퍼스_토큰즈 = bm25s.토크나이즈(코퍼스, show_progress=False)",
            "corpus_tokens = bm25s.tokenize(corpus, show_progress=False)",
        ),
        "retrieve": (
            "리트리버.인덱스(코퍼스_토큰즈)\n리절츠 = 리트리버.리트리브(쿼리_토큰즈, k=5)",
            "retriever.index(corpus_tokens)\nresults = retriever.retrieve(query_tokens, k=5)",
        ),
    },
)
