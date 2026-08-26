# Ragas Library Pack

KoPy 0.5.37 adds a namespace-scoped pack for [Ragas](https://pypi.org/project/ragas/), focused on RAG/LLM evaluation rather than retrieval itself.

## Compatibility

- KoPy development baseline: Python 3.12.10
- KoPy Python range: `>=3.12,<3.13`
- CI target: `ragas>=0.4.3,<0.5`
- Ragas 0.4.3 requires Python `>=3.9`

The pack follows the Ragas 0.4 collections-based metric API. Legacy metric import paths are not promoted in new KoPy examples.

## Namespace

```kopy
임포트 라가스
프롬 라가스 임포트 이밸류에이션데이터셋, 싱글턴샘플
프롬 라가스.metrics.collections 임포트 논엘엘엠스트링시밀래리티, 디스턴스메저
```

The real dotted package path `ragas.metrics.collections` remains visible. KoPy only transliterates Ragas-specific imported names and attributes.

## Main mappings

| KoPy | Python |
| --- | --- |
| `라가스` | `ragas` |
| `이밸류에이션데이터셋` | `EvaluationDataset` |
| `싱글턴샘플` | `SingleTurnSample` |
| `멀티턴샘플` | `MultiTurnSample` |
| `논엘엘엠스트링시밀래리티` | `NonLLMStringSimilarity` |
| `디스턴스메저` | `DistanceMeasure` |
| `이그잭트매치` | `ExactMatch` |
| `스트링프레즌스` | `StringPresence` |
| `컨텍스트프리시전` | `ContextPrecision` |
| `컨텍스트리콜` | `ContextRecall` |
| `페이스풀니스` | `Faithfulness` |
| `리스폰스그라운디드니스` | `ResponseGroundedness` |
| `팩추얼코렉트니스` | `FactualCorrectness` |
| `시맨틱시밀래리티` | `SemanticSimilarity` |

## Learning-oriented example

```kopy
프롬 라가스 임포트 이밸류에이션데이터셋, 싱글턴샘플
프롬 라가스.metrics.collections 임포트 논엘엘엠스트링시밀래리티, 디스턴스메저

sample = 싱글턴샘플(
    user_input=query,
    response=response,
    reference=reference,
    retrieved_contexts=contexts,
)

dataset = 이밸류에이션데이터셋(samples=[sample])

metric = 논엘엘엠스트링시밀래리티(
    distance_measure=디스턴스메저.LEVENSHTEIN,
)
result = metric.score(reference=reference, response=response)
```

`query`, `response`, `reference`, `contexts`, `user_input`, `retrieved_contexts`, `score()`, `ascore()`, `evaluate()`, and `metrics=` stay in upstream Python form. These are transferable RAG/evaluation concepts, not safe Ragas-only global translations.

## Why the runtime test uses a non-LLM metric

Many Ragas metrics require an evaluator LLM or embedding model. KoPy CI should verify the real library without requiring an API key, remote model, or nondeterministic external service. The runtime test therefore exercises:

1. real `SingleTurnSample`
2. real `EvaluationDataset`
3. real `NonLLMStringSimilarity`
4. real Levenshtein scoring through the new collections API

This confirms both Ragas integration and KoPy translation deterministically on Windows, Ubuntu, and macOS.

## Scope boundary

KoPy does not reimplement Ragas metrics. It only translates supported spellings to the upstream Python API. LLM-backed metrics such as faithfulness or factual correctness still require the model/client configuration expected by Ragas.
