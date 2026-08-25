# Sentence Transformers Library Pack

KoPy 0.5.28 adds namespace-scoped support for `sentence-transformers` / `sentence_transformers`.

## Why this pack

Sentence Transformers connects the existing Transformers, PyTorch, Datasets and TorchMetrics stack to embedding, similarity and semantic-search workflows. The pack does not reimplement the library. KoPy transliterates selected API names and the upstream library performs the actual computation.

## Namespace

```kopy
임포트 센텐스트랜스포머스 애즈 st
```

becomes:

```python
import sentence_transformers as st
```

Common mappings include:

- `센텐스트랜스포머` → `SentenceTransformer`
- `크로스인코더` → `CrossEncoder`
- `스파스인코더` → `SparseEncoder`
- `인코드` → `encode`
- `인코드쿼리` → `encode_query`
- `인코드도큐먼트` → `encode_document`
- `유틸.코사인심` → `util.cos_sim`
- `유틸.시맨틱서치` → `util.semantic_search`
- `모델즈.보우` → `models.BoW`

## Learning-oriented conventions

KoPy deliberately keeps model IDs, tensor/data variable conventions and generic keyword arguments in upstream form. Names such as `model`, `sentences`, `embeddings`, `query_embeddings`, `corpus_embeddings`, plus `batch_size=`, `convert_to_tensor=`, `normalize_embeddings=`, `top_k=` and `device=` remain Python-native.

This preserves the bridge to real Sentence Transformers examples instead of creating a parallel vocabulary learners must later unlearn.

## Example

```kopy
임포트 센텐스트랜스포머스 애즈 st

model = st.센텐스트랜스포머("sentence-transformers/all-MiniLM-L6-v2")
embeddings = model.인코드(sentences, convert_to_tensor=True)
query_embeddings = model.인코드(query, convert_to_tensor=True)
hits = st.유틸.시맨틱서치(query_embeddings, embeddings, top_k=5)
```

## Runtime testing

CI installs Sentence Transformers 6.0.x on Python 3.12.10 across Windows, Ubuntu and macOS. The runtime test avoids network/model downloads by constructing a real `SentenceTransformer` from the built-in `models.BoW` module, then executes `encode`, `util.cos_sim` and `util.semantic_search` and validates actual embedding shapes and search scores.
