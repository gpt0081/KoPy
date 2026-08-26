# Haystack Library Pack

KoPy 0.5.40의 `haystack-ai` 팩은 Haystack의 검색/RAG pipeline 구성 요소를 한글 음역으로 익히되 실제 Python 패키지 구조와 공통 RAG 어휘를 유지합니다.

기준: `haystack-ai 3.0.x`, Python 3.12.10.

## 지원 namespace

- Python: `haystack`
- KoPy: `헤이스택`
- dotted paths는 원문 유지: `haystack.document_stores.in_memory`, `haystack.components.retrievers.in_memory` 등

## 주요 음역

- `Document` → `도큐먼트`
- `Pipeline` → `파이프라인`
- `AsyncPipeline` → `어싱크파이프라인`
- `InMemoryDocumentStore` → `인메모리도큐먼트스토어`
- `InMemoryBM25Retriever` → `인메모리비엠이십오리트리버`
- `InMemoryEmbeddingRetriever` → `인메모리임베딩리트리버`
- `DocumentWriter` → `도큐먼트라이터`
- `DocumentSplitter` → `도큐먼트스플리터`
- `DocumentCleaner` → `도큐먼트클리너`
- `PromptBuilder` → `프롬프트빌더`
- `AnswerBuilder` → `앤서빌더`
- `DuplicatePolicy` → `듀플리케이트폴리시`

## 원문으로 남기는 표현

`documents`, `query`, `pipeline`, `retriever`, `document_store`, `add_component()`, `connect()`, `run()`, `write_documents()`, `top_k=` 등은 검색/RAG와 Python 프레임워크 전반에서 재사용되는 표현이므로 번역하지 않습니다. KoPy 학습자가 Haystack 원문 코드와 다른 RAG 프레임워크로 자연스럽게 넘어가기 위한 의도적인 선택입니다.

## 예제

```kopy
프롬 헤이스택 임포트 도큐먼트, 파이프라인
프롬 헤이스택.document_stores.in_memory 임포트 인메모리도큐먼트스토어
프롬 헤이스택.components.retrievers.in_memory 임포트 인메모리비엠이십오리트리버

document_store = 인메모리도큐먼트스토어()
document_store.write_documents([
    도큐먼트(content="KoPy teaches Python."),
    도큐먼트(content="Haystack builds RAG pipelines."),
])

retriever = 인메모리비엠이십오리트리버(document_store=document_store, top_k=2)
pipeline = 파이프라인()
pipeline.add_component("retriever", retriever)
result = pipeline.run({"retriever": {"query": query}})
```

실제 runtime test는 외부 API나 모델 다운로드 없이 `InMemoryDocumentStore + InMemoryBM25Retriever + Pipeline`을 실행해 BM25 검색 결과를 검증합니다.
