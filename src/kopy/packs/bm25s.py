"""Official BM25S lexical-search library pack for KoPy.

The pack translates BM25S-specific entry points while preserving transferable
information-retrieval vocabulary such as ``index``, ``retrieve``, ``corpus``,
``query``, ``k``, ``documents``, and ``scores`` in upstream Python form.
"""

from __future__ import annotations

from .base import LibraryPack


BM25S_PACK = LibraryPack(
    name="bm25s",
    module="bm25s",
    kopy_module="비엠이십오에스",
    preferred_aliases=("bm25s", "bm25"),
    description="BM25 lexical search를 위한 토큰화·BM25 retriever API 팩",
    members={
        "비엠이십오": "BM25",
        "토크나이즈": "tokenize",
        "리절츠": "Results",
        "겟유니크토큰즈": "get_unique_tokens",
    },
    member_descriptions={
        "BM25": "BM25 sparse lexical retriever를 생성합니다.",
        "tokenize": "문서와 query를 BM25S가 사용할 token 표현으로 변환합니다.",
        "Results": "retrieve 결과의 documents와 scores를 담는 결과 타입입니다.",
        "get_unique_tokens": "tokenized corpus에서 고유 token 집합을 계산합니다.",
    },
    examples={
        "BM25": (
            "임포트 비엠이십오에스 애즈 bm25s\nretriever = bm25s.비엠이십오(corpus=corpus)",
            "import bm25s\nretriever = bm25s.BM25(corpus=corpus)",
        ),
        "tokenize": (
            "corpus_tokens = bm25s.토크나이즈(corpus, show_progress=False)",
            "corpus_tokens = bm25s.tokenize(corpus, show_progress=False)",
        ),
    },
)
