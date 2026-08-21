import unittest

from kopy.packs.registry import pack_by_name, packs_payload, resolve_pack_member
from kopy.translator import to_kopy, translate


class LibraryPackTests(unittest.TestCase):
    def test_numpy_pack_is_registered(self):
        pack = pack_by_name("numpy")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.kopy_module, "넘파이")
        self.assertGreater(len(pack.members), 50)

    def test_packs_payload_reports_numpy(self):
        payload = packs_payload()
        numpy_entries = [item for item in payload["packs"] if item["name"] == "numpy"]
        self.assertEqual(len(numpy_entries), 1)
        self.assertGreater(numpy_entries[0]["member_count"], 50)

    def test_numpy_alias_and_attributes_translate(self):
        source = (
            "임포트 넘파이 애즈 np\n"
            "x = np.어레이([1, 2, 3, 4])\n"
            "y = x.리셰이프(2, 2)\n"
            "크기 = np.린알지.노름(y)\n"
        )
        python = translate(source).python
        self.assertIn("import numpy as np", python)
        self.assertIn("np.array([1, 2, 3, 4])", python)
        self.assertIn("x.reshape(2, 2)", python)
        self.assertIn("np.linalg.norm(y)", python)

    def test_pack_words_do_not_become_global_without_import(self):
        source = "x = np.어레이([1, 2, 3])\n"
        self.assertEqual(source, translate(source).python)

    def test_from_import_translates_member_and_later_use(self):
        source = "프롬 넘파이 임포트 어레이\nx = 어레이([1, 2, 3])\n"
        python = translate(source).python
        self.assertIn("from numpy import array", python)
        self.assertIn("x = array([1, 2, 3])", python)

    def test_numpy_reverse_translation_round_trip(self):
        source = (
            "import numpy as np\n"
            "x = np.arange(6).reshape(2, 3)\n"
            "average = np.mean(x)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 넘파이 애즈 np", kopy)
        self.assertIn("np.에이레인지(6).리셰이프(2, 3)", kopy)
        self.assertIn("np.미인(x)", kopy)
        self.assertEqual(source, translate(kopy).python)

    def test_numpy_strings_and_comments_remain_untouched(self):
        source = (
            "임포트 넘파이 애즈 np\n"
            "text = 'np.어레이 넘파이'  # np.리셰이프 넘파이\n"
        )
        python = translate(source).python
        self.assertIn("'np.어레이 넘파이'", python)
        self.assertIn("# np.리셰이프 넘파이", python)

    def test_pack_help_resolution_accepts_alias_and_python_name(self):
        alias_match = resolve_pack_member("np.어레이")
        python_match = resolve_pack_member("numpy.array")
        self.assertIsNotNone(alias_match)
        self.assertIsNotNone(python_match)
        self.assertEqual(alias_match[1].python, "array")
        self.assertEqual(python_match[1].kopy, "어레이")


if __name__ == "__main__":
    unittest.main()
