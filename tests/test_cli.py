import io
import os
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout

from kopy.cli import main


class CliTests(unittest.TestCase):
    def _temp_source(self, source: str) -> str:
        handle = tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            suffix=".py",
            delete=False,
        )
        try:
            handle.write(source)
            return handle.name
        finally:
            handle.close()

    def test_spelling_hint_stops_before_execution(self):
        path = self._temp_source('pritn("Hello")\n')
        stderr = io.StringIO()
        stdout = io.StringIO()
        try:
            with redirect_stdout(stdout), redirect_stderr(stderr):
                code = main(["run", "--spelling", path])
        finally:
            os.unlink(path)

        text = stderr.getvalue()
        self.assertEqual(1, code)
        self.assertIn("'pritn' → 'print'", text)
        self.assertIn("실행을 중단했습니다", text)
        self.assertNotIn("Traceback", text)
        self.assertNotIn("NameError", text)

    def test_runtime_error_is_compact_when_spelling_disabled(self):
        path = self._temp_source('pritn("Hello")\n')
        stderr = io.StringIO()
        stdout = io.StringIO()
        try:
            with redirect_stdout(stdout), redirect_stderr(stderr):
                code = main(["run", "--no-spelling", path])
        finally:
            os.unlink(path)

        text = stderr.getvalue()
        self.assertEqual(1, code)
        self.assertIn("KoPy 실행 오류 [NameError]", text)
        self.assertNotIn("Traceback", text)


if __name__ == "__main__":
    unittest.main()
