import unittest
from pathlib import Path

from 학습_코스.course_testkit import load_python


MODULE = load_python(Path(__file__).with_name("solution.py"))


class SolutionTests(unittest.TestCase):
    def test_only_real_name_tokens(self):
        source = '이프 트루:\n    프린트("이프 프린트")  # 프린트\n'
        self.assertEqual(
            MODULE.변환된_이름들(source),
            [("이프", "if"), ("트루", "True"), ("프린트", "print")],
        )


if __name__ == "__main__":
    unittest.main()
