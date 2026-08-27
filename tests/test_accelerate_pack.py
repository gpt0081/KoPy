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

    def test_canonical_underscore_spellings_translate_to_python(self):
        source = (
            "임포트 액셀러레이트 애즈 acc\n"
            "모델 = acc.프리페어_모델(모델)\n"
            "리절츠 = acc.개더_포_메트릭스(피처스)\n"
            "모델 = acc.언랩_모델(모델)\n"
            "acc.웨이트_포_에브리원()\n"
            "acc.세이브_스테이트()\n"
            "acc.셋_시드(42)\n"
        )
        result = translate(source).python
        self.assertIn("model = acc.prepare_model(model)", result)
        self.assertIn("results = acc.gather_for_metrics(features)", result)
        self.assertIn("model = acc.unwrap_model(model)", result)
        self.assertIn("acc.wait_for_everyone()", result)
        self.assertIn("acc.save_state()", result)
        self.assertIn("acc.set_seed(42)", result)

    def test_reverse_translate_accelerate_api_prefers_canonical_spellings(self):
        source = (
            "import accelerate as acc\n"
            "model = acc.unwrap_model(model)\n"
            "results = acc.gather_for_metrics(features)\n"
            "acc.wait_for_everyone()\n"
            "acc.load_checkpoint_and_dispatch()\n"
        )
        result = to_kopy(source).kopy
        self.assertIn("임포트 액셀러레이트 애즈 acc", result)
        self.assertIn("모델 = acc.언랩_모델(모델)", result)
        self.assertIn("리절츠 = acc.개더_포_메트릭스(피처스)", result)
        self.assertIn("acc.웨이트_포_에브리원()", result)
        self.assertIn("acc.로드_체크포인트_앤드_디스패치()", result)

    def test_legacy_compact_spellings_remain_input_compatible(self):
        source = (
            "임포트 액셀러레이트 애즈 acc\n"
            "모델 = acc.언랩모델(모델)\n"
            "리절츠 = acc.개더포메트릭스(피처스)\n"
            "acc.웨이트포에브리원()\n"
            "acc.셋시드(7)\n"
        )
        result = translate(source).python
        self.assertIn("model = acc.unwrap_model(model)", result)
        self.assertIn("results = acc.gather_for_metrics(features)", result)
        self.assertIn("acc.wait_for_everyone()", result)
        self.assertIn("acc.set_seed(7)", result)

    def test_accelerate_members_remain_namespace_scoped(self):
        source = "언랩_모델 = 1\n개더_포_메트릭스 = 2\n"
        self.assertEqual(translate(source).python, source)


if __name__ == "__main__":
    unittest.main()
