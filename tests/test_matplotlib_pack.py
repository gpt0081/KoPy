import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class MatplotlibPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("matplotlib")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.kopy_module, "맷플롯립")
        self.assertIn("plt", pack.preferred_aliases)

    def test_pyplot_translation_is_namespace_scoped(self):
        source = (
            "임포트 맷플롯립.pyplot 애즈 plt\n"
            "plt.플롯([1, 2, 3], [2, 4, 3])\n"
            "plt.타이틀('demo')\n"
            "plt.엑스라벨('epoch')\n"
            "plt.와이라벨('loss')\n"
            "plt.레전드()\n"
        )
        python_source = translate(source).python
        self.assertIn("import matplotlib.pyplot as plt", python_source)
        self.assertIn("plt.plot([1, 2, 3], [2, 4, 3])", python_source)
        self.assertIn("plt.title('demo')", python_source)
        self.assertIn("plt.xlabel('epoch')", python_source)
        self.assertIn("plt.ylabel('loss')", python_source)
        self.assertIn("plt.legend()", python_source)

    def test_axes_methods_translate_when_pack_is_active(self):
        source = (
            "임포트 맷플롯립.pyplot 애즈 plt\n"
            "피겨, 축 = plt.서브플롯츠()\n"
            "축.스캐터([1, 2], [3, 4])\n"
            "축.셋타이틀('points')\n"
            "축.셋엑스라벨('x')\n"
            "축.셋와이라벨('y')\n"
        )
        python_source = translate(source).python
        self.assertIn("plt.subplots()", python_source)
        self.assertIn("축.scatter([1, 2], [3, 4])", python_source)
        self.assertIn("축.set_title('points')", python_source)
        self.assertIn("축.set_xlabel('x')", python_source)
        self.assertIn("축.set_ylabel('y')", python_source)

    def test_unimported_matplotlib_word_is_not_global(self):
        source = "플롯([1, 2], [3, 4])\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy(self):
        source = (
            "import matplotlib.pyplot as plt\n"
            "fig, ax = plt.subplots()\n"
            "ax.plot([1, 2], [3, 4])\n"
            "ax.set_title('demo')\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 맷플롯립.파이플롯 애즈 plt", kopy)
        self.assertIn("plt.서브플롯츠()", kopy)
        self.assertIn("ax.플롯([1, 2], [3, 4])", kopy)
        self.assertIn("ax.셋타이틀('demo')", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("맷플롯립.플롯")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "plot")


if __name__ == "__main__":
    unittest.main()
