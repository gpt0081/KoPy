import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class XGBoostPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("xgboost")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.kopy_module, "엑스지부스트")
        self.assertIn("xgb", pack.preferred_aliases)

    def test_alias_translation_is_namespace_scoped(self):
        source = (
            "임포트 엑스지부스트 애즈 xgb\n"
            "모델 = xgb.엑스지비클래시파이어(n_estimators=5, max_depth=2)\n"
            "모델.핏(X, y)\n"
            "예측 = 모델.프리딕트(X)\n"
        )
        python_source = translate(source).python
        self.assertIn("import xgboost as xgb", python_source)
        self.assertIn("xgb.XGBClassifier(n_estimators=5, max_depth=2)", python_source)
        self.assertIn("모델.fit(X, y)", python_source)
        self.assertIn("모델.predict(X)", python_source)

    def test_core_training_api_translation(self):
        source = (
            "임포트 엑스지부스트 애즈 xgb\n"
            "데이터 = xgb.디매트릭스(X, label=y)\n"
            "모델 = xgb.트레인({\"objective\": \"binary:logistic\"}, 데이터, num_boost_round=3)\n"
        )
        python_source = translate(source).python
        self.assertIn("xgb.DMatrix(X, label=y)", python_source)
        self.assertIn("xgb.train({\"objective\": \"binary:logistic\"}, 데이터, num_boost_round=3)", python_source)

    def test_unimported_xgboost_word_is_not_global(self):
        source = "모델 = 엑스지비클래시파이어()\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy(self):
        source = (
            "import xgboost as xgb\n"
            "model = xgb.XGBClassifier(n_estimators=5)\n"
            "model.fit(X, y)\n"
            "pred = model.predict(X)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 엑스지부스트 애즈 xgb", kopy)
        self.assertIn("xgb.엑스지비클래시파이어(n_estimators=5)", kopy)
        self.assertIn("model.핏(X, y)", kopy)
        self.assertIn("model.프리딕트(X)", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("엑스지부스트.엑스지비클래시파이어")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "XGBClassifier")


if __name__ == "__main__":
    unittest.main()
