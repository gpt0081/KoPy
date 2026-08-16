import unittest

from kopy.spelling import find_spelling_hints


class SpellingTests(unittest.TestCase):
    def test_transposed_builtin_is_suggested(self):
        hints = find_spelling_hints('pritn("hello")\n')
        self.assertTrue(any(h.suggestion == "print" for h in hints))

    def test_transposed_keyword_is_suggested(self):
        hints = find_spelling_hints("retrun 1\n")
        self.assertTrue(any(h.suggestion == "return" for h in hints))

    def test_assignment_is_not_treated_as_builtin_call(self):
        hints = find_spelling_hints("pritn = 10\n")
        self.assertFalse(any(h.found == "pritn" for h in hints))


if __name__ == "__main__":
    unittest.main()
