import importlib.util
import os
import subprocess
import sys
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("lightgbm"), "LightGBM is not installed")
class LightGBMRuntimeTests(unittest.TestCase):
    def test_real_lightgbm_classifier_and_dataset_training(self):
        source = (
            "임포트 넘파이 애즈 np\n"
            "임포트 라이트지비엠 애즈 lgb\n"
            "X = np.어레이([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0], [0.1, 0.2], [0.9, 0.8]], dtype=np.플로트64)\n"
            "y = np.어레이([0, 0, 0, 1, 0, 1])\n"
            "모델 = lgb.엘지비엠클래시파이어(n_estimators=8, num_leaves=4, min_child_samples=1, learning_rate=0.5, verbosity=-1, n_jobs=1, random_state=0)\n"
            "모델.핏(X, y)\n"
            "예측 = 모델.프리딕트(X)\n"
            "확률 = 모델.프리딕트프로바(X)\n"
            "디 = lgb.데이터셋(X, label=y, free_raw_data=False)\n"
            "부스터 = lgb.트레인({\"objective\": \"binary\", \"verbosity\": -1, \"num_threads\": 1, \"min_data_in_leaf\": 1, \"num_leaves\": 4, \"learning_rate\": 0.5}, 디, num_boost_round=4)\n"
            "부스터예측 = 부스터.프리딕트(X)\n"
        )
        python_source = translate(source).python + (
            "\nassert 예측.shape == (6,)\n"
            "assert 확률.shape == (6, 2)\n"
            "assert 부스터예측.shape == (6,)\n"
            "assert np.isfinite(확률).all()\n"
            "assert np.isfinite(부스터예측).all()\n"
            "assert np.allclose(확률.sum(axis=1), 1.0, atol=1e-6)\n"
            "디.construct()\n"
            "assert 디.num_data() == 6\n"
            "assert 디.num_feature() == 2\n"
            "print('LIGHTGBM_RUNTIME_OK')\n"
        )

        env = os.environ.copy()
        env.setdefault("OMP_NUM_THREADS", "1")
        env.setdefault("OMP_THREAD_LIMIT", "1")
        completed = subprocess.run(
            [sys.executable, "-c", python_source],
            capture_output=True,
            text=True,
            env=env,
            timeout=60,
            check=False,
        )

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("LIGHTGBM_RUNTIME_OK", completed.stdout)


if __name__ == "__main__":
    unittest.main()
