# RapidFuzz Library Pack

KoPy 0.5.45의 `rapidfuzz / 래피드퍼즈` 팩은 검색/RAG 전처리에서 자주 쓰는 fuzzy string matching을 지원합니다. 실제 점수 계산과 후보 추출은 원본 RapidFuzz 라이브러리가 수행합니다.

## 설계 원칙

RapidFuzz 고유 scorer/extraction API만 namespace-scoped 음역을 제공합니다. 실제 Python package 구조인 `rapidfuzz.fuzz`와 `rapidfuzz.process`는 그대로 노출합니다.

다음 표현은 검색·RAG 전반에서 반복되는 핵심 원문 어휘이므로 번역하지 않습니다.

- `query`, `choices`, `candidate`, `results`
- `scorer=`, `processor=`, `score_cutoff=`, `limit=`
- `fuzz`, `process`, `utils`, `distance`

따라서 KoPy를 학습하면서 원문 RapidFuzz 코드도 자연스럽게 읽을 수 있습니다.

## 주요 음역

| KoPy | Python |
| --- | --- |
| `레이쇼` | `ratio` |
| `파셜레이쇼` | `partial_ratio` |
| `토큰소트레이쇼` | `token_sort_ratio` |
| `토큰셋레이쇼` | `token_set_ratio` |
| `더블유레이쇼` | `WRatio` |
| `큐레이쇼` | `QRatio` |
| `익스트랙트` | `extract` |
| `익스트랙트원` | `extractOne` |
| `익스트랙트이터` | `extract_iter` |
| `씨디스트` | `cdist` |
| `씨피디스트` | `cpdist` |

## 예제

```kopy
프롬 래피드퍼즈 임포트 fuzz, process

query = "KoPy Python"
choices = [
    "KoPy Python learning",
    "Rubber chemistry",
    "Python machine learning",
]

best = process.익스트랙트원(
    query,
    choices,
    scorer=fuzz.더블유레이쇼,
)

프린트(best)
```

대응하는 Python 원문은 다음과 같습니다.

```python
from rapidfuzz import fuzz, process

best = process.extractOne(
    query,
    choices,
    scorer=fuzz.WRatio,
)
```

## 설치

```bash
python -m pip install "rapidfuzz>=3.14.5,<3.15"
```

KoPy의 Python 호환 범위는 기존과 동일한 `>=3.12,<3.13`입니다.
