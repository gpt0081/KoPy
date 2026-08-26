import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("kornia"), "kornia is not installed")
class KorniaRuntimeTests(unittest.TestCase):
    def test_real_kornia_color_filter_geometry_and_augmentation(self):
        source = (
            "임포트 토치\n"
            "임포트 코르니아 애즈 K\n"
            "image = 토치.에이레인지(0, 48, dtype=토치.플로트32).리셰이프(1, 3, 4, 4) / 47.0\n"
            "gray = K.컬러.알지비투그레이스케일(image)\n"
            "blurred = K.필터즈.가우시안블러2디(gray, (3, 3), (1.0, 1.0))\n"
            "resized = K.지오메트리.트랜스폼.리사이즈(blurred, (8, 8))\n"
            "aug = K.어그멘테이션.어그멘테이션시퀀셜(K.어그멘테이션.랜덤호리즌털플립(p=1.0))\n"
            "flipped = aug(resized)\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)

        self.assertEqual(tuple(namespace["gray"].shape), (1, 1, 4, 4))
        self.assertEqual(tuple(namespace["blurred"].shape), (1, 1, 4, 4))
        self.assertEqual(tuple(namespace["resized"].shape), (1, 1, 8, 8))
        self.assertEqual(tuple(namespace["flipped"].shape), (1, 1, 8, 8))

        torch = namespace["torch"]
        expected = torch.flip(namespace["resized"], dims=[-1])
        self.assertTrue(torch.allclose(namespace["flipped"], expected))


if __name__ == "__main__":
    unittest.main()
