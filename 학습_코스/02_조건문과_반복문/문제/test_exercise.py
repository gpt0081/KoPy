import unittest
from pathlib import Path

from 학습_코스.course_testkit import load_kopy


MODULE = load_kopy(Path(__file__).with_name("exercise.kpy"))


class ExerciseTests(unittest.TestCase):
    def test_sign(self):
        self.assertEqual(MODULE.수의_부호(3), "양수")
        self.assertEqual(MODULE.수의_부호(0), "0")
        self.assertEqual(MODULE.수의_부호(-2), "음수")

    def test_inclusive_sum(self):
        self.assertEqual(MODULE.구간_합(1, 4), 10)
        self.assertEqual(MODULE.구간_합(5, 5), 5)


if __name__ == "__main__":
    unittest.main()
