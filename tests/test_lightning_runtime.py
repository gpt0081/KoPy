import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("lightning"), "lightning is not installed")
class LightningRuntimeTests(unittest.TestCase):
    def test_real_lightning_trainer_fit(self):
        source = (
            "임포트 라이트닝 애즈 L\n"
            "임포트 토치\n"
            "프롬 torch.utils.data 임포트 DataLoader, TensorDataset\n"
            "L.시드에브리띵(7, workers=True)\n"
            "class TinyModel(L.라이트닝모듈):\n"
            "    def __init__(self):\n"
            "        super().__init__()\n"
            "        self.layer = 토치.엔엔.리니어(2, 1)\n"
            "        self.loss_fn = 토치.엔엔.엠에스이로스()\n"
            "    def forward(self, x):\n"
            "        return self.layer(x)\n"
            "    def 트레이닝스텝(self, batch, batch_idx):\n"
            "        x, y = batch\n"
            "        loss = self.loss_fn(self(x), y)\n"
            "        self.로그('train_loss', loss)\n"
            "        return loss\n"
            "    def 컨피규어옵티마이저스(self):\n"
            "        return 토치.옵팀.에스지디(self.파라미터스(), lr=0.1)\n"
            "X_train = 토치.텐서([[0.0, 0.0], [1.0, 1.0], [2.0, 2.0], [3.0, 3.0]])\n"
            "y_train = 토치.텐서([[0.0], [2.0], [4.0], [6.0]])\n"
            "train_loader = DataLoader(TensorDataset(X_train, y_train), batch_size=4)\n"
            "model = TinyModel()\n"
            "trainer = L.트레이너(max_epochs=1, accelerator='cpu', devices=1, logger=False, enable_checkpointing=False, enable_progress_bar=False, enable_model_summary=False, limit_train_batches=1)\n"
            "trainer.핏(model, train_loader)\n"
            "global_step = trainer.global_step\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)
        self.assertEqual(namespace["global_step"], 1)
        self.assertEqual(namespace["trainer"].max_epochs, 1)


if __name__ == "__main__":
    unittest.main()
