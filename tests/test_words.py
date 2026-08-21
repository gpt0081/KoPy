import builtins
import keyword
import unittest

from kopy.words import PY_TO_KO, WORDS, info_for


class WordRegistryTests(unittest.TestCase):
    def test_all_python_keywords_have_kopy_mapping(self):
        required = set(keyword.kwlist) | set(getattr(keyword, "softkwlist", ()))
        required.discard("_")
        missing = sorted(required - set(PY_TO_KO))
        self.assertEqual(missing, [], f"missing keyword mappings: {missing}")

    def test_all_public_builtins_have_kopy_mapping(self):
        required = {name for name in dir(builtins) if not name.startswith("_") and name.isidentifier()}
        missing = sorted(required - set(PY_TO_KO))
        self.assertEqual(missing, [], f"missing builtin mappings: {missing}")

    def test_reverse_mapping_is_unambiguous(self):
        self.assertEqual(len(PY_TO_KO), len(set(WORDS.values())))

    def test_every_word_has_teaching_metadata(self):
        for word in WORDS:
            with self.subTest(word=word):
                info = info_for(word)
                self.assertIsNotNone(info)
                assert info is not None
                self.assertTrue(info.description)


if __name__ == "__main__":
    unittest.main()
