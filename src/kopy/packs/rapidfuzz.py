"""Official RapidFuzz fuzzy matching library pack for KoPy.

The pack transliterates RapidFuzz-specific scorer and extraction APIs while
preserving transferable search vocabulary such as ``query``, ``choices``,
``scorer``, ``processor``, ``score_cutoff``, and ``limit`` in upstream Python
form. The real ``rapidfuzz.fuzz`` and ``rapidfuzz.process`` package structure
is intentionally preserved for learning.
"""

from __future__ import annotations

from .base import LibraryPack


RAPIDFUZZ_PACK = LibraryPack(
    name="rapidfuzz",
    module="rapidfuzz",
    kopy_module="래피드퍼즈",
    preferred_aliases=("rapidfuzz", "rf"),
    description="검색 전처리·중복 제거·fuzzy matching에 쓰는 RapidFuzz scorer·extraction API 팩",
    members={
        "레이쇼": "ratio",
        "파셜레이쇼": "partial_ratio",
        "토큰소트레이쇼": "token_sort_ratio",
        "토큰셋레이쇼": "token_set_ratio",
        "더블유레이쇼": "WRatio",
        "큐레이쇼": "QRatio",
        "익스트랙트": "extract",
        "익스트랙트원": "extractOne",
        "익스트랙트이터": "extract_iter",
        "씨디스트": "cdist",
        "씨피디스트": "cpdist",
    },
    member_descriptions={
        "ratio": "두 문자열의 정규화된 유사도 점수를 계산합니다.",
        "partial_ratio": "부분 문자열 기준 fuzzy similarity를 계산합니다.",
        "token_sort_ratio": "토큰 정렬 후 문자열 유사도를 계산합니다.",
        "token_set_ratio": "토큰 집합 기준 문자열 유사도를 계산합니다.",
        "WRatio": "여러 fuzzy scorer를 조합한 가중 유사도 점수를 계산합니다.",
        "QRatio": "빠른 기본 ratio 계열 점수를 계산합니다.",
        "extract": "choices에서 상위 fuzzy matches를 반환합니다.",
        "extractOne": "choices에서 최상위 fuzzy match 하나를 반환합니다.",
        "extract_iter": "fuzzy matches를 iterator로 반환합니다.",
        "cdist": "query/choice 집합 사이의 pairwise similarity 행렬을 계산합니다.",
        "cpdist": "대응하는 query/choice 쌍의 similarity를 계산합니다.",
    },
    examples={
        "WRatio": (
            "프롬 래피드퍼즈 임포트 fuzz\nscore = fuzz.더블유레이쇼(query, candidate)",
            "from rapidfuzz import fuzz\nscore = fuzz.WRatio(query, candidate)",
        ),
        "extractOne": (
            "프롬 래피드퍼즈 임포트 process, fuzz\nbest = process.익스트랙트원(query, choices, scorer=fuzz.더블유레이쇼)",
            "from rapidfuzz import process, fuzz\nbest = process.extractOne(query, choices, scorer=fuzz.WRatio)",
        ),
    },
)
