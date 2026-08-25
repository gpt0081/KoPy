import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class TimmPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("timm")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "timm")
        self.assertEqual(pack.kopy_module, "팀엠")

    def test_module_translation_is_namespace_scoped(self):
        source = (
            "임포트 팀엠\n"
            "model_names = 팀엠.리스트모델즈('resnet*')\n"
            "model = 팀엠.크리에이트모델('resnet18', pretrained=False, num_classes=10)\n"
            "features = model.포워드피처스(x)\n"
        )
        python_source = translate(source).python
        self.assertIn("import timm", python_source)
        self.assertIn("timm.list_models('resnet*')", python_source)
        self.assertIn("timm.create_model('resnet18', pretrained=False, num_classes=10)", python_source)
        self.assertIn("model.forward_features(x)", python_source)

    def test_alias_translation(self):
        source = (
            "임포트 팀엠 애즈 tm\n"
            "model = tm.크리에이트모델('resnet18', pretrained=False)\n"
            "config = tm.데이터.리졸브데이터컨피그(model.pretrained_cfg, model=model)\n"
        )
        python_source = translate(source).python
        self.assertIn("import timm as tm", python_source)
        self.assertIn("tm.create_model('resnet18', pretrained=False)", python_source)
        self.assertIn("tm.data.resolve_data_config", python_source)

    def test_unimported_words_are_not_global(self):
        source = "model = 크리에이트모델('resnet18')\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy(self):
        source = (
            "import timm\n"
            "model_names = timm.list_models('resnet*')\n"
            "model = timm.create_model('resnet18', pretrained=False)\n"
            "features = model.forward_features(x)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 팀엠", kopy)
        self.assertIn("팀엠.리스트모델즈", kopy)
        self.assertIn("팀엠.크리에이트모델", kopy)
        self.assertIn("model.포워드피처스", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("팀엠.크리에이트모델")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "create_model")

    def test_keyword_arguments_remain_python_spelling(self):
        source = (
            "임포트 팀엠\n"
            "model = 팀엠.크리에이트모델('resnet18', pretrained=False, num_classes=10, "
            "in_chans=3, features_only=False)\n"
        )
        python_source = translate(source).python
        self.assertIn("pretrained=False", python_source)
        self.assertIn("num_classes=10", python_source)
        self.assertIn("in_chans=3", python_source)
        self.assertIn("features_only=False", python_source)


if __name__ == "__main__":
    unittest.main()
