"""Official pypdf document-ingestion library pack for KoPy.

The pack transliterates pypdf-specific document and page APIs while
preserving transferable RAG/document vocabulary such as ``document``,
``reader``, ``writer``, ``pages``, ``text``, ``metadata``, ``write()``, and
file paths in upstream Python form. PDF contents and strings are never
translated by this pack.
"""

from __future__ import annotations

from .base import LibraryPack


PYPDF_PACK = LibraryPack(
    name="pypdf",
    module="pypdf",
    kopy_module="파이피디에프",
    preferred_aliases=("pypdf",),
    description="RAG 문서 ingestion에 쓰는 pypdf PDF 읽기·텍스트 추출·페이지 조작 API 팩",
    members={
        "피디에프리더": "PdfReader",
        "피디에프라이터": "PdfWriter",
        "페이지오브젝트": "PageObject",
        "트랜스포메이션": "Transformation",
        "익스트랙트텍스트": "extract_text",
        "애드블랭크페이지": "add_blank_page",
        "애드메타데이터": "add_metadata",
        "애드페이지": "add_page",
        "인서트블랭크페이지": "insert_blank_page",
        "클론도큐먼트프롬리더": "clone_document_from_reader",
        "어펜드페이지즈프롬리더": "append_pages_from_reader",
    },
    member_descriptions={
        "PdfReader": "PDF 파일이나 binary stream을 읽어 페이지와 metadata에 접근합니다.",
        "PdfWriter": "PDF 페이지를 만들거나 결합해 새 PDF를 작성합니다.",
        "PageObject": "PDF 한 페이지를 표현하는 pypdf 객체입니다.",
        "Transformation": "페이지 좌표 변환을 표현합니다.",
        "extract_text": "페이지의 텍스트를 추출합니다.",
        "add_blank_page": "PdfWriter에 빈 페이지를 추가합니다.",
        "add_metadata": "PdfWriter에 문서 metadata를 추가합니다.",
        "add_page": "PdfWriter에 PageObject를 추가합니다.",
        "insert_blank_page": "지정 위치에 빈 페이지를 삽입합니다.",
        "clone_document_from_reader": "PdfReader의 문서 구조를 PdfWriter로 복제합니다.",
        "append_pages_from_reader": "PdfReader의 페이지들을 PdfWriter에 이어 붙입니다.",
    },
    examples={
        "PdfReader": (
            "프롬 파이피디에프 임포트 피디에프리더\nreader = 피디에프리더(\"document.pdf\")\ntext = \"\\n\".join(page.익스트랙트텍스트() or \"\" for page in reader.pages)",
            "from pypdf import PdfReader\nreader = PdfReader(\"document.pdf\")\ntext = \"\\n\".join(page.extract_text() or \"\" for page in reader.pages)",
        ),
        "PdfWriter": (
            "프롬 파이피디에프 임포트 피디에프라이터\nwriter = 피디에프라이터()\nwriter.애드블랭크페이지(width=612, height=792)",
            "from pypdf import PdfWriter\nwriter = PdfWriter()\nwriter.add_blank_page(width=612, height=792)",
        ),
    },
)
