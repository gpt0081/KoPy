import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class PolarsPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("polars")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.kopy_module, "폴라스")
        self.assertIn("pl", pack.preferred_aliases)

    def test_alias_translation_is_namespace_scoped(self):
        source = (
            "임포트 폴라스 애즈 pl\n"
            "표 = pl.데이터프레임({\"x\": [1, 2], \"y\": [3, 4]})\n"
            "표 = 표.위드컬럼즈((pl.컬(\"x\") * 2).에일리어스(\"x2\"))\n"
            "결과 = 표.필터(pl.컬(\"x2\") > 2)\n"
        )
        python_source = translate(source).python
        self.assertIn("import polars as pl", python_source)
        self.assertIn("pl.DataFrame", python_source)
        self.assertIn("표.with_columns", python_source)
        self.assertIn("pl.col(\"x\")", python_source)
        self.assertIn(".alias(\"x2\")", python_source)
        self.assertIn("표.filter", python_source)

    def test_lazy_and_groupby_translation(self):
        source = (
            "임포트 폴라스 애즈 pl\n"
            "요약 = 표.레이지().그룹바이(\"label\").어그(pl.컬(\"value\").미인()).콜렉트()\n"
        )
        python_source = translate(source).python
        self.assertIn("표.lazy().group_by(\"label\").agg(pl.col(\"value\").mean()).collect()", python_source)

    def test_unimported_polars_word_is_not_global(self):
        source = "표 = 데이터프레임({\"x\": [1, 2]})\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy(self):
        source = (
            "import polars as pl\n"
            "table = pl.DataFrame({\"x\": [1, 2]})\n"
            "result = table.with_columns((pl.col(\"x\") * 2).alias(\"x2\"))\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 폴라스 애즈 pl", kopy)
        self.assertIn("pl.데이터프레임", kopy)
        self.assertIn("table.위드컬럼즈", kopy)
        self.assertIn("pl.컬(\"x\")", kopy)
        self.assertIn(".에일리어스(\"x2\")", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("폴라스.데이터프레임")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "DataFrame")

    def test_keywords_remain_python_spelling(self):
        source = "임포트 폴라스 애즈 pl\n표 = pl.리드씨에스브이(\"data.csv\", has_header=True, separator=\",\")\n"
        python_source = translate(source).python
        self.assertIn("has_header=True", python_source)
        self.assertIn("separator=\",\"", python_source)


if __name__ == "__main__":
    unittest.main()
