"""Persistent KoPy user settings."""

from __future__ import annotations

import json
from pathlib import Path

CONFIG_DIR = Path.home() / ".kopy"
CONFIG_FILE = CONFIG_DIR / "config.json"
DEFAULT_CONFIG = {"spelling": True}


def load_config() -> dict[str, bool]:
    if not CONFIG_FILE.exists():
        return DEFAULT_CONFIG.copy()

    try:
        data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return DEFAULT_CONFIG.copy()

    return {
        "spelling": bool(data.get("spelling", DEFAULT_CONFIG["spelling"])),
    }


def save_config(config: dict[str, bool]) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(
        json.dumps(config, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def spelling_enabled() -> bool:
    return bool(load_config()["spelling"])


def set_spelling_enabled(enabled: bool) -> None:
    config = load_config()
    config["spelling"] = enabled
    save_config(config)
