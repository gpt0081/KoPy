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
            "모델 = xgb.엑스지비클래시파이어(엔_에스티메이터즈=5, 맥스_뎁스=2)\n"
            "모델.핏(엑스, 와이)\n"
            "프레즈 = 모델.프리딕트(엑스)\n"
        )
        python_source = translate(source).python
        self.assertIn("import xgboost as xgb", python_source)
        self.assertIn("xgb.XGBClassifier(n_estimators=5, max_depth=2)", python_source)
        self.assertIn("model.fit(X, y)", python_source)
        self.assertIn("model.predict(X)", python_source)

    def test_core_training_api_translation(self):
        source = (
            "임포트 엑스지부스트 애즈 xgb\n"
            "데이터 = xgb.디매트릭스(엑스, 레이블=와이)\n"
            "모델 = xgb.트레인({\"objective\": \"binary:logistic\"}, 데이터, 넘_부스트_라운드=3)\n"
        )
        python_source = translate(source).python
        self.assertIn("xgb.DMatrix(X, label=y)", python_source)
        self.assertIn("model = xgb.train", python_source)
        self.assertIn("num_boost_round=3", python_source)

    def test_unimported_pack_member_is_not_global(self):
        source = "모델 = 엑스지비클래시파이어()\n"
        self.assertEqual(translate(source).python, "model = 엑스지비클래시파이어()\n")

    def test_python_to_kopy(self):
        source = (
            "import xgboost as xgb\n"
            "model = xgb.XGBClassifier(n_estimators=5, learning_rate=0.2)\n"
            "model.fit(X, y)\n"
            "preds = model.predict(X)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 엑스지부스트 애즈 xgb", kopy)
        self.assertIn("모델 = xgb.엑스지비클래시파이어(엔_에스티메이터즈=5, 러닝_레이트=0.2)", kopy)
        self.assertIn("모델.핏(엑스, 와이)", kopy)
        self.assertIn("프레즈 = 모델.프리딕트(엑스)", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("엑스지부스트.엑스지비클래시파이어")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "XGBClassifier")


if __name__ == "__main__":
    unittest.main()
