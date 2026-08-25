# FAISS Library Pack

KoPy 0.5.30 adds a namespace-scoped pack for `faiss`, the Python module provided by the `faiss-cpu` package.

## Why FAISS

FAISS is a useful first step for KoPy's vector-search and RAG direction. It lets learners work with embeddings, nearest-neighbor indexes, cosine/L2 similarity, index persistence, IVF, and HNSW without first running a separate database server.

The KoPy pack deliberately translates distinctive FAISS names while preserving generic index methods such as `add()`, `search()`, and common variables such as `embeddings`, `query`, `index`, `distances`, `indices`, and `top_k`. These names appear constantly in real Python retrieval code, and translating them globally would create ambiguity.

## Install

```bash
python -m pip install "faiss-cpu>=1.15,<1.16"
```

KoPy continues to target Python 3.12.x. FAISS 1.15 provides CPython 3.12 wheels for supported Windows, Linux, and macOS platforms.

## Basic exact vector search

```python
임포트 넘파이 애즈 np
임포트 파이스 애즈 faiss

embeddings = np.어레이([
    [0.0, 0.0],
    [1.0, 1.0],
    [2.0, 2.0],
], dtype=np.플로트32)

query = np.어레이([[1.1, 1.0]], dtype=np.플로트32)

index = faiss.인덱스플랫엘투(embeddings.shape[1])
index.add(embeddings)

distances, indices = index.search(query, 2)
프린트(indices)
프린트(distances)
```

Equivalent Python API:

```python
import numpy as np
import faiss

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)
distances, indices = index.search(query, 2)
```

## Cosine similarity pattern

FAISS commonly implements cosine search by L2-normalizing vectors and using inner-product search:

```python
faiss.노멀라이즈엘투(embeddings)
faiss.노멀라이즈엘투(query)
index = faiss.인덱스플랫아이피(embeddings.shape[1])
index.add(embeddings)
scores, indices = index.search(query, 5)
```

## Supported KoPy names

High-value mappings include:

- `인덱스플랫엘투` → `IndexFlatL2`
- `인덱스플랫아이피` → `IndexFlatIP`
- `인덱스아이디맵` → `IndexIDMap`
- `인덱스아이브이에프플랫` → `IndexIVFFlat`
- `인덱스에이치엔에스더블유플랫` → `IndexHNSWFlat`
- `노멀라이즈엘투` → `normalize_L2`
- `인덱스팩토리` → `index_factory`
- `라이트인덱스` → `write_index`
- `리드인덱스` → `read_index`

Generic operations including `add`, `search`, `train`, `reset`, `remove_ids`, `reconstruct`, and attributes such as `ntotal` remain upstream Python. This is intentional, not missing translation.

## RAG learning path

A practical KoPy progression is:

`documents → Sentence Transformers → embeddings → FAISS index → search → retrieved documents → LLM`

This keeps the essential retrieval vocabulary visible while KoPy reduces friction around the library-specific API surface.
