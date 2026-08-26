"""Haystack RAG/search orchestration pack for KoPy.

Only Haystack-specific type/component names are transliterated. Transferable
pipeline/search vocabulary such as documents, query, pipeline, retriever,
add_component(), connect(), run(), and write_documents() stays Python-native.
Dotted upstream paths remain unchanged.
"""

from __future__ import annotations

from .base import LibraryPack


HAYSTACK_PACK = LibraryPack(
    name="haystack-ai",
    module="haystack",
    kopy_module="헤이스택",
    preferred_aliases=("haystack", "haystack-ai"),
    description="Pipeline·Document·in-memory document store·BM25 retriever 등 Haystack RAG/search orchestration 팩",
    members={
        "도큐먼트": "Document",
        "파이프라인": "Pipeline",
        "어싱크파이프라인": "AsyncPipeline",
        "인메모리도큐먼트스토어": "InMemoryDocumentStore",
        "인메모리비엠이십오리트리버": "InMemoryBM25Retriever",
        "인메모리임베딩리트리버": "InMemoryEmbeddingRetriever",
        "도큐먼트라이터": "DocumentWriter",
        "도큐먼트스플리터": "DocumentSplitter",
        "도큐먼트클리너": "DocumentCleaner",
        "프롬프트빌더": "PromptBuilder",
        "앤서빌더": "AnswerBuilder",
        "듀플리케이트폴리시": "DuplicatePolicy",
    },
    member_descriptions={
        "Document": "content와 metadata를 담는 Haystack 기본 document 객체입니다.",
        "Pipeline": "Haystack component를 연결하고 실행하는 동기 orchestration graph입니다.",
        "AsyncPipeline": "Haystack component graph의 비동기 실행 버전입니다.",
        "InMemoryDocumentStore": "외부 서비스 없이 실험 가능한 in-memory document store입니다.",
        "InMemoryBM25Retriever": "InMemoryDocumentStore에서 BM25 lexical retrieval을 수행합니다.",
        "InMemoryEmbeddingRetriever": "in-memory embedding similarity retrieval component입니다.",
        "DocumentWriter": "Document를 document store에 기록하는 component입니다.",
        "DocumentSplitter": "Document를 chunk로 분할하는 preprocessing component입니다.",
        "DocumentCleaner": "Document text를 정리하는 preprocessing component입니다.",
        "PromptBuilder": "retrieved documents 등을 prompt template에 조립하는 component입니다.",
        "AnswerBuilder": "generator output과 source documents를 answer 객체로 조립합니다.",
        "DuplicatePolicy": "document ID 중복 처리 정책을 정의합니다.",
    },
    examples={
        "Pipeline": (
            "프롬 헤이스택 임포트 도큐먼트, 파이프라인\n프롬 헤이스택.document_stores.in_memory 임포트 인메모리도큐먼트스토어\n프롬 헤이스택.components.retrievers.in_memory 임포트 인메모리비엠이십오리트리버\ndocument_store = 인메모리도큐먼트스토어()\ndocument_store.write_documents([도큐먼트(content='KoPy teaches Python.')])\nretriever = 인메모리비엠이십오리트리버(document_store=document_store)\npipeline = 파이프라인()\npipeline.add_component('retriever', retriever)\nresult = pipeline.run({'retriever': {'query': query}})",
            "from haystack import Document, Pipeline\nfrom haystack.document_stores.in_memory import InMemoryDocumentStore\nfrom haystack.components.retrievers.in_memory import InMemoryBM25Retriever\ndocument_store = InMemoryDocumentStore()\ndocument_store.write_documents([Document(content='KoPy teaches Python.')])\nretriever = InMemoryBM25Retriever(document_store=document_store)\npipeline = Pipeline()\npipeline.add_component('retriever', retriever)\nresult = pipeline.run({'retriever': {'query': query}})",
        ),
    },
)
