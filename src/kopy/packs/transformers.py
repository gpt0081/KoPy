"""Official Hugging Face Transformers library pack for KoPy.

Covers the common pretrained-model, tokenizer, generation, pipeline and Trainer
workflow used in modern NLP/LLM development. The actual implementation remains
upstream Hugging Face Transformers.
"""

from __future__ import annotations

from .base import LibraryPack


TRANSFORMERS_PACK = LibraryPack(
    name="transformers",
    module="transformers",
    kopy_module="트랜스포머스",
    description="사전학습 모델·토크나이저·텍스트 생성·학습을 위한 Hugging Face Transformers API 팩",
    members={
        # Auto classes / base classes
        "오토컨피그": "AutoConfig",
        "오토토크나이저": "AutoTokenizer",
        "오토모델": "AutoModel",
        "오토모델포시퀀스클래시피케이션": "AutoModelForSequenceClassification",
        "오토모델포토큰클래시피케이션": "AutoModelForTokenClassification",
        "오토모델포퀘스천앤서링": "AutoModelForQuestionAnswering",
        "오토모델포마스크드엘엠": "AutoModelForMaskedLM",
        "오토모델포코절엘엠": "AutoModelForCausalLM",
        "오토모델포시퀀스투시퀀스엘엠": "AutoModelForSeq2SeqLM",
        "프리트레인드모델": "PreTrainedModel",
        "프리트레인드토크나이저": "PreTrainedTokenizer",
        "프리트레인드토크나이저패스트": "PreTrainedTokenizerFast",

        # Common concrete classes useful for offline/local tests and education
        "버트컨피그": "BertConfig",
        "버트모델": "BertModel",
        "지피티2컨피그": "GPT2Config",
        "지피티2엘엠헤드모델": "GPT2LMHeadModel",

        # Loading / saving / hub workflow
        "프롬프리트레인드": "from_pretrained",
        "세이브프리트레인드": "save_pretrained",
        "푸시투허브": "push_to_hub",
        "리사이즈토큰임베딩스": "resize_token_embeddings",

        # Tokenization / decoding / chat templates
        "토크나이저": "tokenizer",
        "토크나이즈": "tokenize",
        "인코드": "encode",
        "디코드": "decode",
        "배치디코드": "batch_decode",
        "컨버트토큰스투아이디스": "convert_tokens_to_ids",
        "컨버트아이디스투토큰스": "convert_ids_to_tokens",
        "애드스페셜토큰스": "add_special_tokens",
        "애드토큰스": "add_tokens",
        "어플라이챗템플릿": "apply_chat_template",
        "패드토큰": "pad_token",
        "이오에스토큰": "eos_token",
        "비오에스토큰": "bos_token",
        "언크토큰": "unk_token",
        "마스크토큰": "mask_token",
        "모델맥스렝스": "model_max_length",
        "보캡_사이즈": "vocab_size",
        "리턴_텐서즈": "return_tensors",
        "인풋_아이디즈": "input_ids",
        "아웃풋_아이디즈": "output_ids",
        "어텐션_마스크": "attention_mask",
        "토큰_타입_아이디즈": "token_type_ids",
        "맥스_렝스": "max_length",
        "패딩": "padding",
        "트렁케이션": "truncation",
        "배치_사이즈": "batch_size",

        # Model configuration identifiers / keyword arguments
        "히든_사이즈": "hidden_size",
        "넘_히든_레이어즈": "num_hidden_layers",
        "넘_어텐션_헤즈": "num_attention_heads",
        "인터미디어트_사이즈": "intermediate_size",

        # Model outputs / inference / generation
        "제너레이트": "generate",
        "포워드": "forward",
        "라스트히든스테이트": "last_hidden_state",
        "로짓츠": "logits",
        "로스": "loss",
        "히든스테이츠": "hidden_states",
        "어텐션스": "attentions",
        "제너레이션컨피그": "GenerationConfig",

        # Pipeline API
        "파이프라인": "pipeline",
        "제너레이터": "generator",
        "텍스트제너레이션파이프라인": "TextGenerationPipeline",
        "텍스트클래시피케이션파이프라인": "TextClassificationPipeline",
        "피처익스트랙션파이프라인": "FeatureExtractionPipeline",

        # Training / data collation
        "트레이너": "Trainer",
        "트레이닝아규먼츠": "TrainingArguments",
        "시퀀스투시퀀스트레이너": "Seq2SeqTrainer",
        "시퀀스투시퀀스트레이닝아규먼츠": "Seq2SeqTrainingArguments",
        "데이터콜레이터위드패딩": "DataCollatorWithPadding",
        "데이터콜레이터포랭귀지모델링": "DataCollatorForLanguageModeling",
        "데이터콜레이터포시퀀스투시퀀스": "DataCollatorForSeq2Seq",
        "트레인": "train",
        "이밸류에이트": "evaluate",
        "프리딕트": "predict",

        # Reproducibility / utility
        "셋시드": "set_seed",
    },
    member_descriptions={
        "AutoTokenizer": "모델 이름이나 로컬 경로에 맞는 토크나이저 클래스를 자동으로 선택합니다.",
        "AutoModel": "체크포인트 설정에 맞는 기본 Transformer 모델 클래스를 자동으로 선택합니다.",
        "AutoModelForCausalLM": "다음 토큰 예측 기반 생성형 언어모델 클래스를 자동으로 선택합니다.",
        "AutoModelForSequenceClassification": "문장·문서 분류용 사전학습 모델 클래스를 자동으로 선택합니다.",
        "from_pretrained": "Hugging Face Hub 또는 로컬 경로에서 사전학습 설정·가중치를 불러옵니다.",
        "save_pretrained": "모델이나 토크나이저를 Transformers 표준 형식으로 저장합니다.",
        "apply_chat_template": "채팅 메시지 목록을 모델이 기대하는 프롬프트 형식으로 변환합니다.",
        "generate": "언어모델에서 토큰 시퀀스를 생성합니다.",
        "pipeline": "추론 태스크를 모델·토크나이저와 묶어 간단한 호출 인터페이스로 만듭니다.",
        "Trainer": "Transformers의 범용 모델 학습·평가 루프를 제공합니다.",
        "TrainingArguments": "Trainer의 학습 하이퍼파라미터와 실행 옵션을 정의합니다.",
        "GenerationConfig": "텍스트 생성 전략과 샘플링·길이 관련 설정을 보관합니다.",
        "BertConfig": "BERT 모델 구조를 정의하는 설정 객체입니다.",
        "BertModel": "BERT 인코더 모델 구현입니다.",
        "set_seed": "Python, NumPy, PyTorch 등 지원 백엔드의 난수 시드를 맞춥니다.",
    },
    examples={
        "AutoTokenizer": (
            "프롬 트랜스포머스 임포트 오토토크나이저\n토크나이저 = 오토토크나이저.프롬프리트레인드(\"모델-경로\")",
            "from transformers import AutoTokenizer\ntokenizer = AutoTokenizer.from_pretrained(\"model-path\")",
        ),
        "AutoModelForCausalLM": (
            "프롬 트랜스포머스 임포트 오토모델포코절엘엠\n모델 = 오토모델포코절엘엠.프롬프리트레인드(\"모델-경로\")",
            "from transformers import AutoModelForCausalLM\nmodel = AutoModelForCausalLM.from_pretrained(\"model-path\")",
        ),
        "generate": (
            "아웃풋_아이디즈 = 모델.제너레이트(인풋_아이디즈=인풋_아이디즈)",
            "output_ids = model.generate(input_ids=input_ids)",
        ),
        "pipeline": (
            "프롬 트랜스포머스 임포트 파이프라인\n제너레이터 = 파이프라인(\"text-generation\", 모델=모델, 토크나이저=토크나이저)",
            "from transformers import pipeline\ngenerator = pipeline(\"text-generation\", model=model, tokenizer=tokenizer)",
        ),
    },
)
