import unittest
from pathlib import Path

from 학습_코스.course_testkit import load_python


MODULE = load_python(Path(__file__).with_name("exercise.py"))


class ExerciseTests(unittest.TestCase):
    def test_pack_statistics(self):
        result = MODULE.팩_통계()
        self.assertEqual(result["count"], 51)
        self.assertEqual(result["names"], sorted(result["names"]))
        self.assertIn("numpy", result["names"])
        self.assertGreater(result["member_count"], 100)
        self.assertIsInstance(result["installed"], list)


if __name__ == "__main__":
    unittest.main()
