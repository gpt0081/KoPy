import unittest
from pathlib import Path

from 학습_코스.course_testkit import load_kopy


MODULE = load_kopy(Path(__file__).with_name("exercise.kpy"))


class ExerciseTests(unittest.TestCase):
    def test_safe_divide(self):
        self.assertEqual(MODULE.안전_나누기(8, 2), 4)
        with self.assertRaises(ValueError):
            MODULE.안전_나누기(1, 0)

    def test_median(self):
        self.assertEqual(MODULE.중앙값([9, 1, 3]), 3)
        self.assertEqual(MODULE.중앙값([1, 2, 3, 4]), 2.5)
        with self.assertRaises(ValueError):
            MODULE.중앙값([])


if __name__ == "__main__":
    unittest.main()
