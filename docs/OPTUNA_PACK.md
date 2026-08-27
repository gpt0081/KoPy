# Optuna Library Pack

KoPy의 Optuna 팩은 하이퍼파라미터 탐색에서 가장 자주 쓰는 Study/Trial API를 namespace-scoped 방식으로 제공합니다. 실제 최적화는 upstream Optuna가 수행합니다.

기준 라이브러리는 Optuna 4.9.x이며 KoPy의 Python 3.12.10 범위와 호환됩니다.

현재 canonical 음역은 Python 식별자의 `_` 구조를 유지합니다. 예를 들어 `create_study → 크리에이트_스터디`, `suggest_float → 서제스트_플로트`, `best_params → 베스트_패럼즈`입니다. 예전의 `크리에이트스터디`, `서제스트플로트`, `베스트파람스` 같은 표기는 기존 KoPy 소스 호환을 위해 입력 alias로 계속 허용하지만, Python → KoPy 변환과 새 학습 자료에서는 canonical 표기를 사용합니다.

```kopy
임포트 옵튜나


def objective(trial):
    러닝_레이트 = trial.서제스트_플로트("learning_rate", 1e-4, 1e-1, log=True)
    맥스_뎁스 = trial.서제스트_인트("max_depth", 2, 8)
    return (러닝_레이트 - 0.01) ** 2 + (맥스_뎁스 - 4) ** 2


study = 옵튜나.크리에이트_스터디(direction="minimize")
study.옵티마이즈(objective, n_trials=20)
프린트(study.베스트_패럼즈)
```

위 코드는 다음 Python 표현으로 변환됩니다.

```python
import optuna


def objective(trial):
    learning_rate = trial.suggest_float("learning_rate", 1e-4, 1e-1, log=True)
    max_depth = trial.suggest_int("max_depth", 2, 8)
    return (learning_rate - 0.01) ** 2 + (max_depth - 4) ** 2


study = optuna.create_study(direction="minimize")
study.optimize(objective, n_trials=20)
print(study.best_params)
```

## 지원 범위

주요 지원 API는 `create_study`, `load_study`, `delete_study`, `Study`, `Trial`, `FrozenTrial`, `TrialState`, `optimize`, `suggest_float`, `suggest_int`, `suggest_categorical`, `report`, `should_prune`, `best_trial`, `best_value`, `best_params`, `trials`, `get_trials`, `ask`, `tell`, `enqueue_trial` 등입니다.

## 음역 및 충돌 방지 원칙

숫자와 문자열 데이터는 변환하지 않습니다. 사용자 정의 Optuna 파라미터 이름인 `"learning_rate"`, `"max_depth"`도 문자열 데이터이므로 그대로 둡니다.

`learning_rate`, `max_depth`처럼 이미 안전한 공통 학습 식별자는 각각 `러닝_레이트`, `맥스_뎁스`로 음역합니다. 반면 `study`, `trial`, `objective`는 `Study`, `Trial` 클래스와 직접 충돌하는 스코프 문제가 있고, `direction=`, `storage=`, `timeout=`, `log=` 같은 키워드는 여러 라이브러리에서 재사용됩니다. 이들은 영구 영어 예외가 아니라 후속 문맥/namespace 기반 감사 대상입니다. 단순 전역 치환으로 넣지는 않습니다.

Optuna API 음역은 `옵튜나`가 import된 코드에서만 활성화됩니다. 따라서 다른 라이브러리의 `optimize`, `report`, `stop` 같은 이름과 전역 충돌하지 않습니다.
