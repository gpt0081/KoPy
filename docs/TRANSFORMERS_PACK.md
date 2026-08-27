# KoPy Transformers Pack

KoPy 0.5.4부터 Hugging Face Transformers를 라이브러리 팩으로 지원합니다.

실제 모델 로딩, 추론, 학습은 원래 `transformers` 라이브러리가 담당합니다. KoPy는 import된 Transformers 네임스페이스 안에서 API 이름과 식별자를 안전하게 한글 음역으로 변환합니다.

## 설치

```powershell
python -m pip install "transformers>=5.15,<5.16" torch
```

## 예시

```kopy
프롬 트랜스포머스 임포트 오토토크나이저, 오토모델포코절엘엠

토크나이저 = 오토토크나이저.프롬프리트레인드("local-model")
모델 = 오토모델포코절엘엠.프롬프리트레인드("local-model")
입력값 = 토크나이저("안녕하세요", 리턴_텐서즈="pt")
출력 = 모델.제너레이트(**입력값)
텍스트 = 토크나이저.배치디코드(출력)
```

이 팩은 영어를 가능한 한 한글 음역으로 보여주는 현재 KoPy 원칙을 따릅니다. 예를 들어 `return_tensors → 리턴_텐서즈`, `input_ids → 인풋_아이디즈`, `vocab_size → 보캡_사이즈`, `hidden_size → 히든_사이즈`, `num_attention_heads → 넘_어텐션_헤즈`로 씁니다. `_` 구조는 유지하고 숫자는 음역하지 않습니다. 따라서 `GPT2Config → 지피티2컨피그`이며 `지피티투컨피그`로 쓰지 않습니다.

모델 ID, 태스크명, 문자열 데이터, 숫자 값은 변환하지 않습니다. 예를 들어 `"local-model"`, `"pt"`, `32`, `2`는 그대로 Python에 전달됩니다. 실제 `transformers` 모듈 경로도 원문 구조를 보존합니다.

## BERT 설정 예시

```kopy
프롬 트랜스포머스 임포트 버트컨피그, 버트모델
임포트 토치

컨피그 = 버트컨피그(
    보캡_사이즈=32,
    히든_사이즈=16,
    넘_히든_레이어즈=1,
    넘_어텐션_헤즈=2,
    인터미디어트_사이즈=32,
)

모델 = 버트모델(컨피그)
인풋_아이디즈 = 토치.텐서([[1, 2, 3, 4]])
출력 = 모델(인풋_아이디즈=인풋_아이디즈)
```

원문 Python에서는 각각 `vocab_size`, `hidden_size`, `num_hidden_layers`, `num_attention_heads`, `intermediate_size`, `input_ids`입니다. KoPy 교재에서는 이 대응 관계를 함께 제시해 원문 코드로 자연스럽게 넘어갈 수 있게 합니다.

## 주요 범위

- `AutoTokenizer`, `AutoModel`, `AutoModelForCausalLM`, 분류/QA/MLM/Seq2Seq Auto 클래스
- `from_pretrained`, `save_pretrained`, `generate`
- `tokenize`, `encode`, `decode`, `batch_decode`, `apply_chat_template`
- `return_tensors`, `input_ids`, `attention_mask`, `token_type_ids`, `max_length`, `padding`, `truncation`, `batch_size`
- `vocab_size`, `hidden_size`, `num_hidden_layers`, `num_attention_heads`, `intermediate_size`
- `pipeline`
- `Trainer`, `TrainingArguments`, Seq2Seq Trainer
- Data Collator 계열
- `GenerationConfig`, `set_seed`
- 교육·오프라인 테스트용 `BertConfig`, `BertModel`, `GPT2Config`, `GPT2LMHeadModel`

## 오프라인 검증

CI는 외부 모델 다운로드에 의존하지 않습니다. 작은 `BertConfig`를 메모리에서 생성하고 `BertModel` forward를 실제로 실행합니다.

```powershell
kopy run examples\transformers_bert.kpy
```

예상 shape는 `(1, 4, 16)`입니다.
