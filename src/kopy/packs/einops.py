"""Official einops library pack for KoPy.

Covers the small, high-value top-level tensor transformation API while keeping
einops pattern strings and axis names in their standard Python form. Actual
tensor computation remains upstream einops and its NumPy/PyTorch/JAX backend.
"""

from __future__ import annotations

from .base import LibraryPack


EINOPS_PACK = LibraryPack(
    name="einops",
    module="einops",
    kopy_module="에이놉스",
    preferred_aliases=("einops",),
    description="딥러닝 텐서 차원 재배열·축약·반복·패킹을 읽기 쉬운 패턴으로 표현하는 API 팩",
    members={
        "리어레인지": "rearrange",
        "리듀스": "reduce",
        "리피트": "repeat",
        "아인섬": "einsum",
        "팩": "pack",
        "언팩": "unpack",
        "파스셰이프": "parse_shape",
        "애즈넘파이": "asnumpy",
    },
    member_descriptions={
        "rearrange": "이름 붙은 축 패턴으로 transpose, reshape, squeeze/unsqueeze 등을 표현합니다.",
        "reduce": "이름 붙은 축 패턴으로 mean, sum, max 등의 축약을 표현합니다.",
        "repeat": "이름 붙은 축 패턴으로 반복과 broadcast 형태를 표현합니다.",
        "einsum": "축 이름을 사용하는 einops 스타일 einsum 연산을 수행합니다.",
        "pack": "서로 다른 모양의 여러 텐서를 별표 축으로 패킹합니다.",
        "unpack": "pack이 반환한 shape 정보를 사용해 패킹된 텐서를 복원합니다.",
        "parse_shape": "텐서 shape를 축 이름과 길이의 사전으로 해석합니다.",
        "asnumpy": "지원되는 텐서를 NumPy ndarray로 변환합니다.",
    },
    examples={
        "rearrange": (
            "프롬 에이놉스 임포트 리어레인지\nimages = 리어레인지(images, 'b h w c -> b c h w')",
            "from einops import rearrange\nimages = rearrange(images, 'b h w c -> b c h w')",
        ),
        "reduce": (
            "프롬 에이놉스 임포트 리듀스\npooled = 리듀스(features, 'b c h w -> b c', 'mean')",
            "from einops import reduce\npooled = reduce(features, 'b c h w -> b c', 'mean')",
        ),
        "repeat": (
            "프롬 에이놉스 임포트 리피트\nbatch = 리피트(vector, 'c -> b c', b=8)",
            "from einops import repeat\nbatch = repeat(vector, 'c -> b c', b=8)",
        ),
    },
)
