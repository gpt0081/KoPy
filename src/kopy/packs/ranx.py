"""Official ranx hybrid-retrieval fusion and IR-evaluation pack for KoPy.

The pack transliterates ranx-specific entry points while preserving transferable
information-retrieval vocabulary such as ``runs``, ``qrels``, ``method``,
``norm``, ``metric``, ``evaluate``, and ``compare`` in upstream Python form.
"""

from __future__ import annotations

from .base import LibraryPack


RANX_PACK = LibraryPack(
    name="ranx",
    module="ranx",
    kopy_module="랜엑스",
    preferred_aliases=("ranx",),
    description="dense/sparse 검색 결과의 rank fusion과 IR 평가를 위한 ranx API 팩",
    members={
        "큐렐즈": "Qrels",
        "런": "Run",
        "퓨즈": "fuse",
        "옵티마이즈퓨전": "optimize_fusion",
    },
    member_descriptions={
        "Qrels": "query별 relevance judgment를 담아 retrieval 평가의 정답 기준을 만듭니다.",
        "Run": "retriever가 문서에 부여한 ranking score를 query별로 저장합니다.",
        "fuse": "여러 retrieval Run을 RRF, sum 등의 fusion 방식으로 결합합니다.",
        "optimize_fusion": "qrels와 metric을 사용해 fusion 파라미터를 탐색합니다.",
    },
    examples={
        "Run": (
            "프롬 랜엑스 임포트 런\ndense_run = 런(dense_scores, name='dense')",
            "from ranx import Run\ndense_run = Run(dense_scores, name='dense')",
        ),
        "fuse": (
            "프롬 랜엑스 임포트 퓨즈\nhybrid_run = 퓨즈(runs=[dense_run, lexical_run], method='rrf')",
            "from ranx import fuse\nhybrid_run = fuse(runs=[dense_run, lexical_run], method='rrf')",
        ),
    },
)
