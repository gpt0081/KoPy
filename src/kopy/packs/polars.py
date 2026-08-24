"""Official Polars library pack for KoPy.

Polars remains the runtime implementation. This pack transliterates stable,
public API names only after the polars namespace has been activated.
"""

from __future__ import annotations

from .base import LibraryPack


POLARS_PACK = LibraryPack(
    name="polars",
    module="polars",
    kopy_module="폴라스",
    preferred_aliases=("pl",),
    description="AI 데이터 전처리·집계·lazy query에 쓰는 Polars DataFrame API 팩",
    members={
        # Core containers / expressions
        "데이터프레임": "DataFrame",
        "레이지프레임": "LazyFrame",
        "시리즈": "Series",
        "익스프레션": "Expr",
        "컬": "col",
        "릿": "lit",
        "웬": "when",
        "덴": "then",
        "아더와이즈": "otherwise",

        # Readers / scanners / writers
        "리드씨에스브이": "read_csv",
        "리드파케이": "read_parquet",
        "리드제이슨": "read_json",
        "스캔씨에스브이": "scan_csv",
        "스캔파케이": "scan_parquet",
        "라이트씨에스브이": "write_csv",
        "라이트파케이": "write_parquet",
        "투넘파이": "to_numpy",
        "투딕트": "to_dict",
        "투딕츠": "to_dicts",

        # Query / projection / transformation
        "셀렉트": "select",
        "위드컬럼즈": "with_columns",
        "필터": "filter",
        "그룹바이": "group_by",
        "어그": "agg",
        "소트": "sort",
        "조인": "join",
        "컨캣": "concat",
        "드롭": "drop",
        "리네임": "rename",
        "유니크": "unique",
        "익스플로드": "explode",
        "피벗": "pivot",
        "언피벗": "unpivot",

        # Missing values / dtypes
        "필널": "fill_null",
        "드롭널즈": "drop_nulls",
        "필낸": "fill_nan",
        "드롭낸즈": "drop_nans",
        "이즈널": "is_null",
        "이즈낫널": "is_not_null",
        "캐스트": "cast",

        # Lazy API
        "레이지": "lazy",
        "콜렉트": "collect",
        "페치": "fetch",
        "익스플레인": "explain",

        # Inspect / common reductions
        "헤드": "head",
        "테일": "tail",
        "샘플": "sample",
        "디스크라이브": "describe",
        "셰이프": "shape",
        "컬럼즈": "columns",
        "디타입즈": "dtypes",
        "미인": "mean",
        "미디언": "median",
        "에스티디": "std",
        "바": "var",
        "썸": "sum",
        "민": "min",
        "맥스": "max",
        "카운트": "count",
        "엔유니크": "n_unique",

        # Expression helpers
        "에일리어스": "alias",
        "오버": "over",
        "시프트": "shift",
        "디프": "diff",
        "롤링미인": "rolling_mean",
        "클립": "clip",
    },
    member_descriptions={
        "DataFrame": "Polars의 eager 표 데이터 구조입니다.",
        "LazyFrame": "쿼리를 최적화한 뒤 collect 시점에 실행하는 Polars lazy 데이터 구조입니다.",
        "read_csv": "CSV 데이터를 DataFrame으로 읽습니다.",
        "scan_csv": "CSV를 즉시 적재하지 않고 LazyFrame으로 스캔합니다.",
        "col": "이름으로 열을 선택하는 Polars expression을 만듭니다.",
        "with_columns": "기존 열을 변환하거나 새 열을 추가합니다.",
        "filter": "조건 expression에 맞는 행만 남깁니다.",
        "group_by": "하나 이상의 열을 기준으로 데이터를 그룹화합니다.",
        "agg": "그룹 또는 expression 집계를 수행합니다.",
        "collect": "LazyFrame 쿼리를 실행해 DataFrame으로 수집합니다.",
        "to_numpy": "Polars 객체를 NumPy 배열로 변환합니다.",
    },
    examples={
        "DataFrame": (
            '임포트 폴라스 애즈 pl\n표 = pl.데이터프레임({"x": [1, 2], "y": [3, 4]})',
            'import polars as pl\ntable = pl.DataFrame({"x": [1, 2], "y": [3, 4]})',
        ),
        "with_columns": (
            '임포트 폴라스 애즈 pl\n표 = 표.위드컬럼즈((pl.컬("x") * 2).에일리어스("x2"))',
            'import polars as pl\ntable = table.with_columns((pl.col("x") * 2).alias("x2"))',
        ),
        "group_by": (
            '임포트 폴라스 애즈 pl\n요약 = 표.그룹바이("label").어그(pl.컬("value").미인())',
            'import polars as pl\nsummary = table.group_by("label").agg(pl.col("value").mean())',
        ),
        "collect": (
            '임포트 폴라스 애즈 pl\n결과 = 표.레이지().필터(pl.컬("x") > 0).콜렉트()',
            'import polars as pl\nresult = table.lazy().filter(pl.col("x") > 0).collect()',
        ),
    },
)
