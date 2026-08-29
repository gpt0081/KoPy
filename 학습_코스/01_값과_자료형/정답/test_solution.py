import unittest
from pathlib import Path

from 학습_코스.course_testkit import load_kopy


MODULE = load_kopy(Path(__file__).with_name("solution.kpy"))


class SolutionTests(unittest.TestCase):
    def test_temperature(self):
        self.assertEqual(MODULE.섭씨를_화씨로(0), 32)
        self.assertEqual(MODULE.섭씨를_화씨로(100), 212)

    def test_even(self):
        self.assertTrue(MODULE.짝수인가(8))
        self.assertFalse(MODULE.짝수인가(7))


if __name__ == "__main__":
    unittest.main()
