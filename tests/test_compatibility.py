import io
import unittest
from contextlib import redirect_stdout

from kopy.translator import to_kopy, translate


GOLDEN_PROGRAMS = (
    "print(1 + 2 * 3)\n",
    "for i in range(4):\n    print(i)\n",
    "x = 7\nif x > 5:\n    print('big')\nelse:\n    print('small')\n",
    "def add(a, b):\n    return a + b\nprint(add(2, 5))\n",
    "items = [3, 1, 2]\nprint(sorted(items))\nprint(len(items))\n",
)


def execute(source: str) -> str:
    output = io.StringIO()
    namespace = {"__name__": "__main__"}
    with redirect_stdout(output):
        exec(compile(source, "<golden>", "exec"), namespace, namespace)
    return output.getvalue()


class CompatibilityTests(unittest.TestCase):
    def test_python_and_generated_kopy_have_same_behavior(self):
        for python_source in GOLDEN_PROGRAMS:
            with self.subTest(source=python_source):
                expected = execute(python_source)
                kopy_source = to_kopy(python_source).kopy
                restored_python = translate(kopy_source).python
                actual = execute(restored_python)
                self.assertEqual(expected, actual)

    def test_generated_kopy_compiles_after_translation(self):
        for python_source in GOLDEN_PROGRAMS:
            with self.subTest(source=python_source):
                kopy_source = to_kopy(python_source).kopy
                compile(translate(kopy_source).python, "<kopy-golden>", "exec")


if __name__ == "__main__":
    unittest.main()
