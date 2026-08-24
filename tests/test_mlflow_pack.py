import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class MLflowPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("mlflow")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.kopy_module, "엠엘플로우")
        self.assertIn("mlf", pack.preferred_aliases)

    def test_tracking_translation_is_namespace_scoped(self):
        source = (
            "임포트 엠엘플로우 애즈 mlf\n"
            "mlf.셋익스페리먼트('demo')\n"
            "위드 mlf.스타트런() 애즈 실행:\n"
            "    mlf.로그파람('lr', 0.01)\n"
            "    mlf.로그메트릭('loss', 0.25)\n"
            "    mlf.셋태그('stage', 'test')\n"
        )
        python_source = translate(source).python
        self.assertIn("import mlflow as mlf", python_source)
        self.assertIn("mlf.set_experiment('demo')", python_source)
        self.assertIn("with mlf.start_run() as 실행:", python_source)
        self.assertIn("mlf.log_param('lr', 0.01)", python_source)
        self.assertIn("mlf.log_metric('loss', 0.25)", python_source)
        self.assertIn("mlf.set_tag('stage', 'test')", python_source)

    def test_run_object_attributes_translate_when_pack_is_active(self):
        source = (
            "임포트 엠엘플로우\n"
            "실행 = 엠엘플로우.스타트런()\n"
            "식별자 = 실행.인포.런아이디\n"
            "엠엘플로우.엔드런()\n"
        )
        python_source = translate(source).python
        self.assertIn("mlflow.start_run()", python_source)
        self.assertIn("실행.info.run_id", python_source)
        self.assertIn("mlflow.end_run()", python_source)

    def test_unimported_mlflow_word_is_not_global(self):
        source = "로그메트릭('loss', 0.5)\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy(self):
        source = (
            "import mlflow as mlf\n"
            "with mlf.start_run() as run:\n"
            "    mlf.log_metric('score', 0.9)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 엠엘플로우 애즈 mlf", kopy)
        self.assertIn("mlf.스타트런()", kopy)
        self.assertIn("mlf.로그메트릭('score', 0.9)", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("엠엘플로우.스타트런")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "start_run")


if __name__ == "__main__":
    unittest.main()
