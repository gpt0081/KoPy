# KoPy Hugging Face Datasets Pack

KoPy의 `datasets / 데이터셋츠` 팩은 Hugging Face Datasets의 데이터 로딩, 전처리, 분할, 포맷 변환 API를 KoPy 음역으로 사용할 수 있게 합니다. 실제 데이터 처리 엔진은 원래 `datasets` 패키지입니다.

## 설치

```powershell
python -m pip install "datasets>=4.8,<4.9"
```

## 예시

```kopy
프롬 데이터셋츠 임포트 데이터셋

데이터 = 데이터셋.프롬딕트({
    "text": ["a", "bb", "ccc", "dddd"],
    "label": [0, 1, 0, 1],
})

가공 = 데이터.맵(lambda row: {"length": 렌(row["text"])})
정제 = 가공.필터(lambda row: row["length"] >= 2)
분할 = 정제.트레인테스트스플릿(test_size=0.5, seed=42)
토치용 = 정제.위드포맷("torch")
```

표준 Python으로는 다음 흐름입니다.

```python
from datasets import Dataset

data = Dataset.from_dict({
    "text": ["a", "bb", "ccc", "dddd"],
    "label": [0, 1, 0, 1],
})

processed = data.map(lambda row: {"length": len(row["text"])})
filtered = processed.filter(lambda row: row["length"] >= 2)
split = filtered.train_test_split(test_size=0.5, seed=42)
torch_ready = filtered.with_format("torch")
```

## 주요 대응

- `데이터셋` → `Dataset`
- `데이터셋딕트` → `DatasetDict`
- `로드데이터셋` → `load_dataset`
- `프롬딕트` → `from_dict`
- `맵` → `map`
- `필터` → `filter`
- `셀렉트` → `select`
- `셔플` → `shuffle`
- `트레인테스트스플릿` → `train_test_split`
- `위드포맷` → `with_format`
- `세이브투디스크` → `save_to_disk`
- `로드프롬디스크` → `load_from_disk`

## 안전 규칙

`test_size=`, `seed=`, `batched=`, `batch_size=`, `num_proc=`, `data_files=` 같은 키워드 인자 이름은 Python 원형을 유지합니다. 이 이름들은 다른 라이브러리에서도 쓰이므로 KoPy Core 전역 단어로 번역하지 않습니다.

`맵`, `필터`, `셔플` 같은 일반적인 단어도 `datasets` 팩이 import되어 활성화된 경우에만 외부 API 번역 후보가 됩니다. 여러 활성 팩이 같은 KoPy 철자를 서로 다른 Python 이름으로 정의하면 KoPy는 임의로 선택하지 않습니다.
