# LlamaIndex Core Library Pack

KoPy 0.5.38 adds namespace-scoped support for `llama-index-core`, the foundational RAG/orchestration package used by LlamaIndex.

## Install

```powershell
python -m pip install "llama-index-core>=0.14.24,<0.15"
```

KoPy keeps its existing Python compatibility range `>=3.12,<3.13`. The tested development interpreter remains Python 3.12.10.

## Namespace

```kopy
프롬 라마인덱스.core 임포트 도큐먼트, 벡터스토어인덱스, 목임베딩
```

translates to:

```python
from llama_index.core import Document, VectorStoreIndex, MockEmbedding
```

The real dotted package structure stays visible. For example:

```kopy
프롬 라마인덱스.core.node_parser 임포트 센텐스스플리터
```

becomes:

```python
from llama_index.core.node_parser import SentenceSplitter
```

## Main mappings

| KoPy | Python |
| --- | --- |
| `도큐먼트` | `Document` |
| `벡터스토어인덱스` | `VectorStoreIndex` |
| `스토리지컨텍스트` | `StorageContext` |
| `세팅즈` | `Settings` |
| `쿼리번들` | `QueryBundle` |
| `목임베딩` | `MockEmbedding` |
| `심플디렉터리리더` | `SimpleDirectoryReader` |
| `텍스트노드` | `TextNode` |
| `노드위드스코어` | `NodeWithScore` |
| `센텐스스플리터` | `SentenceSplitter` |
| `인제스천파이프라인` | `IngestionPipeline` |
| `메타데이터필터스` | `MetadataFilters` |
| `메타데이터필터` | `MetadataFilter` |
| `필터오퍼레이터` | `FilterOperator` |

## RAG example

```kopy
프롬 라마인덱스.core 임포트 도큐먼트, 벡터스토어인덱스, 목임베딩

documents = [
    도큐먼트(text="KoPy teaches Python through transliteration."),
    도큐먼트(text="LlamaIndex composes retrieval augmented generation pipelines."),
]

index = 벡터스토어인덱스.from_documents(
    documents,
    embed_model=목임베딩(embed_dim=8),
    show_progress=False,
)

retriever = index.as_retriever(similarity_top_k=2)
nodes = retriever.retrieve(query)
```

`MockEmbedding` is useful for deterministic local/CI pipeline tests. Production RAG applications normally inject a real embedding integration.

## Intentionally preserved Python vocabulary

KoPy does **not** globally transliterate generic RAG/orchestration vocabulary such as:

```text
documents nodes query index retriever metadata transformations
from_documents() as_retriever() retrieve() query() insert() refresh()
similarity_top_k= embed_model= show_progress= storage_context=
```

These names recur across LlamaIndex, vector databases, retrievers, papers, tutorials, and other RAG frameworks. Keeping them in Python form both prevents ambiguous cross-pack translations and helps learners recognize upstream code.

Likewise, submodule paths such as `llama_index.core.node_parser`, `llama_index.core.ingestion`, and `llama_index.core.vector_stores` remain Python-native after the root `llama_index` namespace.

## Runtime test

CI installs the real `llama-index-core` package and constructs an in-memory `VectorStoreIndex` from actual `Document` objects using `MockEmbedding`. It then calls `as_retriever()` and `retrieve()` and verifies returned LlamaIndex nodes and scores. No external API key, model download, or database server is required.
