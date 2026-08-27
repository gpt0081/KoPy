import unittest

from kopy.translator import to_kopy, translate


class TokenizersPackTests(unittest.TestCase):
    def test_tokenizers_from_import_and_methods_translate(self):
        source = (
            "프롬 토크나이저스 임포트 토크나이저\n"
            "프롬 토크나이저스.models 임포트 워드피스\n"
            "모델 = 워드피스(vocab={'[UNK]': 0, 'hello': 1}, unk_token='[UNK]')\n"
            "토크 = 토크나이저(모델)\n"
            "결과 = 토크.엔코드('hello')\n"
            "아이디 = 결과.아이디스\n"
        )
        python_source = translate(source).python
        self.assertIn("from tokenizers import Tokenizer", python_source)
        self.assertIn("from tokenizers.models import WordPiece", python_source)
        self.assertIn("model = WordPiece", python_source)
        self.assertIn("Tokenizer(model)", python_source)
        self.assertIn("토크.encode('hello')", python_source)
        self.assertIn("결과.ids", python_source)

    def test_tokenizers_words_do_not_become_global_without_import(self):
        source = "결과 = 토크.엔코드('hello')\n"
        self.assertEqual(source, translate(source).python)

    def test_python_to_kopy_round_trip_for_tokenizers(self):
        source = (
            "from tokenizers import Tokenizer\n"
            "from tokenizers.models import WordPiece\n"
            "model = WordPiece(vocab={'[UNK]': 0}, unk_token='[UNK]')\n"
            "tokenizer = Tokenizer(model)\n"
            "result = tokenizer.encode('hello')\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 토크나이저스 임포트 토크나이저", kopy)
        self.assertIn("프롬 토크나이저스.models 임포트 워드피스", kopy)
        self.assertIn("모델 = 워드피스", kopy)
        self.assertIn("토크나이저 = 토크나이저(모델)", kopy)
        self.assertIn("리절트 = 토크나이저.엔코드('hello')", kopy)
        self.assertEqual(source, translate(kopy).python)


if __name__ == "__main__":
    unittest.main()
