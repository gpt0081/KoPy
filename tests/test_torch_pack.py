import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class TorchPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("pytorch")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "torch")
        self.assertEqual(pack.kopy_module, "토치")

    def test_tensor_nn_optimizer_and_methods_translate(self):
        source = (
            "임포트 토치\n"
            "x = 토치.텐서([[1.0, 2.0]])\n"
            "모델 = 토치.엔엔.리니어(2, 1)\n"
            "옵티마이저 = 토치.옵팀.아담더블유(모델.파라미터스(), lr=0.01)\n"
            "출력 = 모델(x)\n"
            "손실 = 출력.썸()\n"
            "손실.백워드()\n"
            "옵티마이저.스텝()\n"
        )
        python_source = translate(source).python
        self.assertIn("import torch", python_source)
        self.assertIn("torch.tensor", python_source)
        self.assertIn("torch.nn.Linear", python_source)
        self.assertIn("torch.optim.AdamW", python_source)
        self.assertIn(".parameters()", python_source)
        self.assertIn(".backward()", python_source)
        self.assertIn(".step()", python_source)

    def test_reverse_translation(self):
        source = (
            "import torch\n"
            "model = torch.nn.Sequential(torch.nn.Linear(2, 1))\n"
            "loss = model(torch.ones(1, 2)).sum()\n"
            "loss.backward()\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 토치", kopy)
        self.assertIn("토치.엔엔.시퀀셜", kopy)
        self.assertIn("토치.엔엔.리니어", kopy)
        self.assertIn("토치.원즈", kopy)
        self.assertIn(".백워드()", kopy)

    def test_help_term_resolves(self):
        resolved = resolve_pack_member("토치.텐서")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "tensor")


if __name__ == "__main__":
    unittest.main()
