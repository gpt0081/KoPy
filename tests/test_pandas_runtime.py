import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("pandas"), "pandas is not installed")
class PandasRuntimeTests(unittest.TestCase):
    def test_kopy_pandas_code_executes_with_real_pandas(self):
        source = (
            "임포트 판다스 애즈 pd\n"
            "표 = pd.데이터프레임({'label': ['a', 'a', 'b'], 'x': [1.0, None, 5.0]})\n"
            "정제 = 표.필엔에이(0.0)\n"
            "요약 = 정제.그룹바이('label').미인()\n"
            "행수 = 정제.셰이프[0]\n"
        )
        python_source = translate(source).python
        namespace: dict[str, object] = {}
        exec(compile(python_source, "<kopy-pandas-smoke>", "exec"), namespace)

        self.assertEqual(namespace["행수"], 3)
        summary = namespace["요약"]
        self.assertAlmostEqual(float(summary.loc["a", "x"]), 0.5)
        self.assertAlmostEqual(float(summary.loc["b", "x"]), 5.0)


if __name__ == "__main__":
    unittest.main()
