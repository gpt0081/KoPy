import unittest
from pathlib import Path

from 학습_코스.course_testkit import load_python


MODULE = load_python(Path(__file__).with_name("exercise.py"))


class ExerciseTests(unittest.TestCase):
    def test_round_trip(self):
        source = 'for value in range(2):\n    print("for print", value)\n'
        kopy, restored, stable = MODULE.왕복(source)
        self.assertIn("포", kopy)
        self.assertIn('"for print"', kopy)
        self.assertEqual(restored, source)
        self.assertTrue(stable)


if __name__ == "__main__":
    unittest.main()
