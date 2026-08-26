# LanceDB Library Pack

KoPy 0.5.39의 `lancedb / 랜스디비` 팩은 로컬·원격 LanceDB를 사용하는 vector search, full-text search, hybrid retrieval 학습을 위한 namespace-scoped Library Pack입니다.

기준 런타임은 Python 3.12.10과 `lancedb>=0.37.1,<0.38`입니다. LanceDB 0.37.1은 Python 3.10 이상을 요구하고 Windows x86-64, Linux x86-64/ARM64, macOS ARM64 wheel을 제공합니다.

## 설계 원칙

KoPy는 LanceDB를 다시 구현하지 않습니다. `랜스디비` 같은 모듈 음역과 LanceDB 고유 타입에만 선택적으로 KoPy 표기를 제공하고, 실제 database/retrieval 코드를 읽을 때 계속 등장하는 표현은 upstream Python 그대로 남깁니다.

의도적으로 원문을 유지하는 대표 표현:

- `connect()` / `connect_async()`
- `create_table()` / `open_table()`
- `add()` / `search()` / `limit()` / `to_list()`
- `create_index()` / `create_fts_index()` / `rerank()`
- `query`, `documents`, `embeddings`, `table`, `results`
- `data=`, `mode=`, `query_type=`, `vector_column_name=`

이 이름들은 LanceDB만의 표현이 아니라 Python database·vector search·RAG 코드 전반에서 재사용되므로 전역 번역하지 않습니다.

예제에서는 명시적 alias `ldb`를 사용합니다. 원 모듈명과 동일한 alias보다 KoPy↔Python 왕복에서 namespace 경계가 명확하고, 실제 Python에서도 흔히 쓰는 짧은 alias 패턴을 학습할 수 있습니다.

## 지원하는 고유 타입

| KoPy | Python |
| --- | --- |
| `디비커넥션` | `DBConnection` |
| `어싱크커넥션` | `AsyncConnection` |
| `랜스모델` | `LanceModel` |
| `벡터` | `Vector` |
| `리랭커` | `Reranker` |
| `알알에프리랭커` | `RRFReranker` |
| `리니어컴비네이션리랭커` | `LinearCombinationReranker` |

`lancedb.pydantic`, `lancedb.rerankers` 같은 실제 dotted package path도 그대로 노출합니다.

## 로컬 vector search

```kopy
임포트 랜스디비 애즈 ldb

db = ldb.connect("./lancedb-data")

documents = [
    {"id": "alpha", "vector": [1.0, 0.0], "text": "alpha document"},
    {"id": "beta", "vector": [0.0, 1.0], "text": "beta document"},
]

table = db.create_table(
    "docs",
    data=documents,
    mode="overwrite",
)

query = [0.99, 0.01]
results = table.search(query).limit(2).to_list()
```

KoPy 변환 후 핵심 구조는 그대로 표준 LanceDB Python이다.

```python
import lancedb as ldb

db = ldb.connect("./lancedb-data")
table = db.create_table("docs", data=documents, mode="overwrite")
results = table.search(query).limit(2).to_list()
```

## schema와 reranker

```kopy
프롬 랜스디비.pydantic 임포트 랜스모델, 벡터
프롬 랜스디비.rerankers 임포트 알알에프리랭커
```

이는 다음 Python 원문으로 변환된다.

```python
from lancedb.pydantic import LanceModel, Vector
from lancedb.rerankers import RRFReranker
```

## 테스트 범위

CI에서는 `lancedb>=0.37.1,<0.38`을 Windows, Ubuntu, macOS에 실제 설치한다. 임시 로컬 database를 생성한 뒤 `connect → create_table → search → limit → to_list`를 실제 실행하고 nearest-neighbor 순서와 `_distance`를 검증한다. 외부 서버, API key, embedding model download는 사용하지 않는다.
