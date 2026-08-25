# Optuna Library Pack

KoPy 0.5.25의 Optuna 팩은 하이퍼파라미터 탐색에서 가장 자주 쓰는 Study/Trial API를 namespace-scoped 방식으로 제공합니다. 실제 최적화는 upstream Optuna가 수행합니다.

기준 라이브러리는 Optuna 4.9.x이며 KoPy의 Python 3.12.10 범위와 호환됩니다.

```kopy
임포트 옵튜나


def objective(trial):
    learning_rate = trial.서제스트플로트("learning_rate", 1e-4, 1e-1, log=True)
    max_depth = trial.서제스트인트("max_depth", 2, 8)
    return (learning_rate - 0.01) ** 2 + (max_depth - 4) ** 2


study = 옵튜나.크리에이트스터디(direction="minimize")
study.옵티마이즈(objective, n_trials=20)
프린트(study.베스트파람스)
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

## 교육 및 충돌 방지 원칙

`study`, `trial`, `objective`, `learning_rate`, `max_depth`, `best_params`처럼 실제 Optuna/Python 코드에서 반복해서 보는 개념은 학습 연결성을 위해 일부 영어 관례를 남길 수 있습니다. 특히 사용자 정의 파라미터 이름은 문자열이므로 번역하지 않습니다.

`direction=`, `study_name=`, `storage=`, `sampler=`, `pruner=`, `n_trials=`, `timeout=`, `callbacks=`, `catch=`, `gc_after_trial=`, `show_progress_bar=`, `log=` 같은 키워드 인자는 다른 API와 겹치거나 upstream 문서에서 그대로 학습할 가치가 있어 전역 번역하지 않습니다.

Optuna API 음역도 `옵튜나`가 import된 코드에서만 활성화됩니다. 따라서 다른 라이브러리의 `optimize`, `report`, `stop` 같은 이름과 전역 충돌하지 않습니다.
