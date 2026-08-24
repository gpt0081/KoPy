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

        self.assertEqual(namespace["예측"].shape, (6,))
        self.assertEqual(namespace["확률"].shape, (6, 2))
        self.assertEqual(namespace["부스터예측"].shape, (6,))
        self.assertGreaterEqual(float(namespace["모델"].score(namespace["X"], namespace["y"])), 0.8)
        self.assertEqual(namespace["디"].num_row(), 6)
        self.assertEqual(namespace["디"].num_col(), 2)


if __name__ == "__main__":
    unittest.main()
