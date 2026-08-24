import importlib.util
import tempfile
import unittest
from pathlib import Path

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("safetensors"), "Safetensors is not installed")
@unittest.skipUnless(importlib.util.find_spec("torch"), "PyTorch is not installed")
class SafetensorsRuntimeTests(unittest.TestCase):
    def test_kopy_safetensors_round_trip(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "tiny.safetensors"
            source = (
                "임포트 토치\n"
                "프롬 세이프텐서스.torch 임포트 세이브파일, 로드파일\n"
                "프롬 세이프텐서스 임포트 세이프오픈\n"
                f"경로 = {str(path)!r}\n"
                "원본 = 토치.텐서([[1.0, 2.0], [3.0, 4.0]])\n"
                "세이브파일({'weight': 원본}, 경로, metadata={'format': 'kopy-test'})\n"
                "불러온값 = 로드파일(경로)['weight']\n"
                "위드 세이프오픈(경로, framework='pt', device='cpu') 애즈 f:\n"
                "    이름들 = 리스트(f.키즈())\n"
                "    메타 = f.메타데이터()\n"
                "    직접값 = f.겟텐서('weight')\n"
                "같음1 = 토치.allclose(원본, 불러온값)\n"
                "같음2 = 토치.allclose(원본, 직접값)\n"
            )
            namespace: dict[str, object] = {}
            exec(compile(translate(source).python, "<kopy-safetensors-smoke>", "exec"), namespace)

            self.assertTrue(namespace["같음1"])
            self.assertTrue(namespace["같음2"])
            self.assertEqual(namespace["이름들"], ["weight"])
            self.assertEqual(namespace["메타"], {"format": "kopy-test"})


if __name__ == "__main__":
    unittest.main()
