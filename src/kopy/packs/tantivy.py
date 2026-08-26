"""Official Tantivy full-text search library pack for KoPy.

The pack transliterates Tantivy-specific types and schema helpers while
preserving transferable search vocabulary such as ``query``, ``search``,
``index``, ``writer``, ``searcher``, ``limit``, and field names in upstream
Python form.
"""

from __future__ import annotations

from .base import LibraryPack


TANTIVY_PACK = LibraryPack(
    name="tantivy",
    module="tantivy",
    kopy_module="탄티비",
    preferred_aliases=("tantivy",),
    description="Rust 기반 로컬 full-text 검색 엔진 Tantivy의 schema·document·index API 팩",
    members={
        "스키마빌더": "SchemaBuilder",
        "스키마": "Schema",
        "도큐먼트": "Document",
        "인덱스": "Index",
        "인덱스라이터": "IndexWriter",
        "서처": "Searcher",
        "서치리절트": "SearchResult",
        "도큐먼트어드레스": "DocAddress",
        "쿼리": "Query",
        "오더": "Order",
        "오커": "Occur",
        "파스쿼리": "parse_query",
        "파스쿼리리니언트": "parse_query_lenient",
    },
    member_descriptions={
        "SchemaBuilder": "검색 index의 field schema를 정의합니다.",
        "Schema": "빌드된 Tantivy schema 타입입니다.",
        "Document": "index에 저장하거나 조회하는 문서 타입입니다.",
        "Index": "메모리 또는 디스크 Tantivy index를 생성·엽니다.",
        "IndexWriter": "document 추가와 commit을 담당하는 writer 타입입니다.",
        "Searcher": "commit된 index를 query로 검색하는 searcher 타입입니다.",
        "SearchResult": "검색 hits와 count를 담는 결과 타입입니다.",
        "DocAddress": "검색 hit가 가리키는 document 주소입니다.",
        "Query": "Tantivy query 타입입니다.",
        "Order": "정렬 방향 enum입니다.",
        "Occur": "Boolean query clause occurrence enum입니다.",
        "parse_query": "Tantivy query 문자열을 AST로 파싱합니다.",
        "parse_query_lenient": "오류를 복구하며 query 문자열을 파싱합니다.",
    },
    examples={
        "SchemaBuilder": (
            "임포트 탄티비\nbuilder = 탄티비.스키마빌더()",
            "import tantivy\nbuilder = tantivy.SchemaBuilder()",
        ),
        "Index": (
            "index = 탄티비.인덱스(schema)",
            "index = tantivy.Index(schema)",
        ),
        "Document": (
            "doc = 탄티비.도큐먼트()",
            "doc = tantivy.Document()",
        ),
    },
)
