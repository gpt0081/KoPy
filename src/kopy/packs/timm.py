"""Official timm library pack for KoPy.

Covers common PyTorch Image Models discovery, construction, feature-extraction,
data, optimizer, scheduler, and model-inspection APIs. Actual model execution
remains upstream timm/PyTorch.
"""

from __future__ import annotations

from .base import LibraryPack


TIMM_PACK = LibraryPack(
    name="timm",
    module="timm",
    kopy_module="팀엠",
    preferred_aliases=("timm",),
    description="PyTorch Image Models의 모델 탐색·생성·특징 추출·학습 유틸리티 API 팩",
    members={
        # Legacy aliases retained for KoPy source compatibility. Canonical forms
        # below preserve Python underscores and numeric fragments.
        "크리에이트모델": "create_model",
        "리스트모델즈": "list_models",
        "리스트프리트레인드": "list_pretrained",
        "이즈모델": "is_model",
        "모델엔트리포인트": "model_entrypoint",
        "겟프리트레인드컨피그": "get_pretrained_cfg",
        "포워드피처스": "forward_features",
        "포워드헤드": "forward_head",
        "리셋클래시파이어": "reset_classifier",
        "겟클래시파이어": "get_classifier",
        "피처인포": "feature_info",
        "리졸브데이터컨피그": "resolve_data_config",
        "크리에이트트랜스폼": "create_transform",
        "크리에이트데이터셋": "create_dataset",
        "크리에이트로더": "create_loader",
        "크리에이트옵티마이저브이투": "create_optimizer_v2",
        "옵티마이저콰그스": "optimizer_kwargs",
        "크리에이트스케줄러브이투": "create_scheduler_v2",

        # Common namespaces / classes.
        "데이터": "data",
        "옵팀": "optim",
        "스케줄러": "scheduler",
        "로스": "loss",
        "모델즈": "models",
        "레이어즈": "layers",
        "믹스업": "Mixup",
        "소프트타깃크로스엔트로피": "SoftTargetCrossEntropy",
        "라벨스무딩크로스엔트로피": "LabelSmoothingCrossEntropy",

        # Canonical KoPy spellings. Keep '_' structure and digits unchanged.
        "크리에이트_모델": "create_model",
        "리스트_모델즈": "list_models",
        "리스트_프리트레인드": "list_pretrained",
        "이즈_모델": "is_model",
        "모델_엔트리포인트": "model_entrypoint",
        "겟_프리트레인드_컨피그": "get_pretrained_cfg",
        "포워드_피처스": "forward_features",
        "포워드_헤드": "forward_head",
        "리셋_클래시파이어": "reset_classifier",
        "겟_클래시파이어": "get_classifier",
        "피처_인포": "feature_info",
        "리졸브_데이터_컨피그": "resolve_data_config",
        "크리에이트_트랜스폼": "create_transform",
        "크리에이트_데이터셋": "create_dataset",
        "크리에이트_로더": "create_loader",
        "크리에이트_옵티마이저_브이2": "create_optimizer_v2",
        "옵티마이저_콰그스": "optimizer_kwargs",
        "크리에이트_스케줄러_브이2": "create_scheduler_v2",
    },
    member_descriptions={
        "create_model": "이름으로 timm 모델을 생성합니다.",
        "list_models": "사용 가능한 timm 모델 이름을 조회합니다.",
        "forward_features": "분류 헤드 이전의 특징 표현을 계산합니다.",
        "reset_classifier": "분류 헤드를 새로운 클래스 수에 맞게 재설정합니다.",
        "resolve_data_config": "모델의 입력 크기·정규화 등 데이터 설정을 해석합니다.",
        "create_transform": "모델 입력용 이미지 변환 파이프라인을 생성합니다.",
        "create_optimizer_v2": "timm의 optimizer factory로 PyTorch optimizer를 생성합니다.",
    },
    examples={
        "create_model": (
            "임포트 팀엠\n모델 = 팀엠.크리에이트_모델('resnet18', pretrained=False, num_classes=10)",
            "import timm\nmodel = timm.create_model('resnet18', pretrained=False, num_classes=10)",
        ),
        "list_models": (
            "임포트 팀엠\n모델_네임즈 = 팀엠.리스트_모델즈('resnet*')",
            "import timm\nmodel_names = timm.list_models('resnet*')",
        ),
        "forward_features": (
            "임포트 팀엠\n피처스 = 모델.포워드_피처스(엑스)",
            "import timm\nfeatures = model.forward_features(X)",
        ),
    },
)
