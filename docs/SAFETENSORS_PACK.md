# KoPy Safetensors Pack

KoPy 0.5.10의 Safetensors 팩은 Hugging Face Safetensors의 공개 Python API를 KoPy 음역으로 사용할 수 있게 합니다. 실제 저장·로드는 원래 `safetensors` 라이브러리가 수행하고 KoPy는 네임스페이스가 활성화된 경우에만 API 이름을 번역합니다.

## 설치

```bash
python -m pip install "safetensors>=0.8,<0.9" torch
```

## 기본 사용

```kopy
임포트 토치
프롬 세이프텐서스.torch 임포트 세이브파일, 로드파일
프롬 세이프텐서스 임포트 세이프오픈

가중치 = 토치.텐서([[1.0, 2.0], [3.0, 4.0]])
세이브파일({"weight": 가중치}, "model.safetensors")
불러온값 = 로드파일("model.safetensors")["weight"]

위드 세이프오픈("model.safetensors", framework="pt", device="cpu") 애즈 f:
    프린트(리스트(f.키즈()))
    프린트(f.겟텐서("weight"))
```

주요 대응은 `세이프오픈 → safe_open`, `세이브파일 → save_file`, `로드파일 → load_file`, `키즈 → keys`, `겟텐서 → get_tensor`, `겟슬라이스 → get_slice`, `메타데이터 → metadata`입니다.

## 안전 규칙

`framework=`, `device=`, `metadata=` 같은 키워드 인자는 Python 원형을 유지합니다. KoPy가 라이브러리 전역 키워드 인자를 추측해 번역하지 않기 때문에 다른 AI 라이브러리와의 충돌을 피할 수 있습니다.

`from safetensors.torch import ...` 같은 하위 모듈 경로에서 하위 모듈 이름 `torch` 자체는 Python 표기를 유지하고, 루트 `safetensors`와 import된 공개 API만 KoPy 팩이 번역합니다.
