"""Learning journal — human-readable learning events for ECC console."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from automation.lib.paths import find_repo_root


def journal_path(repo_root: Path | None = None) -> Path:
    root = repo_root or find_repo_root()
    path = root / "automation" / "learning" / "state" / "learning_journal.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def emit(
    verb: str,
    detail: str,
    *,
    stage: str = "learning",
    dataset: str | None = None,
    mission_id: str | None = None,
    meta: dict[str, Any] | None = None,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    from datetime import datetime, timezone

    row = {
        "ts": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "verb": verb,
        "detail": detail,
        "stage": stage,
        "dataset": dataset,
        "mission_id": mission_id,
        "meta": meta or {},
    }
    path = journal_path(repo_root)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


def recent(limit: int = 100, repo_root: Path | None = None) -> list[dict[str, Any]]:
    path = journal_path(repo_root)
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    out: list[dict[str, Any]] = []
    for line in lines[-limit:]:
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return out
