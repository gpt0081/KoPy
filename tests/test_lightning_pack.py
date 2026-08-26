import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class LightningPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("lightning")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "lightning")
        self.assertEqual(pack.kopy_module, "라이트닝")

    def test_module_translation_is_namespace_scoped(self):
        source = (
            "임포트 라이트닝 애즈 L\n"
            "trainer = L.트레이너(max_epochs=1, accelerator='cpu')\n"
            "trainer.핏(모델, train_loader)\n"
        )
        python_source = translate(source).python
        self.assertIn("import lightning as L", python_source)
        self.assertIn("L.Trainer(max_epochs=1, accelerator='cpu')", python_source)
        self.assertIn("trainer.fit(model, train_loader)", python_source)

    def test_lightning_module_runtime_methods_translate_after_import(self):
        source = (
            "임포트 라이트닝 애즈 L\n"
            "모델.로그('train_loss', loss)\n"
            "모델.세이브하이퍼파라미터스()\n"
            "모델.매뉴얼백워드(loss)\n"
        )
        python_source = translate(source).python
        self.assertIn("model.log('train_loss', loss)", python_source)
        self.assertIn("model.save_hyperparameters()", python_source)
        self.assertIn("model.manual_backward(loss)", python_source)

    def test_framework_override_hooks_remain_python_native(self):
        source = (
            "임포트 라이트닝 애즈 L\n"
            "class Model(L.라이트닝모듈):\n"
            "    def training_step(self, batch, batch_idx):\n"
            "        return loss\n"
            "    def configure_optimizers(self):\n"
            "        return optimizer\n"
        )
        python_source = translate(source).python
        self.assertIn("def training_step(self, batch, batch_idx):", python_source)
        self.assertIn("def configure_optimizers(self):", python_source)

    def test_common_fit_is_global_but_pack_member_remains_scoped(self):
        source = "trainer.핏(모델, train_loader)\n"
        self.assertEqual(translate(source).python, "trainer.fit(model, train_loader)\n")

    def test_python_to_kopy(self):
        source = (
            "import lightning as L\n"
            "trainer = L.Trainer(max_epochs=1)\n"
            "trainer.fit(model, train_loader)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 라이트닝 애즈 L", kopy)
        self.assertIn("L.트레이너(max_epochs=1)", kopy)
        self.assertIn("trainer.핏(모델, train_loader)", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("라이트닝.트레이너")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "Trainer")

    def test_generic_keywords_remain_python(self):
        source = (
            "임포트 라이트닝 애즈 L\n"
            "trainer = L.트레이너(max_epochs=2, accelerator='cpu', devices=1, logger=False, enable_checkpointing=False)\n"
        )
        python_source = translate(source).python
        for token in ("max_epochs=", "accelerator=", "devices=", "logger=False", "enable_checkpointing=False"):
            self.assertIn(token, python_source)


if __name__ == "__main__":
    unittest.main()
