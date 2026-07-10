"""Knowledge growth metrics — today vs baseline (yesterday snapshot)."""

from __future__ import annotations

import csv
import json
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from automation.lib.paths import find_repo_root


def _state_dir(root: Path) -> Path:
    p = root / "automation" / "learning" / "state"
    p.mkdir(parents=True, exist_ok=True)
    return p


def count_datasets(root: Path) -> dict[str, Any]:
    domains = root / "domains"
    total = 0
    populated = 0
    rows_total = 0
    by_dataset: list[dict[str, Any]] = []
    if domains.exists():
        for path in sorted(domains.rglob("*.csv")):
            total += 1
            rel = str(path.relative_to(root)).replace("\\", "/")
            try:
                text = path.read_text(encoding="utf-8-sig")
                reader = list(csv.reader(text.splitlines()))
                n = max(0, len(reader) - 1) if reader else 0
            except OSError:
                n = 0
            if n > 0:
                populated += 1
            rows_total += n
            by_dataset.append(
                {
                    "path": rel,
                    "name": path.stem,
                    "domain": path.relative_to(domains).parts[0]
                    if path.relative_to(domains).parts
                    else "",
                    "rows": n,
                    "is_gap": n == 0,
                }
            )
    coverage = round((populated / total) * 100, 1) if total else 0.0
    return {
        "datasets_total": total,
        "datasets_populated": populated,
        "datasets_gaps": total - populated,
        "rows_total": rows_total,
        "coverage_pct": coverage,
        "by_dataset": by_dataset,
    }


def snapshot_today(root: Path | None = None) -> dict[str, Any]:
    root = root or find_repo_root()
    counts = count_datasets(root)
    today = date.today().isoformat()
    snap = {
        "date": today,
        "captured_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        **counts,
    }
    path = _state_dir(root) / f"snapshot_{today}.json"
    path.write_text(json.dumps(snap, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    # also write current.json
    (_state_dir(root) / "current_snapshot.json").write_text(
        json.dumps(snap, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return snap


def load_snapshot(day: str, root: Path | None = None) -> dict[str, Any] | None:
    root = root or find_repo_root()
    path = _state_dir(root) / f"snapshot_{day}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def growth_vs_yesterday(root: Path | None = None) -> dict[str, Any]:
    root = root or find_repo_root()
    today = snapshot_today(root)
    # find latest prior snapshot
    files = sorted(_state_dir(root).glob("snapshot_*.json"))
    prior = None
    for path in reversed(files):
        if path.name == f"snapshot_{today['date']}.json":
            continue
        prior = json.loads(path.read_text(encoding="utf-8"))
        break

    if not prior:
        return {
            "today": today,
            "yesterday": None,
            "delta_rows": 0,
            "delta_populated": 0,
            "delta_coverage_pct": 0,
            "smarter_than_yesterday": False,
            "message": "No prior snapshot — baseline established today",
        }

    delta_rows = int(today["rows_total"]) - int(prior.get("rows_total", 0))
    delta_pop = int(today["datasets_populated"]) - int(prior.get("datasets_populated", 0))
    delta_cov = round(
        float(today["coverage_pct"]) - float(prior.get("coverage_pct", 0)), 1
    )
    return {
        "today": today,
        "yesterday": prior,
        "delta_rows": delta_rows,
        "delta_populated": delta_pop,
        "delta_coverage_pct": delta_cov,
        "smarter_than_yesterday": delta_rows > 0 or delta_pop > 0 or delta_cov > 0,
        "message": (
            f"+{delta_rows} rows, +{delta_pop} populated datasets, {delta_cov:+}% coverage"
            if (delta_rows or delta_pop or delta_cov)
            else "No measurable knowledge growth since last snapshot"
        ),
    }


def record_daily_counters(
    *,
    added: int = 0,
    updated: int = 0,
    rejected: int = 0,
    root: Path | None = None,
) -> dict[str, Any]:
    root = root or find_repo_root()
    today = date.today().isoformat()
    path = _state_dir(root) / f"daily_{today}.json"
    data = {
        "date": today,
        "knowledge_added": 0,
        "knowledge_updated": 0,
        "knowledge_rejected": 0,
    }
    if path.exists():
        data.update(json.loads(path.read_text(encoding="utf-8")))
    data["knowledge_added"] = int(data.get("knowledge_added", 0)) + added
    data["knowledge_updated"] = int(data.get("knowledge_updated", 0)) + updated
    data["knowledge_rejected"] = int(data.get("knowledge_rejected", 0)) + rejected
    data["updated_at"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return data


def load_daily(root: Path | None = None) -> dict[str, Any]:
    root = root or find_repo_root()
    today = date.today().isoformat()
    path = _state_dir(root) / f"daily_{today}.json"
    if not path.exists():
        return {
            "date": today,
            "knowledge_added": 0,
            "knowledge_updated": 0,
            "knowledge_rejected": 0,
        }
    return json.loads(path.read_text(encoding="utf-8"))
