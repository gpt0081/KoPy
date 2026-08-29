import unittest
from pathlib import Path

from 학습_코스.course_testkit import load_python


MODULE = load_python(Path(__file__).with_name("solution.py"))


class SolutionTests(unittest.TestCase):
    def test_valid_source(self):
        result = MODULE.검사('프린트("프린트")\n')
        self.assertEqual(result["python"], 'print("프린트")\n')
        self.assertEqual(result["replacement_count"], 1)
        self.assertEqual(result["pairs"], [["프린트", "print"]])
        self.assertTrue(result["ok"])
        self.assertEqual(result["diagnostics"], [])

    def test_spelling_source(self):
        result = MODULE.검사('pritn("x")\n')
        self.assertFalse(result["ok"])
        self.assertEqual(result["diagnostics"][0]["code"], "spelling")


if __name__ == "__main__":
    unittest.main()
