# XGBoost Library Pack

KoPy 0.5.16의 XGBoost 팩은 `xgboost`, `엑스지부스트`, `xgb` 네임스페이스에서 자주 쓰는 공개 Python API를 한글 음역으로 사용할 수 있게 합니다.

실제 학습과 예측은 XGBoost가 수행합니다. KoPy는 import로 활성화된 네임스페이스 안에서만 등록된 API 이름을 번역합니다.

## 설치

```powershell
python -m pip install "xgboost>=3.4,<3.5"
```

KoPy의 현재 Python 기준은 3.12.10이며 XGBoost 3.4.x는 Python 3.12 이상을 지원합니다.

## 분류기 예시

```kopy
임포트 넘파이 애즈 np
임포트 엑스지부스트 애즈 xgb

X = np.어레이([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
y = np.어레이([0, 0, 0, 1])

모델 = xgb.엑스지비클래시파이어(
    n_estimators=20,
    max_depth=3,
    tree_method="hist",
    device="cpu",
)
모델.핏(X, y)
예측 = 모델.프리딕트(X)
확률 = 모델.프리딕트프로바(X)
```

표준 Python으로는 다음과 같습니다.

```python
import numpy as np
import xgboost as xgb

X = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
y = np.array([0, 0, 0, 1])

모델 = xgb.XGBClassifier(
    n_estimators=20,
    max_depth=3,
    tree_method="hist",
    device="cpu",
)
모델.fit(X, y)
예측 = 모델.predict(X)
확률 = 모델.predict_proba(X)
```

## Core training API

```kopy
임포트 엑스지부스트 애즈 xgb

학습데이터 = xgb.디매트릭스(X, label=y)
부스터 = xgb.트레인(
    {"objective": "binary:logistic", "tree_method": "hist"},
    학습데이터,
    num_boost_round=10,
)
예측 = 부스터.프리딕트(학습데이터)
```

## 주요 번역

- `DMatrix` → `디매트릭스`
- `QuantileDMatrix` → `퀀타일디매트릭스`
- `Booster` → `부스터`
- `train` → `트레인`
- `cv` → `시브이`
- `XGBClassifier` → `엑스지비클래시파이어`
- `XGBRegressor` → `엑스지비리그레서`
- `XGBRanker` → `엑스지비랭커`
- `fit` → `핏`
- `predict` → `프리딕트`
- `predict_proba` → `프리딕트프로바`
- `save_model` → `세이브모델`
- `load_model` → `로드모델`
- `get_booster` → `겟부스터`
- `get_score` → `겟스코어`
- `EarlyStopping` → `얼리스토핑`

## 충돌 방지

`n_estimators=`, `max_depth=`, `learning_rate=`, `objective=`, `eval_metric=`, `tree_method=`, `device=`, `n_jobs=`, `random_state=`, `num_boost_round=` 같은 키워드 인자는 Python 원형을 유지합니다.

이 이름들은 XGBoost 밖에서도 쓰일 수 있으므로 KoPy Core 전역 단어표에 등록하지 않습니다. `핏`, `프리딕트` 같은 API 이름 역시 XGBoost import가 활성화된 문맥에서만 이 팩의 규칙으로 처리됩니다.
