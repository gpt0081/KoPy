# BM25S Library Pack

KoPy 0.5.33 adds a namespace-scoped pack for `bm25s`, a sparse lexical-search implementation of BM25.

## Scope

The KoPy module name is `비엠이십오에스`.

| KoPy | Python |
| --- | --- |
| `비엠이십오에스` | `bm25s` |
| `비엠이십오` | `BM25` |
| `토크나이즈` | `tokenize` |
| `리절츠` | `Results` |
| `겟유니크토큰즈` | `get_unique_tokens` |

BM25S-specific entry points are transliterated only when the pack namespace is active.

## Retrieval vocabulary deliberately kept in Python

KoPy intentionally keeps the following names in upstream Python form:

- `corpus`, `query`, `corpus_tokens`, `query_tokens`, `retriever`, `results`
- `documents`, `scores`, `k`
- `index()`, `retrieve()`, `save()`, `load()`
- keyword arguments such as `show_progress=`, `stopwords=`, `stemmer=`, `method=`, `backend=`

These are transferable information-retrieval concepts or generic method names. Translating them globally would both hide useful original terminology and create ambiguity with other search, vector database, and indexing libraries.

## Example

```kopy
임포트 비엠이십오에스 애즈 bm25s

corpus = [
    "machine learning uses data",
    "rubber chemistry uses vulcanization additives",
    "vector search retrieves documents",
]

corpus_tokens = bm25s.토크나이즈(corpus, show_progress=False)
retriever = bm25s.비엠이십오(corpus=corpus)
retriever.index(corpus_tokens, show_progress=False)

query = "rubber vulcanization"
query_tokens = bm25s.토크나이즈([query], show_progress=False)
results = retriever.retrieve(query_tokens, k=2, show_progress=False)

프린트(results.documents)
프린트(results.scores)
```

This translates to the same BM25S workflow used in ordinary Python: tokenize the corpus, build the sparse BM25 index, tokenize the query, then retrieve ranked documents and scores.

## Compatibility and testing

The pack targets KoPy's existing Python 3.12.10 compatibility range. CI installs `bm25s>=0.3.10,<0.4` and runs the real library on Windows, Ubuntu, and macOS. The runtime test builds an actual BM25 index and checks that a lexical query ranks the expected document first.
