import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("tokenizers"), "Tokenizers is not installed")
class TokenizersRuntimeTests(unittest.TestCase):
    def test_kopy_tokenizers_wordpiece_encode_executes_offline(self):
        source = (
            "프롬 토크나이저스 임포트 토크나이저\n"
            "프롬 토크나이저스.models 임포트 워드피스\n"
            "프롬 토크나이저스.pre_tokenizers 임포트 화이트스페이스\n"
            "모델 = 워드피스(vocab={'[UNK]': 0, 'hello': 1, 'world': 2}, unk_token='[UNK]')\n"
            "토크 = 토크나이저(모델)\n"
            "토크.pre_tokenizer = 화이트스페이스()\n"
            "결과 = 토크.엔코드('hello world')\n"
            "아이디들 = 결과.아이디스\n"
            "토큰들 = 결과.토큰스\n"
            "보캡크기 = 토크.겟보캡사이즈()\n"
        )
        namespace: dict[str, object] = {}
        exec(compile(translate(source).python, "<kopy-tokenizers-smoke>", "exec"), namespace)
        self.assertEqual(namespace["아이디들"], [1, 2])
        self.assertEqual(namespace["토큰들"], ["hello", "world"])
        self.assertEqual(namespace["보캡크기"], 3)


if __name__ == "__main__":
    unittest.main()
