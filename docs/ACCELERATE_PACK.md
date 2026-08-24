# KoPy Accelerate Pack

KoPy 0.5.7의 Hugging Face Accelerate 팩은 실제 `accelerate` 라이브러리 위에 한글 음역 인터페이스를 제공합니다. 계산·분산 처리·장치 배치는 원래 Accelerate와 PyTorch가 수행하며 KoPy는 import와 등록된 API 이름만 변환합니다.

기준 안정판: Accelerate 1.14.x

## 예시

```kopy
프롬 액셀러레이트 임포트 액셀러레이터
임포트 토치

가속기 = 액셀러레이터()
모델 = 토치.엔엔.리니어(3, 1)
옵티마이저 = 토치.옵팀.아담더블유(모델.파라미터스())
모델, 옵티마이저 = 가속기.프리페어(모델, 옵티마이저)
가속기.백워드(손실)
옵티마이저.스텝()
```

주요 대응은 `액셀러레이터 → Accelerator`, `프리페어 → prepare`, `백워드 → backward`, `개더포메트릭스 → gather_for_metrics`, `언랩모델 → unwrap_model`, `세이브스테이트 → save_state`, `웨이트포에브리원 → wait_for_everyone`입니다.

`cpu=`, `mixed_precision=`, `gradient_accumulation_steps=` 같은 키워드 인자는 Python 원형을 유지합니다. 키워드 인자를 전역 치환하면 다른 AI 라이브러리와 충돌할 수 있기 때문입니다.

```bash
kopy packs accelerate
kopy help 액셀러레이트.액셀러레이터
```
