"""Official Kornia library pack for KoPy.

Covers common differentiable computer-vision, filtering, color, geometry,
augmentation, morphology, and metrics APIs. Actual computation remains
upstream Kornia/PyTorch. Canonical KoPy spellings preserve Python underscore
structure and numeric fragments, while legacy compact spellings remain accepted
for source compatibility.
"""

from __future__ import annotations

from .base import LibraryPack


KORNIA_PACK = LibraryPack(
    name="kornia",
    module="kornia",
    kopy_module="코르니아",
    preferred_aliases=("kornia", "K"),
    description="PyTorch 기반 미분가능 컴퓨터비전·증강·필터·기하 API 팩",
    members={
        # Common namespaces
        "어그멘테이션": "augmentation",
        "컬러": "color",
        "필터즈": "filters",
        "지오메트리": "geometry",
        "트랜스폼": "transform",
        "모폴로지": "morphology",
        "메트릭스": "metrics",
        "로시즈": "losses",
        "피처": "feature",
        "인핸스": "enhance",

        # Legacy compact aliases retained for KoPy source compatibility.
        "알지비투그레이스케일": "rgb_to_grayscale",
        "그레이스케일투알지비": "grayscale_to_rgb",
        "알지비투에이치에스브이": "rgb_to_hsv",
        "에이치에스브이투알지비": "hsv_to_rgb",
        "가우시안블러2디": "gaussian_blur2d",
        "미디안블러": "median_blur",
        "워프어파인": "warp_affine",
        "워프퍼스펙티브": "warp_perspective",

        # Color / filtering canonical spellings. Preserve Python '_' and digits.
        "알지비_투_그레이스케일": "rgb_to_grayscale",
        "그레이스케일_투_알지비": "grayscale_to_rgb",
        "알지비_투_에이치에스브이": "rgb_to_hsv",
        "에이치에스브이_투_알지비": "hsv_to_rgb",
        "가우시안_블러2디": "gaussian_blur2d",
        "소벨": "sobel",
        "캐니": "canny",
        "라플라시안": "laplacian",
        "미디안_블러": "median_blur",

        # Geometry / morphology / metrics
        "리사이즈": "resize",
        "로테이트": "rotate",
        "워프_어파인": "warp_affine",
        "워프_퍼스펙티브": "warp_perspective",
        "딜레이션": "dilation",
        "이로전": "erosion",
        "오프닝": "opening",
        "클로징": "closing",
        "피에스엔알": "psnr",
        "에스에스아이엠": "ssim",

        # Augmentation classes
        "어그멘테이션시퀀셜": "AugmentationSequential",
        "랜덤어파인": "RandomAffine",
        "랜덤호리즌털플립": "RandomHorizontalFlip",
        "랜덤버티컬플립": "RandomVerticalFlip",
        "랜덤로테이션": "RandomRotation",
        "랜덤크롭": "RandomCrop",
        "센터크롭": "CenterCrop",
        "컬러지글": "ColorJiggle",
        "노멀라이즈": "Normalize",
        "디노멀라이즈": "Denormalize",
    },
    member_descriptions={
        "rgb_to_grayscale": "RGB 텐서를 grayscale 텐서로 변환합니다.",
        "gaussian_blur2d": "2D 이미지 배치에 Gaussian blur를 적용합니다.",
        "sobel": "Sobel gradient를 계산합니다.",
        "resize": "텐서 이미지를 지정한 공간 크기로 변경합니다.",
        "AugmentationSequential": "여러 Kornia 증강을 하나의 파이프라인으로 결합합니다.",
        "RandomAffine": "미분가능한 랜덤 affine 증강을 적용합니다.",
    },
    examples={
        "rgb_to_grayscale": (
            "임포트 코르니아\n피처스 = 코르니아.컬러.알지비_투_그레이스케일(엑스)",
            "import kornia\nfeatures = kornia.color.rgb_to_grayscale(X)",
        ),
        "gaussian_blur2d": (
            "임포트 코르니아\n리절트 = 코르니아.필터즈.가우시안_블러2디(피처스, (3, 3), (1.5, 1.5))",
            "import kornia\nresult = kornia.filters.gaussian_blur2d(features, (3, 3), (1.5, 1.5))",
        ),
        "AugmentationSequential": (
            "임포트 코르니아 애즈 K\n파이프라인 = K.어그멘테이션.어그멘테이션시퀀셜(K.어그멘테이션.랜덤호리즌털플립(p=1.0))",
            "import kornia as K\npipeline = K.augmentation.AugmentationSequential(K.augmentation.RandomHorizontalFlip(p=1.0))",
        ),
    },
)
