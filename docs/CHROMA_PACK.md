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

클라이언트 = chroma.클라이언트()
컬렉션 = 클라이언트.크리에이트컬렉션(
    name="docs",
    embedding_function=None,
)

컬렉션.애드(
    ids=["a", "b"],
    embeddings=임베딩즈,
    documents=다큐먼츠,
)

리절트 = 컬렉션.쿼리(
    query_embeddings=쿼리_임베딩즈,
    n_results=2,
)
```

대응하는 원문 Python의 핵심은 `client`, `collection`, `add()`, `query()`, `embeddings`, `documents`, `result`입니다. KoPy 예제에서는 가능한 범위에서 한글 음역을 우선 사용합니다.

`name=`, `embedding_function=`, `ids=`, `query_embeddings=`, `n_results=` 같은 키워드 인자는 이번 단계에서 원문을 허용합니다. keyword argument는 호출 시그니처에 직접 연결되므로 전체 팩을 대상으로 별도 충돌 감사를 거쳐 확장합니다.

## 설치

```bash
python -m pip install "chromadb>=1.5.9,<1.6"
```

KoPy의 Python 기준은 3.12.x입니다.
