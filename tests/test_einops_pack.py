import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class EinopsPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("einops")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "einops")
        self.assertEqual(pack.kopy_module, "에이놉스")

    def test_module_translation_is_namespace_scoped(self):
        source = (
            "임포트 에이놉스\n"
            "images = 에이놉스.리어레인지(images, 'b h w c -> b c h w')\n"
            "pooled = 에이놉스.리듀스(images, 'b c h w -> b c', 'mean')\n"
            "batch = 에이놉스.리피트(vector, 'c -> b c', b=8)\n"
        )
        python_source = translate(source).python
        self.assertIn("import einops", python_source)
        self.assertIn("einops.rearrange(images, 'b h w c -> b c h w')", python_source)
        self.assertIn("einops.reduce(images, 'b c h w -> b c', 'mean')", python_source)
        self.assertIn("einops.repeat(vector, 'c -> b c', b=8)", python_source)

    def test_from_import_translation(self):
        source = (
            "프롬 에이놉스 임포트 리어레인지, 리듀스, 리피트\n"
            "x = 리어레인지(x, 'b h w -> b w h')\n"
            "y = 리듀스(x, 'b w h -> b w', 'mean')\n"
            "z = 리피트(y, 'b w -> b c w', c=3)\n"
        )
        python_source = translate(source).python
        self.assertIn("from einops import rearrange, reduce, repeat", python_source)
        self.assertIn("rearrange(x, 'b h w -> b w h')", python_source)
        self.assertIn("reduce(x, 'b w h -> b w', 'mean')", python_source)
        self.assertIn("repeat(y, 'b w -> b c w', c=3)", python_source)

    def test_unimported_words_are_not_global(self):
        source = "x = 리어레인지(x, 'b h w -> b w h')\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy(self):
        source = (
            "import einops\n"
            "images = einops.rearrange(images, 'b h w c -> b c h w')\n"
            "pooled = einops.reduce(images, 'b c h w -> b c', 'mean')\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 에이놉스", kopy)
        self.assertIn("에이놉스.리어레인지", kopy)
        self.assertIn("에이놉스.리듀스", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("에이놉스.리어레인지")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "rearrange")

    def test_pattern_and_axis_names_remain_standard(self):
        source = (
            "프롬 에이놉스 임포트 리피트\n"
            "batch = 리피트(vector, 'channels -> batch channels', batch=4)\n"
        )
        python_source = translate(source).python
        self.assertIn("'channels -> batch channels'", python_source)
        self.assertIn("batch=4", python_source)


if __name__ == "__main__":
    unittest.main()
