import unittest

from kopy.translator import to_kopy, translate


class AcceleratePackTests(unittest.TestCase):
    def test_translate_accelerate_training_api(self):
        source = (
            "프롬 액셀러레이트 임포트 액셀러레이터\n"
            "가속기 = 액셀러레이터()\n"
            "모델, 옵티마이저 = 가속기.프리페어(모델, 옵티마이저)\n"
            "가속기.백워드(손실)\n"
        )
        result = translate(source).python
        self.assertIn("from accelerate import Accelerator", result)
        self.assertIn("가속기 = Accelerator()", result)
        self.assertIn("model, 옵티마이저 = 가속기.prepare(model, 옵티마이저)", result)
        self.assertIn("가속기.backward(손실)", result)

    def test_reverse_translate_accelerate_api(self):
        source = (
            "from accelerate import Accelerator\n"
            "accelerator = Accelerator()\n"
            "model = accelerator.unwrap_model(model)\n"
        )
        result = to_kopy(source).kopy
        self.assertIn("프롬 액셀러레이트 임포트 액셀러레이터", result)
        self.assertIn("모델 = accelerator.언랩모델(모델)", result)


if __name__ == "__main__":
    unittest.main()
