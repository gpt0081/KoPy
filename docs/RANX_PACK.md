# ranx Library Pack

KoPy 0.5.34의 `ranx / 랜엑스` 팩은 dense vector retrieval과 BM25 같은 lexical retrieval의 결과를 하나의 ranking으로 결합하고, 그 결과를 정보검색(IR) metric으로 평가하는 학습 흐름을 지원합니다.

## 설치

```bash
python -m pip install "ranx>=0.3.21,<0.4"
```

KoPy 자체의 Python 호환 범위는 `>=3.12,<3.13`을 유지합니다.

## 지원 음역

- `Qrels` → `큐렐즈`
- `Run` → `런`
- `fuse` → `퓨즈`
- `optimize_fusion` → `옵티마이즈퓨전`

## 의도적으로 영어로 남기는 표현

`runs`, `qrels`, `method`, `norm`, `metric`, `params`, `evaluate`, `compare`, `name`은 번역하지 않습니다.

이 표현들은 ranx만의 API가 아니라 정보검색 논문, 평가 코드, hybrid retrieval 구현에서 반복해서 등장하는 원문 용어입니다. KoPy 학습 후 실제 Python/RAG 코드를 읽을 때 연결이 끊기지 않도록 그대로 노출합니다.

또한 `evaluate()`와 `compare()`처럼 여러 라이브러리에서 사용할 수 있는 일반적인 동사는 전역 번역하지 않습니다. ranx 고유 진입점만 namespace-scoped 팩으로 다룹니다.

## Hybrid retrieval 예제

```python
프롬 랜엑스 임포트 큐렐즈, 런, 퓨즈, evaluate

qrels = 큐렐즈({
    "q1": {"doc_b": 1},
})

dense_run = 런({
    "q1": {
        "doc_a": 0.91,
        "doc_b": 0.82,
        "doc_c": 0.10,
    }
}, name="dense")

lexical_run = 런({
    "q1": {
        "doc_b": 3.0,
        "doc_a": 2.0,
        "doc_c": 0.1,
    }
}, name="bm25")

hybrid_run = 퓨즈(
    runs=[dense_run, lexical_run],
    norm="min-max",
    method="sum",
)

ndcg = evaluate(qrels, hybrid_run, "ndcg@3")
프린트(ndcg)
```

원문 Python에서는 `큐렐즈 → Qrels`, `런 → Run`, `퓨즈 → fuse`만 바뀝니다. `dense_run`, `lexical_run`, `hybrid_run`, `qrels`, `ndcg`, `runs=`, `method=` 같은 검색 관례는 그대로 남습니다.

## RRF

ranx는 Reciprocal Rank Fusion도 지원합니다.

```python
hybrid_run = 퓨즈(
    runs=[dense_run, lexical_run],
    method="rrf",
)
```

RRF, score normalization, weighted fusion을 공부할 때는 `method`, `norm`, `params`의 원문 이름을 그대로 익히는 것을 권장합니다.

## 역할

현재 KoPy 검색/RAG 스택은 다음처럼 이어집니다.

```text
Sentence Transformers
        ↓
 dense embeddings
        ↓
FAISS / Qdrant / Chroma
        +
      BM25S
        ↓
   ranx fusion
        ↓
IR evaluation / reranking
```

ranx는 새로운 retriever가 아니라 **여러 retriever의 ranking을 결합하고 평가하는 층**입니다.
