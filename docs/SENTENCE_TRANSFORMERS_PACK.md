# Sentence Transformers Library Pack

KoPy 0.5.28 adds namespace-scoped support for `sentence-transformers` / `sentence_transformers`.

## Why this pack

Sentence Transformers connects the existing Transformers, PyTorch, Datasets and TorchMetrics stack to embedding and similarity workflows. The pack does not reimplement the library. KoPy transliterates selected public API names and the upstream library performs the actual computation.

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
- `멀티벡터인코더` → `MultiVectorEncoder`
- `시밀래리티펑션` → `SimilarityFunction`
- `인코드` → `encode`
- `인코드쿼리` → `encode_query`
- `인코드도큐먼트` → `encode_document`
- `시밀래리티` → `similarity`

## Sentence Transformers 6 dotted submodules

Sentence Transformers 6.x does not expose `models` and `util` as public attributes on `import sentence_transformers as st`. Therefore KoPy does not invent `st.모델즈` or `st.유틸` spellings. Dotted module paths remain real Python:

```kopy
프롬 sentence_transformers.models 임포트 BoW
프롬 sentence_transformers.util 임포트 semantic_search
```

This mirrors KoPy's general rule for framework-sensitive or deeply nested module paths: keep the real Python path when translating it would create an API shape that upstream does not provide.

## Learning-oriented conventions

KoPy deliberately keeps model IDs, tensor/data variable conventions and generic keyword arguments in upstream form. Names such as `model`, `sentences`, `embeddings`, `query_embeddings`, `corpus_embeddings`, plus `batch_size=`, `convert_to_tensor=`, `normalize_embeddings=`, `top_k=` and `device=` remain Python-native.

## Example

```kopy
임포트 센텐스트랜스포머스 애즈 st

model = st.센텐스트랜스포머("sentence-transformers/all-MiniLM-L6-v2")
embeddings = model.인코드(sentences, convert_to_tensor=True)
query_embeddings = model.인코드(query, convert_to_tensor=True)
scores = model.시밀래리티(query_embeddings, embeddings)
```

## Runtime testing

CI installs Sentence Transformers 6.0.x on Python 3.12.10 across Windows, Ubuntu and macOS. The runtime test avoids network/model downloads by importing the real `sentence_transformers.models.BoW` module via its Python-native dotted path, constructing a real `SentenceTransformer`, and then executing KoPy-translated `encode` and `similarity` plus upstream `semantic_search`. It validates real embedding shapes, similarity output and retrieval scores.
