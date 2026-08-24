"""Official Hugging Face Tokenizers library pack for KoPy."""

from __future__ import annotations

from .base import LibraryPack


TOKENIZERS_PACK = LibraryPack(
    name="tokenizers",
    module="tokenizers",
    kopy_module="토크나이저스",
    description="고속 토큰화·어휘 학습·인코딩을 위한 Hugging Face Tokenizers API 팩",
    members={
        # Core tokenizer objects
        "토크나이저": "Tokenizer",
        "인코딩": "Encoding",
        "애디드토큰": "AddedToken",
        "엔코드": "encode",
        "엔코드배치": "encode_batch",
        "디코드": "decode",
        "디코드배치": "decode_batch",
        "프롬파일": "from_file",
        "프롬프리트레인드": "from_pretrained",
        "세이브": "save",
        "트레인": "train",
        "트레인프롬이터레이터": "train_from_iterator",
        "겟보캡": "get_vocab",
        "겟보캡사이즈": "get_vocab_size",
        "토큰투아이디": "token_to_id",
        "아이디투토큰": "id_to_token",
        "애드토큰스": "add_tokens",
        "애드스페셜토큰스": "add_special_tokens",
        "이네이블패딩": "enable_padding",
        "노패딩": "no_padding",
        "이네이블트렁케이션": "enable_truncation",
        "노트렁케이션": "no_truncation",

        # Encoding fields/methods
        "아이디스": "ids",
        "토큰스": "tokens",
        "어텐션마스크": "attention_mask",
        "타입아이디스": "type_ids",
        "오프셋스": "offsets",
        "스페셜토큰스마스크": "special_tokens_mask",
        "워드아이디스": "word_ids",
        "시퀀스아이디스": "sequence_ids",
        "차투토큰": "char_to_token",
        "토큰투차스팬": "token_to_chars",

        # Models
        "비피이": "BPE",
        "워드피스": "WordPiece",
        "유니그램": "Unigram",
        "워드레벨": "WordLevel",

        # Trainers
        "비피이트레이너": "BpeTrainer",
        "워드피스트레이너": "WordPieceTrainer",
        "유니그램트레이너": "UnigramTrainer",
        "워드레벨트레이너": "WordLevelTrainer",

        # Normalizers / pre-tokenizers / decoders / processors
        "버트노멀라이저": "BertNormalizer",
        "로어케이스": "Lowercase",
        "엔에프씨": "NFC",
        "엔에프케이씨": "NFKC",
        "시퀀스": "Sequence",
        "화이트스페이스": "Whitespace",
        "화이트스페이스스플릿": "WhitespaceSplit",
        "바이트레벨": "ByteLevel",
        "버트프리토크나이저": "BertPreTokenizer",
        "메타스페이스": "Metaspace",
        "워드피스디코더": "WordPiece",
        "비피이디코더": "BPEDecoder",
        "바이트레벨디코더": "ByteLevel",
        "템플릿프로세싱": "TemplateProcessing",
        "버트프로세싱": "BertProcessing",
    },
    member_descriptions={
        "Tokenizer": "토큰화 파이프라인 전체를 구성하고 실행하는 핵심 객체입니다.",
        "Encoding": "토큰 ID, 문자열 토큰, 오프셋과 마스크를 담는 인코딩 결과입니다.",
        "encode": "문자열 하나를 토큰화해 Encoding으로 반환합니다.",
        "encode_batch": "여러 입력을 한 번에 토큰화합니다.",
        "decode": "토큰 ID 시퀀스를 문자열로 복원합니다.",
        "train_from_iterator": "메모리의 문자열 반복자에서 새 어휘를 학습합니다.",
        "get_vocab": "현재 토크나이저의 token→id 어휘 사전을 반환합니다.",
        "WordPiece": "BERT 계열에서 널리 쓰이는 WordPiece 토큰화 모델입니다.",
        "BPE": "빈도 기반 병합 규칙을 학습하는 Byte Pair Encoding 모델입니다.",
        "Whitespace": "공백과 구두점을 기준으로 입력을 사전 토큰화합니다.",
        "WordPieceTrainer": "WordPiece 모델의 어휘를 학습하는 trainer입니다.",
        "TemplateProcessing": "[CLS], [SEP] 같은 특수 토큰을 최종 시퀀스에 배치합니다.",
    },
    examples={
        "Tokenizer": (
            "프롬 토크나이저스 임포트 토크나이저\n",
            "from tokenizers import Tokenizer\n",
        ),
        "encode": (
            "결과 = 토크나이저.엔코드(\"안녕하세요\")",
            "result = tokenizer.encode(\"안녕하세요\")",
        ),
        "decode": (
            "텍스트 = 토크나이저.디코드(결과.아이디스)",
            "text = tokenizer.decode(result.ids)",
        ),
        "train_from_iterator": (
            "토크나이저.트레인프롬이터레이터(말뭉치, 트레이너)",
            "tokenizer.train_from_iterator(corpus, trainer)",
        ),
    },
)
