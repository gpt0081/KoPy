"""Official Hugging Face PEFT library pack for KoPy."""

from __future__ import annotations

from .base import LibraryPack


PEFT_PACK = LibraryPack(
    name="peft",
    module="peft",
    kopy_module="페프트",
    description="LoRA 등 파라미터 효율 미세조정을 위한 Hugging Face PEFT API 팩",
    members={
        # Core configuration / model types
        "페프트모델": "PeftModel",
        "페프트컨피그": "PeftConfig",
        "로라컨피그": "LoraConfig",
        "로라모델": "LoraModel",
        "태스크타입": "TaskType",
        "페프트타입": "PeftType",
        "프롬프트튜닝컨피그": "PromptTuningConfig",
        "프롬프트인코더컨피그": "PromptEncoderConfig",
        "프리픽스튜닝컨피그": "PrefixTuningConfig",
        "아이에이쓰리컨피그": "IA3Config",
        "에이다로라컨피그": "AdaLoraConfig",

        # Construction / loading
        "겟페프트모델": "get_peft_model",
        "겟페프트모델스테이트딕트": "get_peft_model_state_dict",
        "셋페프트모델스테이트딕트": "set_peft_model_state_dict",
        "프리페어모델포케이비트트레이닝": "prepare_model_for_kbit_training",
        "프롬프리트레인드": "from_pretrained",
        "세이브프리트레인드": "save_pretrained",

        # Adapter lifecycle
        "애드어댑터": "add_adapter",
        "셋어댑터": "set_adapter",
        "로드어댑터": "load_adapter",
        "딜리트어댑터": "delete_adapter",
        "인에이블어댑터레이어스": "enable_adapter_layers",
        "디스에이블어댑터레이어스": "disable_adapter_layers",
        "머지어댑터": "merge_adapter",
        "언머지어댑터": "unmerge_adapter",
        "머지앤언로드": "merge_and_unload",
        "언로드": "unload",
        "애드웨이티드어댑터": "add_weighted_adapter",

        # Inspection / helpers
        "프린트트레이너블파라미터스": "print_trainable_parameters",
        "겟모델스테이터스": "get_model_status",
        "겟레이어스테이터스": "get_layer_status",
        "겟베이스모델": "get_base_model",
        "액티브어댑터": "active_adapter",
        "액티브어댑터스": "active_adapters",
        "페프트컨피그": "peft_config",
        "베이스모델": "base_model",
        "푸시투허브": "push_to_hub",
    },
    member_descriptions={
        "LoraConfig": "LoRA rank, target module, dropout 등 어댑터 학습 설정을 정의합니다.",
        "get_peft_model": "기본 모델에 PEFT 설정을 적용해 PeftModel을 만듭니다.",
        "PeftModel": "기본 모델과 하나 이상의 PEFT 어댑터를 관리하는 모델 래퍼입니다.",
        "prepare_model_for_kbit_training": "양자화된 모델을 k-bit PEFT 학습에 맞게 준비합니다.",
        "print_trainable_parameters": "전체 파라미터 중 실제 학습되는 PEFT 파라미터 수를 표시합니다.",
        "merge_and_unload": "활성 어댑터 가중치를 기본 모델에 병합하고 PEFT 래퍼를 제거합니다.",
        "set_adapter": "사용할 활성 어댑터를 선택합니다.",
    },
    examples={
        "LoraConfig": (
            "프롬 페프트 임포트 로라컨피그\n설정 = 로라컨피그(r=8, lora_alpha=16, target_modules=[\"query\", \"value\"])",
            "from peft import LoraConfig\nconfig = LoraConfig(r=8, lora_alpha=16, target_modules=[\"query\", \"value\"])",
        ),
        "get_peft_model": (
            "프롬 페프트 임포트 겟페프트모델\n모델 = 겟페프트모델(모델, 설정)",
            "from peft import get_peft_model\nmodel = get_peft_model(model, config)",
        ),
        "merge_and_unload": (
            "병합모델 = 모델.머지앤언로드()",
            "merged_model = model.merge_and_unload()",
        ),
    },
)
