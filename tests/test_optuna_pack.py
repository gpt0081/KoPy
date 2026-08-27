import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class OptunaPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("optuna")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "optuna")
        self.assertEqual(pack.kopy_module, "옵튜나")

    def test_module_translation_is_namespace_scoped(self):
        source = (
            "임포트 옵튜나\n"
            "study = 옵튜나.크리에이트_스터디(direction='minimize')\n"
            "study.옵티마이즈(objective, n_trials=10)\n"
            "best = study.베스트_패럼즈\n"
        )
        python_source = translate(source).python
        self.assertIn("import optuna", python_source)
        self.assertIn("optuna.create_study(direction='minimize')", python_source)
        self.assertIn("study.optimize(objective, n_trials=10)", python_source)
        self.assertIn("study.best_params", python_source)

    def test_trial_methods_translate_after_optuna_import(self):
        source = (
            "임포트 옵튜나\n"
            "x = trial.서제스트_플로트('x', -5.0, 5.0)\n"
            "depth = trial.서제스트_인트('depth', 2, 8)\n"
            "model = trial.서제스트_캐터고리컬('model', ['a', 'b'])\n"
        )
        python_source = translate(source).python
        self.assertIn("trial.suggest_float('x', -5.0, 5.0)", python_source)
        self.assertIn("trial.suggest_int('depth', 2, 8)", python_source)
        self.assertIn("trial.suggest_categorical('model', ['a', 'b'])", python_source)

    def test_legacy_compact_spellings_still_translate(self):
        source = (
            "임포트 옵튜나\n"
            "study = 옵튜나.크리에이트스터디(direction='minimize')\n"
            "x = trial.서제스트플로트('x', 0.0, 1.0)\n"
            "best = study.베스트파람스\n"
        )
        python_source = translate(source).python
        self.assertIn("optuna.create_study(direction='minimize')", python_source)
        self.assertIn("trial.suggest_float('x', 0.0, 1.0)", python_source)
        self.assertIn("study.best_params", python_source)

    def test_unimported_words_are_not_global(self):
        source = "x = trial.서제스트_플로트('x', 0.0, 1.0)\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy_prefers_canonical_underscore_spellings(self):
        source = (
            "import optuna\n"
            "study = optuna.create_study(direction='minimize')\n"
            "x = trial.suggest_float('x', 0.0, 1.0)\n"
            "best = study.best_params\n"
            "study.optimize(objective, n_trials=5)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 옵튜나", kopy)
        self.assertIn("옵튜나.크리에이트_스터디", kopy)
        self.assertIn("trial.서제스트_플로트", kopy)
        self.assertIn("study.베스트_패럼즈", kopy)
        self.assertIn("study.옵티마이즈", kopy)
        self.assertNotIn("크리에이트스터디", kopy)
        self.assertNotIn("서제스트플로트", kopy)
        self.assertNotIn("베스트파람스", kopy)

    def test_help_resolution_uses_canonical_spelling(self):
        resolved = resolve_pack_member("옵튜나.크리에이트_스터디")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "create_study")
        self.assertEqual(info.kopy, "크리에이트_스터디")

    def test_generic_keywords_and_parameter_names_remain_python_for_now(self):
        source = (
            "임포트 옵튜나\n"
            "study = 옵튜나.크리에이트_스터디(direction='maximize', study_name='demo')\n"
            "study.옵티마이즈(objective, n_trials=20, timeout=30)\n"
            "rate = trial.서제스트_플로트('learning_rate', 1e-4, 1e-1, log=True)\n"
        )
        python_source = translate(source).python
        for token in ("direction=", "study_name=", "n_trials=", "timeout=", "log=True", "'learning_rate'"):
            self.assertIn(token, python_source)


if __name__ == "__main__":
    unittest.main()
