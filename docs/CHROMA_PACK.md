# Chroma Library Pack

Chroma 팩은 `chromadb`의 client, collection 관리, 저장·검색 메서드를 namespace-scoped 방식으로 음역합니다. 실제 저장과 검색은 원래 Chroma가 수행합니다.

## 주요 음역

- `Client` → `클라이언트`
- `PersistentClient` → `퍼시스턴트클라이언트`
- `create_collection` → `크리에이트컬렉션`
- `get_or_create_collection` → `겟오어크리에이트컬렉션`
- `add()` → `애드()`
- `query()` → `쿼리()`
- `upsert()` → `업서트()`
- `get()` → `겟()`
- `update()` → `업데이트()`
- `delete()` → `딜리트()`
- `count()` → `카운트()`

이 메서드들은 다른 데이터베이스에서도 흔하므로 전역 번역하지 않습니다. Chroma가 import된 코드에서만 활성화됩니다.

## 기본 예제

```kopy
임포트 크로마 애즈 chroma

client = chroma.클라이언트()
collection = client.크리에이트컬렉션(
    name="docs",
    embedding_function=None,
)

collection.애드(
    ids=["a", "b"],
    embeddings=임베딩즈,
    documents=다큐먼츠,
)

리절트 = collection.쿼리(
    query_embeddings=query_embeddings,
    n_results=2,
)
```

`embeddings → 임베딩즈`, `documents → 다큐먼츠`, `result → 리절트`는 이미 공통 식별자 음역으로 지원합니다. `client`, `collection`, `query_embeddings`는 아직 공통 식별자 전수 감사가 끝나지 않아 원문을 유지합니다. 이것은 영구 예외가 아니라 **남은 감사 범위**입니다.

`name=`, `embedding_function=`, `ids=`, `query_embeddings=`, `n_results=` 같은 키워드 인자도 함수 시그니처에 직접 연결되므로 전체 팩을 대상으로 별도 충돌 감사를 거쳐 확장합니다.

## 설치

```bash
python -m pip install "chromadb>=1.5.9,<1.6"
```

KoPy의 Python 기준은 3.12.x입니다.
