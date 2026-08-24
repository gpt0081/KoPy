import importlib.util
import tempfile
import unittest
from pathlib import Path

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("sentencepiece"), "SentencePiece is not installed")
class SentencePieceRuntimeTests(unittest.TestCase):
    def test_kopy_sentencepiece_train_encode_decode_executes(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            corpus = root / "corpus.txt"
            corpus.write_text(
                "hello world\n"
                "hello kopy world\n"
                "sentencepiece tokenization works\n"
                "kopy learns ai libraries\n" * 20,
                encoding="utf-8",
            )
            prefix = root / "tiny"

            source = (
                "임포트 센텐스피스 애즈 spm\n"
                f"spm.센텐스피스트레이너.트레인(input={str(corpus)!r}, model_prefix={str(prefix)!r}, vocab_size=32, hard_vocab_limit=False)\n"
                f"토크나이저 = spm.센텐스피스프로세서(model_file={str(prefix) + '.model'!r})\n"
                "피시들 = 토크나이저.엔코드('hello kopy world', out_type=str)\n"
                "아이디들 = 토크나이저.엔코드('hello kopy world', out_type=int)\n"
                "복원 = 토크나이저.디코드(아이디들)\n"
                "어휘크기 = 토크나이저.겟피스사이즈()\n"
                "첫피스 = 토크나이저.아이디투피스(0)\n"
                "첫아이디 = 토크나이저.피스토아이디(첫피스)\n"
            )
            namespace: dict[str, object] = {}
            python_source = translate(source).python
            exec(compile(python_source, "<kopy-sentencepiece-smoke>", "exec"), namespace)

            self.assertTrue(namespace["피시들"])
            self.assertTrue(namespace["아이디들"])
            self.assertEqual(namespace["복원"], "hello kopy world")
            self.assertGreater(namespace["어휘크기"], 0)
            self.assertEqual(namespace["첫아이디"], 0)
            self.assertTrue((root / "tiny.model").exists())
            self.assertTrue((root / "tiny.vocab").exists())


if __name__ == "__main__":
    unittest.main()
