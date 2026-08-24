# KoPy Polars Pack

KoPy 0.5.18 adds a namespace-scoped Polars pack for fast tabular data preparation in AI and machine-learning workflows.

## Import

```python
임포트 폴라스 애즈 pl
```

translates to:

```python
import polars as pl
```

The pack is activated only after `polars` / `폴라스` is imported. Polars names are not added to KoPy's global translation table.

## Example

```python
임포트 폴라스 애즈 pl

df = pl.데이터프레임({
    "label": ["A", "A", "B", "B"],
    "x": [1, 2, 3, 4],
})

features = df.위드컬럼즈(
    (pl.컬("x") * 2).에일리어스("x2")
)

summary = (
    features
    .필터(pl.컬("x2") >= 4)
    .그룹바이("label")
    .어그(pl.컬("x2").미인().에일리어스("x2_mean"))
)
```

This becomes ordinary Polars Python:

```python
import polars as pl

df = pl.DataFrame({
    "label": ["A", "A", "B", "B"],
    "x": [1, 2, 3, 4],
})

features = df.with_columns(
    (pl.col("x") * 2).alias("x2")
)

summary = (
    features
    .filter(pl.col("x2") >= 4)
    .group_by("label")
    .agg(pl.col("x2").mean().alias("x2_mean"))
)
```

## Covered API areas

The pack covers the stable, common surfaces used for ML data preparation:

- `DataFrame`, `LazyFrame`, `Series`, `Expr`
- `read_csv`, `read_parquet`, `scan_csv`, `scan_parquet`
- `col`, `lit`, `when`, `then`, `otherwise`
- `select`, `with_columns`, `filter`, `group_by`, `agg`, `sort`, `join`, `concat`
- null/NaN handling and dtype casting
- lazy execution with `lazy`, `collect`, and `explain`
- common reductions and DataFrame export helpers

Use `kopy packs polars` to inspect the registered names.

## Keyword arguments stay in Python spelling

Keyword arguments such as `has_header=`, `separator=`, `schema=`, `strict=`, `maintain_order=`, and `streaming=` intentionally remain unchanged. They are API contract names and translating them globally would create ambiguity with other libraries.

## Learning policy

KoPy does not try to erase conventional Python/data-science notation. Examples intentionally retain familiar names such as `df`, `features`, and `summary` where useful, so the learner sees the same structural vocabulary used in ordinary Python code.

## Runtime policy

KoPy does not reimplement Polars. The runtime test installs the real Polars package, translates KoPy source, and executes real `DataFrame`, expression, group-by, and lazy-query operations.
