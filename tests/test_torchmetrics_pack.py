import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class TorchMetricsPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("torchmetrics")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "torchmetrics")
        self.assertEqual(pack.kopy_module, "토치메트릭스")

    def test_module_translation_is_namespace_scoped(self):
        source = (
            "임포트 토치메트릭스 애즈 tm\n"
            "accuracy = tm.애큐러시(task='binary')\n"
            "에프1 = tm.에프1스코어(task='multiclass', num_classes=3)\n"
            "mean_loss = tm.미인메트릭()\n"
        )
        python_source = translate(source).python
        self.assertIn("import torchmetrics as tm", python_source)
        self.assertIn("tm.Accuracy(task='binary')", python_source)
        self.assertIn("f1 = tm.F1Score(task='multiclass', num_classes=3)", python_source)
        self.assertIn("tm.MeanMetric()", python_source)

    def test_unimported_words_are_not_pack_global(self):
        source = "accuracy = tm.애큐러시(task='binary')\n"
        self.assertEqual(translate(source).python, source)

    def test_common_metric_identifier_translates(self):
        source = (
            "임포트 토치메트릭스 애즈 tm\n"
            "메트릭 = tm.애큐러시(task='binary')\n"
            "메트릭.update(프레즈, 타깃)\n"
            "value = 메트릭.compute()\n"
            "메트릭.reset()\n"
        )
        python_source = translate(source).python
        self.assertIn("metric.update(preds, target)", python_source)
        self.assertIn("metric.compute()", python_source)
        self.assertIn("metric.reset()", python_source)

    def test_python_to_kopy(self):
        source = (
            "import torchmetrics as tm\n"
            "accuracy = tm.Accuracy(task='binary')\n"
            "f1 = tm.F1Score(task='binary')\n"
            "metric = tm.Accuracy(task='binary')\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 토치메트릭스 애즈 tm", kopy)
        self.assertIn("tm.애큐러시(task='binary')", kopy)
        self.assertIn("에프1 = tm.에프1스코어(task='binary')", kopy)
        self.assertIn("메트릭 = tm.애큐러시(task='binary')", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("토치메트릭스.에프1스코어")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "F1Score")

    def test_generic_keywords_remain_python(self):
        source = (
            "임포트 토치메트릭스 애즈 tm\n"
            "메트릭 = tm.에프1스코어(task='multiclass', num_classes=4, average='macro')\n"
        )
        python_source = translate(source).python
        for token in ("task=", "num_classes=", "average="):
            self.assertIn(token, python_source)


if __name__ == "__main__":
    unittest.main()
