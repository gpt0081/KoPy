import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("einops"), "einops is not installed")
class EinopsRuntimeTests(unittest.TestCase):
    def test_real_einops_tensor_transformations(self):
        source = (
            "임포트 넘파이 애즈 np\n"
            "프롬 에이놉스 임포트 리어레인지, 리듀스, 리피트, 팩, 언팩, 파스셰이프\n"
            "x = np.에이레인지(24, dtype=np.플로트64).리셰이프(2, 3, 4)\n"
            "reordered = 리어레인지(x, 'b h w -> b w h')\n"
            "pooled = 리듀스(x, 'b h w -> b h', 'mean')\n"
            "repeated = 리피트(np.어레이([1, 2, 3]), 'c -> b c', b=2)\n"
            "left = np.원즈((2, 3))\n"
            "right = np.제로즈((2, 5))\n"
            "packed, packed_shapes = 팩([left, right], 'b *')\n"
            "unpacked = 언팩(packed, packed_shapes, 'b *')\n"
            "shape_info = 파스셰이프(x, 'batch height width')\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)

        import numpy as np

        self.assertEqual(namespace["reordered"].shape, (2, 4, 3))
        np.testing.assert_allclose(namespace["reordered"], np.transpose(namespace["x"], (0, 2, 1)))
        self.assertEqual(namespace["pooled"].shape, (2, 3))
        np.testing.assert_allclose(namespace["pooled"], namespace["x"].mean(axis=2))
        np.testing.assert_array_equal(namespace["repeated"], np.array([[1, 2, 3], [1, 2, 3]]))
        self.assertEqual(namespace["packed"].shape, (2, 8))
        np.testing.assert_array_equal(namespace["unpacked"][0], namespace["left"])
        np.testing.assert_array_equal(namespace["unpacked"][1], namespace["right"])
        self.assertEqual(namespace["shape_info"], {"batch": 2, "height": 3, "width": 4})


if __name__ == "__main__":
    unittest.main()
