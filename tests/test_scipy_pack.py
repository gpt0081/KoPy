import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class SciPyPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("scipy")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.kopy_module, "사이파이")
        self.assertIn("sp", pack.preferred_aliases)

    def test_optimize_translation_is_namespace_scoped(self):
        source = (
            "프롬 사이파이.optimize 임포트 미니마이즈\n"
            "결과 = 미니마이즈(lambda x: (x[0] - 3) ** 2, [0.0])\n"
        )
        python_source = translate(source).python
        self.assertIn("from scipy.optimize import minimize", python_source)
        self.assertIn("minimize(lambda x: (x[0] - 3) ** 2, [0.0])", python_source)

    def test_alias_attribute_translation(self):
        source = (
            "임포트 사이파이.stats 애즈 sp\n"
            "점수 = sp.지스코어([1.0, 2.0, 3.0])\n"
        )
        python_source = translate(source).python
        self.assertIn("import scipy.stats as sp", python_source)
        self.assertIn("sp.zscore([1.0, 2.0, 3.0])", python_source)

    def test_unimported_scipy_word_is_not_global(self):
        source = "미니마이즈(lambda x: x * x, 1.0)\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy(self):
        source = (
            "from scipy.optimize import minimize\n"
            "result = minimize(lambda x: (x[0] - 2) ** 2, [0.0])\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 사이파이.옵티마이즈 임포트 미니마이즈", kopy)
        self.assertIn("미니마이즈(람다 x: (x[0] - 2) ** 2, [0.0])", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("사이파이.미니마이즈")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "minimize")


if __name__ == "__main__":
    unittest.main()
