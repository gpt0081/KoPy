import pathlib
import tomllib
import unittest

import kopy


ROOT = pathlib.Path(__file__).resolve().parents[1]


class VersionMetadataTests(unittest.TestCase):
    def test_runtime_version_matches_project_metadata(self):
        with (ROOT / "pyproject.toml").open("rb") as handle:
            project = tomllib.load(handle)["project"]

        self.assertEqual(kopy.__version__, project["version"])

    def test_python_baseline_matches_supported_minor(self):
        with (ROOT / "pyproject.toml").open("rb") as handle:
            project = tomllib.load(handle)["project"]

        self.assertEqual(kopy.PYTHON_BASELINE, "3.12.10")
        self.assertEqual(project["requires-python"], ">=3.12,<3.13")


if __name__ == "__main__":
    unittest.main()
