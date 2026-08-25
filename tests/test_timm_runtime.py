import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("timm"), "timm is not installed")
class TimmRuntimeTests(unittest.TestCase):
    def test_real_timm_model_discovery_creation_and_forward(self):
        source = (
            "임포트 토치\n"
            "임포트 팀엠\n"
            "model_names = 팀엠.리스트모델즈('resnet18')\n"
            "model = 팀엠.크리에이트모델('resnet18', pretrained=False, num_classes=10)\n"
            "model.eval()\n"
            "x = 토치.랜든((1, 3, 64, 64))\n"
            "위드 토치.노그라드():\n"
            "    features = model.포워드피처스(x)\n"
            "    logits = model(x)\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)

        self.assertIn("resnet18", namespace["model_names"])
        self.assertEqual(namespace["model"].get_classifier().out_features, 10)
        self.assertEqual(tuple(namespace["logits"].shape), (1, 10))
        self.assertEqual(namespace["features"].ndim, 4)
        self.assertEqual(namespace["features"].shape[0], 1)


if __name__ == "__main__":
    unittest.main()
