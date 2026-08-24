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
            "모델 = lgb.엘지비엠클래시파이어(n_estimators=5, num_leaves=4)\n"
            "모델.핏(X, y)\n"
            "예측 = 모델.프리딕트(X)\n"
        )
        python_source = translate(source).python
        self.assertIn("import lightgbm as lgb", python_source)
        self.assertIn("lgb.LGBMClassifier(n_estimators=5, num_leaves=4)", python_source)
        self.assertIn("모델.fit(X, y)", python_source)
        self.assertIn("모델.predict(X)", python_source)

    def test_core_training_api_translation(self):
        source = (
            "임포트 라이트지비엠 애즈 lgb\n"
            "데이터 = lgb.데이터셋(X, label=y)\n"
            "모델 = lgb.트레인({\"objective\": \"binary\"}, 데이터, num_boost_round=3)\n"
        )
        python_source = translate(source).python
        self.assertIn("lgb.Dataset(X, label=y)", python_source)
        self.assertIn("lgb.train({\"objective\": \"binary\"}, 데이터, num_boost_round=3)", python_source)

    def test_unimported_lightgbm_word_is_not_global(self):
        source = "모델 = 엘지비엠클래시파이어()\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy(self):
        source = (
            "import lightgbm as lgb\n"
            "model = lgb.LGBMClassifier(n_estimators=5)\n"
            "model.fit(X, y)\n"
            "pred = model.predict(X)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 라이트지비엠 애즈 lgb", kopy)
        self.assertIn("lgb.엘지비엠클래시파이어(n_estimators=5)", kopy)
        self.assertIn("model.핏(X, y)", kopy)
        self.assertIn("model.프리딕트(X)", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("라이트지비엠.엘지비엠클래시파이어")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "LGBMClassifier")


if __name__ == "__main__":
    unittest.main()
