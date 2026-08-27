import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class TorchVisionPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("torchvision")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "torchvision")
        self.assertEqual(pack.kopy_module, "토치비전")

    def test_alias_translation_is_namespace_scoped(self):
        source = (
            "임포트 토치비전 애즈 tv\n"
            "transform = tv.트랜스폼즈.컴포즈([\n"
            "    tv.트랜스폼즈.리사이즈((224, 224)),\n"
            "    tv.트랜스폼즈.노멀라이즈(mean=[0.5] * 3, std=[0.5] * 3),\n"
            "])\n"
            "모델 = tv.모델즈.레스넷18(weights=None)\n"
        )
        python_source = translate(source).python
        self.assertIn("import torchvision as tv", python_source)
        self.assertIn("tv.transforms.Compose", python_source)
        self.assertIn("tv.transforms.Resize", python_source)
        self.assertIn("tv.transforms.Normalize", python_source)
        self.assertIn("tv.models.resnet18(weights=None)", python_source)

    def test_unimported_words_are_not_global(self):
        source = "transform = 컴포즈([리사이즈((32, 32))])\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy_uses_canonical_function_spellings(self):
        source = (
            "import torchvision as tv\n"
            "grid = tv.utils.make_grid(images)\n"
            "iou = tv.ops.box_iou(boxes1, boxes2)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 토치비전 애즈 tv", kopy)
        self.assertIn("tv.유틸즈.메이크_그리드", kopy)
        self.assertIn("tv.옵스.박스_아이오유", kopy)
        self.assertNotIn("메이크그리드", kopy)
        self.assertNotIn("박스아이오유", kopy)

    def test_model_names_preserve_digits_and_underscores(self):
        source = (
            "import torchvision as tv\n"
            "a = tv.models.mobilenet_v3_large(weights=None)\n"
            "b = tv.models.efficientnet_b0(weights=None)\n"
            "c = tv.models.vit_b_16(weights=None)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("tv.모델즈.모빌넷_브이3_라지", kopy)
        self.assertIn("tv.모델즈.이피션트넷_비0", kopy)
        self.assertIn("tv.모델즈.브이아이티_비_16", kopy)
        self.assertNotIn("모빌넷브이스리라지", kopy)
        self.assertNotIn("이피션트넷비제로", kopy)

    def test_legacy_compact_spellings_still_translate(self):
        source = (
            "임포트 토치비전 애즈 tv\n"
            "grid = tv.유틸즈.메이크그리드(images)\n"
            "iou = tv.옵스.박스아이오유(boxes1, boxes2)\n"
            "model = tv.모델즈.모빌넷브이스리라지(weights=None)\n"
        )
        python_source = translate(source).python
        self.assertIn("tv.utils.make_grid", python_source)
        self.assertIn("tv.ops.box_iou", python_source)
        self.assertIn("tv.models.mobilenet_v3_large", python_source)

    def test_help_resolution(self):
        resolved = resolve_pack_member("토치비전.레스넷18")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "resnet18")

    def test_unresolved_keyword_arguments_are_not_mislabeled_as_permanent_exceptions(self):
        source = (
            "임포트 토치비전 애즈 tv\n"
            "transform = tv.트랜스폼즈.노멀라이즈(mean=[0.5], std=[0.5], inplace=False)\n"
            "모델 = tv.모델즈.레스넷18(weights=None, progress=True, num_classes=10)\n"
        )
        python_source = translate(source).python
        self.assertIn("mean=[0.5]", python_source)
        self.assertIn("std=[0.5]", python_source)
        self.assertIn("inplace=False", python_source)
        self.assertIn("weights=None", python_source)
        self.assertIn("progress=True", python_source)
        self.assertIn("num_classes=10", python_source)


if __name__ == "__main__":
    unittest.main()
