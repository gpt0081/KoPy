"""Official RapidFuzz fuzzy matching library pack for KoPy.

RapidFuzz-specific scorer and extraction APIs are namespace-scoped. Common
search identifiers and signature keywords such as ``query``, ``choices``,
``scorer``, ``processor``, ``score_cutoff`` and ``limit`` use KoPy's common
educational transliteration registry. The real dotted package structure remains
visible for Python learning.
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
        "퍼즈": "fuzz",
        "프로세스": "process",
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
        "fuzz": "RapidFuzz의 문자열 similarity scorer 모듈입니다.",
        "process": "choices 검색과 상위 fuzzy match 추출 기능을 제공합니다.",
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
            "프롬 래피드퍼즈 임포트 퍼즈\n스코어 = 퍼즈.더블유레이쇼(쿼리, 캔디데이트)",
            "from rapidfuzz import fuzz\nscore = fuzz.WRatio(query, candidate)",
        ),
        "extractOne": (
            "프롬 래피드퍼즈 임포트 프로세스, 퍼즈\n베스트 = 프로세스.익스트랙트원(쿼리, 초이시즈, 스코어러=퍼즈.더블유레이쇼)",
            "from rapidfuzz import process, fuzz\nbest = process.extractOne(query, choices, scorer=fuzz.WRatio)",
        ),
    },
)
