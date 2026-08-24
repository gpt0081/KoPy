import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("polars"), "Polars is not installed")
class PolarsRuntimeTests(unittest.TestCase):
    def test_real_polars_dataframe_lazy_and_groupby(self):
        source = (
            "임포트 폴라스 애즈 pl\n"
            "표 = pl.데이터프레임({\"group\": [\"a\", \"a\", \"b\", \"b\"], \"x\": [1, 2, 3, 4]})\n"
            "가공 = 표.위드컬럼즈((pl.컬(\"x\") * 2).에일리어스(\"x2\"))\n"
            "필터됨 = 가공.필터(pl.컬(\"x2\") >= 4)\n"
            "요약 = 필터됨.그룹바이(\"group\").어그(pl.컬(\"x2\").썸().에일리어스(\"total\")).소트(\"group\")\n"
            "레이지결과 = 표.레이지().필터(pl.컬(\"x\") > 1).셀렉트([\"group\", \"x\"]).콜렉트()\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)

        pl = namespace["pl"]
        summary = namespace["요약"]
        lazy_result = namespace["레이지결과"]

        self.assertIsInstance(summary, pl.DataFrame)
        self.assertEqual(summary.to_dict(as_series=False), {"group": ["a", "b"], "total": [4, 14]})
        self.assertEqual(lazy_result.shape, (3, 2))
        self.assertEqual(lazy_result["x"].to_list(), [2, 3, 4])


if __name__ == "__main__":
    unittest.main()
