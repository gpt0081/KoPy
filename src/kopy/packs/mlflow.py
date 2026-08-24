"""Official MLflow library pack for KoPy.

The pack focuses on experiment tracking, run lifecycle, metrics/parameters,
artifacts, model registry helpers, and the high-level fluent API. MLflow itself
remains the runtime implementation; KoPy only transliterates names.
"""

from __future__ import annotations

from .base import LibraryPack


MLFLOW_PACK = LibraryPack(
    name="mlflow",
    module="mlflow",
    kopy_module="엠엘플로우",
    preferred_aliases=("mlf",),
    description="AI 실험 추적·파라미터·메트릭·아티팩트·모델 기록을 위한 MLflow API 팩",
    members={
        # Tracking configuration / experiment lifecycle
        "셋트래킹유알아이": "set_tracking_uri",
        "겟트래킹유알아이": "get_tracking_uri",
        "셋레지스트리유알아이": "set_registry_uri",
        "겟레지스트리유알아이": "get_registry_uri",
        "셋익스페리먼트": "set_experiment",
        "크리에이트익스페리먼트": "create_experiment",
        "겟익스페리먼트": "get_experiment",
        "겟익스페리먼트바이네임": "get_experiment_by_name",
        "딜리트익스페리먼트": "delete_experiment",
        "리스토어익스페리먼트": "restore_experiment",
        "셋익스페리먼트태그": "set_experiment_tag",
        "서치익스페리먼츠": "search_experiments",

        # Run lifecycle
        "스타트런": "start_run",
        "엔드런": "end_run",
        "액티브런": "active_run",
        "라스트액티브런": "last_active_run",
        "겟런": "get_run",
        "서치런즈": "search_runs",

        # Logging
        "로그파람": "log_param",
        "로그파람즈": "log_params",
        "로그메트릭": "log_metric",
        "로그메트릭스": "log_metrics",
        "로그아티팩트": "log_artifact",
        "로그아티팩츠": "log_artifacts",
        "로그딕트": "log_dict",
        "로그텍스트": "log_text",
        "로그테이블": "log_table",
        "로그인풋": "log_input",
        "로그인풋스": "log_inputs",
        "셋태그": "set_tag",
        "셋태그스": "set_tags",
        "딜리트태그": "delete_tag",

        # Model helpers / registry
        "로그모델": "log_model",
        "로드모델": "load_model",
        "세이브모델": "save_model",
        "레지스터모델": "register_model",
        "겟모델버전": "get_model_version",
        "서치모델버전즈": "search_model_versions",
        "트랜지션모델버전스테이지": "transition_model_version_stage",

        # Client / automation helpers
        "엠엘플로우클라이언트": "MlflowClient",
        "오토로그": "autolog",
        "플러시트레이스비동기로그": "flush_trace_async_logging",

        # Common entity attributes/methods exposed on MLflow objects
        "런아이디": "run_id",
        "익스페리먼트아이디": "experiment_id",
        "아티팩트유알아이": "artifact_uri",
        "라이프사이클스테이지": "lifecycle_stage",
        "데이터": "data",
        "인포": "info",
        "파람즈": "params",
        "메트릭스": "metrics",
        "태그스": "tags",
    },
    member_descriptions={
        "set_tracking_uri": "MLflow Tracking 저장소의 URI를 설정합니다.",
        "set_experiment": "활성 실험을 이름으로 선택하거나 없으면 생성합니다.",
        "start_run": "새 MLflow run을 시작하며 컨텍스트 매니저로도 사용할 수 있습니다.",
        "end_run": "현재 활성 run을 종료합니다.",
        "log_param": "현재 run에 하나의 하이퍼파라미터를 기록합니다.",
        "log_params": "현재 run에 여러 하이퍼파라미터를 한 번에 기록합니다.",
        "log_metric": "현재 run에 하나의 수치 metric을 기록합니다.",
        "log_metrics": "현재 run에 여러 metric을 한 번에 기록합니다.",
        "log_artifact": "파일 하나를 현재 run의 artifact로 기록합니다.",
        "log_text": "문자열을 텍스트 artifact로 기록합니다.",
        "set_tag": "현재 run에 태그를 설정합니다.",
        "get_run": "run ID로 기록된 run 정보를 조회합니다.",
        "search_runs": "조건에 맞는 run을 검색합니다.",
        "MlflowClient": "Tracking/Registry 저수준 API에 접근하는 MLflow 클라이언트입니다.",
        "autolog": "지원되는 ML 프레임워크의 학습 정보를 자동 기록하도록 설정합니다.",
    },
    examples={
        "start_run": (
            "임포트 엠엘플로우 애즈 mlf\n위드 mlf.스타트런() 애즈 실행:\n    mlf.로그파람('lr', 0.01)\n    mlf.로그메트릭('loss', 0.25)",
            "import mlflow as mlf\nwith mlf.start_run() as run:\n    mlf.log_param('lr', 0.01)\n    mlf.log_metric('loss', 0.25)",
        ),
        "set_experiment": (
            "mlf.셋익스페리먼트('kopy-demo')",
            "mlf.set_experiment('kopy-demo')",
        ),
        "log_artifact": (
            "mlf.로그아티팩트('metrics.json')",
            "mlf.log_artifact('metrics.json')",
        ),
    },
)
