# KoPy PEFT Pack

KoPy의 `peft / 페프트` 팩은 Hugging Face PEFT API 이름을 KoPy 표현으로 번역합니다. 실제 LoRA/adapter 계산은 설치된 원래 `peft` 라이브러리가 수행합니다.

기준 통합 테스트: PEFT 0.20.x + Transformers 5.15.x + PyTorch 2.13.x.

## 설치

```bash
pip install peft
kopy packs peft
```

## 기본 LoRA 흐름

```kopy
프롬 페프트 임포트 로라컨피그, 겟페프트모델

로라설정 = 로라컨피그(
    r=8,
    lora_alpha=16,
    target_modules=["query", "value"],
    lora_dropout=0.05,
)

모델 = 겟페프트모델(기본모델, 로라설정)
모델.프린트트레이너블파라미터스()
```

이는 `LoraConfig`, `get_peft_model`, `print_trainable_parameters`를 사용하는 표준 PEFT 코드로 번역됩니다.

## 주요 지원 API

- 설정/모델: `LoraConfig`, `PeftModel`, `PeftConfig`, `TaskType`, prompt/prefix/IA3/AdaLoRA config
- 생성/양자화 준비: `get_peft_model`, `prepare_model_for_kbit_training`
- 저장/복원: `from_pretrained`, `save_pretrained`, PEFT state dict helpers
- 어댑터 관리: `add_adapter`, `set_adapter`, `load_adapter`, `delete_adapter`
- 병합: `merge_adapter`, `unmerge_adapter`, `merge_and_unload`, `unload`
- 점검: `print_trainable_parameters`, model/layer status helpers

## 호환성 원칙

`r=`, `lora_alpha=`, `target_modules=`, `task_type=` 같은 키워드 인자 이름은 Python 원형을 유지합니다. 키워드 인자는 여러 라이브러리와 함수 사이에서 의미가 겹칠 수 있으므로 현재 KoPy의 namespace-scoped 팩이 안전하게 판별할 수 있을 때까지 전역 번역하지 않습니다.

PEFT 팩은 upstream 라이브러리를 복제하지 않습니다. 따라서 실제 실행에는 `peft`, 그리고 사용 모델에 따라 `torch`와 `transformers`가 별도로 설치되어 있어야 합니다.
