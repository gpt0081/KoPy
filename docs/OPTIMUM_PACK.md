# KoPy Optimum Pack

KoPy 0.5.11부터 Hugging Face Optimum의 핵심 모델 작업·export 관리 API를 KoPy 음역으로 사용할 수 있습니다.

실제 최적화와 모델 처리는 원래 `optimum` 라이브러리가 수행하며 KoPy 팩은 namespace-scoped 번역 레이어입니다.

## 설치

```bash
python -m pip install "optimum>=2.3,<2.4"
```

하드웨어별 backend는 Optimum의 별도 패키지/extra 정책을 따릅니다. KoPy는 backend 설치를 자동 추측하지 않습니다.

## 예제

```kopy
프롬 옵티멈.exporters.tasks 임포트 태스크매니저

태스크들 = 태스크매니저.겟올태스크스()
모델클래스 = 태스크매니저.겟모델클래스포태스크("text-classification")
표준태스크 = 태스크매니저.맵프롬시노님("sentiment-analysis")
```

표준 Python으로는 다음과 같습니다.

```python
from optimum.exporters.tasks import TasksManager

tasks = TasksManager.get_all_tasks()
model_class = TasksManager.get_model_class_for_task("text-classification")
normalized_task = TasksManager.map_from_synonym("sentiment-analysis")
```

## 지원 범위

현재 팩은 `TasksManager`와 모델 task/exporter 탐색 API에 집중합니다. `optimum.onnxruntime`, OpenVINO, Neuron, Habana 등 하드웨어별 backend의 클래스는 각 생태계가 독립적으로 빠르게 변하므로 이번 팩에서 전역 번역하지 않습니다.

`framework=`, `library_name=`, `exporter=` 같은 키워드 인자도 Python 원형을 유지합니다. 같은 이름이 여러 라이브러리에서 사용될 수 있기 때문에 KoPy의 충돌 방지 원칙에 따라 전역 치환하지 않습니다.
