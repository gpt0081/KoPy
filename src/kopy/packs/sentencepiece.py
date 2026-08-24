"""Official Google SentencePiece library pack for KoPy.

The pack targets the modern Python API used for subword tokenization and model
training. Training keyword arguments stay in standard Python spelling to avoid
cross-library ambiguity.
"""

from __future__ import annotations

from .base import LibraryPack


SENTENCEPIECE_PACK = LibraryPack(
    name="sentencepiece",
    module="sentencepiece",
    kopy_module="센텐스피스",
    preferred_aliases=("spm",),
    description="SentencePiece 서브워드 토크나이저의 학습·인코딩·디코딩·어휘 조회 API 팩",
    members={
        "센텐스피스프로세서": "SentencePieceProcessor",
        "센텐스피스트레이너": "SentencePieceTrainer",
        "트레인": "train",
        "로드": "load",
        "엔코드": "encode",
        "디코드": "decode",
        "엔코드애즈피시즈": "encode_as_pieces",
        "엔코드애즈아이디스": "encode_as_ids",
        "디코드피시즈": "decode_pieces",
        "디코드아이디스": "decode_ids",
        "겟피스사이즈": "get_piece_size",
        "피스토아이디": "piece_to_id",
        "아이디투피스": "id_to_piece",
        "겟스코어": "get_score",
        "이즈언노운": "is_unknown",
        "이즈컨트롤": "is_control",
        "이즈언유즈드": "is_unused",
        "이즈바이트": "is_byte",
        "언크아이디": "unk_id",
        "보스아이디": "bos_id",
        "이오스아이디": "eos_id",
        "패드아이디": "pad_id",
        "노멀라이즈": "normalize",
        "세트엔코드엑스트라옵션스": "set_encode_extra_options",
        "세트디코드엑스트라옵션스": "set_decode_extra_options",
        "샘플엔코드애즈피시즈": "sample_encode_as_pieces",
        "샘플엔코드애즈아이디스": "sample_encode_as_ids",
        "엔베스트엔코드애즈피시즈": "nbest_encode_as_pieces",
        "엔베스트엔코드애즈아이디스": "nbest_encode_as_ids",
        "시리얼라이즈드모델프로토": "serialized_model_proto",
    },
    member_descriptions={
        "SentencePieceProcessor": "학습된 SentencePiece 모델을 로드하고 텍스트를 인코딩·디코딩하는 핵심 클래스입니다.",
        "SentencePieceTrainer": "원시 텍스트에서 SentencePiece 모델을 학습하는 API를 제공합니다.",
        "train": "말뭉치에서 SentencePiece 모델과 vocabulary를 학습합니다.",
        "encode": "문자열을 subword piece 또는 vocabulary ID로 변환합니다.",
        "decode": "piece 또는 vocabulary ID를 원래 텍스트로 복원합니다.",
        "get_piece_size": "학습된 vocabulary의 전체 piece 수를 반환합니다.",
        "piece_to_id": "piece 문자열을 vocabulary ID로 변환합니다.",
        "id_to_piece": "vocabulary ID를 piece 문자열로 변환합니다.",
        "normalize": "SentencePiece 모델의 정규화 규칙으로 입력 문자열을 정규화합니다.",
    },
    examples={
        "SentencePieceProcessor": (
            "임포트 센텐스피스 애즈 spm\n토크나이저 = spm.센텐스피스프로세서(model_file='model.model')",
            "import sentencepiece as spm\ntokenizer = spm.SentencePieceProcessor(model_file='model.model')",
        ),
        "train": (
            "임포트 센텐스피스 애즈 spm\nspm.센텐스피스트레이너.트레인(input='corpus.txt', model_prefix='m', vocab_size=8000)",
            "import sentencepiece as spm\nspm.SentencePieceTrainer.train(input='corpus.txt', model_prefix='m', vocab_size=8000)",
        ),
        "encode": (
            "피시들 = 토크나이저.엔코드('안녕하세요', out_type=스트링)",
            "pieces = tokenizer.encode('안녕하세요', out_type=str)",
        ),
        "decode": (
            "텍스트 = 토크나이저.디코드(아이디들)",
            "text = tokenizer.decode(ids)",
        ),
    },
)
