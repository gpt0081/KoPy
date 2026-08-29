import unittest
from pathlib import Path

from 학습_코스.course_testkit import load_python


MODULE = load_python(Path(__file__).with_name("exercise.py"))
ROOT = Path(__file__).resolve().parents[3]


class ExerciseTests(unittest.TestCase):
    def test_repository_metadata(self):
        result = MODULE.메타데이터_상태(ROOT)
        self.assertEqual(result["package_version"], "0.5.51")
        self.assertEqual(result["runtime_version"], "0.5.51")
        self.assertTrue(result["readme_has_version"])
        self.assertEqual(result["python_baseline"], "3.12.10")
        self.assertTrue(result["versions_match"])


if __name__ == "__main__":
    unittest.main()
