# Qdrant Client Library Pack

KoPy 0.5.31의 Qdrant Client 팩은 벡터DB collection 생성, point 저장, nearest-neighbor query와 payload filter를 학습할 수 있게 합니다. 실제 저장·검색은 `qdrant-client`가 수행하며 KoPy는 API 이름만 Python으로 변환합니다.

기준 런타임은 Python 3.12.10과 `qdrant-client>=1.19,<1.20`입니다. Qdrant Client 1.19는 Python 3.10 이상을 지원합니다.

모듈 음역은 `큐드란트`, 클라이언트 클래스 음역은 `큐드란트클라이언트`로 구분합니다. 모듈명과 클래스명을 같은 표현으로 만들면 `from ... import ...` 변환이 모호해지므로 의도적으로 분리한 것입니다.

## 기본 사용

```kopy
프롬 큐드란트 임포트 큐드란트클라이언트
프롬 큐드란트.models 임포트 벡터파람스, 디스턴스, 포인트스트럭트

client = 큐드란트클라이언트(":memory:")
client.크리에이트컬렉션(
    collection_name="docs",
    vectors_config=벡터파람스(size=384, distance=디스턴스.COSINE),
)

client.upsert(collection_name="docs", points=points)
result = client.쿼리포인츠(
    collection_name="docs",
    query=query,
    limit=5,
)
```

위 코드는 핵심적으로 다음 Python API를 사용합니다.

```python
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

client = QdrantClient(":memory:")
client.create_collection(...)
client.upsert(...)
result = client.query_points(...)
```

## 지원 범위

주요 client API는 `QdrantClient`, `AsyncQdrantClient`, `create_collection`, `delete_collection`, `get_collection`, `get_collections`, `collection_exists`, `query_points`, `query_batch_points`입니다.

주요 model 타입은 `VectorParams`, `SparseVectorParams`, `SparseVector`, `PointStruct`, `Distance`, `FieldCondition`, `MatchValue`, `Filter`, `Range`, `NamedVector`입니다. `qdrant_client.models` 같은 dotted submodule 구조는 Python 원문 형태를 유지하고 그 안에서 import하는 Qdrant 고유 타입만 KoPy 음역을 제공합니다.

## 원문 그대로 남기는 표현

`client`, `collection`, `points`, `query`, `result`, `payload`, `score`, `vector`, `collection_name=`, `vectors_config=`, `with_payload=`, `limit=`는 실제 Qdrant/RAG 예제에서 반복적으로 등장하므로 그대로 둡니다.

또한 `upsert()`, `scroll()`, `retrieve()`, `delete()`, `count()` 같은 메서드는 데이터베이스·검색 라이브러리 전반에서 매우 일반적이므로 번역하지 않습니다. Qdrant를 import했다고 해서 다른 객체의 일반 메서드까지 바뀌는 일을 피하기 위한 규칙입니다.

이 원칙은 KoPy가 한국어 API를 별도로 암기하게 만드는 대신 실제 Python vector-DB 코드를 읽는 능력으로 연결되도록 하기 위한 것입니다.

## 로컬 테스트

Qdrant Client는 별도 서버 없이 `QdrantClient(":memory:")`로 로컬 in-memory 모드를 실행할 수 있습니다. KoPy CI는 이 모드에서 실제 collection 생성, point upsert, `query_points()` 검색과 score 순서를 검증합니다. 따라서 테스트는 문자열 변환만 확인하는 mock 테스트가 아닙니다.
