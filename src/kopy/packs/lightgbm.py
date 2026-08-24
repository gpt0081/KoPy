"""Official LightGBM library pack for KoPy.

LightGBM remains the runtime implementation. This pack transliterates stable,
public API names only after the lightgbm namespace has been activated.
"""

from __future__ import annotations

from .base import LibraryPack


LIGHTGBM_PACK = LibraryPack(
    name="lightgbm",
    module="lightgbm",
    kopy_module="라이트지비엠",
    preferred_aliases=("lgb",),
    description="그래디언트 부스팅 학습·예측·평가·모델 관리를 위한 LightGBM API 팩",
    members={
        # Core training API
        "데이터셋": "Dataset",
        "부스터": "Booster",
        "트레인": "train",
        "시브이": "cv",

        # Scikit-learn style estimators
        "엘지비엠모델": "LGBMModel",
        "엘지비엠클래시파이어": "LGBMClassifier",
        "엘지비엠리그레서": "LGBMRegressor",
        "엘지비엠랭커": "LGBMRanker",

        # Common estimator / booster methods
        "핏": "fit",
        "프리딕트": "predict",
        "프리딕트프로바": "predict_proba",
        "스코어": "score",
        "겟파람스": "get_params",
        "셋파람스": "set_params",
        "세이브모델": "save_model",
        "모델투스트링": "model_to_string",
        "모델프롬스트링": "model_from_string",
        "덤프모델": "dump_model",
        "피처임포턴스": "feature_importance",
        "피처네임": "feature_name",
        "커런트이터레이션": "current_iteration",
        "리핏": "refit",

        # Dataset helpers
        "컨스트럭트": "construct",
        "겟라벨": "get_label",
        "셋라벨": "set_label",
        "겟웨이트": "get_weight",
        "셋웨이트": "set_weight",
        "넘데이터": "num_data",
        "넘피처": "num_feature",
        "서브셋": "subset",
        "세이브바이너리": "save_binary",

        # Callback API
        "얼리스토핑": "early_stopping",
        "로그이밸류에이션": "log_evaluation",
        "레코드이밸류에이션": "record_evaluation",
        "리셋파라미터": "reset_parameter",

        # Model inspection / plotting
        "플롯임포턴스": "plot_importance",
        "플롯메트릭": "plot_metric",
        "플롯트리": "plot_tree",
        "크리에이트트리다이그래프": "create_tree_digraph",

        # Common fitted attributes
        "부스터_": "booster_",
        "베스트이터레이션_": "best_iteration_",
        "베스트스코어_": "best_score_",
        "피처임포턴시즈_": "feature_importances_",
        "피처네임스인_": "feature_names_in_",
        "클래시즈_": "classes_",
        "엔피처스인_": "n_features_in_",
    },
    member_descriptions={
        "Dataset": "LightGBM 학습용 데이터 컨테이너를 생성합니다.",
        "train": "파라미터와 Dataset을 사용해 Booster 모델을 학습합니다.",
        "cv": "LightGBM 교차검증을 수행합니다.",
        "LGBMClassifier": "scikit-learn 호환 LightGBM 분류기입니다.",
        "LGBMRegressor": "scikit-learn 호환 LightGBM 회귀기입니다.",
        "fit": "LightGBM estimator를 학습합니다.",
        "predict": "학습된 모델로 예측합니다.",
        "predict_proba": "분류 확률을 예측합니다.",
        "early_stopping": "검증 성능이 개선되지 않을 때 학습을 조기 종료하는 callback을 만듭니다.",
        "save_model": "Booster 모델을 파일로 저장합니다.",
    },
    examples={
        "LGBMClassifier": (
            "임포트 라이트지비엠 애즈 lgb\n모델 = lgb.엘지비엠클래시파이어(n_estimators=20, num_leaves=15)\n모델.핏(X, y)\n예측 = 모델.프리딕트(X)",
            "import lightgbm as lgb\n모델 = lgb.LGBMClassifier(n_estimators=20, num_leaves=15)\n모델.fit(X, y)\n예측 = 모델.predict(X)",
        ),
        "train": (
            "임포트 라이트지비엠 애즈 lgb\n학습데이터 = lgb.데이터셋(X, label=y)\n모델 = lgb.트레인({\"objective\": \"binary\"}, 학습데이터)",
            "import lightgbm as lgb\n학습데이터 = lgb.Dataset(X, label=y)\n모델 = lgb.train({\"objective\": \"binary\"}, 학습데이터)",
        ),
    },
)
