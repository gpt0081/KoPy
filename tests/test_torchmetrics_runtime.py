import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("torchmetrics"), "torchmetrics is not installed")
class TorchMetricsRuntimeTests(unittest.TestCase):
    def test_real_torchmetrics_metrics(self):
        source = (
            "임포트 토치\n"
            "임포트 토치메트릭스 애즈 tm\n"
            "preds = 토치.텐서([0, 1, 1, 0])\n"
            "target = 토치.텐서([0, 1, 0, 0])\n"
            "accuracy_metric = tm.애큐러시(task='binary')\n"
            "f1_metric = tm.에프원스코어(task='binary')\n"
            "accuracy_value = float(accuracy_metric(preds, target))\n"
            "f1_value = float(f1_metric(preds, target))\n"
            "mean_metric = tm.미인메트릭()\n"
            "mean_metric.update(토치.텐서(2.0))\n"
            "mean_metric.update(토치.텐서(4.0))\n"
            "mean_value = float(mean_metric.compute())\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)
        self.assertAlmostEqual(namespace["accuracy_value"], 0.75, places=6)
        self.assertAlmostEqual(namespace["f1_value"], 2.0 / 3.0, places=6)
        self.assertAlmostEqual(namespace["mean_value"], 3.0, places=6)


if __name__ == "__main__":
    unittest.main()
