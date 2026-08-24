"""Official PyTorch library pack for KoPy.

Covers the core tensor, autograd, neural-network and optimizer workflow used in
modern AI development. The actual computation remains upstream PyTorch.
"""

from __future__ import annotations

from .base import LibraryPack


TORCH_PACK = LibraryPack(
    name="pytorch",
    module="torch",
    kopy_module="토치",
    preferred_aliases=("torch",),
    description="딥러닝 텐서·자동미분·신경망·최적화를 위한 PyTorch API 팩",
    members={
        # Tensor creation / dtypes / devices
        "텐서": "tensor",
        "텐서클래스": "Tensor",
        "제로즈": "zeros",
        "원즈": "ones",
        "엠프티": "empty",
        "풀": "full",
        "랜드": "rand",
        "랜드엔": "randn",
        "랜드인트": "randint",
        "에이레인지": "arange",
        "린스페이스": "linspace",
        "플로트32": "float32",
        "플로트64": "float64",
        "인트32": "int32",
        "인트64": "int64",
        "불": "bool",
        "디바이스": "device",

        # Tensor operations / shapes
        "셰이프": "shape",
        "사이즈": "size",
        "리셰이프": "reshape",
        "뷰": "view",
        "플래튼": "flatten",
        "트랜스포즈": "transpose",
        "퍼뮤트": "permute",
        "스퀴즈": "squeeze",
        "언스퀴즈": "unsqueeze",
        "스택": "stack",
        "캣": "cat",
        "청크": "chunk",
        "스플릿": "split",
        "닷": "dot",
        "매트멀": "matmul",
        "엠엠": "mm",
        "썸": "sum",
        "미인": "mean",
        "맥스": "max",
        "민": "min",
        "아그맥스": "argmax",
        "아그민": "argmin",
        "소프트맥스": "softmax",
        "시그모이드": "sigmoid",
        "렐루": "relu",
        "클램프": "clamp",
        "노름": "norm",

        # Autograd / tensor lifecycle
        "백워드": "backward",
        "그라드": "grad",
        "리콰이어즈그라드": "requires_grad",
        "디태치": "detach",
        "아이템": "item",
        "넘파이": "numpy",
        "클론": "clone",
        "투": "to",
        "씨피유": "cpu",
        "쿠다": "cuda",
        "노그라드": "no_grad",
        "인퍼런스모드": "inference_mode",

        # Neural-network namespace / layers / losses
        "엔엔": "nn",
        "모듈": "Module",
        "리니어": "Linear",
        "시퀀셜": "Sequential",
        "렐루레이어": "ReLU",
        "시그모이드레이어": "Sigmoid",
        "드롭아웃": "Dropout",
        "임베딩": "Embedding",
        "레이어노름": "LayerNorm",
        "배치노름원디": "BatchNorm1d",
        "컨브원디": "Conv1d",
        "컨브투디": "Conv2d",
        "엘에스티엠": "LSTM",
        "그루": "GRU",
        "트랜스포머인코더레이어": "TransformerEncoderLayer",
        "크로스엔트로피로스": "CrossEntropyLoss",
        "엠에스이로스": "MSELoss",
        "비씨이위드로짓스로스": "BCEWithLogitsLoss",

        # Module methods
        "포워드": "forward",
        "파라미터스": "parameters",
        "트레인": "train",
        "이밸": "eval",
        "스테이트딕트": "state_dict",
        "로드스테이트딕트": "load_state_dict",

        # Optimizers
        "옵팀": "optim",
        "에스지디": "SGD",
        "아담": "Adam",
        "아담더블유": "AdamW",
        "알엠에스프롭": "RMSprop",
        "제로그라드": "zero_grad",
        "스텝": "step",

        # Data utilities / serialization
        "데이터": "data",
        "데이터로더": "DataLoader",
        "텐서데이터셋": "TensorDataset",
        "세이브": "save",
        "로드": "load",
        "매뉴얼시드": "manual_seed",
    },
    member_descriptions={
        "tensor": "Python 데이터에서 PyTorch 텐서를 만듭니다.",
        "Tensor": "PyTorch의 핵심 다차원 배열 객체입니다.",
        "backward": "현재 스칼라 결과에서 역전파해 기울기를 계산합니다.",
        "no_grad": "블록 안에서 자동미분 기록을 끕니다.",
        "Module": "PyTorch 신경망 모듈의 기본 클래스입니다.",
        "Linear": "완전연결 선형 변환 계층입니다.",
        "CrossEntropyLoss": "다중 클래스 분류에서 흔히 쓰는 교차엔트로피 손실입니다.",
        "AdamW": "가중치 감쇠를 분리한 AdamW 최적화 알고리즘입니다.",
        "DataLoader": "데이터셋을 미니배치 단위로 순회하도록 로딩합니다.",
        "state_dict": "모델 또는 옵티마이저의 상태 사전을 반환합니다.",
    },
    examples={
        "tensor": (
            "임포트 토치\nx = 토치.텐서([1.0, 2.0, 3.0], requires_grad=True)",
            "import torch\nx = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)",
        ),
        "Linear": (
            "임포트 토치\n모델 = 토치.엔엔.리니어(3, 1)",
            "import torch\nmodel = torch.nn.Linear(3, 1)",
        ),
        "backward": (
            "손실.백워드()",
            "loss.backward()",
        ),
        "AdamW": (
            "임포트 토치\n옵티마이저 = 토치.옵팀.아담더블유(모델.파라미터스())",
            "import torch\noptimizer = torch.optim.AdamW(model.parameters())",
        ),
    },
)
