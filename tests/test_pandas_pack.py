import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class PandasPackTests(unittest.TestCase):
    def test_pack_registered(self):
        pack = pack_by_name("pandas")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.kopy_module, "판다스")
        self.assertEqual(pack.python_for("데이터프레임"), "DataFrame")

    def test_alias_scoped_translation(self):
        source = (
            "임포트 판다스 애즈 pd\n"
            "표 = pd.데이터프레임({'x': [1, 2, 3]})\n"
            "요약 = 표.헤드(2)\n"
        )
        result = translate(source).python
        self.assertIn("import pandas as pd", result)
        self.assertIn("pd.DataFrame", result)
        self.assertIn("표.head(2)", result)

    def test_pandas_word_does_not_become_global(self):
        source = "데이터프레임 = 3\n프린트(데이터프레임)\n"
        result = translate(source).python
        self.assertIn("데이터프레임 = 3", result)
        self.assertIn("print(데이터프레임)", result)

    def test_reverse_translation(self):
        source = (
            "import pandas as pd\n"
            "table = pd.DataFrame({'x': [1, 2, 3]})\n"
            "clean = table.dropna().reset_index()\n"
        )
        result = to_kopy(source).kopy
        self.assertIn("임포트 판다스 애즈 pd", result)
        self.assertIn("pd.데이터프레임", result)
        self.assertIn("table.드롭엔에이().리셋인덱스()", result)

    def test_help_resolution(self):
        resolved = resolve_pack_member("pd.그룹바이")
        self.assertIsNotNone(resolved)
        pack, info = resolved
        self.assertEqual(pack.name, "pandas")
        self.assertEqual(info.python, "groupby")

    def test_shared_numpy_pandas_spelling_with_same_target_is_safe(self):
        source = (
            "임포트 넘파이 애즈 np\n"
            "임포트 판다스 애즈 pd\n"
            "표 = pd.데이터프레임({'x': [1, 2, 3]})\n"
            "평균 = 표.미인()\n"
        )
        result = translate(source).python
        self.assertIn("표.mean()", result)


if __name__ == "__main__":
    unittest.main()
