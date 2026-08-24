# KoPy SentencePiece Pack

KoPy 0.5.12 adds a namespace-scoped pack for Google SentencePiece 0.2.2.

KoPy does not reimplement SentencePiece. It translates KoPy API spellings to the real `sentencepiece` Python package, which performs model training, tokenization and detokenization.

## Install

```powershell
python -m pip install "sentencepiece>=0.2.2,<0.3"
```

## Example

```kopy
임포트 센텐스피스 애즈 spm

spm.센텐스피스트레이너.트레인(
    input="corpus.txt",
    model_prefix="m",
    vocab_size=8000,
)

토크나이저 = spm.센텐스피스프로세서(model_file="m.model")
피시들 = 토크나이저.엔코드("안녕하세요", out_type=str)
아이디들 = 토크나이저.엔코드("안녕하세요", out_type=int)
복원 = 토크나이저.디코드(아이디들)
```

Equivalent Python:

```python
import sentencepiece as spm

spm.SentencePieceTrainer.train(
    input="corpus.txt",
    model_prefix="m",
    vocab_size=8000,
)

tokenizer = spm.SentencePieceProcessor(model_file="m.model")
pieces = tokenizer.encode("안녕하세요", out_type=str)
ids = tokenizer.encode("안녕하세요", out_type=int)
restored = tokenizer.decode(ids)
```

## Scope and compatibility

The pack covers the processor/trainer classes, encode/decode, vocabulary lookup, normalization and common sampling helpers. Keyword arguments such as `input=`, `model_prefix=`, `vocab_size=`, `out_type=`, `model_file=`, `nbest_size=` and `alpha=` remain standard Python. They are not globally transliterated because identical keyword names can appear in unrelated libraries.

The pack activates only when `sentencepiece` or `센텐스피스` is imported. Bare words are not translated globally.
