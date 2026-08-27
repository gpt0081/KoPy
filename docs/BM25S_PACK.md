# BM25S Library Pack

BM25S 팩은 sparse lexical retrieval 흐름을 namespace-scoped 방식으로 음역합니다. 숫자는 읽어 쓰지 않고 그대로 유지하므로 `BM25S → 비엠25에스`, `BM25 → 비엠25`가 표준입니다.

## 주요 음역

| Python | KoPy |
| --- | --- |
| `bm25s` | `비엠25에스` |
| `BM25` | `비엠25` |
| `tokenize` | `토크나이즈` |
| `index()` | `인덱스()` |
| `retrieve()` | `리트리브()` |
| `Results` | `리절츠` |
| `save()` | `세이브()` |
| `load()` | `로드()` |

`index`, `retrieve`, `save`, `load`는 다른 라이브러리에서도 흔하므로 전역 번역하지 않고 BM25S가 import된 코드에서만 위 음역을 활성화합니다.

## 예제

```kopy
임포트 비엠25에스 애즈 bm25s

코퍼스_토큰즈 = bm25s.토크나이즈(코퍼스, show_progress=False)
리트리버 = bm25s.비엠25(코퍼스=코퍼스)
리트리버.인덱스(코퍼스_토큰즈, show_progress=False)

쿼리_토큰즈 = bm25s.토크나이즈([쿼리], show_progress=False)
리절츠 = 리트리버.리트리브(쿼리_토큰즈, k=2, show_progress=False)

프린트(리절츠.다큐먼츠)
프린트(리절츠.스코어즈)
```

대응 원문은 `corpus`, `retriever`, `query`, `results`, `documents`, `scores`, `index()`, `retrieve()`입니다. KoPy는 이를 음역과 1:1로 연결해 원문 코드 학습을 돕습니다.

`show_progress`, `k`처럼 라이브러리의 세부 키워드 인자는 아직 원문을 허용합니다. 이들은 향후 전체 keyword-argument 감사에서 충돌 가능성과 교육 가치를 따로 검토합니다.

## 호환성

KoPy는 Python 3.12.x를 대상으로 하며 CI에서 실제 BM25S 인덱스를 만들고 lexical query의 순위를 검증합니다.
