# KoPy (코파이)

KoPy는 Python 문법을 그대로 배우면서 영어 예약어와 주요 API를 한글 음역으로도 사용할 수 있게 하는 Python 호환 학습 레이어입니다.

현재 Core 버전: **0.5.11**  
개발 기준 Python: **3.12.10**

## KoPy v0.5 방향: AI 개발

v0.5부터 KoPy는 Python Core를 넘어 AI 개발 생태계로 확장합니다. Library Pack은 외부 라이브러리를 다시 구현하지 않습니다. 해당 라이브러리가 import된 파일에서만 API 이름을 KoPy 표현과 Python 표현 사이에서 번역하고, 실제 계산·학습·추론은 원래 Python 라이브러리가 담당합니다.

현재 공식 AI 라이브러리 팩:

- **NumPy**: 배열·통계·선형대수·난수
- **pandas**: DataFrame·정제·집계·파일 입출력
- **scikit-learn**: 전처리·모델 학습·평가·파이프라인
- **PyTorch**: 텐서·자동미분·신경망·최적화
- **Hugging Face Transformers**: 사전학습 모델·생성·Trainer
- **Hugging Face Datasets**: 데이터 로딩·전처리·분할
- **Hugging Face Tokenizers**: 고속 토큰화·Encoding·어휘 모델
- **Hugging Face Accelerate**: 장치·분산 학습 준비와 실행
- **Hugging Face PEFT**: LoRA 등 파라미터 효율 미세조정
- **ONNX Runtime**: ONNX 모델 로딩·실행 공급자·최적화·추론
- **Safetensors**: AI 텐서의 안전한 저장·로드·부분 읽기
- **Hugging Face Optimum**: 모델 작업·export 구성·하드웨어 최적화 흐름 연결

```text
KoPy 코드
   ↓
KoPy Core + 활성 Library Pack
   ↓
표준 Python 코드
   ↓
CPython + 실제 AI 라이브러리
```

## Optimum 예시

```kopy
프롬 옵티멈.exporters.tasks 임포트 태스크매니저

태스크들 = 태스크매니저.겟올태스크스()
모델클래스 = 태스크매니저.겟모델클래스포태스크("text-classification")
표준태스크 = 태스크매니저.맵프롬시노님("sequence-classification")
```

Optimum의 하드웨어별 backend와 `framework=`, `library_name=`, `exporter=` 같은 키워드 인자는 Python 원형을 유지합니다.

## Safetensors 예시

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

## ONNX Runtime 예시

```kopy
임포트 온엑스런타임 애즈 ort
임포트 넘파이 애즈 np

세션 = ort.인퍼런스세션("model.onnx", providers=ort.겟어베일러블프로바이더스())
입력이름 = 세션.겟인풋스()[0].name
출력이름 = 세션.겟아웃풋스()[0].name
입력값 = np.어레이([[1.0, 2.0]], np.플로트32)
결과 = 세션.런([출력이름], {입력이름: 입력값})[0]
```

표준 Python의 `onnxruntime.InferenceSession`, `get_inputs`, `get_outputs`, `run`으로 번역되며 실제 추론은 ONNX Runtime이 수행합니다.

## PEFT 예시

```kopy
프롬 페프트 임포트 로라컨피그, 겟페프트모델

설정 = 로라컨피그(r=8, lora_alpha=16, target_modules=["query", "value"])
모델 = 겟페프트모델(기본모델, 설정)
모델.프린트트레이너블파라미터스()
```

## Accelerate 예시

```kopy
프롬 액셀러레이트 임포트 액셀러레이터

가속기 = 액셀러레이터()
모델, 옵티마이저 = 가속기.프리페어(모델, 옵티마이저)
가속기.백워드(손실)
```

## Transformers 예시

```kopy
프롬 트랜스포머스 임포트 오토토크나이저, 오토모델포코절엘엠

토크나이저 = 오토토크나이저.프롬프리트레인드("local-model")
모델 = 오토모델포코절엘엠.프롬프리트레인드("local-model")
입력값 = 토크나이저("안녕하세요", return_tensors="pt")
출력 = 모델.제너레이트(**입력값)
```

## Datasets 예시

```kopy
프롬 데이터셋츠 임포트 데이터셋

데이터 = 데이터셋.프롬딕트({"text": ["a", "bb"], "label": [0, 1]})
가공 = 데이터.맵(lambda row: {"length": 렌(row["text"])})
분할 = 가공.트레인테스트스플릿(test_size=0.5, seed=42)
```

## Tokenizers 예시

```kopy
프롬 토크나이저스 임포트 토크나이저
프롬 토크나이저스.models 임포트 워드피스

모델 = 워드피스(vocab={"[UNK]": 0, "hello": 1}, unk_token="[UNK]")
토크 = 토크나이저(모델)
결과 = 토크.엔코드("hello")
```

## NumPy 예시

```kopy
임포트 넘파이 애즈 np

x = np.어레이([1, 2, 3, 4], np.플로트32)
y = x.리셰이프(2, 2)
평균 = np.미인(y)
크기 = np.린알지.노름(y)
```

## 라이브러리 팩의 충돌 방지 원칙

외부 라이브러리 API는 Core 전역 단어표에 섞지 않습니다. 해당 라이브러리를 import한 파일에서만 관련 규칙이 활성화됩니다. 여러 활성 팩이 같은 KoPy 철자를 서로 다른 Python API로 정의하면 KoPy는 임의로 추측하지 않고 모호한 표현을 번역하지 않습니다.

`device=`, `providers=`, `test_size=`, `return_tensors=`, `target_modules=`, `metadata=`, `framework=` 같은 키워드 인자 이름은 아직 Python 원형을 유지합니다. 라이브러리마다 같은 이름을 다른 의미로 사용할 수 있으므로 전역 치환하지 않습니다.

## 실제 라이브러리 설치

KoPy는 번역 팩을 제공하며 실제 라이브러리는 일반 Python과 동일하게 별도 설치해야 합니다.

```powershell
python -m pip install numpy pandas scikit-learn torch transformers datasets tokenizers accelerate peft onnxruntime safetensors optimum
```

상태 확인:

```powershell
kopy packs
kopy packs numpy
kopy packs pytorch
kopy packs transformers
kopy packs peft
kopy packs onnxruntime
kopy packs safetensors
kopy packs optimum
```

## Core 예시

```kopy
이름 = 인풋("이름: ")
나이 = 인트(인풋("나이: "))

이프 나이 >= 20:
    프린트(이름, "성인입니다.")
엘스:
    프린트(이름, "미성년자입니다.")
```

KoPy는 Python 문법 자체를 바꾸지 않고 표준 Python으로 변환한 뒤 CPython에서 실행합니다.

## 개발용 설치

```powershell
git clone https://github.com/gpt0081/KoPy.git
cd KoPy
python -m pip install -e .
```

## 주요 CLI

```powershell
kopy run examples\hello.kpy
kopy check examples\hello.kpy
kopy translate examples\hello.kpy
kopy convert-python example.py
kopy help 프린트
kopy help np.어레이
kopy help 온엑스런타임.인퍼런스세션
kopy help 세이프텐서스.세이프오픈
kopy help 옵티멈.태스크매니저
kopy explain examples\hello.kpy
kopy learn examples\hello.kpy
kopy words
kopy packs
kopy packs onnxruntime
kopy packs safetensors
kopy packs optimum
kopy version
```

## 편집기용 Core API

```powershell
kopy words --json
kopy info --json
kopy diagnose examples\hello.kpy --json
kopy packs --json
kopy packs onnxruntime --json
kopy packs safetensors --json
kopy packs optimum --json
```

VS Code 확장은 별도 Core 단어표나 오타 알고리즘을 유지하지 않고 KoPy Core를 사용합니다.

## 테스트 철학

KoPy는 Python 호환성을 가장 중요한 기준으로 둡니다. AI Library Pack은 GitHub Actions에서 Windows, Linux, macOS 각각에 실제 라이브러리를 설치해 전체 테스트와 런타임 smoke test를 수행합니다. 테스트는 가능한 한 외부 모델·데이터 다운로드 없이 메모리에서 실제 라이브러리 코드를 실행합니다.

## 구조

```text
src/kopy
   ├─ words.py
   ├─ packs/
   │   ├─ base.py
   │   ├─ registry.py
   │   ├─ numpy.py
   │   ├─ pandas.py
   │   ├─ sklearn.py
   │   ├─ torch.py
   │   ├─ transformers.py
   │   ├─ datasets.py
   │   ├─ tokenizers.py
   │   ├─ accelerate.py
   │   ├─ peft.py
   │   ├─ onnxruntime.py
   │   ├─ safetensors.py
   │   └─ optimum.py
   ├─ translator.py
   ├─ spelling.py
   ├─ education.py
   ├─ runtime.py
   ├─ editor.py
   └─ cli.py
```

## 다음 AI 확장 후보

- Matplotlib
- SentencePiece
- MLflow

## 버전 정책

Python 새 버전이 발표되어도 KoPy가 자동 추종하지는 않습니다. 문법, 호환성, 보안, 교육적 가치를 검토한 뒤 기준 버전을 올립니다. 현재 기준은 Python 3.12.10입니다.

## 라이선스

MIT License
