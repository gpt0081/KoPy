# KoPy PEFT Pack

KoPy의 `peft / 페프트` 팩은 Hugging Face PEFT API 이름을 KoPy 표현으로 음역합니다. 실제 LoRA/adapter 계산은 설치된 원래 `peft` 라이브러리가 수행합니다.

기준 통합 테스트: PEFT 0.20.x + Transformers 5.15.x + PyTorch 2.13.x.

## 음역 원칙

PEFT 팩도 KoPy 공통 원칙을 따릅니다.

- Python 식별자의 `_` 구조를 보존합니다. 예: `get_peft_model → 겟_페프트_모델`.
- 숫자는 한글로 풀어쓰지 않습니다. 예: `IA3Config → 아이에이3컨피그`.
- 과거 compact 표기(`겟페프트모델`, `아이에이쓰리컨피그`)는 기존 KoPy 코드 호환을 위한 입력 alias로 유지합니다.
- 새 학습 자료와 Python → KoPy 변환은 canonical 표기를 우선합니다.

## 설치

```bash
pip install peft
kopy packs peft
```

## 기본 LoRA 흐름

```kopy
프롬 페프트 임포트 로라컨피그, 겟_페프트_모델

모델 = 겟_페프트_모델(
    베이스_모델,
    로라컨피그(
        r=8,
        lora_alpha=16,
        target_modules=["query", "value"],
        lora_dropout=0.05,
    ),
)
모델.프린트_트레이너블_파라미터스()
```

이는 `LoraConfig`, `get_peft_model`, `print_trainable_parameters`를 사용하는 표준 PEFT 코드로 번역됩니다.

## 주요 canonical API

- 설정/모델: `LoraConfig → 로라컨피그`, `PeftModel → 페프트모델`, `IA3Config → 아이에이3컨피그`
- 생성/양자화 준비: `get_peft_model → 겟_페프트_모델`, `prepare_model_for_kbit_training → 프리페어_모델_포_케이비트_트레이닝`
- 저장/복원: `from_pretrained → 프롬_프리트레인드`, `save_pretrained → 세이브_프리트레인드`, PEFT state dict helpers
- 어댑터 관리: `add_adapter → 애드_어댑터`, `set_adapter → 셋_어댑터`, `load_adapter → 로드_어댑터`, `delete_adapter → 딜리트_어댑터`
- 병합: `merge_adapter → 머지_어댑터`, `unmerge_adapter → 언머지_어댑터`, `merge_and_unload → 머지_앤드_언로드`
- 점검: `print_trainable_parameters → 프린트_트레이너블_파라미터스`, model/layer status helpers

## 남은 키워드 인자 감사

`r=`, `lora_alpha=`, `target_modules=`, `task_type=`, `lora_dropout=` 같은 키워드 인자는 이번 API canonicalization에서 영구 영어 예외로 선언하지 않습니다. 이 이름들은 함수 인자 문맥과 다른 라이브러리의 식별자 충돌을 확인한 뒤 context-aware 음역 대상으로 후속 감사합니다.

문자열 데이터인 `"query"`, `"value"`와 숫자 `8`, `16`, `0.05`는 번역하지 않습니다.

PEFT 팩은 upstream 라이브러리를 복제하지 않습니다. 따라서 실제 실행에는 `peft`, 그리고 사용 모델에 따라 `torch`와 `transformers`가 별도로 설치되어 있어야 합니다.
