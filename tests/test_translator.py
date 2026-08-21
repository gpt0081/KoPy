import unittest

from kopy.translator import to_kopy, translate


class TranslatorTests(unittest.TestCase):
    def test_mixed_kopy_and_python(self):
        source = "포 x 인 range(3):\n    프린트(x)\n"
        result = translate(source)
        self.assertIn("for x in range(3):", result.python)
        self.assertIn("print(x)", result.python)

    def test_strings_and_comments_are_not_translated(self):
        source = '프린트("이프 프린트")  # 이프 프린트\n'
        result = translate(source)
        self.assertIn('print("이프 프린트")', result.python)
        self.assertIn("# 이프 프린트", result.python)

    def test_plain_python_stays_python(self):
        source = "for x in range(3):\n    print(x)\n"
        result = translate(source)
        self.assertEqual(source, result.python)
        self.assertEqual((), result.replacements)

    def test_python_to_kopy_is_token_safe(self):
        source = 'for x in range(3):\n    print("for print")  # for print\n'
        result = to_kopy(source)
        self.assertIn("포 x 인 레인지(3):", result.kopy)
        self.assertIn('프린트("for print")', result.kopy)
        self.assertIn("# for print", result.kopy)

    def test_round_trip_registered_names(self):
        source = "for x in range(3):\n    print(len([x]))\n"
        kopy = to_kopy(source).kopy
        restored = translate(kopy).python
        self.assertEqual(source, restored)


if __name__ == "__main__":
    unittest.main()
