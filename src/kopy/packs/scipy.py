"""Official SciPy library pack for KoPy.

SciPy remains the runtime implementation. This pack only transliterates
well-known public API names after the scipy namespace has been activated.
"""

from __future__ import annotations

from .base import LibraryPack


SCIPY_PACK = LibraryPack(
    name="scipy",
    module="scipy",
    kopy_module="사이파이",
    preferred_aliases=("sp",),
    description="최적화·통계·희소행렬·선형대수·신호처리·적분을 위한 SciPy API 팩",
    members={
        # Public submodules
        "옵티마이즈": "optimize",
        "스탯츠": "stats",
        "스파스": "sparse",
        "리날그": "linalg",
        "시그널": "signal",
        "스페이셜": "spatial",
        "인티그레이트": "integrate",
        "인터폴레이트": "interpolate",
        "에프에프티": "fft",
        "엔디이미지": "ndimage",
        "스페셜": "special",

        # scipy.optimize
        "미니마이즈": "minimize",
        "미니마이즈스칼라": "minimize_scalar",
        "루트": "root",
        "루트스칼라": "root_scalar",
        "커브핏": "curve_fit",
        "리스트스퀘어스": "least_squares",
        "리니어섬어사인먼트": "linear_sum_assignment",
        "브렌트큐": "brentq",

        # scipy.stats
        "지스코어": "zscore",
        "피어슨알": "pearsonr",
        "스피어맨알": "spearmanr",
        "티테스트인드": "ttest_ind",
        "티테스트릴": "ttest_rel",
        "치스퀘어": "chisquare",
        "디스크라이브": "describe",
        "노름": "norm",
        "유니폼": "uniform",
        "바이놈": "binom",
        "포아송": "poisson",

        # scipy.sparse
        "시이에스알매트릭스": "csr_matrix",
        "시이에스시매트릭스": "csc_matrix",
        "쿠매트릭스": "coo_matrix",
        "아이": "eye",
        "다이애그스": "diags",
        "이스스파스": "issparse",
        "브이스택": "vstack",
        "에이치스택": "hstack",

        # scipy.linalg
        "솔브": "solve",
        "인브": "inv",
        "디트": "det",
        "아이그": "eig",
        "아이그밸시": "eigvalsh",
        "에스브이디": "svd",
        "큐알": "qr",
        "촐레스키": "cholesky",

        # scipy.signal / integrate
        "파인드피크스": "find_peaks",
        "버터": "butter",
        "필트필트": "filtfilt",
        "컨볼브": "convolve",
        "코릴레이트": "correlate",
        "심슨": "simpson",
        "쿼드": "quad",
        "솔브아이브이피": "solve_ivp",

        # Common sparse-object APIs
        "토덴스": "todense",
        "토어레이": "toarray",
        "겟엔엔지": "getnnz",
    },
    member_descriptions={
        "minimize": "목적 함수를 수치적으로 최소화합니다.",
        "root": "비선형 방정식의 근을 찾습니다.",
        "zscore": "표준점수(z-score)를 계산합니다.",
        "pearsonr": "두 변수의 Pearson 상관계수와 p-value를 계산합니다.",
        "csr_matrix": "CSR 형식 희소행렬을 생성합니다.",
        "solve": "선형 방정식 Ax=b를 풉니다.",
        "svd": "특이값 분해를 수행합니다.",
        "find_peaks": "1차원 신호에서 피크를 찾습니다.",
        "quad": "1차원 함수를 수치 적분합니다.",
    },
    examples={
        "minimize": (
            "프롬 사이파이.optimize 임포트 미니마이즈\n결과 = 미니마이즈(lambda x: (x[0] - 3) ** 2, [0.0])",
            "from scipy.optimize import minimize\n결과 = minimize(lambda x: (x[0] - 3) ** 2, [0.0])",
        ),
        "zscore": (
            "프롬 사이파이.stats 임포트 지스코어\n표준화 = 지스코어([1.0, 2.0, 3.0])",
            "from scipy.stats import zscore\n표준화 = zscore([1.0, 2.0, 3.0])",
        ),
        "csr_matrix": (
            "프롬 사이파이.sparse 임포트 시이에스알매트릭스\n행렬 = 시이에스알매트릭스([[1, 0], [0, 2]])",
            "from scipy.sparse import csr_matrix\n행렬 = csr_matrix([[1, 0], [0, 2]])",
        ),
    },
)
