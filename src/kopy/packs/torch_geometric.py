"""Official PyTorch Geometric library pack for KoPy."""

from __future__ import annotations

from .base import LibraryPack


TORCH_GEOMETRIC_PACK = LibraryPack(
    name="pytorch-geometric",
    module="torch_geometric",
    kopy_module="토치지오메트릭",
    preferred_aliases=("torch-geometric", "torch_geometric", "pyg"),
    description="그래프 데이터·GNN 레이어·그래프 유틸리티를 위한 PyTorch Geometric API 팩",
    members={
        "데이터": "Data",
        "헤테로데이터": "HeteroData",
        "배치": "Batch",
        "데이터로더": "DataLoader",
        "지씨엔컨브": "GCNConv",
        "지에이티컨브": "GATConv",
        "세이지컨브": "SAGEConv",
        "진컨브": "GINConv",
        "그래프컨브": "GraphConv",
        "메시지패싱": "MessagePassing",
        "글로벌미인풀": "global_mean_pool",
        "글로벌맥스풀": "global_max_pool",
        "글로벌애드풀": "global_add_pool",
        "애드셀프룹스": "add_self_loops",
        "리무브셀프룹스": "remove_self_loops",
        "투언디렉티드": "to_undirected",
        "디그리": "degree",
        "네거티브샘플링": "negative_sampling",
        "서브그래프": "subgraph",
    },
    member_descriptions={
        "Data": "노드 특성, edge_index, 라벨 등을 담는 기본 동종 그래프 컨테이너입니다.",
        "HeteroData": "여러 노드·엣지 타입을 갖는 이종 그래프 컨테이너입니다.",
        "GCNConv": "Graph Convolutional Network 레이어입니다.",
        "GATConv": "Graph Attention Network 레이어입니다.",
        "SAGEConv": "GraphSAGE 레이어입니다.",
        "global_mean_pool": "batch별 노드 표현을 평균으로 graph-level 표현으로 집계합니다.",
        "to_undirected": "edge_index를 무방향 그래프 형태로 변환합니다.",
    },
    examples={
        "Data": (
            "프롬 토치지오메트릭.data 임포트 데이터\ngraph = 데이터(x=x, edge_index=edge_index)",
            "from torch_geometric.data import Data\ngraph = Data(x=x, edge_index=edge_index)",
        ),
        "GCNConv": (
            "프롬 토치지오메트릭.nn 임포트 지씨엔컨브\nconv = 지씨엔컨브(in_channels=8, out_channels=16)",
            "from torch_geometric.nn import GCNConv\nconv = GCNConv(in_channels=8, out_channels=16)",
        ),
    },
)
