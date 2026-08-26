import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class RapidFuzzPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("rapidfuzz")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "rapidfuzz")
        self.assertEqual(pack.kopy_module, "래피드퍼즈")

    def test_scorers_and_extractors_translate(self):
        source = (
            "프롬 래피드퍼즈 임포트 fuzz, process\n"
            "score = fuzz.더블유레이쇼(query, candidate)\n"
            "best = process.익스트랙트원(query, choices, scorer=fuzz.더블유레이쇼)\n"
        )
        python_source = translate(source).python
        self.assertIn("from rapidfuzz import fuzz, process", python_source)
        self.assertIn("fuzz.WRatio(query, candidate)", python_source)
        self.assertIn("process.extractOne(query, choices, scorer=fuzz.WRatio)", python_source)

    def test_transferable_search_vocabulary_stays_python(self):
        source = (
            "프롬 래피드퍼즈 임포트 fuzz, process\n"
            "query = 'kopy python'\n"
            "choices = ['KoPy Python', 'rubber chemistry']\n"
            "result = process.익스트랙트원(query, choices, scorer=fuzz.레이쇼, score_cutoff=50)\n"
        )
        python_source = translate(source).python
        self.assertIn("query =", python_source)
        self.assertIn("choices =", python_source)
        self.assertIn("scorer=fuzz.ratio", python_source)
        self.assertIn("score_cutoff=50", python_source)

    def test_unimported_words_are_not_global(self):
        source = "score = fuzz.더블유레이쇼(query, candidate)\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy_preserves_real_submodules(self):
        source = (
            "from rapidfuzz import fuzz, process\n"
            "score = fuzz.token_set_ratio(query, candidate)\n"
            "best = process.extractOne(query, choices, scorer=fuzz.WRatio)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 래피드퍼즈 임포트 fuzz, process", kopy)
        self.assertIn("fuzz.토큰셋레이쇼(query, candidate)", kopy)
        self.assertIn("process.익스트랙트원(query, choices, scorer=fuzz.더블유레이쇼)", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("래피드퍼즈.익스트랙트원")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "extractOne")


if __name__ == "__main__":
    unittest.main()
