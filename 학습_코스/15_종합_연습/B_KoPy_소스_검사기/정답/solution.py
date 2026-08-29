from __future__ import annotations

import argparse
import json
from pathlib import Path

from kopy.editor import diagnose_source
from kopy.translator import translate


def 검사(source: str, filename: str = "<source>") -> dict:
    translation = translate(source)
    diagnosis = diagnose_source(source, filename)
    pairs = []
    seen = set()
    for before, after, _line, _column in translation.replacements:
        pair = (before, after)
        if pair not in seen:
            seen.add(pair)
            pairs.append([before, after])
    return {
        "python": translation.python,
        "replacement_count": len(translation.replacements),
        "pairs": pairs,
        "ok": diagnosis["ok"],
        "diagnostics": diagnosis["diagnostics"],
    }


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="KoPy 소스를 실행하지 않고 검사합니다.")
    parser.add_argument("file")
    args = parser.parse_args(argv)
    path = Path(args.file)
    result = 검사(path.read_text(encoding="utf-8"), str(path))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
