# KoPy MLflow Pack

KoPy 0.5.13부터 `mlflow`의 실험 추적 API를 `엠엘플로우` 이름으로 사용할 수 있습니다.

KoPy 팩은 MLflow를 다시 구현하지 않습니다. KoPy 소스를 표준 Python `mlflow` 호출로 변환하고, run 관리·메트릭 기록·아티팩트 저장은 설치된 실제 MLflow가 수행합니다.

## 설치

전체 MLflow 기능이 필요하면:

```powershell
python -m pip install "mlflow>=3.15,<3.16"
```

KoPy의 최신 pandas 3.x 환경과 같은 가상환경에서 기본 tracking client만 함께 쓰려면:

```powershell
python -m pip install "mlflow-skinny>=3.15,<3.16"
```

MLflow 3.15.1 정식 배포판은 현재 `pandas<3`을 요구합니다. 따라서 pandas 3.x를 고정한 환경에는 full `mlflow`와 pandas 3.x를 동시에 설치할 수 없습니다. KoPy 팩 자체의 문제가 아니라 upstream 패키지 의존성입니다. KoPy CI는 이를 숨기지 않고 두 환경을 따로 검증합니다.

- 전체 AI stack + pandas 3.x: `mlflow-skinny`로 namespace/tracking 호환성 검증
- full MLflow 3.15: 별도 Windows/Ubuntu/macOS job에서 실제 local tracking 검증

확인:

```powershell
kopy packs mlflow
kopy help 엠엘플로우.스타트런
```

## 기본 실험 추적

```kopy
임포트 엠엘플로우 애즈 mlf

mlf.셋트래킹유알아이("file:./mlruns")
mlf.셋익스페리먼트("kopy-demo")

위드 mlf.스타트런(run_name="baseline") 애즈 실행:
    mlf.로그파람("learning_rate", 0.01)
    mlf.로그메트릭("loss", 0.25)
    mlf.셋태그("stage", "baseline")
    mlf.로그텍스트("KoPy experiment", "notes.txt")

    프린트(실행.인포.런아이디)
```

표준 Python으로는 다음 API를 호출합니다.

```python
import mlflow as mlf

mlf.set_tracking_uri("file:./mlruns")
mlf.set_experiment("kopy-demo")

with mlf.start_run(run_name="baseline") as run:
    mlf.log_param("learning_rate", 0.01)
    mlf.log_metric("loss", 0.25)
    mlf.set_tag("stage", "baseline")
    mlf.log_text("KoPy experiment", "notes.txt")
```

## 주요 대응

| KoPy | Python MLflow |
|---|---|
| `셋트래킹유알아이` | `set_tracking_uri` |
| `셋익스페리먼트` | `set_experiment` |
| `스타트런` | `start_run` |
| `엔드런` | `end_run` |
| `로그파람` | `log_param` |
| `로그파람즈` | `log_params` |
| `로그메트릭` | `log_metric` |
| `로그메트릭스` | `log_metrics` |
| `로그아티팩트` | `log_artifact` |
| `로그텍스트` | `log_text` |
| `셋태그` | `set_tag` |
| `겟런` | `get_run` |
| `서치런즈` | `search_runs` |
| `엠엘플로우클라이언트` | `MlflowClient` |
| `오토로그` | `autolog` |

## 충돌 방지

`로그`, `데이터`, `메트릭스`, `태그스`처럼 다른 라이브러리에서도 흔히 등장할 수 있는 이름은 MLflow가 import된 파일에서만 MLflow 팩의 후보가 됩니다. 여러 활성 팩이 같은 KoPy 철자를 서로 다른 Python 이름으로 정의하면 KoPy는 임의로 하나를 선택하지 않습니다.

`run_name=`, `experiment_id=`, `artifact_path=`, `step=`, `tags=` 같은 키워드 인자 이름은 Python 원형을 유지합니다. 현재 KoPy의 라이브러리 팩은 API 이름 번역에 집중하며, 키워드 인자를 전역 치환하지 않습니다.

## 런타임 테스트

full MLflow CI는 외부 서버 없이 임시 로컬 tracking store를 만들고 실제 MLflow를 사용해 다음을 검증합니다.

1. tracking URI 설정
2. experiment 생성/선택
3. run 시작
4. parameter·metric·tag·text artifact 기록
5. run ID로 다시 조회
6. 기록된 값 비교

이 테스트는 Windows, Ubuntu, macOS에서 실행됩니다.
