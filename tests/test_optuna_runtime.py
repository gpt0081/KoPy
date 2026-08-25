import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("optuna"), "optuna is not installed")
class OptunaRuntimeTests(unittest.TestCase):
    def test_real_optuna_study_and_trial_api(self):
        source = (
            "임포트 옵튜나\n"
            "옵튜나.logging.set_verbosity(옵튜나.logging.WARNING)\n"
            "데프 objective(trial):\n"
            "    x = trial.서제스트플로트('x', -5.0, 5.0)\n"
            "    depth = trial.서제스트인트('depth', 1, 4)\n"
            "    kind = trial.서제스트캐터고리컬('kind', ['a', 'b'])\n"
            "    리턴 (x - 1.5) ** 2 + (depth - 2) ** 2 + (0 이프 kind == 'a' 엘스 0.25)\n"
            "study = 옵튜나.크리에이트스터디(direction='minimize', sampler=옵튜나.samplers.RandomSampler(seed=7))\n"
            "study.옵티마이즈(objective, n_trials=8)\n"
            "best_value = study.베스트밸류\n"
            "best_params = study.베스트파람스\n"
            "trial_count = 렌(study.트라이얼즈)\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)

        self.assertEqual(namespace["trial_count"], 8)
        self.assertIsInstance(namespace["best_value"], float)
        self.assertGreaterEqual(namespace["best_value"], 0.0)
        self.assertEqual(set(namespace["best_params"]), {"x", "depth", "kind"})
        self.assertGreaterEqual(namespace["best_params"]["x"], -5.0)
        self.assertLessEqual(namespace["best_params"]["x"], 5.0)
        self.assertIn(namespace["best_params"]["depth"], range(1, 5))
        self.assertIn(namespace["best_params"]["kind"], {"a", "b"})


if __name__ == "__main__":
    unittest.main()
