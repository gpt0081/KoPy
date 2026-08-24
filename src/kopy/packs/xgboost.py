"""Official XGBoost library pack for KoPy.

XGBoost remains the runtime implementation. This pack transliterates stable,
public API names only after the xgboost namespace has been activated.
"""

from __future__ import annotations

from .base import LibraryPack


XGBOOST_PACK = LibraryPack(
    name="xgboost",
    module="xgboost",
    kopy_module="엑스지부스트",
    preferred_aliases=("xgb",),
    description="그래디언트 부스팅 학습·예측·모델 관리·평가를 위한 XGBoost API 팩",
    members={
        # Core training API
        "디매트릭스": "DMatrix",
        "퀀타일디매트릭스": "QuantileDMatrix",
        "부스터": "Booster",
        "트레인": "train",
        "시브이": "cv",

        # Scikit-learn style estimators
        "엑스지비모델": "XGBModel",
        "엑스지비클래시파이어": "XGBClassifier",
        "엑스지비리그레서": "XGBRegressor",
        "엑스지비랭커": "XGBRanker",
        "엑스지비알에프클래시파이어": "XGBRFClassifier",
        "엑스지비알에프리그레서": "XGBRFRegressor",

        # Common estimator / booster methods
        "핏": "fit",
        "프리딕트": "predict",
        "프리딕트프로바": "predict_proba",
        "스코어": "score",
        "겟부스터": "get_booster",
        "겟파람스": "get_params",
        "셋파람스": "set_params",
        "세이브모델": "save_model",
        "로드모델": "load_model",
        "세이브컨피그": "save_config",
        "로드컨피그": "load_config",
        "겟스코어": "get_score",
        "인플레이스프리딕트": "inplace_predict",
        "이발스리절트": "evals_result",
        "어플라이": "apply",

        # DMatrix helpers
        "겟라벨": "get_label",
        "셋라벨": "set_label",
        "겟웨이트": "get_weight",
        "셋웨이트": "set_weight",
        "넘로우": "num_row",
        "넘콜": "num_col",
        "넘논미싱": "num_nonmissing",
        "겟데이터": "get_data",

        # Model inspection / plotting
        "플롯임포턴스": "plot_importance",
        "플롯트리": "plot_tree",
        "투그래프비즈": "to_graphviz",

        # Callback API
        "트레이닝콜백": "TrainingCallback",
        "얼리스토핑": "EarlyStopping",
        "이밸류에이션모니터": "EvaluationMonitor",
        "러닝레이트스케줄러": "LearningRateScheduler",

        # Public attributes frequently used after training
        "베스트이터레이션": "best_iteration",
        "베스트스코어": "best_score",
        "피처임포턴시즈_": "feature_importances_",
        "클래시즈_": "classes_",
        "엔피처스인_": "n_features_in_",
    },
    member_descriptions={
        "DMatrix": "XGBoost의 최적화된 데이터 컨테이너를 생성합니다.",
        "train": "파라미터와 DMatrix를 사용해 Booster 모델을 학습합니다.",
        "cv": "XGBoost 교차검증을 수행합니다.",
        "XGBClassifier": "scikit-learn 호환 XGBoost 분류기입니다.",
        "XGBRegressor": "scikit-learn 호환 XGBoost 회귀기입니다.",
        "fit": "XGBoost estimator를 학습합니다.",
        "predict": "학습된 모델로 예측합니다.",
        "predict_proba": "분류 확률을 예측합니다.",
        "save_model": "모델을 파일로 저장합니다.",
        "get_score": "Booster의 feature importance 점수를 조회합니다.",
    },
    examples={
        "XGBClassifier": (
            "임포트 엑스지부스트 애즈 xgb\n모델 = xgb.엑스지비클래시파이어(n_estimators=20, max_depth=3)\n모델.핏(X, y)\n예측 = 모델.프리딕트(X)",
            "import xgboost as xgb\n모델 = xgb.XGBClassifier(n_estimators=20, max_depth=3)\n모델.fit(X, y)\n예측 = 모델.predict(X)",
        ),
        "train": (
            "임포트 엑스지부스트 애즈 xgb\n학습데이터 = xgb.디매트릭스(X, label=y)\n모델 = xgb.트레인({\"objective\": \"binary:logistic\"}, 학습데이터)",
            "import xgboost as xgb\n학습데이터 = xgb.DMatrix(X, label=y)\n모델 = xgb.train({\"objective\": \"binary:logistic\"}, 학습데이터)",
        ),
    },
)
