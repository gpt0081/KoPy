import unittest
from pathlib import Path

from 학습_코스.course_testkit import load_python


MODULE = load_python(Path(__file__).with_name("solution.py"))


class SolutionTests(unittest.TestCase):
    def test_version_success(self):
        code, stdout, stderr = MODULE.명령_실행(["version"])
        self.assertEqual(code, 0)
        self.assertIn("KoPy", stdout)
        self.assertEqual(stderr, "")

    def test_unknown_pack(self):
        code, _stdout, stderr = MODULE.명령_실행(["packs", "없는팩"])
        self.assertEqual(code, 1)
        self.assertIn("찾지 못했습니다", stderr)


if __name__ == "__main__":
    unittest.main()
