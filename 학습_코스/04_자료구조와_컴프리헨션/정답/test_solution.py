import unittest
from pathlib import Path

from 학습_코스.course_testkit import load_kopy


MODULE = load_kopy(Path(__file__).with_name("solution.kpy"))


class SolutionTests(unittest.TestCase):
    def test_unique_keeps_order(self):
        self.assertEqual(MODULE.중복_제거([3, 1, 3, 2, 1]), [3, 1, 2])

    def test_counts(self):
        self.assertEqual(MODULE.등장_횟수(["a", "b", "a"]), {"a": 2, "b": 1})


if __name__ == "__main__":
    unittest.main()
