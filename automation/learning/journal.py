"""Learning journal — live learning events (not a system log).

All pipeline stages write here. ECC console + dashboard subscribe via SSE.
"""

from __future__ import annotations

import json
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from automation.lib.paths import find_repo_root

_lock = threading.Lock()
_seq = 0


def _state_dir(repo_root: Path | None = None) -> Path:
    root = repo_root or find_repo_root()
    path = root / "automation" / "learning" / "state"
    path.mkdir(parents=True, exist_ok=True)
    return path


def journal_path(repo_root: Path | None = None) -> Path:
    return _state_dir(repo_root) / "learning_journal.jsonl"


def session_path(session_id: str, repo_root: Path | None = None) -> Path:
    d = _state_dir(repo_root) / "sessions"
    d.mkdir(parents=True, exist_ok=True)
    return d / f"{session_id}.jsonl"


def activity_path(repo_root: Path | None = None) -> Path:
    return _state_dir(repo_root) / "live_activity.json"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def emit(
    verb: str,
    detail: str,
    *,
    stage: str = "learning",
    dataset: str | None = None,
    mission_id: str | None = None,
    session_id: str | None = None,
    progress: float | None = None,
    current_task: str | None = None,
    current_entity: str | None = None,
    current_document: str | None = None,
    current_source: str | None = None,
    current_relationship: str | None = None,
    confidence: float | None = None,
    status: str = "running",  # started | progress | completed | error | warning
    duration_ms: float | None = None,
    meta: dict[str, Any] | None = None,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """Emit a learning journal event immediately (append-only, thread-safe)."""
    global _seq
    with _lock:
        _seq += 1
        seq = _seq
        row = {
            "seq": seq,
            "ts": utc_now_iso(),
            "verb": verb,
            "detail": detail,
            "stage": stage,
            "status": status,
            "dataset": dataset,
            "mission_id": mission_id,
            "session_id": session_id,
            "progress": progress,
            "current_task": current_task or detail,
            "current_entity": current_entity,
            "current_document": current_document,
            "current_source": current_source,
            "current_relationship": current_relationship,
            "confidence": confidence,
            "duration_ms": duration_ms,
            "meta": meta or {},
        }
        path = journal_path(repo_root)
        with path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
        if session_id:
            sp = session_path(session_id, repo_root)
            with sp.open("a", encoding="utf-8", newline="\n") as handle:
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
        # live activity snapshot for dashboard "what is IDA doing now"
        write_activity(
            {
                "updated_at": row["ts"],
                "session_id": session_id,
                "mission_id": mission_id,
                "status": status if status != "completed" else "running",
                "verb": verb,
                "stage": stage,
                "progress": progress,
                "current_thought": detail,
                "current_task": current_task or detail,
                "current_entity": current_entity,
                "current_document": current_document,
                "current_source": current_source,
                "current_dataset": dataset,
                "current_relationship": current_relationship,
                "current_confidence": confidence,
                "last_event": row,
            },
            repo_root=repo_root,
        )
    return row


def write_activity(data: dict[str, Any], repo_root: Path | None = None) -> None:
    path = activity_path(repo_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def read_activity(repo_root: Path | None = None) -> dict[str, Any]:
    path = activity_path(repo_root)
    if not path.exists():
        return {
            "status": "idle",
            "current_thought": "Idle — Continuous Learning standing by",
            "progress": 0,
        }
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"status": "idle", "current_thought": "Waiting for first execution"}


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


def load_session(session_id: str, repo_root: Path | None = None) -> list[dict[str, Any]]:
    path = session_path(session_id, repo_root)
    if not path.exists():
        return []
    out: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return out


def list_sessions(repo_root: Path | None = None) -> list[dict[str, Any]]:
    d = _state_dir(repo_root) / "sessions"
    if not d.exists():
        return []
    sessions = []
    for path in sorted(d.glob("*.jsonl"), reverse=True):
        events = load_session(path.stem, repo_root)
        sessions.append(
            {
                "session_id": path.stem,
                "events": len(events),
                "started": events[0].get("ts") if events else None,
                "ended": events[-1].get("ts") if events else None,
                "last_verb": events[-1].get("verb") if events else None,
            }
        )
    return sessions


def journal_offset(repo_root: Path | None = None) -> int:
    """Byte size of journal file — used by SSE tailer."""
    path = journal_path(repo_root)
    if not path.exists():
        return 0
    return path.stat().st_size
