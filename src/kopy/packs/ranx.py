"""Official ranx hybrid-retrieval fusion and IR-evaluation pack for KoPy.

The pack transliterates ranx-specific entry points. Common IR identifiers and
keyword arguments such as ``qrels``, ``runs``, ``method``, ``norm`` and ``metric``
are handled by KoPy's common educational identifier registry so examples do not
leave avoidable English spellings behind.
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
        "이밸류에이트": "evaluate",
        "컴페어": "compare",
    },
    member_descriptions={
        "Qrels": "query별 relevance judgment를 담아 retrieval 평가의 정답 기준을 만듭니다.",
        "Run": "retriever가 문서에 부여한 ranking score를 query별로 저장합니다.",
        "fuse": "여러 retrieval Run을 RRF, sum 등의 fusion 방식으로 결합합니다.",
        "optimize_fusion": "qrels와 metric을 사용해 fusion 파라미터를 탐색합니다.",
        "evaluate": "qrels와 run을 표준 IR metric으로 평가합니다.",
        "compare": "여러 retrieval run의 평가 결과를 비교합니다.",
    },
    examples={
        "Run": (
            "프롬 랜엑스 임포트 런\n덴스_런 = 런(덴스_스코어즈, 네임='dense')",
            "from ranx import Run\ndense_run = Run(dense_scores, name='dense')",
        ),
        "fuse": (
            "프롬 랜엑스 임포트 퓨즈\n하이브리드_런 = 퓨즈(런즈=[덴스_런, 렉시컬_런], 메서드='rrf')",
            "from ranx import fuse\nhybrid_run = fuse(runs=[dense_run, lexical_run], method='rrf')",
        ),
    },
)
