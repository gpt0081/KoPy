"""Official sqlite-vec vector-search library pack for KoPy.

sqlite-vec embeds vector search inside SQLite. The pack transliterates the
small Python binding surface while intentionally preserving transferable
SQLite/vector-search vocabulary such as ``connection``, ``query``, SQL
statements, ``execute()``, and vector column names in upstream Python form.
"""

from __future__ import annotations

from .base import LibraryPack


SQLITE_VEC_PACK = LibraryPack(
    name="sqlite-vec",
    module="sqlite_vec",
    kopy_module="에스큐엘라이트벡",
    preferred_aliases=("sqlite_vec",),
    description="SQLite 안에서 서버 없이 벡터 저장·거리 계산·KNN 검색을 수행하는 sqlite-vec 팩",
    members={
        "로드": "load",
        "시리얼라이즈플로트32": "serialize_float32",
        "시리얼라이즈인트8": "serialize_int8",
    },
    member_descriptions={
        "load": "sqlite-vec 확장을 기존 sqlite3 Connection에 로드합니다.",
        "serialize_float32": "Python float vector를 sqlite-vec float32 BLOB 형식으로 직렬화합니다.",
        "serialize_int8": "Python int8 vector를 sqlite-vec BLOB 형식으로 직렬화합니다.",
    },
    examples={
        "load": (
            "임포트 sqlite3\n임포트 에스큐엘라이트벡 애즈 sqlite_vec\nconnection = sqlite3.connect(':memory:')\nsqlite_vec.로드(connection)",
            "import sqlite3\nimport sqlite_vec\nconnection = sqlite3.connect(':memory:')\nsqlite_vec.load(connection)",
        ),
        "serialize_float32": (
            "프롬 에스큐엘라이트벡 임포트 시리얼라이즈플로트32\nblob = 시리얼라이즈플로트32(embedding)",
            "from sqlite_vec import serialize_float32\nblob = serialize_float32(embedding)",
        ),
    },
)
