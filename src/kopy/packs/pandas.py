"""Official pandas library pack for KoPy.

This pack focuses on the pandas APIs most useful for AI/data workflows:
loading tabular data, cleaning, reshaping, joining, grouping and feature
preparation.
"""

from __future__ import annotations

from .base import LibraryPack


PANDAS_PACK = LibraryPack(
    name="pandas",
    module="pandas",
    kopy_module="판다스",
    preferred_aliases=("pd",),
    description="AI 데이터 적재·정제·전처리에 쓰는 pandas DataFrame/Series API 팩",
    members={
        # Core containers / dtypes
        "데이터프레임": "DataFrame",
        "시리즈": "Series",
        "인덱스": "Index",
        "카테고리컬": "Categorical",
        "스트링디타입": "StringDtype",

        # Readers / writers
        "리드씨에스브이": "read_csv",
        "리드제이슨": "read_json",
        "리드파케이": "read_parquet",
        "리드엑셀": "read_excel",
        "투씨에스브이": "to_csv",
        "투제이슨": "to_json",
        "투파케이": "to_parquet",
        "투엑셀": "to_excel",
        "투넘파이": "to_numpy",
        "투딕트": "to_dict",

        # Inspect / select
        "헤드": "head",
        "테일": "tail",
        "샘플": "sample",
        "디스크라이브": "describe",
        "인포": "info",
        "셰이프": "shape",
        "컬럼즈": "columns",
        "디타입즈": "dtypes",
        "록": "loc",
        "아이록": "iloc",
        "앳": "at",
        "아이앳": "iat",
        "셀렉트디타입즈": "select_dtypes",
        "쿼리": "query",

        # Missing values / cleaning
        "이즈엔에이": "isna",
        "이즈널": "isnull",
        "낫엔에이": "notna",
        "낫널": "notnull",
        "드롭엔에이": "dropna",
        "필엔에이": "fillna",
        "에프필": "ffill",
        "비필": "bfill",
        "드롭듀플리케이츠": "drop_duplicates",
        "리플레이스": "replace",
        "애즈타입": "astype",
        "인퍼오브젝트즈": "infer_objects",
        "컨버트디타입즈": "convert_dtypes",

        # Transform / feature engineering
        "어플라이": "apply",
        "맵": "map",
        "어그": "agg",
        "어그리게이트": "aggregate",
        "트랜스폼": "transform",
        "애즈사인": "assign",
        "리네임": "rename",
        "클립": "clip",
        "웨어": "where",
        "마스크": "mask",
        "컷": "cut",
        "큐컷": "qcut",
        "겟더미즈": "get_dummies",
        "팩터라이즈": "factorize",

        # Sort / index / reshape
        "소트밸류즈": "sort_values",
        "소트인덱스": "sort_index",
        "셋인덱스": "set_index",
        "리셋인덱스": "reset_index",
        "리인덱스": "reindex",
        "멜트": "melt",
        "피벗": "pivot",
        "피벗테이블": "pivot_table",
        "스택": "stack",
        "언스택": "unstack",
        "익스플로드": "explode",

        # Combine / group
        "컨캣": "concat",
        "머지": "merge",
        "조인": "join",
        "그룹바이": "groupby",
        "크로스타브": "crosstab",
        "밸류카운츠": "value_counts",
        "유니크": "unique",
        "엔유니크": "nunique",

        # Common reductions / statistics
        "미인": "mean",
        "미디언": "median",
        "에스티디": "std",
        "바": "var",
        "썸": "sum",
        "민": "min",
        "맥스": "max",
        "카운트": "count",
        "코르": "corr",
        "코브": "cov",
        "랭크": "rank",
        "컴썸": "cumsum",
        "컴프로드": "cumprod",

        # Time series
        "투데이타임": "to_datetime",
        "데이트레인지": "date_range",
        "리샘플": "resample",
        "롤링": "rolling",
        "시프트": "shift",
        "디프": "diff",
    },
    member_descriptions={
        "DataFrame": "행과 열로 구성된 pandas의 2차원 표 데이터 구조입니다.",
        "Series": "하나의 열처럼 사용할 수 있는 pandas의 1차원 데이터 구조입니다.",
        "read_csv": "CSV 파일이나 CSV 형식 데이터를 DataFrame으로 읽습니다.",
        "read_parquet": "Parquet 데이터를 DataFrame으로 읽습니다.",
        "head": "앞쪽 행 일부를 확인합니다.",
        "describe": "수치형/범주형 데이터의 요약 통계를 생성합니다.",
        "dropna": "결측값이 있는 행이나 열을 제거합니다.",
        "fillna": "결측값을 지정한 값으로 채웁니다.",
        "groupby": "하나 이상의 키로 데이터를 그룹화합니다.",
        "merge": "공통 키를 기준으로 DataFrame을 결합합니다.",
        "concat": "여러 pandas 객체를 축을 따라 이어 붙입니다.",
        "get_dummies": "범주형 값을 원-핫 인코딩용 더미 변수로 변환합니다.",
        "to_numpy": "DataFrame 또는 Series를 NumPy 배열로 변환합니다.",
        "value_counts": "고유 값별 빈도를 계산합니다.",
        "sort_values": "값을 기준으로 행을 정렬합니다.",
        "reset_index": "현재 인덱스를 열로 되돌리거나 기본 정수 인덱스로 재설정합니다.",
    },
    examples={
        "DataFrame": (
            '임포트 판다스 애즈 pd\n표 = pd.데이터프레임({"x": [1, 2], "y": [3, 4]})',
            'import pandas as pd\ntable = pd.DataFrame({"x": [1, 2], "y": [3, 4]})',
        ),
        "read_csv": (
            '임포트 판다스 애즈 pd\n표 = pd.리드씨에스브이("data.csv")',
            'import pandas as pd\ntable = pd.read_csv("data.csv")',
        ),
        "dropna": (
            '임포트 판다스 애즈 pd\n정제 = 표.드롭엔에이()',
            'import pandas as pd\ncleaned = table.dropna()',
        ),
        "groupby": (
            '임포트 판다스 애즈 pd\n요약 = 표.그룹바이("label").미인()',
            'import pandas as pd\nsummary = table.groupby("label").mean()',
        ),
        "get_dummies": (
            '임포트 판다스 애즈 pd\n특징 = pd.겟더미즈(표, columns=["category"])',
            'import pandas as pd\nfeatures = pd.get_dummies(table, columns=["category"])',
        ),
    },
)
