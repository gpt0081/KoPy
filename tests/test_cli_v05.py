import io
import unittest
from contextlib import redirect_stderr, redirect_stdout

from kopy.cli import main


class CliV05Tests(unittest.TestCase):
    def test_packs_lists_numpy(self):
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = main(["packs"])
        self.assertEqual(code, 0)
        self.assertIn("numpy", stdout.getvalue())
        self.assertIn("넘파이", stdout.getvalue())

    def test_numpy_pack_details(self):
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = main(["packs", "numpy"])
        self.assertEqual(code, 0)
        text = stdout.getvalue()
        self.assertIn("어레이", text)
        self.assertIn("array", text)

    def test_help_numpy_member(self):
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = main(["help", "np.어레이"])
        self.assertEqual(code, 0)
        text = stdout.getvalue()
        self.assertIn("numpy.array", text)
        self.assertIn("NumPy 배열", text)

    def test_unknown_pack_is_readable(self):
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            code = main(["packs", "does-not-exist"])
        self.assertEqual(code, 1)
        self.assertIn("팩을 찾지 못했습니다", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
