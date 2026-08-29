import json
import unittest
from pathlib import Path

from 학습_코스.course_testkit import load_kopy


MODULE = load_kopy(Path(__file__).with_name("solution.kpy"))


class SolutionTests(unittest.TestCase):
    def test_word_frequency(self):
        self.assertEqual(MODULE.단어_빈도("KoPy python KOPY"), {"kopy": 2, "python": 1})

    def test_json(self):
        result = MODULE.JSON_문자열({"나": 1, "가": 2})
        self.assertNotIn("\\u", result)
        self.assertEqual(json.loads(result), {"나": 1, "가": 2})


if __name__ == "__main__":
    unittest.main()
