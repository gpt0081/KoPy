# KoPy PEFT Pack

KoPy의 `peft / 페프트` 팩은 Hugging Face PEFT API 이름을 KoPy 표현으로 음역합니다. 실제 LoRA/adapter 계산은 설치된 원래 `peft` 라이브러리가 수행합니다.

기준 통합 테스트: PEFT 0.20.x + Transformers 5.15.x + PyTorch 2.13.x.

## 음역 원칙

PEFT 팩도 KoPy 공통 원칙을 따릅니다.

- Python 식별자의 `_` 구조를 보존합니다. 예: `get_peft_model → 겟_페프트_모델`.
- 숫자는 한글로 풀어쓰지 않습니다. 예: `IA3Config → 아이에이3컨피그`.
- PEFT에 특화된 긴 키워드 식별자도 pack 내부에서 음역합니다. 예: `lora_alpha → 로라_알파`, `target_modules → 타깃_모듈즈`, `task_type → 태스크_타입`, `lora_dropout → 로라_드롭아웃`, `bias → 바이어스`, `inference_mode → 인퍼런스_모드`, `modules_to_save → 모듈즈_투_세이브`, `fan_in_fan_out → 팬_인_팬_아웃`, `use_rslora → 유즈_알에스로라`, `init_lora_weights → 이니트_로라_웨이츠`, `exclude_modules → 익스클루드_모듈즈`, `layers_to_transform → 레이어즈_투_트랜스폼`, `layers_pattern → 레이어즈_패턴`, `rank_pattern → 랭크_패턴`, `alpha_pattern → 알파_패턴`, `use_dora → 유즈_도라`.
- 키워드 인자 음역은 PEFT pack이 활성화된 실제 함수 호출의 키워드 위치에서만 적용합니다. 같은 철자의 일반 변수는 PEFT 키워드로 강제 변환하지 않습니다.
- 과거 compact 표기(`겟페프트모델`, `아이에이쓰리컨피그`)는 기존 KoPy 코드 호환을 위한 입력 alias로 유지합니다.
- 새 학습 자료와 Python → KoPy 변환은 canonical 표기를 우선합니다.
- 한 글자인 `r`은 LoRA rank 외에도 일반 수학/반지름 변수로 널리 쓰여 모호하므로 현재는 원문을 유지합니다.

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
        로라_알파=16,
        타깃_모듈즈=["query", "value"],
        로라_드롭아웃=0.05,
        바이어스="none",
        인퍼런스_모드=펄스,
        모듈즈_투_세이브=["classifier"],
        팬_인_팬_아웃=펄스,
        유즈_알에스로라=펄스,
        이니트_로라_웨이츠=트루,
        익스클루드_모듈즈=["classifier"],
        레이어즈_투_트랜스폼=[0],
        레이어즈_패턴="layers",
        랭크_패턴={},
        알파_패턴={},
        유즈_도라=펄스,
    ),
)
모델.프린트_트레이너블_파라미터스()
```

이는 다음 Python 구조로 돌아갑니다.

```python
model = get_peft_model(
    base_model,
    LoraConfig(
        r=8,
        lora_alpha=16,
        target_modules=["query", "value"],
        lora_dropout=0.05,
        bias="none",
        inference_mode=False,
        modules_to_save=["classifier"],
        fan_in_fan_out=False,
        use_rslora=False,
        init_lora_weights=True,
        exclude_modules=["classifier"],
        layers_to_transform=[0],
        layers_pattern="layers",
        rank_pattern={},
        alpha_pattern={},
        use_dora=False,
    ),
)
```

문자열 데이터인 `"query"`, `"value"`, `"classifier"`, `"none"`, `"layers"`와 숫자 `0`, `8`, `16`, `0.05`는 번역하지 않습니다.

## 주요 canonical API

- 설정/모델: `LoraConfig → 로라컨피그`, `PeftModel → 페프트모델`, `IA3Config → 아이에이3컨피그`
- 생성/양자화 준비: `get_peft_model → 겟_페프트_모델`, `prepare_model_for_kbit_training → 프리페어_모델_포_케이비트_트레이닝`
- LoRA/PEFT 키워드: `lora_alpha → 로라_알파`, `target_modules → 타깃_모듈즈`, `task_type → 태스크_타입`, `lora_dropout → 로라_드롭아웃`, `bias → 바이어스`, `inference_mode → 인퍼런스_모드`, `modules_to_save → 모듈즈_투_세이브`, `fan_in_fan_out → 팬_인_팬_아웃`, `use_rslora → 유즈_알에스로라`, `init_lora_weights → 이니트_로라_웨이츠`, `exclude_modules → 익스클루드_모듈즈`, `layers_to_transform → 레이어즈_투_트랜스폼`, `layers_pattern → 레이어즈_패턴`, `rank_pattern → 랭크_패턴`, `alpha_pattern → 알파_패턴`, `use_dora → 유즈_도라`
- 저장/복원: `from_pretrained → 프롬_프리트레인드`, `save_pretrained → 세이브_프리트레인드`, PEFT state dict helpers
- 어댑터 관리: `add_adapter → 애드_어댑터`, `set_adapter → 셋_어댑터`, `load_adapter → 로드_어댑터`, `delete_adapter → 딜리트_어댑터`
- 병합: `merge_adapter → 머지_어댑터`, `unmerge_adapter → 언머지_어댑터`, `merge_and_unload → 머지_앤드_언로드`
- 점검: `print_trainable_parameters → 프린트_트레이너블_파라미터스`, model/layer status helpers

## 남은 context-aware 감사

`r=`은 매우 짧고 모호해서 현재 원문을 유지합니다. 최신 LoraConfig에는 `layer_replication=`, `runtime_config=`, `loftq_config=` 등 추가 고급 설정 키워드가 더 있습니다. 이들은 실제 사용 빈도와 다른 팩의 충돌 가능성을 확인한 뒤 `keyword_arguments` 구조로 단계적으로 감사합니다. 전역 단어표에 무리하게 넣지 않습니다.

PEFT 팩은 upstream 라이브러리를 복제하지 않습니다. 따라서 실제 실행에는 `peft`, 그리고 사용 모델에 따라 `torch`와 `transformers`가 별도로 설치되어 있어야 합니다.
