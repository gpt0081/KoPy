import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class TorchGeometricPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("pytorch-geometric")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "torch_geometric")
        self.assertEqual(pack.kopy_module, "토치지오메트릭")

    def test_dotted_module_imports_translate(self):
        source = (
            "프롬 토치지오메트릭.data 임포트 데이터\n"
            "프롬 토치지오메트릭.nn 임포트 지씨엔컨브\n"
            "graph = 데이터(x=x, 엣지_인덱스=엣지_인덱스)\n"
            "conv = 지씨엔컨브(in_channels=8, out_channels=16)\n"
        )
        python_source = translate(source).python
        self.assertIn("from torch_geometric.data import Data", python_source)
        self.assertIn("from torch_geometric.nn import GCNConv", python_source)
        self.assertIn("graph = Data(x=x, edge_index=edge_index)", python_source)
        self.assertIn("conv = GCNConv(in_channels=8, out_channels=16)", python_source)

    def test_alias_attribute_translation(self):
        source = (
            "임포트 토치지오메트릭.nn 애즈 pyg_nn\n"
            "conv = pyg_nn.지에이티컨브(8, 4, heads=2)\n"
        )
        python_source = translate(source).python
        self.assertIn("import torch_geometric.nn as pyg_nn", python_source)
        self.assertIn("pyg_nn.GATConv(8, 4, heads=2)", python_source)

    def test_unimported_words_are_not_global(self):
        source = "conv = 지씨엔컨브(8, 16)\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy(self):
        source = (
            "from torch_geometric.data import Data\n"
            "from torch_geometric.nn import GCNConv\n"
            "graph = Data(x=x, edge_index=edge_index)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 토치지오메트릭.data 임포트 데이터", kopy)
        self.assertIn("프롬 토치지오메트릭.nn 임포트 지씨엔컨브", kopy)
        self.assertIn("graph = 데이터(x=x, 엣지_인덱스=엣지_인덱스)", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("토치지오메트릭.지씨엔컨브")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "GCNConv")

    def test_generic_keywords_remain_python(self):
        source = (
            "프롬 토치지오메트릭.nn 임포트 지씨엔컨브\n"
            "conv = 지씨엔컨브(in_channels=8, out_channels=16, add_self_loops=True)\n"
        )
        python_source = translate(source).python
        for token in ("in_channels=", "out_channels=", "add_self_loops="):
            self.assertIn(token, python_source)


if __name__ == "__main__":
    unittest.main()
