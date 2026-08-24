import importlib.util
import tempfile
import unittest
from pathlib import Path

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("matplotlib"), "Matplotlib is not installed")
class MatplotlibRuntimeTests(unittest.TestCase):
    def test_real_matplotlib_plot_and_save(self):
        import matplotlib

        matplotlib.use("Agg")

        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "loss.png"
            source = (
                "임포트 맷플롯립.pyplot 애즈 plt\n"
                "에폭 = [1, 2, 3, 4]\n"
                "손실 = [1.0, 0.7, 0.5, 0.35]\n"
                "피겨, 축 = plt.서브플롯츠()\n"
                "축.플롯(에폭, 손실, marker='o', label='loss')\n"
                "축.셋타이틀('Training loss')\n"
                "축.셋엑스라벨('Epoch')\n"
                "축.셋와이라벨('Loss')\n"
                "축.레전드()\n"
                f"피겨.세이브피그({str(output)!r})\n"
                "plt.클로즈(피겨)\n"
            )
            namespace = {}
            exec(translate(source).python, namespace, namespace)

            self.assertTrue(output.exists())
            self.assertGreater(output.stat().st_size, 1000)


if __name__ == "__main__":
    unittest.main()
