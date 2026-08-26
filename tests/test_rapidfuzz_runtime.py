import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("rapidfuzz"), "rapidfuzz is not installed")
class RapidFuzzRuntimeTests(unittest.TestCase):
    def test_real_fuzzy_match_and_extract_one(self):
        source = (
            "프롬 래피드퍼즈 임포트 fuzz, process\n"
            "query = 'KoPy Python'\n"
            "choices = ['KoPy Python learning', 'Rubber chemistry', 'Python machine learning']\n"
            "direct_score = fuzz.더블유레이쇼(query, choices[0])\n"
            "best = process.익스트랙트원(query, choices, scorer=fuzz.더블유레이쇼)\n"
            "token_score = fuzz.토큰셋레이쇼('python kopy', 'KoPy Python')\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)

        direct_score = float(namespace["direct_score"])
        best = namespace["best"]
        token_score = float(namespace["token_score"])

        self.assertGreater(direct_score, 80.0)
        self.assertEqual(best[0], "KoPy Python learning")
        self.assertGreater(float(best[1]), 80.0)
        self.assertEqual(best[2], 0)
        self.assertGreater(token_score, 90.0)


if __name__ == "__main__":
    unittest.main()
