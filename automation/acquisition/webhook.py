"""Optional webhook / feed-update triggers for acquisition.

Does not redesign mission engine. Provides:
  - config-driven webhook endpoint registry
  - inbox of pending trigger events (JSONL)
  - helper to drain triggers into preferred source list

A separate process/CI can POST events into the inbox file.
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Optional

from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root


def inbox_path(repo_root: Path | None = None) -> Path:
    root = repo_root or find_repo_root()
    return root / "automation" / "learning" / "state" / "webhook_inbox.jsonl"


def register_event(
    *,
    source_id: str,
    event_type: str = "update",
    url: str = "",
    payload: Optional[dict[str, Any]] = None,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """Append a webhook/RSS-update event for the next acquisition cycle."""
    root = repo_root or find_repo_root()
    path = inbox_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    event = {
        "ts": utc_now_iso(),
        "source_id": source_id,
        "event_type": event_type,  # update | rss | atom | webhook
        "url": url,
        "payload": payload or {},
        "consumed": False,
    }
    with path.open("a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")
    return event


def drain_pending_sources(
    *,
    repo_root: Path | None = None,
    max_events: int = 50,
) -> list[str]:
    """Return source_ids from unconsumed events and mark them consumed."""
    root = repo_root or find_repo_root()
    path = inbox_path(root)
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    kept: list[str] = []
    preferred: list[str] = []
    changed = False
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            kept.append(line)
            continue
        if ev.get("consumed"):
            kept.append(json.dumps(ev, ensure_ascii=False))
            continue
        if len(preferred) < max_events:
            sid = str(ev.get("source_id") or "")
            if sid:
                preferred.append(sid)
            ev["consumed"] = True
            ev["consumed_at"] = utc_now_iso()
            changed = True
        kept.append(json.dumps(ev, ensure_ascii=False))
    if changed:
        path.write_text("\n".join(kept) + ("\n" if kept else ""), encoding="utf-8")
    # unique preserve order
    seen: set[str] = set()
    out: list[str] = []
    for s in preferred:
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out


def webhook_config_template() -> dict[str, Any]:
    """Documentation helper for source registry webhook fields."""
    return {
        "webhook_enabled": False,
        "webhook_path": "/hooks/acquisition/{source_id}",
        "supports": ["webhook", "rss_update", "atom_update"],
        "fallback": "scheduled_polling",
    }
