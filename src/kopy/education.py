"""Offline teaching helpers for KoPy.

These features deliberately avoid an LLM. They explain common Python structures
and syntax errors using deterministic rules so KoPy remains fully offline.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass

from .translator import translate


@dataclass(frozen=True)
class SyntaxLesson:
    title: str
    explanation: str
    suggestion: str | None = None


def syntax_lesson(exc: SyntaxError) -> SyntaxLesson:
    message = (exc.msg or "").lower()

    if "expected ':'" in message:
        return SyntaxLesson(
            "콜론(:)이 필요합니다.",
            "if, elif, else, for, while, def, class, try, except 같은 블록 문장은 끝에 ':'를 붙입니다.",
            "해당 줄의 끝에 : 를 추가해 보세요.",
        )
    if "expected an indented block" in message:
        return SyntaxLesson(
            "들여쓴 코드 블록이 필요합니다.",
            "블록을 시작한 다음 줄은 보통 공백 4칸으로 들여씁니다.",
            "다음 줄을 공백 4칸 들여쓰거나, 아직 작성할 코드가 없다면 패스를 사용하세요.",
        )
    if "unexpected indent" in message:
        return SyntaxLesson(
            "예상하지 못한 들여쓰기입니다.",
            "현재 줄이 앞 문맥보다 더 안쪽으로 들어가 있습니다.",
            "불필요한 앞쪽 공백을 줄이고 주변 줄과 들여쓰기 깊이를 맞춰 보세요.",
        )
    if "was never closed" in message or "unterminated" in message:
        return SyntaxLesson(
            "괄호나 문자열이 닫히지 않았습니다.",
            "여는 괄호/따옴표에는 대응하는 닫는 기호가 필요합니다.",
            "(), [], {}, 따옴표의 짝을 확인해 보세요.",
        )
    if "invalid syntax" in message:
        return SyntaxLesson(
            "Python 문법으로 해석할 수 없는 부분이 있습니다.",
            "KoPy는 Python 문법 구조를 그대로 사용하므로 연산자, 괄호, 콜론, 키워드의 위치를 확인해야 합니다.",
            "오류가 표시된 줄과 바로 윗줄을 함께 확인해 보세요.",
        )
    return SyntaxLesson(
        "문법 오류가 있습니다.",
        exc.msg or "Python 문법 규칙에 맞지 않는 부분이 있습니다.",
        "표시된 줄 주변의 괄호, 콜론, 들여쓰기와 키워드 순서를 확인해 보세요.",
    )


def _name(node: ast.AST | None) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = _name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return "표현식"


def explain_source(source: str, filename: str = "<source>") -> list[str]:
    """Explain the program structure without executing user code."""
    python_source = translate(source).python
    tree = ast.parse(python_source, filename=filename)
    steps: list[str] = []

    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            if isinstance(node, ast.Import):
                names = ", ".join(alias.name for alias in node.names)
            else:
                names = node.module or "모듈"
            steps.append(f"{node.lineno}행: {names} 모듈의 기능을 불러옵니다.")
        elif isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
            steps.append(f"{node.lineno}행: 계산하거나 만든 값을 변수에 저장합니다.")
        elif isinstance(node, ast.If):
            steps.append(f"{node.lineno}행: 이프(if)가 조건을 검사하고 결과에 따라 실행할 코드를 나눕니다.")
        elif isinstance(node, ast.For):
            steps.append(f"{node.lineno}행: 포(for)가 항목을 하나씩 꺼내 반복합니다.")
        elif isinstance(node, ast.While):
            steps.append(f"{node.lineno}행: 와일(while)이 조건이 참인 동안 반복합니다.")
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            steps.append(f"{node.lineno}행: 데프(def)로 '{node.name}' 함수를 정의합니다. 함수 본문은 호출될 때 실행됩니다.")
        elif isinstance(node, ast.ClassDef):
            steps.append(f"{node.lineno}행: 클래스(class) '{node.name}'를 정의합니다.")
        elif isinstance(node, ast.Try):
            steps.append(f"{node.lineno}행: 트라이(try) 블록에서 예외가 날 수 있는 코드를 실행하고 처리 경로를 준비합니다.")
        elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            target = _name(node.value.func)
            if target == "print":
                steps.append(f"{node.lineno}행: 프린트(print)가 값을 화면에 출력합니다.")
            elif target == "input":
                steps.append(f"{node.lineno}행: 인풋(input)이 사용자 입력을 받습니다.")
            else:
                steps.append(f"{node.lineno}행: {target} 함수를 호출합니다.")
        elif isinstance(node, ast.Return):
            steps.append(f"{node.lineno}행: 리턴(return)으로 함수의 값을 돌려줍니다.")
        else:
            steps.append(f"{getattr(node, 'lineno', '?')}행: {type(node).__name__} 문장을 실행합니다.")

    if not steps:
        steps.append("실행할 문장이 없습니다.")
    return steps
