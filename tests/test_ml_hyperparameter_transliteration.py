import unittest

from kopy.translator import to_kopy, translate
from kopy.words import COMMON_IDENTIFIERS, info_for


class MLHyperparameterTransliterationTests(unittest.TestCase):
    def test_common_ml_hyperparameters_translate_both_directions(self):
        source = (
            "모델 = build(엔_에스티메이터즈=20, 맥스_뎁스=2, 러닝_레이트=0.3, 엔_잡스=1)\n"
            "설정 = tune(넘_리브즈=4, 민_차일드_샘플즈=1, 트리_메서드='hist', 디바이스='cpu')\n"
            "데이터 = matrix(엑스, 레이블=와이)\n"
            "모델 = train(데이터, 넘_부스트_라운드=3, 버보시티=-1)\n"
        )
        python_source = translate(source).python
        for expected in (
            "n_estimators=20",
            "max_depth=2",
            "learning_rate=0.3",
            "n_jobs=1",
            "num_leaves=4",
            "min_child_samples=1",
            "tree_method='hist'",
            "device='cpu'",
            "label=y",
            "num_boost_round=3",
            "verbosity=-1",
        ):
            self.assertIn(expected, python_source)

        kopy = to_kopy(python_source).kopy
        for expected in (
            "엔_에스티메이터즈=20",
            "맥스_뎁스=2",
            "러닝_레이트=0.3",
            "엔_잡스=1",
            "넘_리브즈=4",
            "민_차일드_샘플즈=1",
            "트리_메서드='hist'",
            "디바이스='cpu'",
            "레이블=와이",
            "넘_부스트_라운드=3",
            "버보시티=-1",
        ):
            self.assertIn(expected, kopy)

    def test_numeric_and_string_values_are_untouched(self):
        source = "설정 = fn(엔_에스티메이터즈=25, 맥스_뎁스=3, 디바이스='cuda:0')\n"
        python_source = translate(source).python
        self.assertIn("n_estimators=25", python_source)
        self.assertIn("max_depth=3", python_source)
        self.assertIn("device='cuda:0'", python_source)
        self.assertIn("25", to_kopy(python_source).kopy)
        self.assertNotIn("이십오", to_kopy(python_source).kopy)

    def test_new_identifiers_are_editor_visible(self):
        for kopy_word, python_name in (
            ("엔_에스티메이터즈", "n_estimators"),
            ("러닝_레이트", "learning_rate"),
            ("넘_리브즈", "num_leaves"),
            ("넘_부스트_라운드", "num_boost_round"),
        ):
            self.assertIn(python_name, COMMON_IDENTIFIERS.values())
            info = info_for(kopy_word)
            self.assertIsNotNone(info)
            self.assertEqual(info.python, python_name)
            self.assertEqual(info.category, "identifier")


if __name__ == "__main__":
    unittest.main()
