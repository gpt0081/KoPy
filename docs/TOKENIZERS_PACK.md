# KoPy Hugging Face Tokenizers Pack

KoPy v0.5.6 adds a namespace-scoped pack for `tokenizers`.

The pack translates API names only after `tokenizers` / `토크나이저스` is imported. The real Hugging Face Tokenizers library still performs tokenization, vocabulary training and encoding.

CI baseline: Tokenizers 0.22.2. Although Tokenizers 0.23.1 is the newest standalone stable release, Transformers 5.15.x currently requires `tokenizers<=0.23.0`, so KoPy tests the latest stable line that is compatible with the rest of its pinned AI stack.

## Example

```kopy
프롬 토크나이저스 임포트 토크나이저
프롬 토크나이저스.models 임포트 워드피스
프롬 토크나이저스.pre_tokenizers 임포트 화이트스페이스

모델 = 워드피스(vocab={"[UNK]": 0, "hello": 1, "world": 2}, unk_token="[UNK]")
토크 = 토크나이저(모델)
토크.pre_tokenizer = 화이트스페이스()
결과 = 토크.엔코드("hello world")
프린트(결과.토큰스)
프린트(결과.아이디스)
```

This becomes normal Python using `Tokenizer`, `WordPiece`, `Whitespace`, `encode`, `tokens` and `ids`.

## Scope

The initial pack covers the core Tokenizer/Encoding API, BPE/WordPiece/Unigram/WordLevel models, common trainers, normalizers, pre-tokenizers, decoders and post-processors.

Submodule path names such as `models`, `pre_tokenizers`, `normalizers`, `decoders` and `processors` remain in their original Python spelling. Keyword arguments such as `vocab`, `unk_token`, `special_tokens`, `min_frequency` and `vocab_size` also remain unchanged. This avoids ambiguous global keyword translation across different AI libraries.

## Runtime validation

CI installs the real `tokenizers` package and constructs a WordPiece tokenizer entirely in memory. The smoke test verifies real encoding output without downloading a model or tokenizer from the Hugging Face Hub.
