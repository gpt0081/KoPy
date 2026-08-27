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
            "엑스 = 토치.텐서([[1.0, 2.0]])\n"
            "모델 = 토치.엔엔.리니어(2, 1)\n"
            "옵티마이저 = 토치.옵팀.아담더블유(모델.파라미터스(), lr=0.01)\n"
            "출력 = 모델(엑스)\n"
            "손실 = 출력.썸()\n"
            "옵티마이저.제로_그라드()\n"
            "손실.백워드()\n"
            "옵티마이저.스텝()\n"
        )
        python_source = translate(source).python
        self.assertIn("import torch", python_source)
        self.assertIn("X = torch.tensor", python_source)
        self.assertIn("torch.nn.Linear", python_source)
        self.assertIn("torch.optim.AdamW", python_source)
        self.assertIn(".parameters()", python_source)
        self.assertIn(".zero_grad()", python_source)
        self.assertIn(".backward()", python_source)
        self.assertIn(".step()", python_source)

    def test_reverse_translation_uses_canonical_underscore_and_digit_spellings(self):
        source = (
            "import torch\n"
            "model = torch.nn.Conv2d(3, 8, 3)\n"
            "optimizer = torch.optim.AdamW(model.parameters())\n"
            "optimizer.zero_grad()\n"
            "state = model.state_dict()\n"
            "with torch.no_grad():\n"
            "    output = model(torch.ones(1, 3, 8, 8))\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 토치", kopy)
        self.assertIn("토치.엔엔.컨브2디", kopy)
        self.assertIn(".제로_그라드()", kopy)
        self.assertIn(".스테이트_딕트()", kopy)
        self.assertIn("토치.노_그라드()", kopy)
        self.assertNotIn("컨브투디", kopy)
        self.assertNotIn("제로그라드", kopy)

    def test_legacy_compact_spellings_still_translate(self):
        source = (
            "임포트 토치\n"
            "모델 = 토치.엔엔.컨브투디(3, 8, 3)\n"
            "옵티마이저.제로그라드()\n"
            "상태 = 모델.스테이트딕트()\n"
            "위드 토치.노그라드():\n"
            "    패스\n"
        )
        python_source = translate(source).python
        self.assertIn("torch.nn.Conv2d", python_source)
        self.assertIn(".zero_grad()", python_source)
        self.assertIn("model.state_dict()", python_source)
        self.assertIn("with torch.no_grad():", python_source)

    def test_digit_bearing_layers_keep_digits(self):
        source = "import torch\na = torch.nn.BatchNorm1d(8)\nb = torch.nn.Conv1d(2, 4, 3)\n"
        kopy = to_kopy(source).kopy
        self.assertIn("토치.엔엔.배치노름1디", kopy)
        self.assertIn("토치.엔엔.컨브1디", kopy)
        self.assertNotIn("배치노름원디", kopy)
        self.assertNotIn("컨브원디", kopy)

    def test_help_term_resolves(self):
        resolved = resolve_pack_member("토치.텐서")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "tensor")


if __name__ == "__main__":
    unittest.main()
