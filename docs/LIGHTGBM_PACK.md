# LightGBM Library Pack

KoPy 0.5.17의 LightGBM 팩은 `lightgbm`, `라이트지비엠`, `lgb` 네임스페이스에서 자주 쓰는 공개 Python API를 한글 음역으로 사용할 수 있게 합니다.

실제 학습과 예측은 LightGBM이 수행합니다. KoPy는 import로 활성화된 네임스페이스 안에서만 등록된 API 이름을 번역합니다.

## 설치

```powershell
python -m pip install "lightgbm>=4.7,<4.8"
```

KoPy의 현재 Python 기준은 3.12.10이며 LightGBM 4.7.x는 Python 3.12를 지원합니다.

## 분류기 예시

```kopy
임포트 넘파이 애즈 np
임포트 라이트지비엠 애즈 lgb

X = np.어레이([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
y = np.어레이([0, 0, 0, 1])

모델 = lgb.엘지비엠클래시파이어(
    n_estimators=20,
    num_leaves=4,
    min_child_samples=1,
    learning_rate=0.2,
    verbosity=-1,
    n_jobs=1,
)
모델.핏(X, y)
예측 = 모델.프리딕트(X)
확률 = 모델.프리딕트프로바(X)
```

표준 Python으로는 다음과 같습니다.

```python
import numpy as np
import lightgbm as lgb

X = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
y = np.array([0, 0, 0, 1])

모델 = lgb.LGBMClassifier(
    n_estimators=20,
    num_leaves=4,
    min_child_samples=1,
    learning_rate=0.2,
    verbosity=-1,
    n_jobs=1,
)
모델.fit(X, y)
예측 = 모델.predict(X)
확률 = 모델.predict_proba(X)
```

## Core training API

```kopy
임포트 라이트지비엠 애즈 lgb

학습데이터 = lgb.데이터셋(X, label=y)
부스터 = lgb.트레인(
    {"objective": "binary", "verbosity": -1},
    학습데이터,
    num_boost_round=10,
)
예측 = 부스터.프리딕트(X)
```

## 주요 번역

- `Dataset` → `데이터셋`
- `Booster` → `부스터`
- `train` → `트레인`
- `cv` → `시브이`
- `LGBMClassifier` → `엘지비엠클래시파이어`
- `LGBMRegressor` → `엘지비엠리그레서`
- `LGBMRanker` → `엘지비엠랭커`
- `fit` → `핏`
- `predict` → `프리딕트`
- `predict_proba` → `프리딕트프로바`
- `early_stopping` → `얼리스토핑`
- `log_evaluation` → `로그이밸류에이션`
- `save_model` → `세이브모델`
- `feature_importance` → `피처임포턴스`

## 키워드 인자 정책

`n_estimators=`, `num_leaves=`, `min_child_samples=`, `learning_rate=`, `objective=`, `verbosity=`, `n_jobs=`, `random_state=`, `num_boost_round=`, `label=` 같은 키워드 인자는 Python 원형을 유지합니다.

이 이름들은 다른 라이브러리에서도 사용될 수 있으므로 KoPy Core 전역 단어표에 넣지 않습니다. LightGBM API 이름 역시 `lightgbm` 네임스페이스가 활성화된 경우에만 번역합니다.
