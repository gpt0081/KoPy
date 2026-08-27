import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class LightGBMPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("lightgbm")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.kopy_module, "라이트지비엠")
        self.assertIn("lgb", pack.preferred_aliases)

    def test_alias_translation_is_namespace_scoped(self):
        source = (
            "임포트 라이트지비엠 애즈 lgb\n"
            "모델 = lgb.엘지비엠클래시파이어(엔_에스티메이터즈=5, 넘_리브즈=4)\n"
            "모델.핏(엑스, 와이)\n"
            "프레즈 = 모델.프리딕트(엑스)\n"
        )
        python_source = translate(source).python
        self.assertIn("import lightgbm as lgb", python_source)
        self.assertIn("lgb.LGBMClassifier(n_estimators=5, num_leaves=4)", python_source)
        self.assertIn("model.fit(X, y)", python_source)
        self.assertIn("preds = model.predict(X)", python_source)

    def test_core_training_api_translation(self):
        source = (
            "임포트 라이트지비엠 애즈 lgb\n"
            "데이터 = lgb.데이터셋(엑스, 레이블=와이)\n"
            "모델 = lgb.트레인({\"objective\": \"binary\"}, 데이터, 넘_부스트_라운드=3)\n"
        )
        python_source = translate(source).python
        self.assertIn("lgb.Dataset(X, label=y)", python_source)
        self.assertIn("model = lgb.train", python_source)
        self.assertIn("num_boost_round=3", python_source)

    def test_unimported_pack_member_stays_kopy_but_common_identifier_translates(self):
        source = "모델 = 엘지비엠클래시파이어()\n"
        self.assertEqual(translate(source).python, "model = 엘지비엠클래시파이어()\n")

    def test_python_to_kopy(self):
        source = (
            "import lightgbm as lgb\n"
            "model = lgb.LGBMClassifier(n_estimators=5, learning_rate=0.2)\n"
            "model.fit(X, y)\n"
            "preds = model.predict(X)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 라이트지비엠 애즈 lgb", kopy)
        self.assertIn("모델 = lgb.엘지비엠클래시파이어(엔_에스티메이터즈=5, 러닝_레이트=0.2)", kopy)
        self.assertIn("모델.핏(엑스, 와이)", kopy)
        self.assertIn("프레즈 = 모델.프리딕트(엑스)", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("라이트지비엠.엘지비엠클래시파이어")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "LGBMClassifier")


if __name__ == "__main__":
    unittest.main()
