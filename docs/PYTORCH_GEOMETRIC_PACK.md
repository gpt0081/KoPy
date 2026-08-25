# PyTorch Geometric Pack

KoPy 0.5.29 adds a namespace-scoped pack for PyTorch Geometric (PyG).

Target runtime: Python 3.12.10 with `torch-geometric>=2.8.0.post1,<2.9`.

## Install

```bash
python -m pip install "torch-geometric>=2.8.0.post1,<2.9"
```

PyG 2.8 can use its core Python package with PyTorch alone. Optional accelerated packages such as `pyg-lib`, `torch-scatter`, and `torch-sparse` are intentionally not required by KoPy's baseline runtime test.

## KoPy example

```python
임포트 토치
프롬 토치지오메트릭.data 임포트 데이터
프롬 토치지오메트릭.nn 임포트 지씨엔컨브, 글로벌미인풀

x = 토치.텐서([[1.0, 0.0], [0.0, 1.0]])
edge_index = 토치.텐서([[0, 1], [1, 0]], dtype=토치.인트64)

graph = 데이터(x=x, edge_index=edge_index)
conv = 지씨엔컨브(in_channels=2, out_channels=4)
node_embeddings = conv(graph.x, graph.edge_index)
```

Equivalent Python:

```python
import torch
from torch_geometric.data import Data
from torch_geometric.nn import GCNConv, global_mean_pool

x = torch.tensor([[1.0, 0.0], [0.0, 1.0]])
edge_index = torch.tensor([[0, 1], [1, 0]], dtype=torch.int64)

graph = Data(x=x, edge_index=edge_index)
conv = GCNConv(in_channels=2, out_channels=4)
node_embeddings = conv(graph.x, graph.edge_index)
```

## Translation policy

PyG API names such as `Data`, `GCNConv`, `GATConv`, `SAGEConv`, `global_mean_pool`, and `to_undirected` are translated only after a PyG namespace is imported. They are not added to KoPy's global word table.

Standard graph/ML variables such as `x`, `edge_index`, `batch`, `graph`, `node_embeddings`, and `model` stay Python-native. Generic keyword arguments such as `in_channels=`, `out_channels=`, `heads=`, `add_self_loops=`, and `num_neighbors=` also stay Python-native. This keeps real PyG code recognizable while avoiding ambiguous translations shared by other libraries.
