import io
import os
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout

from kopy.cli import main


class CliV04Tests(unittest.TestCase):
    def _temp_source(self, source: str, suffix: str = ".py") -> str:
        handle = tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", suffix=suffix, delete=False)
        try:
            handle.write(source)
            return handle.name
        finally:
            handle.close()

    def test_help_accepts_kopy_word(self):
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = main(["help", "프린트"])
        self.assertEqual(code, 0)
        self.assertIn("Python print", stdout.getvalue())
        self.assertIn("출력", stdout.getvalue())

    def test_help_accepts_python_word(self):
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = main(["help", "print"])
        self.assertEqual(code, 0)
        self.assertIn("프린트", stdout.getvalue())

    def test_convert_python_command(self):
        path = self._temp_source("for i in range(2):\n    print(i)\n")
        stdout = io.StringIO()
        try:
            with redirect_stdout(stdout):
                code = main(["convert-python", path])
        finally:
            os.unlink(path)
        self.assertEqual(code, 0)
        self.assertIn("포 i 인 레인지(2):", stdout.getvalue())
        self.assertIn("프린트(i)", stdout.getvalue())

    def test_explain_command(self):
        path = self._temp_source('x = 1\n이프 x:\n    프린트("ok")\n', suffix=".kpy")
        stdout = io.StringIO()
        try:
            with redirect_stdout(stdout):
                code = main(["explain", path])
        finally:
            os.unlink(path)
        self.assertEqual(code, 0)
        self.assertIn("조건", stdout.getvalue())

    def test_syntax_error_has_learning_hint(self):
        path = self._temp_source('이프 트루\n    프린트("x")\n', suffix=".kpy")
        stderr = io.StringIO()
        try:
            with redirect_stderr(stderr):
                code = main(["check", "--no-spelling", path])
        finally:
            os.unlink(path)
        self.assertEqual(code, 1)
        self.assertIn("학습 힌트", stderr.getvalue())
        self.assertIn("콜론", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
