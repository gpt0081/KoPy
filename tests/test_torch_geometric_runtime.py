import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("torch_geometric"), "torch_geometric is not installed")
class TorchGeometricRuntimeTests(unittest.TestCase):
    def test_real_graph_data_gcn_and_pooling(self):
        source = (
            "임포트 토치\n"
            "프롬 토치지오메트릭.data 임포트 데이터\n"
            "프롬 토치지오메트릭.nn 임포트 지씨엔컨브, 글로벌미인풀\n"
            "프롬 토치지오메트릭.utils 임포트 투언디렉티드\n"
            "x = 토치.텐서([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]], dtype=토치.플로트32)\n"
            "edge_index = 토치.텐서([[0, 1], [1, 2]], dtype=토치.인트64)\n"
            "edge_index = 투언디렉티드(edge_index)\n"
            "graph = 데이터(x=x, edge_index=edge_index)\n"
            "conv = 지씨엔컨브(in_channels=2, out_channels=4)\n"
            "node_embeddings = conv(graph.x, graph.edge_index)\n"
            "batch = 토치.제로즈(graph.num_nodes, dtype=토치.인트64)\n"
            "graph_embedding = 글로벌미인풀(node_embeddings, batch)\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)

        graph = namespace["graph"]
        self.assertEqual(graph.num_nodes, 3)
        self.assertEqual(tuple(graph.edge_index.shape), (2, 4))
        self.assertEqual(tuple(namespace["node_embeddings"].shape), (3, 4))
        self.assertEqual(tuple(namespace["graph_embedding"].shape), (1, 4))
        self.assertTrue(namespace["torch"].isfinite(namespace["graph_embedding"]).all().item())


if __name__ == "__main__":
    unittest.main()
