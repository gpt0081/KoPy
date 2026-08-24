# KoPy pandas 팩

KoPy 0.5.1은 AI/데이터 전처리용 공식 `pandas` 라이브러리 팩을 제공합니다.

실제 계산과 데이터 처리는 원래 pandas가 수행하고, KoPy 팩은 import와 API 이름을 namespace 범위에서 번역합니다.

```kopy
임포트 판다스 애즈 pd

표 = pd.데이터프레임({
    "label": ["a", "a", "b"],
    "x": [1.0, None, 5.0],
})

정제 = 표.필엔에이(0.0)
요약 = 정제.그룹바이("label").미인()
프린트(요약)
```

표준 Python으로는 다음 의미입니다.

```python
import pandas as pd

table = pd.DataFrame({
    "label": ["a", "a", "b"],
    "x": [1.0, None, 5.0],
})

cleaned = table.fillna(0.0)
summary = cleaned.groupby("label").mean()
print(summary)
```

주요 대응 예시는 다음과 같습니다.

- `pd.데이터프레임` → `pd.DataFrame`
- `pd.시리즈` → `pd.Series`
- `pd.리드씨에스브이` → `pd.read_csv`
- `표.드롭엔에이()` → `table.dropna()`
- `표.필엔에이()` → `table.fillna()`
- `표.그룹바이()` → `table.groupby()`
- `pd.머지()` → `pd.merge()`
- `pd.컨캣()` → `pd.concat()`
- `표.투넘파이()` → `table.to_numpy()`
- `pd.겟더미즈()` → `pd.get_dummies()`

팩은 pandas가 import된 파일에서만 활성화됩니다. pandas 단어를 KoPy 전역 단어로 등록하지 않으므로 다른 라이브러리와 이름이 겹쳐도 무조건 치환하지 않습니다.

현재 KoPy는 외부 라이브러리 함수의 한글 키워드 인자 이름까지 번역하지 않습니다. 예를 들어 `columns=` 같은 Python 키워드 인자는 그대로 사용하는 것이 안전합니다.

```kopy
특징 = pd.겟더미즈(표, columns=["category"])
```

설치 확인과 팩 목록은 다음 명령으로 볼 수 있습니다.

```bash
kopy packs
kopy packs pandas
kopy help pd.데이터프레임
```
