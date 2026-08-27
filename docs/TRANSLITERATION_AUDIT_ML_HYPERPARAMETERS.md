# ML 하이퍼파라미터 음역 감사

KoPy의 기본값은 영어 식별자와 API를 한글로 **음역**하는 것입니다. 이번 감사에서는 XGBoost와 LightGBM 예제에 남아 있던 공통 머신러닝 식별자와 키워드 인자를 정리합니다.

## 추가된 공통 음역

| Python | KoPy |
| --- | --- |
| `n_estimators` | `엔_에스티메이터즈` |
| `max_depth` | `맥스_뎁스` |
| `learning_rate` | `러닝_레이트` |
| `n_jobs` | `엔_잡스` |
| `num_leaves` | `넘_리브즈` |
| `min_child_samples` | `민_차일드_샘플즈` |
| `tree_method` | `트리_메서드` |
| `device` | `디바이스` |
| `verbosity` | `버보시티` |
| `label` | `레이블` |
| `num_boost_round` | `넘_부스트_라운드` |
| `proba` | `프로바` |

언더스코어는 원문의 단어 경계를 그대로 유지합니다. `n_estimators`의 `n`은 `엔`, `num_leaves`의 `num`은 `넘`으로 음역합니다.

## 숫자와 데이터 값

숫자는 음역하지 않습니다.

```kopy
모델 = xgb.엑스지비클래시파이어(
    엔_에스티메이터즈=20,
    맥스_뎁스=2,
    러닝_레이트=0.3,
)
```

여기서 `20`, `2`, `0.3`은 그대로 Python 숫자입니다. `디바이스="cuda:0"`, `트리_메서드="hist"`처럼 문자열 데이터도 바꾸지 않습니다.

## 원문 Python과의 연결

```kopy
모델 = xgb.엑스지비클래시파이어(
    엔_에스티메이터즈=20,
    맥스_뎁스=2,
    러닝_레이트=0.3,
    트리_메서드="hist",
    디바이스="cpu",
)
모델.핏(엑스, 와이)
프레즈 = 모델.프리딕트(엑스)
```

위 코드는 다음 Python으로 복원됩니다.

```python
model = xgb.XGBClassifier(
    n_estimators=20,
    max_depth=2,
    learning_rate=0.3,
    tree_method="hist",
    device="cpu",
)
model.fit(X, y)
preds = model.predict(X)
```

KoPy 학습 자료는 음역을 기본으로 보여주되 바로 대응되는 원문 Python 이름을 함께 설명합니다. `top_k`처럼 별도로 문서화된 교육 예외가 아닌 영어 식별자를 관성적으로 남기지 않는 것이 기준입니다.
