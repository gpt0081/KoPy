import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("xgboost"), "XGBoost is not installed")
class XGBoostRuntimeTests(unittest.TestCase):
    def test_real_xgboost_classifier_and_dmatrix_training(self):
        source = (
            "임포트 넘파이 애즈 np\n"
            "임포트 엑스지부스트 애즈 xgb\n"
            "X = np.어레이([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0], [0.1, 0.2], [0.9, 0.8]], dtype=np.플로트32)\n"
            "y = np.어레이([0, 0, 0, 1, 0, 1])\n"
            "모델 = xgb.엑스지비클래시파이어(n_estimators=8, max_depth=2, learning_rate=0.5, tree_method=\"hist\", device=\"cpu\", n_jobs=1, random_state=0)\n"
            "모델.핏(X, y)\n"
            "예측 = 모델.프리딕트(X)\n"
            "확률 = 모델.프리딕트프로바(X)\n"
            "디 = xgb.디매트릭스(X, label=y)\n"
            "부스터 = xgb.트레인({\"objective\": \"binary:logistic\", \"max_depth\": 2, \"eta\": 0.5, \"tree_method\": \"hist\", \"device\": \"cpu\", \"nthread\": 1}, 디, num_boost_round=4)\n"
            "부스터예측 = 부스터.프리딕트(디)\n"
        )
        namespace = {}
        exec(translate(source).python, namespace, namespace)

        predictions = namespace["예측"]
        probabilities = namespace["확률"]
        booster_predictions = namespace["부스터예측"]

        self.assertEqual(predictions.shape, (6,))
        self.assertEqual(probabilities.shape, (6, 2))
        self.assertEqual(booster_predictions.shape, (6,))
        self.assertTrue(namespace["np"].isfinite(probabilities).all())
        self.assertTrue(namespace["np"].isfinite(booster_predictions).all())
        self.assertTrue(namespace["np"].allclose(probabilities.sum(axis=1), 1.0, atol=1e-6))
        self.assertEqual(namespace["디"].num_row(), 6)
        self.assertEqual(namespace["디"].num_col(), 2)


if __name__ == "__main__":
    unittest.main()
