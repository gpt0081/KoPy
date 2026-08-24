import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class SentencePiecePackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("sentencepiece")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.kopy_module, "센텐스피스")
        self.assertIn("spm", pack.preferred_aliases)

    def test_processor_translation_is_namespace_scoped(self):
        source = (
            "임포트 센텐스피스 애즈 spm\n"
            "토크나이저 = spm.센텐스피스프로세서(model_file='m.model')\n"
            "피시들 = 토크나이저.엔코드('hello world', out_type=str)\n"
            "복원 = 토크나이저.디코드(피시들)\n"
        )
        python_source = translate(source).python
        self.assertIn("import sentencepiece as spm", python_source)
        self.assertIn("spm.SentencePieceProcessor(model_file='m.model')", python_source)
        self.assertIn("토크나이저.encode('hello world', out_type=str)", python_source)
        self.assertIn("토크나이저.decode(피시들)", python_source)

    def test_trainer_translation(self):
        source = (
            "임포트 센텐스피스 애즈 spm\n"
            "spm.센텐스피스트레이너.트레인(input='corpus.txt', model_prefix='m', vocab_size=32)\n"
        )
        python_source = translate(source).python
        self.assertIn("spm.SentencePieceTrainer.train(", python_source)
        self.assertIn("vocab_size=32", python_source)

    def test_unimported_sentencepiece_word_is_not_global(self):
        source = "피시들 = 토크나이저.엔코드('hello')\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy(self):
        source = (
            "import sentencepiece as spm\n"
            "processor = spm.SentencePieceProcessor(model_file='m.model')\n"
            "pieces = processor.encode('hello', out_type=str)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 센텐스피스 애즈 spm", kopy)
        self.assertIn("spm.센텐스피스프로세서", kopy)
        self.assertIn("processor.엔코드", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("센텐스피스.센텐스피스프로세서")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "SentencePieceProcessor")


if __name__ == "__main__":
    unittest.main()
