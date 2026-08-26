# FAISS Library Pack

FAISS 팩은 `faiss`의 벡터 검색 API를 namespace-scoped 방식으로 음역합니다. KoPy의 기본 원칙은 영어 API와 식별자를 한글로 음역하는 것이며, 숫자는 그대로 유지합니다.

## 핵심 음역

- `IndexFlatL2` → `인덱스플랫엘2`
- `IndexFlatIP` → `인덱스플랫아이피`
- `IndexIDMap2` → `인덱스아이디맵2`
- `normalize_L2` → `노멀라이즈엘2`
- `index_factory` → `인덱스팩토리`
- `add()` → `애드()`
- `search()` → `서치()`
- `train()` → `트레인()`
- `reset()` → `리셋()`

`add`, `search`, `train`처럼 다른 라이브러리에도 존재하는 이름은 전역 번역하지 않습니다. **FAISS가 import된 코드에서만** 위 음역을 활성화해 충돌을 피합니다.

## 기본 벡터 검색

```kopy
임포트 넘파이 애즈 np
임포트 파이스 애즈 faiss

임베딩즈 = np.어레이([[0.0, 0.0], [1.0, 1.0]], dtype=np.플로트32)
쿼리 = np.어레이([[0.9, 1.0]], dtype=np.플로트32)

인덱스 = faiss.인덱스플랫엘2(임베딩즈.shape[1])
인덱스.애드(임베딩즈)
디스턴시즈, 인디시즈 = 인덱스.서치(쿼리, 2)
```

대응하는 원문 Python은 다음과 같습니다.

```python
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)
distances, indices = index.search(query, 2)
```

`embeddings → 임베딩즈`, `query → 쿼리`, `index → 인덱스`, `distances → 디스턴시즈`, `indices → 인디시즈`처럼 원문과 음역을 1:1로 연결합니다.

## 설치 및 호환성

```bash
python -m pip install "faiss-cpu>=1.15,<1.16"
```

KoPy의 Python 기준은 3.12.x입니다. 실제 runtime 테스트는 FAISS 인덱스 생성, 벡터 추가, 최근접 이웃 검색 결과를 검증합니다.
