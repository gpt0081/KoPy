import unittest

from kopy.education import explain_source, syntax_lesson
from kopy.words import info_for


class EducationTests(unittest.TestCase):
    def test_help_metadata_for_print(self):
        info = info_for("프린트")
        self.assertIsNotNone(info)
        assert info is not None
        self.assertEqual(info.python, "print")
        self.assertIn("출력", info.description)
        self.assertIn("프린트", info.kopy_example or "")

    def test_explain_source_does_not_execute(self):
        source = 'x = 1\n이프 x:\n    프린트("ok")\n'
        steps = explain_source(source)
        self.assertTrue(any("변수" in step for step in steps))
        self.assertTrue(any("조건" in step for step in steps))

    def test_syntax_lesson_for_missing_colon(self):
        try:
            compile("if True\n    print('x')\n", "demo.py", "exec")
        except SyntaxError as exc:
            lesson = syntax_lesson(exc)
        else:
            self.fail("SyntaxError expected")
        self.assertIn("콜론", lesson.title)
        self.assertIsNotNone(lesson.suggestion)


if __name__ == "__main__":
    unittest.main()
