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
            "model = tv.모델즈.레스넷18(weights=None)\n"
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

    def test_python_to_kopy(self):
        source = (
            "import torchvision as tv\n"
            "transform = tv.transforms.Compose([tv.transforms.Resize((32, 32))])\n"
            "model = tv.models.resnet18(weights=None)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 토치비전 애즈 tv", kopy)
        self.assertIn("tv.트랜스폼즈.컴포즈", kopy)
        self.assertIn("tv.트랜스폼즈.리사이즈", kopy)
        self.assertIn("tv.모델즈.레스넷18", kopy)

    def test_detection_ops_translate_in_active_namespace(self):
        source = (
            "임포트 토치비전 애즈 tv\n"
            "iou = tv.옵스.박스아이오유(boxes1, boxes2)\n"
            "keep = tv.옵스.엔엠에스(boxes, scores, 0.5)\n"
        )
        python_source = translate(source).python
        self.assertIn("tv.ops.box_iou(boxes1, boxes2)", python_source)
        self.assertIn("tv.ops.nms(boxes, scores, 0.5)", python_source)

    def test_help_resolution(self):
        resolved = resolve_pack_member("토치비전.레스넷18")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "resnet18")

    def test_keyword_arguments_remain_python_spelling(self):
        source = (
            "임포트 토치비전 애즈 tv\n"
            "transform = tv.트랜스폼즈.노멀라이즈(mean=[0.5], std=[0.5], inplace=False)\n"
            "model = tv.모델즈.레스넷18(weights=None, progress=True, num_classes=10)\n"
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
