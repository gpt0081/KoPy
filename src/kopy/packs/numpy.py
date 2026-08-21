"""Official NumPy library pack for KoPy.

The first KoPy AI-development pack focuses on the NumPy APIs most often used
for arrays, preprocessing, statistics, linear algebra and random sampling.
"""

from __future__ import annotations

from .base import LibraryPack


NUMPY_PACK = LibraryPack(
    name="numpy",
    module="numpy",
    kopy_module="넘파이",
    preferred_aliases=("np",),
    description="AI/데이터 계산의 기반이 되는 NumPy 배열·통계·선형대수 API 팩",
    members={
        # Array creation and types
        "어레이": "array",
        "애즈어레이": "asarray",
        "엔디어레이": "ndarray",
        "디타입": "dtype",
        "제로즈": "zeros",
        "원즈": "ones",
        "엠프티": "empty",
        "풀": "full",
        "제로즈라이크": "zeros_like",
        "원즈라이크": "ones_like",
        "엠프티라이크": "empty_like",
        "풀라이크": "full_like",
        "에이레인지": "arange",
        "린스페이스": "linspace",
        "아이": "eye",
        "아이덴티티": "identity",
        "플로트32": "float32",
        "플로트64": "float64",
        "인트32": "int32",
        "인트64": "int64",

        # Shape / manipulation. These also work as attributes on arrays when
        # NumPy is active in the file, e.g. 배열.리셰이프(...).
        "셰이프": "shape",
        "사이즈": "size",
        "엔딤": "ndim",
        "리셰이프": "reshape",
        "래블": "ravel",
        "플래튼": "flatten",
        "트랜스포즈": "transpose",
        "스왑액시즈": "swapaxes",
        "스퀴즈": "squeeze",
        "익스팬드딤즈": "expand_dims",
        "컨캐터네이트": "concatenate",
        "스택": "stack",
        "브이스택": "vstack",
        "에이치스택": "hstack",
        "칼럼스택": "column_stack",
        "스플릿": "split",
        "어레이스플릿": "array_split",
        "리핏": "repeat",
        "타일": "tile",
        "테이크": "take",
        "애즈타입": "astype",
        "투리스트": "tolist",

        # Selection / ordering
        "웨어": "where",
        "논제로": "nonzero",
        "유니크": "unique",
        "소트": "sort",
        "아그소트": "argsort",
        "아그맥스": "argmax",
        "아그민": "argmin",
        "클립": "clip",

        # Statistics. 'mean' uses 미인 to stay distinct from KoPy core 민=min.
        "미인": "mean",
        "에스티디": "std",
        "바": "var",
        "미디언": "median",
        "퍼센타일": "percentile",
        "퀀타일": "quantile",
        "코브": "cov",
        "코르코에프": "corrcoef",
        "프로드": "prod",
        "컴프로드": "cumprod",
        "컴썸": "cumsum",

        # Math / linear algebra
        "닷": "dot",
        "매트멀": "matmul",
        "이너": "inner",
        "아우터": "outer",
        "크로스": "cross",
        "텐서닷": "tensordot",
        "아인섬": "einsum",
        "익스프": "exp",
        "로그": "log",
        "로그텐": "log10",
        "스퀘어루트": "sqrt",
        "사인": "sin",
        "코사인": "cos",
        "탄젠트": "tan",
        "앱솔루트": "absolute",
        "린알지": "linalg",
        "노름": "norm",
        "인브": "inv",
        "솔브": "solve",
        "아이그": "eig",
        "아이그밸스": "eigvals",
        "에스브이디": "svd",
        "디트": "det",

        # Random sampling
        "랜덤": "random",
        "디폴트알엔지": "default_rng",
        "노멀": "normal",
        "스탠더드노멀": "standard_normal",
        "유니폼": "uniform",
        "인티저스": "integers",
        "초이스": "choice",
        "시드": "seed",

        # Constants / I/O
        "파이": "pi",
        "인프": "inf",
        "낸": "nan",
        "로드": "load",
        "세이브": "save",
        "로드티엑스티": "loadtxt",
        "세이브티엑스티": "savetxt",
    },
    member_descriptions={
        "array": "Python 시퀀스에서 NumPy 배열을 만듭니다.",
        "asarray": "입력을 가능한 한 복사 없이 NumPy 배열로 변환합니다.",
        "arange": "일정 간격의 값을 가진 NumPy 배열을 만듭니다.",
        "linspace": "시작값과 끝값 사이를 지정한 개수로 균등 분할합니다.",
        "zeros": "모든 원소가 0인 배열을 만듭니다.",
        "ones": "모든 원소가 1인 배열을 만듭니다.",
        "reshape": "배열의 데이터는 유지하면서 모양(shape)을 바꿉니다.",
        "concatenate": "여러 배열을 지정한 축을 따라 이어 붙입니다.",
        "mean": "배열 원소의 산술 평균을 계산합니다.",
        "std": "배열 원소의 표준편차를 계산합니다.",
        "where": "조건에 따라 원소를 선택하거나 조건을 만족하는 위치를 구합니다.",
        "dot": "벡터 내적 또는 배열의 dot 연산을 수행합니다.",
        "matmul": "행렬 곱셈을 수행합니다.",
        "linalg": "NumPy 선형대수 기능이 모인 하위 네임스페이스입니다.",
        "norm": "벡터 또는 행렬의 노름을 계산합니다.",
        "default_rng": "권장 방식의 NumPy 난수 생성기 Generator를 만듭니다.",
        "normal": "정규분포에서 난수를 샘플링합니다.",
        "float32": "32비트 부동소수점 NumPy 자료형입니다.",
        "float64": "64비트 부동소수점 NumPy 자료형입니다.",
    },
    examples={
        "array": (
            "임포트 넘파이 애즈 np\n배열 = np.어레이([1, 2, 3])",
            "import numpy as np\narray = np.array([1, 2, 3])",
        ),
        "arange": (
            "임포트 넘파이 애즈 np\nx = np.에이레인지(0, 10, 2)",
            "import numpy as np\nx = np.arange(0, 10, 2)",
        ),
        "reshape": (
            "임포트 넘파이 애즈 np\nx = np.에이레인지(6).리셰이프(2, 3)",
            "import numpy as np\nx = np.arange(6).reshape(2, 3)",
        ),
        "mean": (
            "임포트 넘파이 애즈 np\n평균 = np.미인([1, 2, 3])",
            "import numpy as np\naverage = np.mean([1, 2, 3])",
        ),
        "default_rng": (
            "임포트 넘파이 애즈 np\nrng = np.랜덤.디폴트알엔지()",
            "import numpy as np\nrng = np.random.default_rng()",
        ),
        "norm": (
            "임포트 넘파이 애즈 np\n크기 = np.린알지.노름([3, 4])",
            "import numpy as np\nmagnitude = np.linalg.norm([3, 4])",
        ),
    },
)
