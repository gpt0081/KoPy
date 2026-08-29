from pathlib import Path
import tomllib

from kopy import PYTHON_BASELINE, __version__


def 메타데이터_상태(root: Path) -> dict:
    project = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))
    package_version = project["project"]["version"]
    readme = (root / "README.md").read_text(encoding="utf-8")
    return {
        "package_version": package_version,
        "runtime_version": __version__,
        "readme_has_version": f"**{package_version}**" in readme,
        "python_baseline": PYTHON_BASELINE,
        "versions_match": package_version == __version__,
    }
