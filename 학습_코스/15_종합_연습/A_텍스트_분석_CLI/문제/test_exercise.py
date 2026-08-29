import unittest
from pathlib import Path

from 학습_코스.course_testkit import load_kopy


MODULE = load_kopy(Path(__file__).with_name("exercise.kpy"))


class ExerciseTests(unittest.TestCase):
    def test_words(self):
        self.assertEqual(MODULE.단어들("KoPy, python KOPY!"), ["kopy", "python", "kopy"])

    def test_analysis(self):
        result = MODULE.분석("b a b c a b")
        self.assertEqual(result["total"], 6)
        self.assertEqual(result["unique"], 3)
        self.assertEqual(result["frequencies"], {"a": 2, "b": 3, "c": 1})
        self.assertEqual(result["top"], [["b", 3], ["a", 2], ["c", 1]])


if __name__ == "__main__":
    unittest.main()
