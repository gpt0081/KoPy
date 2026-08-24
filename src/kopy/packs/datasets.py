"""Official Hugging Face Datasets library pack for KoPy.

Covers local/Hub dataset loading, in-memory construction, preprocessing,
selection, splitting, formatting and persistence APIs used in AI pipelines.
The actual implementation remains upstream Hugging Face Datasets.
"""

from __future__ import annotations

from .base import LibraryPack


DATASETS_PACK = LibraryPack(
    name="datasets",
    module="datasets",
    kopy_module="데이터셋츠",
    description="AI 데이터 로딩·전처리·분할·포맷 변환을 위한 Hugging Face Datasets API 팩",
    members={
        # Core dataset types / containers
        "데이터셋": "Dataset",
        "이터러블데이터셋": "IterableDataset",
        "데이터셋딕트": "DatasetDict",
        "이터러블데이터셋딕트": "IterableDatasetDict",
        "피처스": "Features",
        "밸류": "Value",
        "클래스레이블": "ClassLabel",
        "시퀀스": "Sequence",
        "오디오": "Audio",
        "이미지": "Image",

        # Loading / construction
        "로드데이터셋": "load_dataset",
        "로드프롬디스크": "load_from_disk",
        "프롬딕트": "from_dict",
        "프롬리스트": "from_list",
        "프롬판다스": "from_pandas",
        "프롬제너레이터": "from_generator",
        "프롬파일": "from_file",
        "투딕트": "to_dict",
        "투판다스": "to_pandas",
        "투리스트": "to_list",

        # Processing / row-column operations
        "맵": "map",
        "필터": "filter",
        "셀렉트": "select",
        "셔플": "shuffle",
        "소트": "sort",
        "트레인테스트스플릿": "train_test_split",
        "샤드": "shard",
        "플래튼": "flatten",
        "캐스트": "cast",
        "캐스트컬럼": "cast_column",
        "리네임컬럼": "rename_column",
        "리네임컬럼스": "rename_columns",
        "리무브컬럼스": "remove_columns",
        "셀렉트컬럼스": "select_columns",
        "애드컬럼": "add_column",
        "컨캐터네이트데이터셋츠": "concatenate_datasets",
        "인터리브데이터셋츠": "interleave_datasets",

        # Formatting / framework bridges
        "셋포맷": "set_format",
        "위드포맷": "with_format",
        "리셋포맷": "reset_format",
        "포매티드애즈": "formatted_as",
        "셋트랜스폼": "set_transform",
        "위드트랜스폼": "with_transform",

        # Metadata / inspection
        "컬럼네임스": "column_names",
        "피처": "features",
        "넘로우스": "num_rows",
        "셰이프": "shape",
        "데이터셋인포": "DatasetInfo",
        "스플릿": "split",
        "스플릿스": "splits",

        # Persistence / export / hub
        "세이브투디스크": "save_to_disk",
        "푸시투허브": "push_to_hub",
        "투씨에스브이": "to_csv",
        "투제이슨": "to_json",
        "투파케이": "to_parquet",
    },
    member_descriptions={
        "Dataset": "메모리 매핑 가능한 Arrow 기반 정형 데이터셋 객체입니다.",
        "DatasetDict": "train/test/validation 같은 split별 Dataset을 묶는 매핑 객체입니다.",
        "load_dataset": "Hub 또는 로컬 파일·빌더에서 데이터셋을 불러옵니다.",
        "from_dict": "Python 딕셔너리의 열 데이터에서 Dataset을 만듭니다.",
        "map": "각 예제 또는 배치에 전처리 함수를 적용하고 새 데이터셋을 만듭니다.",
        "filter": "조건을 만족하는 예제만 남깁니다.",
        "select": "지정한 행 인덱스만 선택합니다.",
        "shuffle": "행 순서를 섞습니다. seed 인자는 Python 원형을 유지합니다.",
        "train_test_split": "데이터셋을 train/test DatasetDict로 분할합니다.",
        "with_format": "PyTorch, NumPy, pandas 등 특정 프레임워크 형식으로 값을 반환하도록 설정한 새 데이터셋을 만듭니다.",
        "save_to_disk": "Arrow 기반 데이터셋을 로컬 디스크에 저장합니다.",
        "load_from_disk": "save_to_disk로 저장한 데이터셋을 다시 불러옵니다.",
        "concatenate_datasets": "여러 Dataset을 이어 붙입니다.",
    },
    examples={
        "Dataset": (
            "프롬 데이터셋츠 임포트 데이터셋\n데이터 = 데이터셋.프롬딕트({\"text\": [\"가\", \"나\"]})",
            "from datasets import Dataset\ndata = Dataset.from_dict({\"text\": [\"a\", \"b\"]})",
        ),
        "load_dataset": (
            "프롬 데이터셋츠 임포트 로드데이터셋\n데이터 = 로드데이터셋(\"csv\", data_files=\"train.csv\")",
            "from datasets import load_dataset\ndata = load_dataset(\"csv\", data_files=\"train.csv\")",
        ),
        "map": (
            "길이추가 = 데이터.맵(함수)",
            "with_length = data.map(function)",
        ),
        "train_test_split": (
            "분할 = 데이터.트레인테스트스플릿(test_size=0.2, seed=42)",
            "split = data.train_test_split(test_size=0.2, seed=42)",
        ),
        "with_format": (
            "토치데이터 = 데이터.위드포맷(\"torch\")",
            "torch_data = data.with_format(\"torch\")",
        ),
    },
)
