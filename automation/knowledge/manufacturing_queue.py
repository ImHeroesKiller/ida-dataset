"""Internal manufacturing queue + reuse ledger.

Graph → Manufacturing Queue → Dataset Candidates → Quality Layer

Does NOT modify the existing publish queue or publisher.
Candidates land under automation/queue/manufacturing/ (additive).
"""

from __future__ import annotations

import hashlib
import json
import threading
from pathlib import Path
from typing import Any, Optional

from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root

_LOCK = threading.Lock()


def queue_root(repo_root: Optional[Path] = None) -> Path:
    root = repo_root or find_repo_root()
    d = root / "automation" / "queue" / "manufacturing"
    d.mkdir(parents=True, exist_ok=True)
    (d / "pending").mkdir(exist_ok=True)
    (d / "ready").mkdir(exist_ok=True)
    (d / "enrichment").mkdir(exist_ok=True)
    return d


def ledger_path(repo_root: Optional[Path] = None) -> Path:
    root = repo_root or find_repo_root()
    store = root / "automation" / "knowledge" / "store"
    store.mkdir(parents=True, exist_ok=True)
    return store / "manufacturing_ledger.json"


def _read_json(path: Path) -> Any:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return None


def _write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    tmp.replace(path)


def manufacture_key(
    *,
    source_id: str,
    target_dataset: str,
    payload: dict[str, Any],
) -> str:
    """Stable key for reuse — same graph knowledge + dataset → same key."""
    material = json.dumps(
        {"s": source_id, "d": target_dataset, "p": payload},
        sort_keys=True,
        ensure_ascii=False,
        default=str,
    )
    return hashlib.sha1(material.encode("utf-8")).hexdigest()


def load_ledger(*, repo_root: Optional[Path] = None) -> dict[str, Any]:
    data = _read_json(ledger_path(repo_root))
    if isinstance(data, dict) and isinstance(data.get("keys"), dict):
        return data
    return {"keys": {}, "updated_at": utc_now_iso()}


def was_manufactured(
    key: str,
    *,
    repo_root: Optional[Path] = None,
) -> bool:
    ledger = load_ledger(repo_root=repo_root)
    return key in (ledger.get("keys") or {})


def mark_manufactured(
    key: str,
    *,
    candidate_id: str,
    target_dataset: str,
    source_id: str,
    repo_root: Optional[Path] = None,
) -> None:
    with _LOCK:
        ledger = load_ledger(repo_root=repo_root)
        keys = dict(ledger.get("keys") or {})
        keys[key] = {
            "candidate_id": candidate_id,
            "target_dataset": target_dataset,
            "source_id": source_id,
            "at": utc_now_iso(),
        }
        ledger["keys"] = keys
        ledger["updated_at"] = utc_now_iso()
        ledger["count"] = len(keys)
        _write_json(ledger_path(repo_root), ledger)


def enqueue_candidate(
    candidate: dict[str, Any],
    *,
    disposition: str = "ready",
    repo_root: Optional[Path] = None,
) -> Path:
    """Write candidate JSON into manufacturing queue subfolder."""
    root = queue_root(repo_root)
    # Map quality disposition to folder
    if disposition == "enrichment_queue":
        folder = root / "enrichment"
    elif disposition == "reject":
        folder = root / "pending"  # hold rejects for review; not publish
    else:
        folder = root / "ready"
    folder.mkdir(parents=True, exist_ok=True)
    cid = str(candidate.get("candidate_id") or "CAND-UNKNOWN")
    path = folder / f"{cid}.json"
    with _LOCK:
        _write_json(path, candidate)
    return path


def queue_stats(*, repo_root: Optional[Path] = None) -> dict[str, int]:
    root = queue_root(repo_root)
    out: dict[str, int] = {}
    for name in ("pending", "ready", "enrichment"):
        d = root / name
        if not d.exists():
            out[name] = 0
            continue
        out[name] = len(list(d.glob("CAND-*.json")))
    ledger = load_ledger(repo_root=repo_root)
    out["ledger"] = int(ledger.get("count") or len(ledger.get("keys") or {}))
    return out
