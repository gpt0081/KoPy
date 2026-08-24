import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("torch"), "PyTorch is not installed")
class TorchRuntimeTests(unittest.TestCase):
    def test_kopy_torch_training_step_executes(self):
        source = (
            "임포트 토치\n"
            "토치.매뉴얼시드(7)\n"
            "X = 토치.텐서([[0.0], [1.0], [2.0], [3.0]])\n"
            "y = 토치.텐서([[0.0], [2.0], [4.0], [6.0]])\n"
            "모델 = 토치.엔엔.리니어(1, 1)\n"
            "손실함수 = 토치.엔엔.엠에스이로스()\n"
            "옵티마이저 = 토치.옵팀.에스지디(모델.파라미터스(), lr=0.05)\n"
            "옵티마이저.제로그라드()\n"
            "예측 = 모델(X)\n"
            "손실 = 손실함수(예측, y)\n"
            "초기손실 = 손실.아이템()\n"
            "손실.백워드()\n"
            "옵티마이저.스텝()\n"
            "새손실 = 손실함수(모델(X), y).아이템()\n"
        )
        namespace: dict[str, object] = {}
        exec(compile(translate(source).python, "<kopy-torch-smoke>", "exec"), namespace)
        self.assertGreater(float(namespace["초기손실"]), 0.0)
        self.assertLess(float(namespace["새손실"]), float(namespace["초기손실"]))


if __name__ == "__main__":
    unittest.main()
