import unittest
from pathlib import Path

from 학습_코스.course_testkit import load_kopy


MODULE = load_kopy(Path(__file__).with_name("exercise.kpy"))


class ExerciseTests(unittest.TestCase):
    def test_increase_and_reset(self):
        counter = MODULE.제한_카운터(3)
        self.assertEqual(counter.증가(2), 2)
        counter.초기화()
        self.assertEqual(counter.값, 0)

    def test_limit(self):
        counter = MODULE.제한_카운터(2)
        counter.증가(2)
        with self.assertRaises(ValueError):
            counter.증가()


if __name__ == "__main__":
    unittest.main()
