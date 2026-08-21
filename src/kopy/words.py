"""Canonical KoPy transliteration registry.

This module is the single source of truth for KoPy spellings. Runtime translation,
Python -> KoPy conversion, editor completion, help and teaching features all read
from this registry.
"""

from __future__ import annotations

import builtins
import keyword
from dataclasses import dataclass


# Python keywords and soft keywords.
WORDS: dict[str, str] = {
    "펄스": "False", "논": "None", "트루": "True",
    "앤드": "and", "애즈": "as", "어설트": "assert", "어싱크": "async",
    "어웨이트": "await", "브레이크": "break", "클래스": "class",
    "컨티뉴": "continue", "데프": "def", "델": "del", "엘리프": "elif",
    "엘스": "else", "익셉트": "except", "파이널리": "finally", "포": "for",
    "프롬": "from", "글로벌": "global", "이프": "if", "임포트": "import",
    "인": "in", "이즈": "is", "람다": "lambda", "논로컬": "nonlocal",
    "낫": "not", "오어": "or", "패스": "pass", "레이즈": "raise",
    "리턴": "return", "트라이": "try", "와일": "while", "위드": "with",
    "일드": "yield", "매치": "match", "케이스": "case",

    # Built-in functions and types.
    "앱스": "abs", "에이터": "aiter", "올": "all", "어넥스트": "anext",
    "애니": "any", "아스키": "ascii", "빈": "bin", "불": "bool",
    "브레이크포인트": "breakpoint", "바이트어레이": "bytearray", "바이트": "bytes",
    "콜러블": "callable", "크르": "chr", "클래스메소드": "classmethod",
    "컴파일": "compile", "컴플렉스": "complex", "델애트르": "delattr",
    "딕트": "dict", "디르": "dir", "디브모드": "divmod", "이뉴머레이트": "enumerate",
    "이밸": "eval", "엑섹": "exec", "필터": "filter", "플로트": "float",
    "포맷": "format", "프로즌셋": "frozenset", "겟애트르": "getattr",
    "글로벌스": "globals", "해즈애트르": "hasattr", "해시": "hash",
    "헬프": "help", "헥스": "hex", "아이디": "id", "인풋": "input",
    "인트": "int", "아이시인스턴스": "isinstance", "아이서브클래스": "issubclass",
    "이터": "iter", "렌": "len", "리스트": "list", "로컬스": "locals",
    "맵": "map", "맥스": "max", "메모리뷰": "memoryview", "민": "min",
    "넥스트": "next", "오브젝트": "object", "옥트": "oct", "오픈": "open",
    "오드": "ord", "파우": "pow", "프린트": "print", "프로퍼티": "property",
    "레인지": "range", "레프르": "repr", "리버스드": "reversed", "라운드": "round",
    "셋": "set", "셋애트르": "setattr", "슬라이스": "slice", "소티드": "sorted",
    "스태틱메소드": "staticmethod", "스트링": "str", "썸": "sum", "슈퍼": "super",
    "튜플": "tuple", "타입": "type", "바스": "vars", "집": "zip",

    # Common built-in exceptions. They are names too, so KoPy can teach and use
    # them without introducing a second exception-specific mechanism.
    "익셉션": "Exception", "베이스익셉션": "BaseException",
    "어설션에러": "AssertionError", "애트리뷰트에러": "AttributeError",
    "EOF에러": "EOFError", "임포트에러": "ImportError",
    "모듈낫파운드에러": "ModuleNotFoundError", "인덴테이션에러": "IndentationError",
    "인덱스에러": "IndexError", "키에러": "KeyError", "키보드인터럽트": "KeyboardInterrupt",
    "메모리에러": "MemoryError", "네임에러": "NameError", "낫임플리멘티드에러": "NotImplementedError",
    "OS에러": "OSError", "오버플로에러": "OverflowError", "퍼미션에러": "PermissionError",
    "리커전에러": "RecursionError", "런타임에러": "RuntimeError", "스톱이터레이션": "StopIteration",
    "신택스에러": "SyntaxError", "탭에러": "TabError", "타임아웃에러": "TimeoutError",
    "타입에러": "TypeError", "언바운드로컬에러": "UnboundLocalError",
    "유니코드에러": "UnicodeError", "밸류에러": "ValueError", "제로디비전에러": "ZeroDivisionError",
    "파일낫파운드에러": "FileNotFoundError", "파일익지스트에러": "FileExistsError",
    "커넥션에러": "ConnectionError", "룩업에러": "LookupError",
}

ENGLISH_TARGETS: frozenset[str] = frozenset(WORDS.values())
PY_TO_KO: dict[str, str] = {python_name: korean for korean, python_name in WORDS.items()}

_KEYWORDS = frozenset(keyword.kwlist) | frozenset(getattr(keyword, "softkwlist", ()))
_BUILTINS = frozenset(name for name in dir(builtins) if not name.startswith("_") and name.isidentifier())
_CONSTANTS = frozenset({"True", "False", "None"})


@dataclass(frozen=True)
class WordInfo:
    kopy: str
    python: str
    category: str
    description: str
    kopy_example: str | None = None
    python_example: str | None = None


_DESCRIPTIONS: dict[str, str] = {
    "print": "값을 화면에 출력합니다.",
    "input": "사용자에게 문자열 입력을 받습니다.",
    "int": "값을 정수로 변환하거나 정수를 만듭니다.",
    "float": "값을 실수로 변환하거나 실수를 만듭니다.",
    "str": "값을 문자열로 변환합니다.",
    "len": "객체의 길이 또는 항목 수를 구합니다.",
    "range": "반복에 사용할 정수 범위를 만듭니다.",
    "if": "조건이 참인지 검사해 실행 흐름을 나눕니다.",
    "for": "반복 가능한 객체의 항목을 하나씩 처리합니다.",
    "while": "조건이 참인 동안 코드를 반복합니다.",
    "def": "함수를 정의합니다.",
    "return": "함수 실행을 끝내고 값을 돌려줍니다.",
    "class": "클래스를 정의합니다.",
    "import": "모듈을 불러옵니다.",
    "try": "예외가 발생할 수 있는 코드를 실행합니다.",
    "except": "발생한 예외를 처리합니다.",
    "list": "순서가 있는 변경 가능한 목록을 만듭니다.",
    "dict": "키와 값의 쌍을 저장하는 사전을 만듭니다.",
    "set": "중복 없는 값의 집합을 만듭니다.",
    "tuple": "순서가 있는 변경 불가능한 묶음을 만듭니다.",
}

_EXAMPLES: dict[str, tuple[str, str]] = {
    "print": ('프린트("안녕하세요")', 'print("안녕하세요")'),
    "input": ('이름 = 인풋("이름: ")', 'name = input("이름: ")'),
    "int": ('나이 = 인트("20")', 'age = int("20")'),
    "len": ('길이 = 렌([1, 2, 3])', 'length = len([1, 2, 3])'),
    "range": ('포 i 인 레인지(3):\n    프린트(i)', 'for i in range(3):\n    print(i)'),
    "if": ('이프 점수 >= 60:\n    프린트("합격")', 'if score >= 60:\n    print("합격")'),
    "def": ('데프 더하기(a, b):\n    리턴 a + b', 'def add(a, b):\n    return a + b'),
}


def category_for(python_name: str) -> str:
    if python_name in _CONSTANTS:
        return "constant"
    if python_name in _KEYWORDS:
        return "keyword"
    if python_name in _BUILTINS:
        if isinstance(getattr(builtins, python_name, None), type) and issubclass(getattr(builtins, python_name), BaseException):
            return "exception"
        return "builtin"
    return "name"


def info_for(kopy_word: str) -> WordInfo | None:
    python_name = WORDS.get(kopy_word)
    if python_name is None:
        return None
    examples = _EXAMPLES.get(python_name)
    return WordInfo(
        kopy=kopy_word,
        python=python_name,
        category=category_for(python_name),
        description=_DESCRIPTIONS.get(python_name, f"Python의 {python_name} 표현을 KoPy 음역으로 사용할 수 있습니다."),
        kopy_example=examples[0] if examples else None,
        python_example=examples[1] if examples else None,
    )


def all_word_info() -> tuple[WordInfo, ...]:
    return tuple(info_for(word) for word in WORDS if info_for(word) is not None)  # type: ignore[misc]
