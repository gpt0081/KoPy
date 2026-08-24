# KoPy ONNX Runtime Pack

KoPy 0.5.9부터 `onnxruntime`을 `온엑스런타임`으로 불러오고 주요 ONNX Runtime Python API를 KoPy 음역 표현으로 사용할 수 있습니다.

## 설치

KoPy 팩은 번역 규칙만 제공합니다. 실제 추론 엔진은 원래 ONNX Runtime 패키지가 담당합니다.

```powershell
python -m pip install onnxruntime
```

GPU나 기타 실행 공급자는 ONNX Runtime의 공식 배포 정책과 사용 환경에 맞춰 별도로 설치합니다.

## 기본 추론

```kopy
임포트 온엑스런타임 애즈 ort
임포트 넘파이 애즈 np

세션 = ort.인퍼런스세션("model.onnx", providers=ort.겟어베일러블프로바이더스())
입력이름 = 세션.겟인풋스()[0].name
출력이름 = 세션.겟아웃풋스()[0].name
입력값 = np.어레이([[1.0, 2.0]], np.플로트32)
결과 = 세션.런([출력이름], {입력이름: 입력값})[0]
```

표준 Python에서는 다음 API를 호출합니다.

```python
import onnxruntime as ort

session = ort.InferenceSession("model.onnx", providers=ort.get_available_providers())
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name
result = session.run([output_name], {input_name: input_array})[0]
```

## 주요 대응

- `인퍼런스세션` → `InferenceSession`
- `세션옵션스` → `SessionOptions`
- `런` → `run`
- `겟인풋스` → `get_inputs`
- `겟아웃풋스` → `get_outputs`
- `겟프로바이더스` → `get_providers`
- `겟어베일러블프로바이더스` → `get_available_providers`
- `아이오바인딩` → `io_binding`
- `그래프옵티마이제이션레벨` → `GraphOptimizationLevel`
- `오트밸류` → `OrtValue`

## 충돌 방지

`providers=`, `sess_options=`, `provider_options=` 같은 키워드 인자는 Python 원형을 유지합니다. 라이브러리별 키워드 인자를 전역 단어로 등록하지 않아 다른 AI 팩과의 충돌을 피합니다.

ONNX Runtime 팩은 `onnxruntime`, `온엑스런타임`, 일반 별칭 `ort` 네임스페이스 안에서 활성화됩니다. 실제 모델 계산은 KoPy가 아니라 ONNX Runtime이 수행합니다.
