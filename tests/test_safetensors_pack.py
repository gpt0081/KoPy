import unittest

from kopy.translator import to_kopy, translate


class SafetensorsPackTests(unittest.TestCase):
    def test_translate_torch_save_and_safe_open(self):
        source = (
            "프롬 세이프텐서스.torch 임포트 세이브파일, 로드파일\n"
            "프롬 세이프텐서스 임포트 세이프오픈\n"
            "세이브파일({'weight': 값}, 'model.safetensors')\n"
            "텐서들 = 로드파일('model.safetensors')\n"
            "위드 세이프오픈('model.safetensors', framework='pt', device='cpu') 애즈 f:\n"
            "    이름들 = 리스트(f.키즈())\n"
            "    가중치 = f.겟텐서('weight')\n"
        )
        result = translate(source).python
        self.assertIn("from safetensors.torch import save_file, load_file", result)
        self.assertIn("from safetensors import safe_open", result)
        self.assertIn("save_file({'weight': 값}", result)
        self.assertIn("load_file('model.safetensors')", result)
        self.assertIn("with safe_open('model.safetensors'", result)
        self.assertIn("f.keys()", result)
        self.assertIn("f.get_tensor('weight')", result)

    def test_reverse_translate_safetensors_api(self):
        source = (
            "from safetensors.torch import save_file, load_file\n"
            "from safetensors import safe_open\n"
            "save_file({'weight': value}, 'model.safetensors')\n"
            "tensors = load_file('model.safetensors')\n"
            "with safe_open('model.safetensors', framework='pt', device='cpu') as f:\n"
            "    names = list(f.keys())\n"
            "    weight = f.get_tensor('weight')\n"
        )
        result = to_kopy(source).kopy
        self.assertIn("프롬 세이프텐서스.torch 임포트 세이브파일, 로드파일", result)
        self.assertIn("프롬 세이프텐서스 임포트 세이프오픈", result)
        self.assertIn("f.키즈()", result)
        self.assertIn("f.겟텐서('weight')", result)


if __name__ == "__main__":
    unittest.main()
