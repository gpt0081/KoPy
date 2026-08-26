# FastEmbed Library Pack

KoPy 0.5.36의 FastEmbed 팩은 검색/RAG 파이프라인에서 사용할 dense embedding, sparse embedding, late-interaction embedding, image embedding, cross-encoder reranking의 주요 진입점을 namespace-scoped 방식으로 제공합니다.

기준 라이브러리: `fastembed>=0.8,<0.9`  
KoPy 개발 기준: Python 3.12.10

## 지원 namespace

- Python: `fastembed`
- KoPy: `패스트임베드`
- 권장 alias: `fastembed`, `fe`

## 주요 음역

| KoPy | Python |
| --- | --- |
| `텍스트임베딩` | `TextEmbedding` |
| `스파스텍스트임베딩` | `SparseTextEmbedding` |
| `레이트인터랙션텍스트임베딩` | `LateInteractionTextEmbedding` |
| `이미지임베딩` | `ImageEmbedding` |
| `텍스트크로스인코더` | `TextCrossEncoder` |

FastEmbed의 실제 패키지 구조를 익힐 수 있도록 `fastembed.rerank.cross_encoder` 같은 dotted submodule 경로는 Python 원문을 유지합니다.

## Reranking 예제

```kopy
프롬 패스트임베드.rerank.cross_encoder 임포트 텍스트크로스인코더

query = "Who maintains FastEmbed?"
documents = [
    "This document is unrelated.",
    "FastEmbed is supported by and maintained by Qdrant.",
]

reranker = 텍스트크로스인코더(
    model_name="Xenova/ms-marco-MiniLM-L-6-v2",
)

scores = list(reranker.rerank(query, documents))
프린트(scores)
```

대응하는 원문 Python은 다음 구조입니다.

```python
from fastembed.rerank.cross_encoder import TextCrossEncoder

reranker = TextCrossEncoder(
    model_name="Xenova/ms-marco-MiniLM-L-6-v2",
)
scores = list(reranker.rerank(query, documents))
```

## 왜 `rerank()`를 번역하지 않는가

`query`, `documents`, `scores`, `model_name`, `embed()`, `rerank()`는 FastEmbed에만 묶인 표현이 아니라 검색/RAG 코드 전반에서 반복됩니다. KoPy는 이런 표현을 전역 한국어 API로 덮지 않습니다. 원문 Python을 읽을 때 바로 연결되도록 그대로 노출합니다.

## 실제 런타임 검증

CI에서는 mock 대신 실제 `fastembed`와 `Xenova/ms-marco-MiniLM-L-6-v2` cross encoder를 사용해 두 문서를 점수화하고, 관련 문서의 score가 무관한 문서보다 높은지 검사합니다. Windows, Ubuntu, macOS의 Python 3.12.10 환경에서 동일 테스트를 실행합니다.
