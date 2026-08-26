# USearch Library Pack

KoPy 0.5.41 adds namespace-scoped support for `usearch`, a compact local approximate-nearest-neighbor engine.

## Why USearch

USearch complements KoPy's existing FAISS, Qdrant, Chroma, and LanceDB support with a small local vector index that is easy to run without a database server or API key. The upstream Python package is implemented with native bindings and supports Windows, Linux, and macOS.

## Import style

```kopy
프롬 유서치.index 임포트 인덱스, 매치즈

index = 인덱스(ndim=384, metric="cos", dtype="f32")
```

This translates to:

```python
from usearch.index import Index, Matches

index = Index(ndim=384, metric="cos", dtype="f32")
```

The real dotted package path `usearch.index` is intentionally preserved.

## Translation policy

USearch-specific public types are transliterated, including `Index`, `Indexes`, `IndexedKeys`, `Match`, `Matches`, `BatchMatches`, `CompiledMetric`, `Clustering`, and `kmeans`.

Transferable vector-search vocabulary remains upstream Python:

- `vectors`, `query`, `keys`, `matches`
- `add()`, `search()`, `save()`, `load()`, `view()`
- `ndim=`, `metric=`, `dtype=`, `connectivity=`, `expansion_add=`, `expansion_search=`

These terms appear across vector databases, ANN libraries, documentation, and papers. Keeping them intact avoids ambiguous global translations and helps KoPy learners move directly into original Python code.

## Local search example

```kopy
임포트 넘파이 애즈 np
프롬 유서치.index 임포트 인덱스

vectors = np.어레이([
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
], dtype=np.플로트32)
keys = np.어레이([10, 20], dtype=np.인트64)
query = np.어레이([0.99, 0.01, 0.0], dtype=np.플로트32)

index = 인덱스(ndim=3, metric="cos", dtype="f32")
index.add(keys, vectors)
matches = index.search(query, 2)
```

## Compatibility

KoPy remains pinned to Python `>=3.12,<3.13`. CI installs USearch 2.26.x and executes a real in-memory vector index/search test on Windows, Ubuntu, and macOS.
