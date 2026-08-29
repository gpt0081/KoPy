import unittest
from pathlib import Path

from 학습_코스.course_testkit import load_python


MODULE = load_python(Path(__file__).with_name("solution.py"))


class SolutionTests(unittest.TestCase):
    def test_valid_source(self):
        self.assertEqual(
            MODULE.진단_요약('프린트("ok")\n'),
            {"ok": True, "errors": 0, "warnings": 0, "codes": []},
        )

    def test_spelling_warning(self):
        summary = MODULE.진단_요약('pritn("x")\n')
        self.assertFalse(summary["ok"])
        self.assertEqual(summary["warnings"], 1)
        self.assertIn("spelling", summary["codes"])


if __name__ == "__main__":
    unittest.main()
