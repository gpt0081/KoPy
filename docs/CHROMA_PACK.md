# Chroma Library Pack

KoPy 0.5.32의 Chroma 팩은 `chromadb`의 로컬·서버 client와 collection 관리 API를 namespace-scoped 방식으로 음역합니다. 실제 저장·검색은 원래 `chromadb` 라이브러리가 수행합니다.

## 설치

```bash
python -m pip install "chromadb>=1.5.9,<1.6"
```

KoPy의 Python 기준은 3.12.10이며 Chroma 1.5.9는 Python 3.9 이상을 지원합니다.

## 기본 예제

```kopy
임포트 크로마 애즈 chroma

client = chroma.클라이언트()
collection = client.크리에이트컬렉션(
    name="docs",
    embedding_function=None,
)

collection.add(
    ids=["a", "b"],
    embeddings=[[1.0, 0.0], [0.0, 1.0]],
    documents=["alpha", "beta"],
)

result = collection.query(
    query_embeddings=[[0.99, 0.01]],
    n_results=2,
)
```

표준 Python에서는 다음 핵심 부분과 대응합니다.

```python
import chromadb as chroma
client = chroma.Client()
collection = client.create_collection(name="docs", embedding_function=None)
```

## 지원 범위

- `Client` → `클라이언트`
- `PersistentClient` → `퍼시스턴트클라이언트`
- `HttpClient` → `에이치티티피클라이언트`
- `AsyncHttpClient` → `어싱크에이치티티피클라이언트`
- `create_collection` → `크리에이트컬렉션`
- `get_collection` → `겟컬렉션`
- `get_or_create_collection` → `겟오어크리에이트컬렉션`
- `delete_collection` → `딜리트컬렉션`
- `list_collections` → `리스트컬렉션즈`
- `count_collections` → `카운트컬렉션즈`

## 의도적으로 번역하지 않는 표현

`collection`, `ids`, `documents`, `embeddings`, `query_embeddings`, `result`, `metadata` 같은 검색/RAG 용어는 실제 Python 코드와 문서에서 반복되므로 그대로 유지합니다.

`add()`, `query()`, `upsert()`, `get()`, `update()`, `delete()`, `count()`도 여러 데이터베이스와 검색 라이브러리에서 공통으로 쓰이는 일반 동작이므로 전역 번역하지 않습니다. `name=`, `embedding_function=`, `ids=`, `embeddings=`, `documents=`, `query_embeddings=`, `n_results=`, `where=` 같은 키워드 인자도 Python 원형을 유지합니다.

이 원칙 덕분에 KoPy에서 Chroma를 익힌 뒤 원문 Chroma/RAG 코드를 읽을 때 용어 연결이 끊기지 않습니다.

## 저장 방식

메모리 실험은 `chroma.클라이언트()`를 사용하고, 로컬 지속 저장은 다음처럼 사용할 수 있습니다.

```kopy
임포트 크로마 애즈 chroma
client = chroma.퍼시스턴트클라이언트(path="./chroma-data")
```

서버 모드에서는 `에이치티티피클라이언트` 또는 `어싱크에이치티티피클라이언트`를 사용할 수 있습니다.
