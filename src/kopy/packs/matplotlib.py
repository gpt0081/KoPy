"""Official Matplotlib library pack for KoPy.

The pack focuses on pyplot's common plotting workflow plus the Figure/Axes
methods most useful for AI and data-science visualisation. Matplotlib remains
the runtime implementation; KoPy only transliterates API names.
"""

from __future__ import annotations

from .base import LibraryPack


MATPLOTLIB_PACK = LibraryPack(
    name="matplotlib",
    module="matplotlib",
    kopy_module="맷플롯립",
    preferred_aliases=("plt",),
    description="AI·데이터 분석 결과의 선·산점도·막대·히스토그램·이미지 시각화를 위한 Matplotlib API 팩",
    members={
        # Module / pyplot entry points
        "파이플롯": "pyplot",
        "유즈": "use",
        "겟백엔드": "get_backend",
        "서브플롯츠": "subplots",
        "서브플롯": "subplot",
        "피겨": "figure",
        "쇼": "show",
        "클로즈": "close",
        "세이브피그": "savefig",
        "타이트레이아웃": "tight_layout",

        # Common plots
        "플롯": "plot",
        "스캐터": "scatter",
        "바": "bar",
        "바에이치": "barh",
        "히스트": "hist",
        "파이": "pie",
        "박스플롯": "boxplot",
        "에러바": "errorbar",
        "스텝": "step",
        "필비트윈": "fill_between",
        "스택플롯": "stackplot",
        "임쇼": "imshow",
        "매트쇼": "matshow",
        "컨투어": "contour",
        "컨투어에프": "contourf",

        # Labels, scales and annotations
        "타이틀": "title",
        "엑스라벨": "xlabel",
        "와이라벨": "ylabel",
        "레전드": "legend",
        "그리드": "grid",
        "엑스림": "xlim",
        "와이림": "ylim",
        "엑스스케일": "xscale",
        "와이스케일": "yscale",
        "엑스틱스": "xticks",
        "와이틱스": "yticks",
        "텍스트": "text",
        "애노테이트": "annotate",
        "액스에이치라인": "axhline",
        "액스브이라인": "axvline",

        # Figure / Axes object methods
        "셋타이틀": "set_title",
        "셋엑스라벨": "set_xlabel",
        "셋와이라벨": "set_ylabel",
        "셋엑스림": "set_xlim",
        "셋와이림": "set_ylim",
        "셋엑스스케일": "set_xscale",
        "셋와이스케일": "set_yscale",
        "겟피겨": "get_figure",
        "애드서브플롯": "add_subplot",
        "애드액시즈": "add_axes",
        "컬러바": "colorbar",
        "클리어": "clear",
        "클라": "cla",
        "클에프": "clf",
    },
    member_descriptions={
        "pyplot": "Matplotlib의 상태 기반 plotting 인터페이스인 pyplot 모듈입니다.",
        "subplots": "Figure와 하나 이상의 Axes를 함께 생성합니다.",
        "plot": "선 그래프를 그립니다.",
        "scatter": "두 변수의 산점도를 그립니다.",
        "bar": "세로 막대그래프를 그립니다.",
        "hist": "값의 분포를 히스토그램으로 그립니다.",
        "imshow": "2차원 배열이나 이미지를 표시합니다.",
        "savefig": "현재 Figure를 이미지 파일로 저장합니다.",
        "legend": "그래프 범례를 표시합니다.",
        "set_title": "Axes 객체의 제목을 설정합니다.",
        "set_xlabel": "Axes 객체의 x축 라벨을 설정합니다.",
        "set_ylabel": "Axes 객체의 y축 라벨을 설정합니다.",
    },
    examples={
        "plot": (
            "임포트 맷플롯립.pyplot 애즈 plt\nplt.플롯([1, 2, 3], [2, 4, 3])\nplt.쇼()",
            "import matplotlib.pyplot as plt\nplt.plot([1, 2, 3], [2, 4, 3])\nplt.show()",
        ),
        "subplots": (
            "임포트 맷플롯립.pyplot 애즈 plt\n피겨, 축 = plt.서브플롯츠()\n축.스캐터([1, 2], [3, 4])",
            "import matplotlib.pyplot as plt\nfigure, axes = plt.subplots()\naxes.scatter([1, 2], [3, 4])",
        ),
        "savefig": (
            "plt.세이브피그('plot.png')",
            "plt.savefig('plot.png')",
        ),
    },
)
