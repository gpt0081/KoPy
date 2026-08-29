import json
import tempfile
from pathlib import Path

data = {"language": "KoPy", "purpose": "학습"}

with tempfile.TemporaryDirectory() as temporary_directory:
    path = Path(temporary_directory) / "data.json"
    content = json.dumps(data, ensure_ascii=False, sort_keys=True)
    path.write_text(content, encoding="utf-8")
    restored = json.loads(path.read_text(encoding="utf-8"))
    print(restored["language"])
    print(restored["purpose"])
