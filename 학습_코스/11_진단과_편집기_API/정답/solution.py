from kopy.editor import diagnose_source


def 진단_요약(source: str) -> dict:
    payload = diagnose_source(source, "exercise.kpy")
    diagnostics = payload["diagnostics"]
    return {
        "ok": payload["ok"],
        "errors": sum(item["severity"] == "error" for item in diagnostics),
        "warnings": sum(item["severity"] == "warning" for item in diagnostics),
        "codes": [item["code"] for item in diagnostics],
    }
