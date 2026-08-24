import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("accelerate"), "Accelerate is not installed")
@unittest.skipUnless(importlib.util.find_spec("torch"), "PyTorch is not installed")
class AccelerateRuntimeTests(unittest.TestCase):
    def test_kopy_accelerate_cpu_training_step(self):
        source = (
            "프롬 액셀러레이트 임포트 액셀러레이터\n"
            "임포트 토치\n"
            "가속기 = 액셀러레이터(cpu=True)\n"
            "모델 = 토치.엔엔.리니어(1, 1)\n"
            "손실함수 = 토치.엔엔.엠에스이로스()\n"
            "옵티마이저 = 토치.옵팀.에스지디(모델.파라미터스(), lr=0.01)\n"
            "모델, 옵티마이저 = 가속기.프리페어(모델, 옵티마이저)\n"
            "입력값 = 토치.텐서([[1.0], [2.0]])\n"
            "목표값 = 토치.텐서([[2.0], [4.0]])\n"
            "출력값 = 모델(입력값)\n"
            "손실 = 손실함수(출력값, 목표값)\n"
            "옵티마이저.제로그라드()\n"
            "가속기.백워드(손실)\n"
            "옵티마이저.스텝()\n"
            "결과 = 손실.디태치().아이템()\n"
        )
        namespace: dict[str, object] = {}
        exec(compile(translate(source).python, "<kopy-accelerate-smoke>", "exec"), namespace)
        self.assertGreater(namespace["결과"], 0.0)


if __name__ == "__main__":
    unittest.main()
