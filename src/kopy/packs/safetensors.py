"""Official Hugging Face Safetensors library pack for KoPy."""

from __future__ import annotations

from .base import LibraryPack


SAFETENSORS_PACK = LibraryPack(
    name="safetensors",
    module="safetensors",
    kopy_module="세이프텐서스",
    preferred_aliases=("st",),
    description="AI 모델 텐서를 안전하고 빠르게 저장·로드하는 Safetensors API 팩",
    members={
        # Core file reader
        "세이프오픈": "safe_open",
        "키즈": "keys",
        "오프셋키즈": "offset_keys",
        "겟텐서": "get_tensor",
        "겟슬라이스": "get_slice",
        "메타데이터": "metadata",
        "겟셰이프": "get_shape",

        # torch / numpy / flax helpers
        "세이브파일": "save_file",
        "로드파일": "load_file",
        "세이브": "save",
        "로드": "load",

        # Common framework-specific helpers
        "플래튼": "_flatten",
        "뷰2스트라이드": "_view2stride",
    },
    member_descriptions={
        "safe_open": "Safetensors 파일을 지연 로딩 방식으로 열어 필요한 텐서만 읽습니다.",
        "keys": "파일에 저장된 텐서 이름 목록을 반환합니다.",
        "get_tensor": "지정한 이름의 텐서 전체를 로드합니다.",
        "get_slice": "지정한 텐서를 슬라이스 단위로 읽기 위한 객체를 반환합니다.",
        "metadata": "Safetensors 헤더에 저장된 문자열 메타데이터를 반환합니다.",
        "save_file": "텐서 딕셔너리를 Safetensors 파일로 저장합니다.",
        "load_file": "Safetensors 파일의 텐서들을 딕셔너리로 로드합니다.",
        "save": "텐서 딕셔너리를 Safetensors 형식의 바이트로 직렬화합니다.",
        "load": "Safetensors 바이트에서 텐서 딕셔너리를 복원합니다.",
    },
    examples={
        "safe_open": (
            "프롬 세이프텐서스 임포트 세이프오픈\n위드 세이프오픈(\"model.safetensors\", framework=\"pt\", device=\"cpu\") 애즈 f:\n    가중치 = f.겟텐서(\"weight\")",
            "from safetensors import safe_open\nwith safe_open(\"model.safetensors\", framework=\"pt\", device=\"cpu\") as f:\n    weights = f.get_tensor(\"weight\")",
        ),
        "save_file": (
            "프롬 세이프텐서스.torch 임포트 세이브파일\n세이브파일({\"weight\": 텐서}, \"model.safetensors\")",
            "from safetensors.torch import save_file\nsave_file({\"weight\": tensor}, \"model.safetensors\")",
        ),
        "load_file": (
            "프롬 세이프텐서스.torch 임포트 로드파일\n텐서들 = 로드파일(\"model.safetensors\")",
            "from safetensors.torch import load_file\ntensors = load_file(\"model.safetensors\")",
        ),
    },
)
