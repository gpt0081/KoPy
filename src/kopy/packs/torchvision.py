"""Official TorchVision library pack for KoPy.

Covers common vision transforms, model constructors, datasets, image utilities
and detection operators. Actual image and tensor execution remains upstream
TorchVision/PyTorch.
"""

from __future__ import annotations

from .base import LibraryPack


TORCHVISION_PACK = LibraryPack(
    name="torchvision",
    module="torchvision",
    kopy_module="토치비전",
    preferred_aliases=("torchvision", "tv"),
    description="PyTorch 이미지 변환·비전 모델·데이터셋·연산을 위한 TorchVision API 팩",
    members={
        # Namespaces
        "트랜스폼즈": "transforms",
        "모델즈": "models",
        "데이터셋츠": "datasets",
        "옵스": "ops",
        "유틸즈": "utils",
        "아이오": "io",

        # Transform composition / common transforms
        "컴포즈": "Compose",
        "리사이즈": "Resize",
        "센터크롭": "CenterCrop",
        "랜덤크롭": "RandomCrop",
        "랜덤리사이즈드크롭": "RandomResizedCrop",
        "랜덤호리즌털플립": "RandomHorizontalFlip",
        "랜덤버티컬플립": "RandomVerticalFlip",
        "랜덤로테이션": "RandomRotation",
        "컬러지터": "ColorJitter",
        "투텐서": "ToTensor",
        "노멀라이즈": "Normalize",
        "투디타입": "ToDtype",
        "투이미지": "ToImage",

        # Functional transform helpers. Compact legacy spellings are retained;
        # underscore-preserving spellings are canonical for Python -> KoPy.
        "투필이미지": "to_pil_image",
        "투_필_이미지": "to_pil_image",
        "필투텐서": "pil_to_tensor",
        "필_투_텐서": "pil_to_tensor",
        "컨버트이미지디타입": "convert_image_dtype",
        "컨버트_이미지_디타입": "convert_image_dtype",
        "리사이즈함수": "resize",
        "노멀라이즈함수": "normalize",
        "에이치플립": "hflip",
        "브이플립": "vflip",
        "로테이트": "rotate",

        # Model constructors / weights. Digits stay digits.
        "레스넷18": "resnet18",
        "레스넷50": "resnet50",
        "모빌넷브이스리라지": "mobilenet_v3_large",
        "모빌넷_브이3_라지": "mobilenet_v3_large",
        "이피션트넷비제로": "efficientnet_b0",
        "이피션트넷_비0": "efficientnet_b0",
        "비전트랜스포머비16": "vit_b_16",
        "브이아이티_비_16": "vit_b_16",
        "스윈티": "swin_t",
        "레스넷18웨이츠": "ResNet18_Weights",
        "레스넷18_웨이츠": "ResNet18_Weights",
        "레스넷50웨이츠": "ResNet50_Weights",
        "레스넷50_웨이츠": "ResNet50_Weights",

        # Common datasets
        "이미지폴더": "ImageFolder",
        "씨파10": "CIFAR10",
        "씨파100": "CIFAR100",
        "엠니스트": "MNIST",
        "패션엠니스트": "FashionMNIST",

        # Utility / detection helpers
        "메이크그리드": "make_grid",
        "메이크_그리드": "make_grid",
        "세이브이미지": "save_image",
        "세이브_이미지": "save_image",
        "박스아이오유": "box_iou",
        "박스_아이오유": "box_iou",
        "엔엠에스": "nms",
        "클립박시스토이미지": "clip_boxes_to_image",
        "클립_박시즈_투_이미지": "clip_boxes_to_image",
        "리무브스몰박시스": "remove_small_boxes",
        "리무브_스몰_박시즈": "remove_small_boxes",
    },
    member_descriptions={
        "Compose": "여러 이미지 변환을 순서대로 연결합니다.",
        "Resize": "PIL 이미지 또는 Tensor 이미지의 크기를 변경합니다.",
        "Normalize": "Tensor 이미지 채널을 평균과 표준편차로 정규화합니다.",
        "resnet18": "TorchVision의 ResNet-18 모델을 생성합니다.",
        "ImageFolder": "폴더 구조에서 분류용 이미지 데이터셋을 구성합니다.",
        "make_grid": "여러 Tensor 이미지를 하나의 이미지 그리드로 배치합니다.",
        "box_iou": "두 bounding-box 집합의 IoU 행렬을 계산합니다.",
    },
    examples={
        "Compose": (
            "임포트 토치비전 애즈 tv\n트랜스폼 = tv.트랜스폼즈.컴포즈([tv.트랜스폼즈.리사이즈((224, 224)), tv.트랜스폼즈.노멀라이즈(mean=[0.5]*3, std=[0.5]*3)])",
            "import torchvision as tv\ntransform = tv.transforms.Compose([tv.transforms.Resize((224, 224)), tv.transforms.Normalize(mean=[0.5]*3, std=[0.5]*3)])",
        ),
        "resnet18": (
            "임포트 토치비전 애즈 tv\n모델 = tv.모델즈.레스넷18(weights=None)",
            "import torchvision as tv\nmodel = tv.models.resnet18(weights=None)",
        ),
        "box_iou": (
            "임포트 토치비전 애즈 tv\n아이오유 = tv.옵스.박스_아이오유(boxes1, boxes2)",
            "import torchvision as tv\niou = tv.ops.box_iou(boxes1, boxes2)",
        ),
    },
)
