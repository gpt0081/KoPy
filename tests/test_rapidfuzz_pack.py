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
            "프롬 래피드퍼즈 임포트 퍼즈, 프로세스\n"
            "리절트 = 퍼즈.더블유레이쇼(쿼리, 캔디데이트)\n"
            "베스트 = 프로세스.익스트랙트원(쿼리, 초이시즈, 스코어러=퍼즈.더블유레이쇼)\n"
        )
        python_source = translate(source).python
        self.assertIn("from rapidfuzz import fuzz, process", python_source)
        self.assertIn("result = fuzz.WRatio(query, candidate)", python_source)
        self.assertIn("best = process.extractOne(query, choices, scorer=fuzz.WRatio)", python_source)

    def test_python_spellings_remain_accepted(self):
        source = (
            "프롬 래피드퍼즈 임포트 퍼즈, 프로세스\n"
            "query = 'kopy python'\n"
            "choices = ['KoPy Python', 'rubber chemistry']\n"
            "result = 프로세스.익스트랙트원(query, choices, scorer=퍼즈.레이쇼, score_cutoff=50)\n"
        )
        python_source = translate(source).python
        self.assertIn("query =", python_source)
        self.assertIn("choices =", python_source)
        self.assertIn("scorer=fuzz.ratio", python_source)
        self.assertIn("score_cutoff=50", python_source)

    def test_unimported_words_are_not_global(self):
        source = "리절트 = fuzz.더블유레이쇼(쿼리, 캔디데이트)\n"
        translated = translate(source).python
        self.assertIn("fuzz.더블유레이쇼", translated)
        self.assertIn("result =", translated)
        self.assertIn("query, candidate", translated)

    def test_python_to_kopy_transliterates_common_search_identifiers(self):
        source = (
            "from rapidfuzz import fuzz, process\n"
            "result = fuzz.token_set_ratio(query, candidate)\n"
            "best = process.extractOne(query, choices, scorer=fuzz.WRatio, score_cutoff=50)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 래피드퍼즈 임포트 퍼즈, 프로세스", kopy)
        self.assertIn("리절트 = 퍼즈.토큰셋레이쇼(쿼리, 캔디데이트)", kopy)
        self.assertIn("베스트 = 프로세스.익스트랙트원(쿼리, 초이시즈, 스코어러=퍼즈.더블유레이쇼, 스코어_컷오프=50)", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("래피드퍼즈.익스트랙트원")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "extractOne")


if __name__ == "__main__":
    unittest.main()
