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
            "모델_네임즈 = 팀엠.리스트_모델즈('resnet*')\n"
            "모델 = 팀엠.크리에이트_모델('resnet18', pretrained=False, num_classes=10)\n"
            "피처스 = 모델.포워드_피처스(엑스)\n"
        )
        python_source = translate(source).python
        self.assertIn("import timm", python_source)
        self.assertIn("timm.list_models('resnet*')", python_source)
        self.assertIn("model = timm.create_model('resnet18', pretrained=False, num_classes=10)", python_source)
        self.assertIn("features = model.forward_features(X)", python_source)

    def test_alias_translation(self):
        source = (
            "임포트 팀엠 애즈 tm\n"
            "모델 = tm.크리에이트_모델('resnet18', pretrained=False)\n"
            "config = tm.데이터.리졸브_데이터_컨피그(모델.pretrained_cfg, model=모델)\n"
        )
        python_source = translate(source).python
        self.assertIn("import timm as tm", python_source)
        self.assertIn("model = tm.create_model('resnet18', pretrained=False)", python_source)
        self.assertIn("tm.data.resolve_data_config", python_source)
        self.assertIn("model=model", python_source)

    def test_unimported_pack_word_is_not_global(self):
        source = "모델 = 크리에이트_모델('resnet18')\n"
        self.assertEqual(translate(source).python, "model = 크리에이트_모델('resnet18')\n")

    def test_python_to_kopy_prefers_canonical_underscores_and_digits(self):
        source = (
            "import timm\n"
            "model_names = timm.list_models('resnet*')\n"
            "model = timm.create_model('resnet18', pretrained=False)\n"
            "features = model.forward_features(X)\n"
            "kwargs = timm.optim.optimizer_kwargs(cfg={})\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 팀엠", kopy)
        self.assertIn("팀엠.리스트_모델즈", kopy)
        self.assertIn("모델 = 팀엠.크리에이트_모델", kopy)
        self.assertIn("피처스 = 모델.포워드_피처스", kopy)
        self.assertIn("옵티마이저_콰그스", kopy)

    def test_numeric_fragments_are_not_spelled_out(self):
        source = (
            "import timm\n"
            "optimizer = timm.optim.create_optimizer_v2(model)\n"
            "scheduler = timm.scheduler.create_scheduler_v2(args, optimizer)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("크리에이트_옵티마이저_브이2", kopy)
        self.assertIn("크리에이트_스케줄러_브이2", kopy)
        self.assertNotIn("브이투", kopy)

    def test_legacy_aliases_still_translate(self):
        source = (
            "임포트 팀엠\n"
            "모델 = 팀엠.크리에이트모델('resnet18')\n"
            "피처스 = 모델.포워드피처스(엑스)\n"
            "옵티마이저 = 팀엠.옵팀.크리에이트옵티마이저브이투(모델)\n"
        )
        python_source = translate(source).python
        self.assertIn("timm.create_model('resnet18')", python_source)
        self.assertIn("model.forward_features(X)", python_source)
        self.assertIn("timm.optim.create_optimizer_v2(model)", python_source)

    def test_help_resolution(self):
        resolved = resolve_pack_member("팀엠.크리에이트_모델")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "create_model")

    def test_unaudited_keyword_arguments_are_not_declared_permanent_exceptions(self):
        source = (
            "임포트 팀엠\n"
            "모델 = 팀엠.크리에이트_모델('resnet18', pretrained=False, num_classes=10, "
            "in_chans=3, features_only=False)\n"
        )
        python_source = translate(source).python
        self.assertIn("pretrained=False", python_source)
        self.assertIn("num_classes=10", python_source)
        self.assertIn("in_chans=3", python_source)
        self.assertIn("features_only=False", python_source)


if __name__ == "__main__":
    unittest.main()
