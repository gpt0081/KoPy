"""Official LlamaIndex Core RAG orchestration pack for KoPy.

The pack transliterates LlamaIndex-specific core building blocks while preserving
transferable RAG vocabulary and generic orchestration methods such as
``documents``, ``nodes``, ``query``, ``index``, ``retriever``,
``from_documents()``, ``as_retriever()``, and ``retrieve()`` in upstream Python
form. Dotted package paths such as ``llama_index.core.node_parser`` remain
Python-native so learners keep seeing the real LlamaIndex package structure.
"""

from __future__ import annotations

from .base import LibraryPack


LLAMA_INDEX_PACK = LibraryPack(
    name="llama-index-core",
    module="llama_index",
    kopy_module="라마인덱스",
    preferred_aliases=("llama-index", "llama_index"),
    description="Document·Node·VectorStoreIndex·retriever·ingestion 등 LlamaIndex Core RAG 구성요소 팩",
    members={
        "도큐먼트": "Document",
        "벡터스토어인덱스": "VectorStoreIndex",
        "스토리지컨텍스트": "StorageContext",
        "세팅즈": "Settings",
        "쿼리번들": "QueryBundle",
        "목임베딩": "MockEmbedding",
        "심플디렉터리리더": "SimpleDirectoryReader",
        "텍스트노드": "TextNode",
        "노드위드스코어": "NodeWithScore",
        "센텐스스플리터": "SentenceSplitter",
        "인제스천파이프라인": "IngestionPipeline",
        "메타데이터필터스": "MetadataFilters",
        "메타데이터필터": "MetadataFilter",
        "필터오퍼레이터": "FilterOperator",
    },
    member_descriptions={
        "Document": "원문 텍스트와 metadata를 담는 LlamaIndex 기본 document 객체입니다.",
        "VectorStoreIndex": "Document/Node를 embedding 기반으로 색인하고 retriever로 연결하는 핵심 vector index입니다.",
        "StorageContext": "docstore·index store·vector store 등 저장 계층을 묶는 context입니다.",
        "Settings": "embedding·LLM·text splitter 등 LlamaIndex 전역 기본 설정을 보관합니다.",
        "QueryBundle": "query string과 embedding 등 retrieval 입력 정보를 묶는 객체입니다.",
        "MockEmbedding": "외부 embedding API 없이 index/retrieval 파이프라인을 테스트할 수 있는 core mock embedding입니다.",
        "SimpleDirectoryReader": "로컬 파일을 Document 목록으로 읽는 기본 reader입니다.",
        "TextNode": "chunk text와 metadata·관계를 담는 기본 Node 구현입니다.",
        "NodeWithScore": "retrieval node와 similarity/relevance score를 함께 담습니다.",
        "SentenceSplitter": "문서를 sentence-aware chunk로 나누는 core node parser입니다.",
        "IngestionPipeline": "chunking·embedding 등 transformations를 순차 적용하는 ingestion pipeline입니다.",
        "MetadataFilters": "여러 vector-store metadata filter를 결합하는 container입니다.",
        "MetadataFilter": "key/value 기반 metadata filter 조건입니다.",
        "FilterOperator": "metadata filter 비교 연산자를 나타냅니다.",
    },
    examples={
        "VectorStoreIndex": (
            "프롬 라마인덱스.core 임포트 도큐먼트, 벡터스토어인덱스, 목임베딩\ndocuments = [도큐먼트(text=\"KoPy supports RAG learning.\")]\nindex = 벡터스토어인덱스.from_documents(documents, embed_model=목임베딩(embed_dim=8))\nretriever = index.as_retriever(similarity_top_k=1)\nnodes = retriever.retrieve(query)",
            "from llama_index.core import Document, VectorStoreIndex, MockEmbedding\ndocuments = [Document(text=\"KoPy supports RAG learning.\")]\nindex = VectorStoreIndex.from_documents(documents, embed_model=MockEmbedding(embed_dim=8))\nretriever = index.as_retriever(similarity_top_k=1)\nnodes = retriever.retrieve(query)",
        ),
        "SentenceSplitter": (
            "프롬 라마인덱스.core.node_parser 임포트 센텐스스플리터\nsplitter = 센텐스스플리터(chunk_size=128, chunk_overlap=16)",
            "from llama_index.core.node_parser import SentenceSplitter\nsplitter = SentenceSplitter(chunk_size=128, chunk_overlap=16)",
        ),
    },
)
