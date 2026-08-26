# sqlite-vec Library Pack

KoPy 0.5.42 adds namespace-scoped support for `sqlite-vec`, a small vector-search extension that runs inside SQLite.

## Why sqlite-vec

`sqlite-vec` is useful for learning and local RAG because it needs no vector-database server. A normal Python `sqlite3.Connection` can load the extension, store vectors in a `vec0` virtual table, and run KNN queries with SQL. KoPy keeps the SQLite and retrieval concepts visible instead of hiding them behind a new abstraction.

The pack targets stable `sqlite-vec 0.1.9`. The upstream project is still pre-1.0, so its API may change more quickly than mature libraries.

## Supported Python binding helpers

KoPy transliterates the small Python-specific public binding surface:

- `load` → `로드`
- `serialize_float32` → `시리얼라이즈플로트32`
- `serialize_int8` → `시리얼라이즈인트8`

Example:

```kopy
임포트 sqlite3
임포트 에스큐엘라이트벡 애즈 sv

connection = sqlite3.connect(":memory:")
connection.enable_load_extension(True)
sv.로드(connection)
connection.enable_load_extension(False)

embedding = [1.0, 0.0, 0.0]
blob = sv.시리얼라이즈플로트32(embedding)
```

This translates to normal Python using `sqlite_vec.load()` and `sqlite_vec.serialize_float32()`.

## Translation policy

The following vocabulary intentionally stays in original Python/SQL form:

- `connection`, `query`, `embedding`, `rowid`, `distance`, `rows`
- `execute()`, `fetchone()`, `fetchall()`
- SQL statements and `vec0` virtual-table syntax
- SQL functions such as `vec_version()` and distance expressions

These names are transferable SQLite and vector-search concepts. They are not safe candidates for global KoPy translations, and keeping them intact helps learners recognize upstream examples and documentation.

KoPy does not rewrite text inside SQL strings. SQL therefore remains exactly the SQL that upstream sqlite-vec expects.

## macOS note

Python's standard `sqlite3` module is not built with loadable-extension support on every platform. This is especially common on macOS, where `sqlite3.Connection` may not expose `enable_load_extension()` at all. That is a Python/SQLite build limitation rather than a KoPy or sqlite-vec translation issue.

For macOS, sqlite-vec upstream recommends a Homebrew Python linked against a SQLite build that permits extensions. KoPy CI therefore keeps the normal Python 3.12.10 matrix, skips only the unsupported extension-loading runtime on that interpreter, and separately executes the real `vec0` KNN test with Homebrew `python@3.12`.

## Local KNN example

```kopy
connection.execute(
    "CREATE VIRTUAL TABLE vec_items USING vec0(embedding float[3])"
)

connection.execute(
    "INSERT INTO vec_items(rowid, embedding) VALUES (?, ?)",
    [1, sv.시리얼라이즈플로트32([1.0, 0.0, 0.0])],
)

query = [0.95, 0.05, 0.0]
rows = connection.execute(
    "SELECT rowid, distance FROM vec_items "
    "WHERE embedding MATCH ? ORDER BY distance LIMIT 2",
    [sv.시리얼라이즈플로트32(query)],
).fetchall()
```

The full runnable example is `examples/sqlite_vec_local_search.kpy`.

## Installation

```powershell
python -m pip install sqlite-vec==0.1.9
```

On macOS, if the interpreter has no `enable_load_extension()`, use Homebrew Python 3.12 instead of changing KoPy's translation rules:

```bash
brew install python@3.12
$(brew --prefix python@3.12)/bin/python3.12 -m pip install sqlite-vec==0.1.9
```

The Python wheel bundles the native extension for the supported platform. KoPy itself keeps no runtime dependency on sqlite-vec; the pack is only activated when the library is imported.
