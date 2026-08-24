"""Official scikit-learn library pack for KoPy.

Focuses on the classical machine-learning workflow used after NumPy/pandas:
preprocessing, train/test splitting, pipelines, estimators and evaluation.
"""

from __future__ import annotations

from .base import LibraryPack


SKLEARN_PACK = LibraryPack(
    name="scikit-learn",
    module="sklearn",
    kopy_module="사이킷런",
    preferred_aliases=("sk",),
    description="AI 전처리·모델 학습·평가·모델 선택을 위한 scikit-learn API 팩",
    members={
        # Model selection / workflow
        "트레인테스트스플릿": "train_test_split",
        "크로스밸스코어": "cross_val_score",
        "그리드서치씨브이": "GridSearchCV",
        "랜덤아이즈드서치씨브이": "RandomizedSearchCV",
        "케이폴드": "KFold",
        "스트래티파이드케이폴드": "StratifiedKFold",
        "파이프라인": "Pipeline",
        "메이크파이프라인": "make_pipeline",

        # Preprocessing
        "스탠더드스케일러": "StandardScaler",
        "민맥스스케일러": "MinMaxScaler",
        "로버스트스케일러": "RobustScaler",
        "원핫인코더": "OneHotEncoder",
        "레이블인코더": "LabelEncoder",
        "오디널인코더": "OrdinalEncoder",
        "폴리노미얼피처스": "PolynomialFeatures",
        "심플임퓨터": "SimpleImputer",

        # Common estimators
        "리니어리그레션": "LinearRegression",
        "로지스틱리그레션": "LogisticRegression",
        "릿지": "Ridge",
        "라쏘": "Lasso",
        "랜덤포레스트클래시파이어": "RandomForestClassifier",
        "랜덤포레스트리그레서": "RandomForestRegressor",
        "그라디언트부스팅클래시파이어": "GradientBoostingClassifier",
        "그라디언트부스팅리그레서": "GradientBoostingRegressor",
        "히스트그라디언트부스팅클래시파이어": "HistGradientBoostingClassifier",
        "히스트그라디언트부스팅리그레서": "HistGradientBoostingRegressor",
        "서포트벡터클래시파이어": "SVC",
        "서포트벡터리그레서": "SVR",
        "케이니이버스클래시파이어": "KNeighborsClassifier",
        "케이니이버스리그레서": "KNeighborsRegressor",
        "디시전트리클래시파이어": "DecisionTreeClassifier",
        "디시전트리리그레서": "DecisionTreeRegressor",
        "케이민즈": "KMeans",
        "피씨에이": "PCA",

        # Estimator methods
        "핏": "fit",
        "프리딕트": "predict",
        "프리딕트프로바": "predict_proba",
        "스코어": "score",
        "트랜스폼": "transform",
        "핏트랜스폼": "fit_transform",
        "겟파람스": "get_params",
        "셋파람스": "set_params",

        # Metrics
        "애큐러시스코어": "accuracy_score",
        "프리시전스코어": "precision_score",
        "리콜스코어": "recall_score",
        "에프원스코어": "f1_score",
        "콘퓨전매트릭스": "confusion_matrix",
        "클래시피케이션리포트": "classification_report",
        "민스퀘어드에러": "mean_squared_error",
        "민앱솔루트에러": "mean_absolute_error",
        "알투스코어": "r2_score",
    },
    member_descriptions={
        "train_test_split": "특징과 정답 데이터를 학습용과 테스트용으로 나눕니다.",
        "StandardScaler": "특징을 평균 0, 표준편차 1을 기준으로 표준화합니다.",
        "Pipeline": "전처리와 모델 단계를 하나의 학습 파이프라인으로 묶습니다.",
        "LogisticRegression": "분류에 사용하는 로지스틱 회귀 추정기입니다.",
        "RandomForestClassifier": "여러 결정트리를 결합하는 랜덤 포레스트 분류기입니다.",
        "RandomForestRegressor": "여러 결정트리를 결합하는 랜덤 포레스트 회귀기입니다.",
        "KMeans": "데이터를 K개의 군집으로 나누는 비지도 학습 알고리즘입니다.",
        "PCA": "주성분 분석으로 데이터 차원을 축소합니다.",
        "fit": "데이터로 추정기 또는 변환기를 학습합니다.",
        "predict": "학습된 추정기로 새로운 입력의 결과를 예측합니다.",
        "accuracy_score": "분류 예측의 정확도를 계산합니다.",
        "mean_squared_error": "회귀 예측의 평균제곱오차를 계산합니다.",
    },
    examples={
        "train_test_split": (
            "프롬 사이킷런.model_selection 임포트 트레인테스트스플릿\nX_train, X_test, y_train, y_test = 트레인테스트스플릿(X, y, test_size=0.2)",
            "from sklearn.model_selection import train_test_split\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)",
        ),
        "StandardScaler": (
            "프롬 사이킷런.preprocessing 임포트 스탠더드스케일러\n스케일러 = 스탠더드스케일러()\nX2 = 스케일러.핏트랜스폼(X)",
            "from sklearn.preprocessing import StandardScaler\nscaler = StandardScaler()\nX2 = scaler.fit_transform(X)",
        ),
        "LogisticRegression": (
            "프롬 사이킷런.linear_model 임포트 로지스틱리그레션\n모델 = 로지스틱리그레션()\n모델.핏(X, y)",
            "from sklearn.linear_model import LogisticRegression\nmodel = LogisticRegression()\nmodel.fit(X, y)",
        ),
        "accuracy_score": (
            "프롬 사이킷런.metrics 임포트 애큐러시스코어\n정확도 = 애큐러시스코어(y, 예측)",
            "from sklearn.metrics import accuracy_score\naccuracy = accuracy_score(y, prediction)",
        ),
    },
)
