import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class OptimumPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("optimum")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.kopy_module, "옵티멈")

    def test_tasks_manager_translation_is_namespace_scoped(self):
        source = (
            "프롬 옵티멈.exporters.tasks 임포트 태스크매니저\n"
            "태스크들 = 태스크매니저.겟올태스크스()\n"
            "클래스 = 태스크매니저.겟모델클래스포태스크('text-classification')\n"
        )
        python_source = translate(source).python
        self.assertIn("from optimum.exporters.tasks import TasksManager", python_source)
        self.assertIn("TasksManager.get_all_tasks()", python_source)
        self.assertIn("TasksManager.get_model_class_for_task('text-classification')", python_source)

    def test_unimported_optimum_word_is_not_global(self):
        source = "태스크들 = 태스크매니저.겟올태스크스()\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy(self):
        source = (
            "from optimum.exporters.tasks import TasksManager\n"
            "tasks = TasksManager.get_all_tasks()\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 옵티멈.exporters.tasks 임포트 태스크매니저", kopy)
        self.assertIn("태스크매니저.겟올태스크스()", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("옵티멈.태스크매니저")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "TasksManager")


if __name__ == "__main__":
    unittest.main()
