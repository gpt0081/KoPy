import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("torchvision"), "TorchVision is not installed")
class TorchVisionRuntimeTests(unittest.TestCase):
    def test_real_torchvision_transforms_model_and_box_iou(self):
        source = (
            "임포트 토치\n"
            "임포트 토치비전 애즈 tv\n"
            "image = 토치.원즈((3, 8, 8), dtype=토치.플로트32)\n"
            "transform = tv.트랜스폼즈.컴포즈([\n"
            "    tv.트랜스폼즈.리사이즈((4, 4)),\n"
            "    tv.트랜스폼즈.노멀라이즈(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]),\n"
            "])\n"
            "output = transform(image)\n"
            "model = tv.모델즈.레스넷18(weights=None)\n"
            "boxes1 = 토치.텐서([[0.0, 0.0, 2.0, 2.0]])\n"
            "boxes2 = 토치.텐서([[1.0, 1.0, 3.0, 3.0]])\n"
            "iou = tv.옵스.박스아이오유(boxes1, boxes2)\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)

        self.assertEqual(tuple(namespace["output"].shape), (3, 4, 4))
        self.assertAlmostEqual(float(namespace["output"].abs().max()), 1.0, places=5)
        self.assertEqual(namespace["model"].fc.out_features, 1000)
        self.assertEqual(tuple(namespace["iou"].shape), (1, 1))
        self.assertAlmostEqual(float(namespace["iou"][0, 0]), 1.0 / 7.0, places=5)


if __name__ == "__main__":
    unittest.main()
