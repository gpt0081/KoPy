"""Official Hugging Face Optimum library pack for KoPy.

This pack focuses on Optimum's model-export task management APIs. Hardware-
specific backends remain in their own Python namespaces and are not guessed.
"""

from __future__ import annotations

from .base import LibraryPack


OPTIMUM_PACK = LibraryPack(
    name="optimum",
    module="optimum",
    kopy_module="옵티멈",
    preferred_aliases=(),
    description="Transformers 모델의 내보내기·하드웨어 최적화 흐름을 연결하는 Hugging Face Optimum 팩",
    members={
        "태스크매니저": "TasksManager",
        "겟올태스크스": "get_all_tasks",
        "겟모델클래스포태스크": "get_model_class_for_task",
        "겟서포티드태스크스포모델타입": "get_supported_tasks_for_model_type",
        "겟서포티드모델타입포태스크": "get_supported_model_type_for_task",
        "겟익스포터컨피그컨스트럭터": "get_exporter_config_constructor",
        "맵프롬시노님": "map_from_synonym",
        "시노님스포태스크": "synonyms_for_task",
        "인퍼태스크프롬모델": "infer_task_from_model",
        "인퍼라이브러리프롬모델": "infer_library_from_model",
        "디터민프레임워크": "determine_framework",
        "스탠더다이즈모델어트리뷰츠": "standardize_model_attributes",
        "크리에이트레지스터": "create_register",
    },
    member_descriptions={
        "TasksManager": "모델 작업, 모델 클래스와 내보내기 구성을 연결하는 Optimum의 중앙 작업 관리자입니다.",
        "get_all_tasks": "Optimum이 알고 있는 전체 모델 작업 이름을 반환합니다.",
        "get_model_class_for_task": "지정한 작업에 대응하는 Transformers AutoModel 클래스를 찾습니다.",
        "get_supported_tasks_for_model_type": "특정 모델 아키텍처와 exporter 조합이 지원하는 작업을 조회합니다.",
        "get_exporter_config_constructor": "모델과 작업에 맞는 exporter 설정 생성자를 조회합니다.",
        "map_from_synonym": "작업 별칭을 Optimum의 표준 작업 이름으로 정규화합니다.",
        "infer_task_from_model": "모델 또는 모델 클래스에서 작업 종류를 추론합니다.",
        "determine_framework": "모델을 내보낼 때 사용할 프레임워크를 판정합니다.",
    },
    examples={
        "TasksManager": (
            "프롬 옵티멈.exporters.tasks 임포트 태스크매니저\n태스크들 = 태스크매니저.겟올태스크스()",
            "from optimum.exporters.tasks import TasksManager\ntasks = TasksManager.get_all_tasks()",
        ),
        "get_model_class_for_task": (
            "프롬 옵티멈.exporters.tasks 임포트 태스크매니저\n클래스 = 태스크매니저.겟모델클래스포태스크('text-classification')",
            "from optimum.exporters.tasks import TasksManager\nmodel_class = TasksManager.get_model_class_for_task('text-classification')",
        ),
    },
)
