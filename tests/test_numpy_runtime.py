import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("numpy"), "NumPy is not installed")
class NumPyRuntimeTests(unittest.TestCase):
    def test_kopy_numpy_code_executes_with_real_numpy(self):
        source = (
            "임포트 넘파이 애즈 np\n"
            "x = np.어레이([1, 2, 3, 4], np.플로트32)\n"
            "y = x.리셰이프(2, 2)\n"
            "평균 = np.미인(y)\n"
            "크기 = np.린알지.노름(y)\n"
        )
        python_source = translate(source).python
        namespace: dict[str, object] = {}
        exec(compile(python_source, "<kopy-numpy-smoke>", "exec"), namespace)

        self.assertAlmostEqual(float(namespace["평균"]), 2.5)
        self.assertGreater(float(namespace["크기"]), 0.0)
        self.assertEqual(tuple(namespace["y"].shape), (2, 2))


if __name__ == "__main__":
    unittest.main()
