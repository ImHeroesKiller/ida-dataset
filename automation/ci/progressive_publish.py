#!/usr/bin/env python3
"""Progressive publish queue worker — backend paced (never UI-simulated).

Reads automation/config/learning.yaml learning_mode.
In development: moves pending → publish queue, publishes at publish_rate.

Exit: 0 success | 2 config
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any, Optional

_REPO = Path(__file__).resolve().parents[2]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))

from automation.ci.common import find_repo_root, load_yaml_file  # noqa: E402
from automation.lib.io_utils import append_csv_rows, read_csv_headers  # noqa: E402
from automation.lib.models import utc_now_iso  # noqa: E402


def load_mode(root: Path) -> dict[str, Any]:
    cfg = load_yaml_file(root / "automation" / "config" / "learning.yaml")
    lm = cfg.get("learning_mode") or {}
    mode = (
        os.environ.get("IDA_LEARNING_MODE")
        or lm.get("mode")
        or "development"
    ).lower()
    if mode not in {"development", "production"}:
        mode = "development"
    profile = (lm.get(mode) or {}) if isinstance(lm.get(mode), dict) else {}
    rate = float(profile.get("publish_rate") or 1)
    return {
        "mode": mode,
        "auto_publish": bool(profile.get("auto_publish", mode == "development")),
        "review_bypassed": bool(profile.get("review_bypassed", mode == "development")),
        "publish_rate": rate,
        "interval": 0.0 if rate <= 0 else 1.0 / max(rate, 0.001),
    }


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as h:
        h.write(json.dumps(row, ensure_ascii=False) + "\n")


def resolve_csv(root: Path, dataset: str) -> Path:
    preferred = root / "domains" / "business_development" / f"{dataset}.csv"
    if preferred.exists():
        return preferred
    matches = list((root / "domains").glob(f"**/{dataset}.csv"))
    return matches[0] if matches else preferred


def entity_present(csv_path: Path, entity_id: str) -> bool:
    if not csv_path.exists() or not entity_id:
        return False
    return entity_id in csv_path.read_text(encoding="utf-8-sig")


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Progressive publish queue")
    p.add_argument("--max", type=int, default=10000)
    p.add_argument("--no-enqueue", action="store_true")
    args = p.parse_args(argv)

    root = find_repo_root()
    mode = load_mode(root)
    pending = root / "automation" / "queue" / "pending"
    publish_q = root / "automation" / "queue" / "publish"
    approved = root / "automation" / "queue" / "approved"
    state_path = root / "automation" / "learning" / "state" / "publish_state.json"
    feed_path = root / "automation" / "learning" / "state" / "knowledge_feed.jsonl"
    journal = root / "automation" / "learning" / "state" / "learning_journal.jsonl"
    publish_q.mkdir(parents=True, exist_ok=True)
    approved.mkdir(parents=True, exist_ok=True)

    # Development: pending → publish queue
    if mode["auto_publish"] and mode["review_bypassed"] and not args.no_enqueue:
        if pending.exists():
            for f in sorted(pending.glob("*.json")):
                data = json.loads(f.read_text(encoding="utf-8"))
                data.setdefault("provenance", {})["validation_status"] = "approved"
                data["provenance"]["reviewer"] = "auto-development"
                dest = publish_q / f.name
                write_json(dest, data)
                f.unlink()

    files = sorted(publish_q.glob("*.json"))
    total = len(files)
    published = 0
    started = utc_now_iso()

    def save_state(**extra: Any) -> None:
        remaining = len(list(publish_q.glob("*.json")))
        st = {
            "status": extra.get("status", "publishing"),
            "total": total,
            "published": published,
            "remaining": remaining,
            "speed": mode["publish_rate"],
            "unit": "rows_per_second",
            "eta_seconds": int(remaining * mode["interval"]) if mode["interval"] else 0,
            "current_dataset": extra.get("dataset"),
            "current_knowledge": extra.get("name"),
            "next_knowledge": extra.get("next"),
            "last_published_at": extra.get("ts"),
            "started_at": started,
            "updated_at": utc_now_iso(),
            "mode": mode["mode"],
            "auto_publish": mode["auto_publish"],
        }
        write_json(state_path, st)

    if not files:
        save_state(status="idle")
        print(json.dumps({"ok": True, "published": 0, "message": "empty queue"}))
        return 0

    save_state(status="publishing")

    for i, fpath in enumerate(files):
        if i >= args.max:
            break
        data = json.loads(fpath.read_text(encoding="utf-8"))
        name = data.get("canonical_name") or data.get("entity_id") or "Knowledge"
        dataset = data.get("target_dataset") or "unknown"
        entity_id = data.get("entity_id") or ""
        conf = float((data.get("provenance") or {}).get("confidence") or 0.9)
        source = (data.get("provenance") or {}).get("source_id") or "source"
        ts = utc_now_iso()

        csv_path = resolve_csv(root, dataset)
        if not entity_present(csv_path, str(entity_id)):
            payload = data.get("payload") or {}
            headers = read_csv_headers(csv_path) or list(payload.keys())
            row = {h: payload.get(h, "") for h in headers}
            append_csv_rows(csv_path, [row], fieldnames=headers)

        data.setdefault("provenance", {})["published_at"] = ts
        data["provenance"]["validation_status"] = "approved"
        data["updated_at"] = ts
        write_json(approved / fpath.name, data)
        fpath.unlink()
        published += 1

        ktype = dataset.replace("_library", "").replace("_", " ").title()
        feed = {
            "ts": ts,
            "knowledge_type": ktype,
            "name": name,
            "dataset": dataset,
            "source": source,
            "confidence": conf,
            "candidate_id": data.get("candidate_id"),
            "published_at": ts,
        }
        append_jsonl(feed_path, feed)
        append_jsonl(
            journal,
            {
                "seq": int(time.time() * 1000),
                "ts": ts,
                "verb": "Publishing",
                "detail": f"Published · {ktype} · {name}",
                "stage": "publish",
                "status": "progress",
                "dataset": dataset,
                "current_entity": name,
                "confidence": conf,
            },
        )
        append_jsonl(
            journal,
            {
                "seq": int(time.time() * 1000) + 1,
                "ts": ts,
                "verb": "Knowledge Added",
                "detail": f"{ktype}: {name}",
                "stage": "knowledge",
                "status": "progress",
                "dataset": dataset,
                "current_entity": name,
            },
        )

        remaining_files = sorted(publish_q.glob("*.json"))
        nxt = None
        if remaining_files:
            try:
                nxt = json.loads(remaining_files[0].read_text(encoding="utf-8")).get(
                    "canonical_name"
                )
            except Exception:
                nxt = None
        save_state(status="publishing", dataset=dataset, name=name, next=nxt, ts=ts)

        if mode["interval"] > 0 and remaining_files:
            time.sleep(mode["interval"])

    append_jsonl(
        journal,
        {
            "seq": int(time.time() * 1000),
            "ts": utc_now_iso(),
            "verb": "Learning Completed",
            "detail": f"Published {published} knowledge row(s)",
            "stage": "complete",
            "status": "completed",
        },
    )
    save_state(status="completed")
    print(json.dumps({"ok": True, "published": published, "mode": mode["mode"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
