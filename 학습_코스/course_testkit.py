"""학습 코스의 .kpy 예제와 문제를 테스트하는 작은 도구."""

from __future__ import annotations

import contextlib
import importlib.util
import io
from pathlib import Path
from types import SimpleNamespace
from typing import Any

from kopy.runtime import compile_source


def load_kopy(path: str | Path) -> SimpleNamespace:
    """실행 결과의 전역 이름을 속성으로 조회할 수 있게 돌려줍니다."""
    file_path = Path(path)
    source = file_path.read_text(encoding="utf-8")
    code, _, hints = compile_source(source, str(file_path), spelling=False)
    if hints:
        raise AssertionError(f"예상하지 못한 스펠링 힌트: {hints}")
    namespace: dict[str, Any] = {
        "__name__": "course_module",
        "__file__": str(file_path),
        "__package__": None,
    }
    with contextlib.redirect_stdout(io.StringIO()):
        exec(code, namespace, namespace)
    public = {name: value for name, value in namespace.items() if not name.startswith("__")}
    return SimpleNamespace(**public)


def capture_kopy(path: str | Path) -> str:
    """한 .kpy 파일의 표준 출력을 문자열로 돌려줍니다."""
    file_path = Path(path)
    source = file_path.read_text(encoding="utf-8")
    code, _, _ = compile_source(source, str(file_path), spelling=False)
    namespace = {"__name__": "__main__", "__file__": str(file_path), "__package__": None}
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        exec(code, namespace, namespace)
    return output.getvalue()


def load_python(path: str | Path) -> SimpleNamespace:
    """경로의 Python 모듈을 고유 이름으로 불러옵니다."""
    file_path = Path(path)
    module_name = f"course_{file_path.parent.parent.name}_{file_path.parent.name}_{file_path.stem}"
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"모듈을 불러올 수 없습니다: {file_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    public = {name: value for name, value in vars(module).items() if not name.startswith("__")}
    return SimpleNamespace(**public)
