"""Official ONNX Runtime library pack for KoPy."""

from __future__ import annotations

from .base import LibraryPack


ONNXRUNTIME_PACK = LibraryPack(
    name="onnxruntime",
    module="onnxruntime",
    kopy_module="온엑스런타임",
    preferred_aliases=("ort",),
    description="ONNX 모델 로딩·추론·실행 공급자·세션 최적화를 위한 ONNX Runtime API 팩",
    members={
        # Sessions and execution
        "인퍼런스세션": "InferenceSession",
        "세션옵션스": "SessionOptions",
        "런옵션스": "RunOptions",
        "런": "run",
        "런위드아이오바인딩": "run_with_iobinding",
        "런위드오트밸류스": "run_with_ort_values",
        "런위드오트밸류벡터": "run_with_ortvaluevector",
        "아이오바인딩": "io_binding",
        "겟인풋스": "get_inputs",
        "겟아웃풋스": "get_outputs",
        "겟오버라이더블이니셜라이저스": "get_overridable_initializers",
        "겟모델메타": "get_modelmeta",
        "겟프로바이더스": "get_providers",
        "겟프로바이더옵션스": "get_provider_options",
        "셋프로바이더스": "set_providers",
        "엔드프로파일링": "end_profiling",
        "겟프로파일스타트타임엔에스": "get_profiling_start_time_ns",

        # Runtime values / binding
        "오트밸류": "OrtValue",
        "오트디바이스": "OrtDevice",
        "셰이프": "shape",
        "데이터타입": "data_type",
        "디바이스네임": "device_name",
        "이즈텐서": "is_tensor",
        "넘파이": "numpy",
        "업데이트인플레이스": "update_inplace",
        "바인드인풋": "bind_input",
        "바인드아웃풋": "bind_output",
        "바인드씨피유인풋": "bind_cpu_input",
        "바인드오트밸류인풋": "bind_ortvalue_input",
        "바인드오트밸류아웃풋": "bind_ortvalue_output",
        "클리어바인딩인풋스": "clear_binding_inputs",
        "클리어바인딩아웃풋스": "clear_binding_outputs",
        "카피아웃풋스투씨피유": "copy_outputs_to_cpu",
        "싱크로나이즈인풋스": "synchronize_inputs",
        "싱크로나이즈아웃풋스": "synchronize_outputs",

        # Providers / environment
        "겟어베일러블프로바이더스": "get_available_providers",
        "겟올프로바이더스": "get_all_providers",
        "겟디바이스": "get_device",
        "셋시드": "set_seed",
        "셋디폴트로거시버리티": "set_default_logger_severity",
        "셋디폴트로거버보시티": "set_default_logger_verbosity",

        # Session configuration / enums
        "그래프옵티마이제이션레벨": "GraphOptimizationLevel",
        "엑시큐션모드": "ExecutionMode",
        "엑시큐션오더": "ExecutionOrder",
        "오트알로케이터타입": "OrtAllocatorType",
        "오트멤타입": "OrtMemType",
        "디스에이블올": "ORT_DISABLE_ALL",
        "인에이블베이직": "ORT_ENABLE_BASIC",
        "인에이블익스텐디드": "ORT_ENABLE_EXTENDED",
        "인에이블올": "ORT_ENABLE_ALL",
        "시퀀셜": "ORT_SEQUENTIAL",
        "패러럴": "ORT_PARALLEL",

        # SessionOptions methods / fields
        "애드프리세션컨피그엔트리": "add_free_dimension_override_by_name",
        "애드프리세션컨피그디노테이션": "add_free_dimension_override_by_denotation",
        "애드세션컨피그엔트리": "add_session_config_entry",
        "겟세션컨피그엔트리": "get_session_config_entry",
        "레지스터커스텀옵스라이브러리": "register_custom_ops_library",
        "인테라옵넘스레즈": "inter_op_num_threads",
        "인트라옵넘스레즈": "intra_op_num_threads",
        "그래프옵티마이제이션레벨필드": "graph_optimization_level",
        "엑시큐션모드필드": "execution_mode",
        "인에이블프로파일링": "enable_profiling",
        "로그시버리티레벨": "log_severity_level",
        "로그버보시티레벨": "log_verbosity_level",
        "옵티마이즈드모델파일패스": "optimized_model_filepath",
    },
    member_descriptions={
        "InferenceSession": "ONNX 모델을 로드하고 지정된 실행 공급자에서 추론 세션을 만듭니다.",
        "run": "입력 피드를 사용해 세션 추론을 실행하고 요청한 출력을 반환합니다.",
        "get_inputs": "모델 입력 메타데이터 목록을 반환합니다.",
        "get_outputs": "모델 출력 메타데이터 목록을 반환합니다.",
        "get_available_providers": "현재 설치 환경에서 사용할 수 있는 실행 공급자 목록을 반환합니다.",
        "SessionOptions": "그래프 최적화, 스레드, 프로파일링 등 세션 실행 옵션을 설정합니다.",
        "GraphOptimizationLevel": "ONNX Runtime 그래프 최적화 수준을 지정하는 열거형입니다.",
        "OrtValue": "ONNX Runtime이 사용하는 텐서·시퀀스 등의 런타임 값 래퍼입니다.",
        "io_binding": "입출력 메모리 위치를 직접 바인딩하기 위한 IOBinding 객체를 만듭니다.",
    },
    examples={
        "InferenceSession": (
            "임포트 온엑스런타임 애즈 ort\n세션 = ort.인퍼런스세션(\"model.onnx\")",
            "import onnxruntime as ort\nsession = ort.InferenceSession(\"model.onnx\")",
        ),
        "run": (
            "결과 = 세션.런(None, {입력이름: 입력배열})",
            "outputs = session.run(None, {input_name: input_array})",
        ),
        "get_available_providers": (
            "프로바이더 = ort.겟어베일러블프로바이더스()",
            "providers = ort.get_available_providers()",
        ),
    },
)
