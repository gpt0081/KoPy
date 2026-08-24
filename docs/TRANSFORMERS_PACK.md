# KoPy Transformers Pack

KoPy 0.5.4부터 Hugging Face Transformers를 라이브러리 팩으로 지원합니다.

실제 모델 로딩, 추론, 학습은 원래 `transformers` 라이브러리가 담당합니다. KoPy는 import된 Transformers 네임스페이스 안에서 API 이름을 안전하게 한글 음역으로 변환합니다.

## 설치

```powershell
python -m pip install "transformers>=5.15,<5.16" torch
```

## 예시

```kopy
프롬 트랜스포머스 임포트 오토토크나이저, 오토모델포코절엘엠

토크나이저 = 오토토크나이저.프롬프리트레인드("local-model")
모델 = 오토모델포코절엘엠.프롬프리트레인드("local-model")
입력값 = 토크나이저("안녕하세요", return_tensors="pt")
출력 = 모델.제너레이트(**입력값)
텍스트 = 토크나이저.배치디코드(출력)
```

키워드 인자 이름(`return_tensors`, `model`, `tokenizer`, `input_ids` 등)은 아직 Python 원형을 유지합니다. 이 이름들을 전역 치환하면 다른 라이브러리와 충돌할 수 있으므로 별도의 안전한 keyword-argument 계층이 생기기 전까지 번역하지 않습니다.

## 주요 범위

- `AutoTokenizer`, `AutoModel`, `AutoModelForCausalLM`, 분류/QA/MLM/Seq2Seq Auto 클래스
- `from_pretrained`, `save_pretrained`, `generate`
- `tokenize`, `encode`, `decode`, `batch_decode`, `apply_chat_template`
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
