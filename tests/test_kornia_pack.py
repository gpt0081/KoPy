import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class KorniaPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("kornia")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "kornia")
        self.assertEqual(pack.kopy_module, "코르니아")

    def test_namespace_scoped_translation(self):
        source = (
            "임포트 코르니아\n"
            "gray = 코르니아.컬러.알지비투그레이스케일(image)\n"
            "blurred = 코르니아.필터즈.가우시안블러투디(gray, (3, 3), (1.5, 1.5))\n"
        )
        python_source = translate(source).python
        self.assertIn("import kornia", python_source)
        self.assertIn("kornia.color.rgb_to_grayscale(image)", python_source)
        self.assertIn("kornia.filters.gaussian_blur2d(gray, (3, 3), (1.5, 1.5))", python_source)

    def test_alias_and_augmentation_translation(self):
        source = (
            "임포트 코르니아 애즈 K\n"
            "aug = K.어그멘테이션.어그멘테이션시퀀셜(\n"
            "    K.어그멘테이션.랜덤호리즌털플립(p=1.0)\n"
            ")\n"
        )
        python_source = translate(source).python
        self.assertIn("import kornia as K", python_source)
        self.assertIn("K.augmentation.AugmentationSequential", python_source)
        self.assertIn("K.augmentation.RandomHorizontalFlip(p=1.0)", python_source)

    def test_unimported_words_are_not_global(self):
        source = "gray = 알지비투그레이스케일(image)\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy(self):
        source = (
            "import kornia\n"
            "gray = kornia.color.rgb_to_grayscale(image)\n"
            "edges = kornia.filters.sobel(gray)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 코르니아", kopy)
        self.assertIn("코르니아.컬러.알지비투그레이스케일", kopy)
        self.assertIn("코르니아.필터즈.소벨", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("코르니아.가우시안블러투디")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "gaussian_blur2d")

    def test_keyword_arguments_remain_python_spelling(self):
        source = (
            "임포트 코르니아 애즈 K\n"
            "aug = K.어그멘테이션.랜덤어파인(degrees=15.0, p=0.5, same_on_batch=True, keepdim=True)\n"
        )
        python_source = translate(source).python
        for keyword in ("degrees=15.0", "p=0.5", "same_on_batch=True", "keepdim=True"):
            self.assertIn(keyword, python_source)


if __name__ == "__main__":
    unittest.main()
