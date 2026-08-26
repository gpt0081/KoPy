"""Official ir-measures retrieval-evaluation pack for KoPy.

The pack transliterates ir-measures-specific entry points while preserving
standard information-retrieval vocabulary and metric symbols such as ``qrels``,
``run``, ``nDCG``, ``P``, ``R``, ``RR``, ``AP``, ``MAP``, and cutoff syntax.
"""

from __future__ import annotations

from .base import LibraryPack


IR_MEASURES_PACK = LibraryPack(
    name="ir-measures",
    module="ir_measures",
    kopy_module="아이알메저스",
    preferred_aliases=("ir_measures", "irm"),
    description="nDCG, Precision, Recall, RR, AP 등 검색/RAG 표준 지표 평가를 위한 ir-measures API 팩",
    members={
        "캘크어그리게이트": "calc_aggregate",
        "이터캘크": "iter_calc",
        "파스메저": "parse_measure",
        "파스트렉메저": "parse_trec_measure",
        "리드트렉큐렐즈": "read_trec_qrels",
        "리드트렉런": "read_trec_run",
        "큐렐": "Qrel",
        "스코어드독": "ScoredDoc",
    },
    member_descriptions={
        "calc_aggregate": "여러 query의 retrieval metric을 aggregate하여 한 번에 계산합니다.",
        "iter_calc": "query별 metric 결과를 순회할 수 있게 계산합니다.",
        "parse_measure": "'nDCG@10' 같은 표준 measure 문자열을 metric 객체로 변환합니다.",
        "parse_trec_measure": "trec_eval 스타일 measure 이름을 ir-measures 객체 목록으로 변환합니다.",
        "read_trec_qrels": "TREC qrels 파일을 읽습니다.",
        "read_trec_run": "TREC run 파일을 읽습니다.",
        "Qrel": "query-document relevance judgment 한 건을 표현합니다.",
        "ScoredDoc": "retrieval run의 query-document score 한 건을 표현합니다.",
    },
    examples={
        "calc_aggregate": (
            "프롬 아이알메저스 임포트 캘크어그리게이트, nDCG, P, RR\nmetrics = 캘크어그리게이트([nDCG@10, P@5, RR], qrels, run)",
            "from ir_measures import calc_aggregate, nDCG, P, RR\nmetrics = calc_aggregate([nDCG@10, P@5, RR], qrels, run)",
        ),
        "parse_measure": (
            "프롬 아이알메저스 임포트 파스메저\nmetric = 파스메저('nDCG@10')",
            "from ir_measures import parse_measure\nmetric = parse_measure('nDCG@10')",
        ),
    },
)
