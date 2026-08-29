import unittest
from pathlib import Path

from 학습_코스.course_testkit import load_kopy


MODULE = load_kopy(Path(__file__).with_name("solution.kpy"))


class SolutionTests(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(MODULE.환영문("민수"), "안녕하세요, 민수!")


if __name__ == "__main__":
    unittest.main()
