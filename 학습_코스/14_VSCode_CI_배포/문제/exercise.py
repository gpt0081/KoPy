from pathlib import Path


def 메타데이터_상태(root: Path) -> dict:
    # TODO: pyproject.toml, README.md, kopy.__version__, PYTHON_BASELINE을 비교하세요.
    return {
        "package_version": "",
        "runtime_version": "",
        "readme_has_version": False,
        "python_baseline": "",
        "versions_match": False,
    }
