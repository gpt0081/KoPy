# Tantivy Library Pack

KoPy 0.5.44 adds a namespace-scoped pack for `tantivy`, the Python bindings for the Rust Tantivy full-text search library.

## Scope

KoPy transliterates Tantivy-specific types such as `SchemaBuilder`, `Document`, `Index`, `IndexWriter`, `Searcher`, `SearchResult`, `DocAddress`, and `Query` only when the Tantivy namespace is imported.

```kopy
임포트 탄티비

builder = 탄티비.스키마빌더()
builder.add_text_field("title", stored=True)
builder.add_text_field("body", stored=True)
schema = builder.build()

index = 탄티비.인덱스(schema)
writer = index.writer(heap_size=15_000_000, num_threads=1)

doc = 탄티비.도큐먼트()
doc.add_text("title", "KoPy Python learning")
doc.add_text("body", "KoPy teaches Python syntax and AI libraries")
writer.add_document(doc)
writer.commit()

index.reload()
searcher = index.searcher()
query = index.parse_query("Python KoPy", ["title", "body"])
results = searcher.search(query, 5)
```

The equivalent upstream Python keeps exactly the same search vocabulary:

```python
import tantivy

builder = tantivy.SchemaBuilder()
builder.add_text_field("title", stored=True)
builder.add_text_field("body", stored=True)
schema = builder.build()

index = tantivy.Index(schema)
writer = index.writer(heap_size=15_000_000, num_threads=1)

doc = tantivy.Document()
doc.add_text("title", "KoPy Python learning")
doc.add_text("body", "KoPy teaches Python syntax and AI libraries")
writer.add_document(doc)
writer.commit()

index.reload()
searcher = index.searcher()
query = index.parse_query("Python KoPy", ["title", "body"])
results = searcher.search(query, 5)
```

## Intentionally preserved Python vocabulary

KoPy does not globally translate `index`, `writer`, `searcher`, `query`, `results`, `search()`, `writer()`, `commit()`, `reload()`, `parse_query()`, `add_document()`, `add_text_field()`, field names, or keyword arguments such as `stored=`, `heap_size=`, `num_threads=`, and `limit=`. These names are common information-retrieval concepts or ordinary Python/library methods and preserving them avoids collisions while helping learners recognize upstream Tantivy and search code.

The same rule applies to query syntax strings. Tantivy query language remains untouched.

## Runtime and compatibility

The pack targets KoPy's Python `>=3.12,<3.13` policy. Cross-platform CI installs Tantivy 0.26.x and executes a real in-memory full-text index: schema creation, document insertion, commit, query parsing, search, and stored-document retrieval. No external server or API key is required.
