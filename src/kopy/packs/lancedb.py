"""Official LanceDB library pack for KoPy.

The pack transliterates LanceDB-specific types while intentionally preserving
transferable database and retrieval vocabulary such as ``connect``,
``create_table``, ``search``, ``limit``, ``to_list``, ``add``, ``query``,
and their keyword arguments in upstream Python form.
"""

from __future__ import annotations

from .base import LibraryPack


LANCEDB_PACK = LibraryPack(
    name="lancedb",
    module="lancedb",
    kopy_module="랜스디비",
    preferred_aliases=("lancedb", "lance"),
    description="LanceDB 로컬 벡터DB·FTS·hybrid search용 namespace-scoped 팩",
    members={
        "디비커넥션": "DBConnection",
        "어싱크커넥션": "AsyncConnection",
        "랜스모델": "LanceModel",
        "벡터": "Vector",
        "리랭커": "Reranker",
        "알알에프리랭커": "RRFReranker",
        "리니어컴비네이션리랭커": "LinearCombinationReranker",
    },
    member_descriptions={
        "DBConnection": "로컬 또는 원격 LanceDB database connection 타입입니다.",
        "AsyncConnection": "LanceDB 비동기 connection 타입입니다.",
        "LanceModel": "LanceDB table schema를 선언하는 Pydantic 기반 모델입니다.",
        "Vector": "LanceDB schema에서 고정 길이 embedding vector 필드를 선언합니다.",
        "Reranker": "LanceDB hybrid/vector/FTS 결과 reranker의 기본 인터페이스입니다.",
        "RRFReranker": "Reciprocal Rank Fusion으로 vector와 FTS 결과를 결합합니다.",
        "LinearCombinationReranker": "vector와 FTS score를 선형 결합하는 reranker입니다.",
    },
    examples={
        "DBConnection": (
            "임포트 랜스디비 애즈 lancedb\ndb = lancedb.connect('./data')",
            "import lancedb\ndb = lancedb.connect('./data')",
        ),
        "LanceModel": (
            "프롬 랜스디비.pydantic 임포트 랜스모델, 벡터",
            "from lancedb.pydantic import LanceModel, Vector",
        ),
        "RRFReranker": (
            "프롬 랜스디비.rerankers 임포트 알알에프리랭커",
            "from lancedb.rerankers import RRFReranker",
        ),
    },
)
