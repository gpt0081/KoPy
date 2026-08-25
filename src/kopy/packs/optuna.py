"""Official Optuna library pack for KoPy.

The pack focuses on the stable, high-value study/trial API used in real
hyperparameter optimization code. Generic keyword arguments and user-defined
parameter names remain in standard Python form to avoid ambiguous global
translations and preserve transfer to upstream Optuna examples.
"""

from __future__ import annotations

from .base import LibraryPack


OPTUNA_PACK = LibraryPack(
    name="optuna",
    module="optuna",
    kopy_module="옵튜나",
    preferred_aliases=("optuna",),
    description="하이퍼파라미터 탐색 Study/Trial·샘플링·가지치기·최적화 API 팩",
    members={
        "크리에이트스터디": "create_study",
        "로드스터디": "load_study",
        "딜리트스터디": "delete_study",
        "스터디": "Study",
        "트라이얼": "Trial",
        "프로즌트라이얼": "FrozenTrial",
        "트라이얼스테이트": "TrialState",
        "옵티마이즈": "optimize",
        "서제스트플로트": "suggest_float",
        "서제스트인트": "suggest_int",
        "서제스트캐터고리컬": "suggest_categorical",
        "리포트": "report",
        "슈드프룬": "should_prune",
        "셋유저애트르": "set_user_attr",
        "셋시스템애트르": "set_system_attr",
        "베스트트라이얼": "best_trial",
        "베스트밸류": "best_value",
        "베스트파람스": "best_params",
        "트라이얼즈": "trials",
        "겟트라이얼즈": "get_trials",
        "스톱": "stop",
        "애스크": "ask",
        "텔": "tell",
        "인큐트라이얼": "enqueue_trial",
        "겟트라이얼": "get_trial",
    },
    member_descriptions={
        "create_study": "새 Optuna Study를 생성합니다.",
        "load_study": "저장된 Study를 불러옵니다.",
        "Study": "여러 Trial과 최적화 상태를 관리하는 객체입니다.",
        "Trial": "한 번의 목적함수 평가와 파라미터 제안을 나타냅니다.",
        "optimize": "목적함수를 반복 평가하여 Study를 최적화합니다.",
        "suggest_float": "Trial에서 부동소수점 하이퍼파라미터를 제안합니다.",
        "suggest_int": "Trial에서 정수 하이퍼파라미터를 제안합니다.",
        "suggest_categorical": "Trial에서 범주형 하이퍼파라미터를 제안합니다.",
        "report": "중간 평가값을 Trial에 보고합니다.",
        "should_prune": "현재 Trial을 조기 종료할지 판단합니다.",
        "best_params": "현재 Study에서 최선 Trial의 파라미터 사전을 반환합니다.",
    },
    examples={
        "create_study": (
            "임포트 옵튜나\nstudy = 옵튜나.크리에이트스터디(direction='minimize')",
            "import optuna\nstudy = optuna.create_study(direction='minimize')",
        ),
        "suggest_float": (
            "x = trial.서제스트플로트('x', -10.0, 10.0)",
            "x = trial.suggest_float('x', -10.0, 10.0)",
        ),
        "optimize": (
            "study.옵티마이즈(objective, n_trials=20)",
            "study.optimize(objective, n_trials=20)",
        ),
    },
)
