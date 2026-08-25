"""Official JAX library pack for KoPy.

Covers array programming, automatic differentiation, compilation, vectorization,
random utilities and common neural-network helpers. Actual numerical execution
remains upstream JAX/jaxlib.
"""

from __future__ import annotations

from .base import LibraryPack


JAX_PACK = LibraryPack(
    name="jax",
    module="jax",
    kopy_module="잭스",
    preferred_aliases=("jax",),
    description="자동미분·JIT·벡터화·가속 배열 계산을 위한 JAX API 팩",
    members={
        # Top-level transformations / runtime
        "그라드": "grad",
        "밸류앤드그라드": "value_and_grad",
        "짓": "jit",
        "브이맵": "vmap",
        "피맵": "pmap",
        "쟉포워드": "jacfwd",
        "쟉리버스": "jacrev",
        "헤시안": "hessian",
        "디바이스풋": "device_put",
        "디바이스겟": "device_get",
        "디바이시즈": "devices",
        "디폴트백엔드": "default_backend",
        "블록언틸레디": "block_until_ready",
        "메이크잭스프": "make_jaxpr",
        "체크포인트": "checkpoint",
        "리맷": "remat",

        # jax.numpy common array APIs. Dotted submodule names themselves stay
        # Python-native (jax.numpy, jax.random, jax.nn, jax.lax, jax.tree)
        # because the current translator deliberately treats import paths as
        # compatibility-sensitive structure rather than ordinary attributes.
        "어레이": "array",
        "애즈어레이": "asarray",
        "제로즈": "zeros",
        "원즈": "ones",
        "풀": "full",
        "아이": "eye",
        "에이레인지": "arange",
        "린스페이스": "linspace",
        "리셰이프": "reshape",
        "트랜스포즈": "transpose",
        "스택": "stack",
        "컨캐터네이트": "concatenate",
        "닷": "dot",
        "매트멀": "matmul",
        "썸": "sum",
        "미인": "mean",
        "맥스": "max",
        "민": "min",
        "아그맥스": "argmax",
        "아그민": "argmin",
        "웨어": "where",
        "클립": "clip",
        "익스프": "exp",
        "로그": "log",
        "스퀘어": "square",
        "스퀘어루트": "sqrt",
        "사인": "sin",
        "코사인": "cos",
        "텐에이치": "tanh",

        # Random API
        "키": "key",
        "피알엔지키": "PRNGKey",
        "스플릿": "split",
        "폴드인": "fold_in",
        "노멀": "normal",
        "유니폼": "uniform",
        "랜디인트": "randint",
        "버누이": "bernoulli",
        "카테고리컬": "categorical",
        "퍼뮤테이션": "permutation",

        # jax.nn helpers
        "렐루": "relu",
        "겔루": "gelu",
        "시그모이드": "sigmoid",
        "소프트맥스": "softmax",
        "로그소프트맥스": "log_softmax",
        "원핫": "one_hot",

        # lax / tree helpers
        "스캔": "scan",
        "포리루프": "fori_loop",
        "컨드": "cond",
        "와일루프": "while_loop",
        "스톱그라디언트": "stop_gradient",
        "맵": "map",
        "리듀스": "reduce",
        "리브스": "leaves",
        "스트럭처": "structure",
    },
    member_descriptions={
        "grad": "스칼라 출력 함수의 자동미분 함수를 만듭니다.",
        "value_and_grad": "함수값과 기울기를 함께 계산하는 변환을 만듭니다.",
        "jit": "JAX 함수를 XLA 컴파일 대상으로 변환합니다.",
        "vmap": "함수를 배치 축에 자동 벡터화합니다.",
        "array": "JAX 배열을 생성합니다.",
        "key": "현행 typed PRNG key를 생성합니다.",
        "split": "PRNG key를 여러 독립 key로 분할합니다.",
        "relu": "ReLU 활성화 함수를 적용합니다.",
        "scan": "반복 계산을 함수형 loop 형태로 구성합니다.",
    },
    examples={
        "grad": (
            "임포트 잭스\n프롬 잭스 임포트 그라드\nf = lambda x: x ** 2\ndf = 그라드(f)",
            "import jax\nfrom jax import grad\nf = lambda x: x ** 2\ndf = grad(f)",
        ),
        "jit": (
            "임포트 잭스\ncompiled = 잭스.짓(lambda x: x * 2)",
            "import jax\ncompiled = jax.jit(lambda x: x * 2)",
        ),
        "array": (
            "임포트 잭스.numpy 애즈 jnp\nX = jnp.어레이([[1.0, 2.0], [3.0, 4.0]])",
            "import jax.numpy as jnp\nX = jnp.array([[1.0, 2.0], [3.0, 4.0]])",
        ),
        "key": (
            "임포트 잭스\nkey = 잭스.random.키(42)",
            "import jax\nkey = jax.random.key(42)",
        ),
    },
)
