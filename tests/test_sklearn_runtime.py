import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("sklearn"), "scikit-learn is not installed")
class SklearnRuntimeTests(unittest.TestCase):
    def test_kopy_sklearn_training_executes(self):
        source = (
            "프롬 사이킷런.model_selection 임포트 트레인테스트스플릿\n"
            "프롬 사이킷런.preprocessing 임포트 스탠더드스케일러\n"
            "프롬 사이킷런.linear_model 임포트 로지스틱리그레션\n"
            "프롬 사이킷런.metrics 임포트 애큐러시스코어\n"
            "X = [[0.0], [1.0], [2.0], [3.0], [4.0], [5.0], [6.0], [7.0]]\n"
            "y = [0, 0, 0, 0, 1, 1, 1, 1]\n"
            "X_train, X_test, y_train, y_test = 트레인테스트스플릿(X, y, test_size=0.25, random_state=7, stratify=y)\n"
            "스케일러 = 스탠더드스케일러()\n"
            "X_train = 스케일러.핏트랜스폼(X_train)\n"
            "X_test = 스케일러.트랜스폼(X_test)\n"
            "모델 = 로지스틱리그레션()\n"
            "모델.핏(X_train, y_train)\n"
            "예측 = 모델.프리딕트(X_test)\n"
            "정확도 = 애큐러시스코어(y_test, 예측)\n"
        )
        namespace: dict[str, object] = {}
        exec(compile(translate(source).python, "<kopy-sklearn-smoke>", "exec"), namespace)
        self.assertGreaterEqual(float(namespace["정확도"]), 0.5)
        self.assertEqual(len(namespace["예측"]), 2)


if __name__ == "__main__":
    unittest.main()
