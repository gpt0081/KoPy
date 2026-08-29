import unittest
from pathlib import Path

from 학습_코스.course_testkit import load_python


MODULE = load_python(Path(__file__).with_name("exercise.py"))


class ExerciseTests(unittest.TestCase):
    def test_current_scope_contract(self):
        self.assertEqual(
            MODULE.스코프_상태(),
            {
                "pack_import_activates": True,
                "no_import_preserves": True,
                "call_keyword_translates": True,
                "callee_specific": False,
            },
        )


if __name__ == "__main__":
    unittest.main()
