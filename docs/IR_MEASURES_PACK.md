# ir-measures Library Pack

KoPy 0.5.35 adds a namespace-scoped pack for [`ir-measures`](https://ir-measur.es/), a common interface for information-retrieval evaluation metrics.

## Why this pack exists

KoPy already supports dense retrieval with FAISS/Qdrant/Chroma, lexical retrieval with BM25S, and rank fusion with ranx. `ir-measures` fills the next layer: measuring retrieval quality with standard IR metrics such as nDCG, Precision, Recall, Reciprocal Rank, and Average Precision.

## Import

```python
프롬 아이알메저스 임포트 캘크어그리게이트, 파스메저, nDCG, P, RR
```

translates to:

```python
from ir_measures import calc_aggregate, parse_measure, nDCG, P, RR
```

## Example

```python
프롬 아이알메저스 임포트 캘크어그리게이트, nDCG, P, RR

qrels = {"q1": {"doc_a": 1, "doc_b": 0}}
run = {"q1": {"doc_a": 0.9, "doc_b": 0.2}}

metrics = 캘크어그리게이트(
    [nDCG@2, P@1, RR],
    qrels,
    run,
)
```

## Translation policy

The pack transliterates only ir-measures-specific entry points:

- `calc_aggregate` → `캘크어그리게이트`
- `iter_calc` → `이터캘크`
- `parse_measure` → `파스메저`
- `parse_trec_measure` → `파스트렉메저`
- `read_trec_qrels` → `리드트렉큐렐즈`
- `read_trec_run` → `리드트렉런`
- `Qrel` → `큐렐`
- `ScoredDoc` → `스코어드독`

Standard IR vocabulary is intentionally preserved in upstream form. This includes `qrels`, `run`, `query_id`, `doc_id`, `score`, and standard metric symbols such as `nDCG`, `P`, `R`, `RR`, `AP`, and `MAP`. The cutoff syntax such as `nDCG@10` is also preserved.

This avoids ambiguous global translations and helps KoPy learners recognize the same vocabulary in papers, benchmarks, and normal Python retrieval code.

## Compatibility

KoPy remains pinned to Python `>=3.12,<3.13`. The CI runtime uses `ir-measures>=0.4.3,<0.5`, whose published requirement is Python 3.9 or newer.
