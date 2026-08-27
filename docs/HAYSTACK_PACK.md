# Haystack Library Pack

Haystack 팩은 검색/RAG pipeline 구성 요소와 핵심 workflow 메서드를 한글 음역으로 익히되 실제 Python package 구조를 유지합니다. 숫자는 그대로 보존하므로 `BM25 → 비엠25`가 표준입니다.

기준: `haystack-ai 3.0.x`, Python 3.12.x.

## 주요 음역

- `Document` → `도큐먼트`
- `Pipeline` → `파이프라인`
- `InMemoryDocumentStore` → `인메모리도큐먼트스토어`
- `InMemoryBM25Retriever` → `인메모리비엠25리트리버`
- `DocumentWriter` → `도큐먼트라이터`
- `DocumentSplitter` → `도큐먼트스플리터`
- `write_documents()` → `라이트도큐먼츠()`
- `add_component()` → `애드컴포넌트()`
- `connect()` → `커넥트()`
- `run()` → `런()`

`write_documents`, `add_component`, `connect`, `run`은 다른 프레임워크에서도 나타날 수 있으므로 전역 번역하지 않고 Haystack pack이 활성화됐을 때만 음역합니다.

실제 dotted import 경로인 `haystack.document_stores.in_memory`, `haystack.components.retrievers.in_memory`는 Python package 구조 학습을 위해 그대로 유지합니다.

## 예제

```kopy
프롬 헤이스택 임포트 도큐먼트, 파이프라인
프롬 헤이스택.document_stores.in_memory 임포트 인메모리도큐먼트스토어
프롬 헤이스택.components.retrievers.in_memory 임포트 인메모리비엠25리트리버

다큐먼트_스토어 = 인메모리도큐먼트스토어()
다큐먼트_스토어.라이트도큐먼츠(다큐먼츠)

리트리버 = 인메모리비엠25리트리버(
    다큐먼트_스토어=다큐먼트_스토어,
    top_k=2,
)

pipeline = 파이프라인()
pipeline.애드컴포넌트("retriever", 리트리버)
리절트 = pipeline.런({"retriever": {"query": 쿼리}})
```

`document_store → 다큐먼트_스토어`, `retriever → 리트리버`, `query → 쿼리`, `result → 리절트`는 공통 식별자 음역으로 지원합니다. 일반 변수 `pipeline`은 클래스 `Pipeline → 파이프라인`과 같은 음역을 공유해 shadowing 범위를 더 넓게 감사해야 하므로 이번 단계에서는 원문 변수명을 유지합니다.

## `top_k` 예외

`top_k`는 검색·추천·머신러닝 논문과 여러 Python 라이브러리에서 거의 동일한 형태로 반복되는 표준 인자입니다. 원문 학습 가치가 높아 현재 KoPy에서는 의도적으로 유지합니다. 이것은 예외이며 기본 원칙은 영어 식별자와 API의 한글 음역입니다.

실제 runtime test는 외부 API나 모델 다운로드 없이 `InMemoryDocumentStore + InMemoryBM25Retriever + Pipeline`을 실행해 검색 결과를 검증합니다.
