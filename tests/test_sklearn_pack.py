import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class SklearnPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("scikit-learn")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "sklearn")
        self.assertEqual(pack.kopy_module, "사이킷런")

    def test_from_import_and_estimator_methods_translate(self):
        source = (
            "프롬 사이킷런.model_selection 임포트 트레인테스트스플릿\n"
            "프롬 사이킷런.linear_model 임포트 로지스틱리그레션\n"
            "X_train, X_test, y_train, y_test = 트레인테스트스플릿(X, y, test_size=0.25)\n"
            "모델 = 로지스틱리그레션()\n"
            "모델.핏(X_train, y_train)\n"
            "예측 = 모델.프리딕트(X_test)\n"
        )
        python_source = translate(source).python
        self.assertIn("from sklearn.model_selection import train_test_split", python_source)
        self.assertIn("from sklearn.linear_model import LogisticRegression", python_source)
        self.assertIn("model", python_source.replace("모델", "model"))
        self.assertIn(".fit(X_train, y_train)", python_source)
        self.assertIn(".predict(X_test)", python_source)

    def test_reverse_translation_keeps_submodule_path_stable(self):
        source = (
            "from sklearn.preprocessing import StandardScaler\n"
            "scaler = StandardScaler()\n"
            "scaled = scaler.fit_transform(X)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 사이킷런.preprocessing 임포트 스탠더드스케일러", kopy)
        self.assertIn(".핏트랜스폼(X)", kopy)

    def test_help_term_resolves(self):
        resolved = resolve_pack_member("사이킷런.애큐러시스코어")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "accuracy_score")


if __name__ == "__main__":
    unittest.main()
