"""Official TorchMetrics library pack for KoPy.

Covers high-value PyTorch metric classes while deliberately preserving generic
lifecycle methods such as update(), compute(), reset(), clone(), and plot() in
upstream Python form. Those names are broadly used outside TorchMetrics and are
better learned as standard framework API than translated as ambiguous members.
"""

from __future__ import annotations

from .base import LibraryPack


TORCHMETRICS_PACK = LibraryPack(
    name="torchmetrics",
    module="torchmetrics",
    kopy_module="토치메트릭스",
    preferred_aliases=("torchmetrics", "tm"),
    description="PyTorch용 정확도·정밀도·재현율·F1·AUROC·평균/합계 등 metric API 팩",
    members={
        "메트릭": "Metric",
        "메트릭컬렉션": "MetricCollection",
        "애큐러시": "Accuracy",
        "프리시전": "Precision",
        "리콜": "Recall",
        "에프원스코어": "F1Score",
        "에이유알오씨": "AUROC",
        "애버리지프리시전": "AveragePrecision",
        "컨퓨전매트릭스": "ConfusionMatrix",
        "코헨카파": "CohenKappa",
        "매튜스코릴레이션코이피션트": "MatthewsCorrCoef",
        "미인메트릭": "MeanMetric",
        "썸메트릭": "SumMetric",
        "맥스메트릭": "MaxMetric",
        "민메트릭": "MinMetric",
        "캣메트릭": "CatMetric",
    },
    member_descriptions={
        "Metric": "TorchMetrics 사용자 정의 metric의 기본 클래스입니다.",
        "MetricCollection": "여러 metric을 한 번에 계산·관리하는 컨테이너입니다.",
        "Accuracy": "분류 정확도를 계산합니다. task 인자로 binary/multiclass/multilabel을 선택합니다.",
        "Precision": "분류 precision을 계산합니다.",
        "Recall": "분류 recall을 계산합니다.",
        "F1Score": "precision과 recall의 조화평균인 F1 score를 계산합니다.",
        "AUROC": "ROC 곡선 아래 면적을 계산합니다.",
        "MeanMetric": "여러 batch에 걸쳐 값의 평균을 누적 계산합니다.",
    },
    examples={
        "Accuracy": (
            "임포트 토치메트릭스 애즈 tm\naccuracy = tm.애큐러시(task='binary')",
            "import torchmetrics as tm\naccuracy = tm.Accuracy(task='binary')",
        ),
        "F1Score": (
            "임포트 토치메트릭스 애즈 tm\nf1 = tm.에프원스코어(task='multiclass', num_classes=3)",
            "import torchmetrics as tm\nf1 = tm.F1Score(task='multiclass', num_classes=3)",
        ),
        "MeanMetric": (
            "임포트 토치메트릭스 애즈 tm\nloss_mean = tm.미인메트릭()",
            "import torchmetrics as tm\nloss_mean = tm.MeanMetric()",
        ),
    },
)
