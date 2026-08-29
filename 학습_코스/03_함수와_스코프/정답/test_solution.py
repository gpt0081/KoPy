import unittest
from pathlib import Path

from 학습_코스.course_testkit import load_kopy


MODULE = load_kopy(Path(__file__).with_name("solution.kpy"))


class SolutionTests(unittest.TestCase):
    def test_power(self):
        self.assertEqual(MODULE.거듭제곱(4), 16)
        self.assertEqual(MODULE.거듭제곱(2, 3), 8)

    def test_apply(self):
        self.assertEqual(MODULE.함수_적용(lambda value: value + 1, 4), 5)


if __name__ == "__main__":
    unittest.main()
