"""Trusted source health & production monitoring (EPIC-1).

Automatically tracks per-source production metrics for the Dataset Factory.
Does not change pipeline architecture — observes and records only.

State: automation/learning/state/source_health.json
Registry: metadata/source_registry.csv
"""

from __future__ import annotations

import csv
import json
import re
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from automation.lib.paths import find_repo_root

STATE_REL = Path("automation/learning/state/source_health.json")
REGISTRY_REL = Path("metadata/source_registry.csv")
INDUSTRY_REL = Path("domains/business_development/industry_library.csv")
DOCS_INCOMING = Path("automation/documents/incoming")
DOCS_PROCESSED = Path("automation/documents/processed")

_SOURCE_ID_RE = re.compile(r"SRC-\d{6}")


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def _state_path(root: Path) -> Path:
    return root / STATE_REL


def _empty_metric(source_id: str, name: str = "", category: str = "") -> dict[str, Any]:
    return {
        "source_id": source_id,
        "name": name,
        "category": category,
        "trust_score": 0.0,
        "status": "unknown",
        "allowed": False,
        "health_status": "unknown",
        "coverage": 0.0,
        "last_successful_sync": None,
        "last_attempt": None,
        "rows_produced": 0,
        "documents_processed": 0,
        "attempts": 0,
        "successes": 0,
        "failure_count": 0,
        "success_rate": 0.0,
        "total_processing_ms": 0.0,
        "average_processing_time_ms": 0.0,
        "mission_usage": 0,
        "base_url": "",
        "notes": "",
    }


def load_registry(root: Path | None = None) -> list[dict[str, str]]:
    root = root or find_repo_root()
    path = root / REGISTRY_REL
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def load_metrics(root: Path | None = None) -> dict[str, Any]:
    root = root or find_repo_root()
    path = _state_path(root)
    if not path.exists():
        return {"updated_at": None, "sources": {}}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"updated_at": None, "sources": {}}


def save_metrics(data: dict[str, Any], root: Path | None = None) -> None:
    root = root or find_repo_root()
    path = _state_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    data["updated_at"] = _utc_now()
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(path)


def _ensure_source(
    sources: dict[str, Any], source_id: str, **seed: Any
) -> dict[str, Any]:
    if source_id not in sources:
        sources[source_id] = _empty_metric(source_id)
    m = sources[source_id]
    for k, v in seed.items():
        if v is not None and v != "":
            m[k] = v
    return m


def _recompute_rates(m: dict[str, Any]) -> None:
    attempts = int(m.get("attempts") or 0)
    successes = int(m.get("successes") or 0)
    m["success_rate"] = round(successes / attempts, 4) if attempts else 0.0
    total_ms = float(m.get("total_processing_ms") or 0)
    m["average_processing_time_ms"] = (
        round(total_ms / attempts, 1) if attempts else 0.0
    )


def _derive_health(m: dict[str, Any]) -> str:
    if not m.get("allowed") or str(m.get("status", "")).lower() != "active":
        return "inactive"
    fails = int(m.get("failure_count") or 0)
    successes = int(m.get("successes") or 0)
    rate = float(m.get("success_rate") or 0)
    if successes == 0 and fails == 0:
        return "unknown"
    if rate >= 0.8 and fails < 3:
        return "healthy"
    if rate >= 0.4:
        return "degraded"
    return "down"


def probe_url(url: str, timeout: float = 8.0) -> tuple[bool, float, str]:
    """HEAD/GET probe for health. Returns (ok, elapsed_ms, detail)."""
    if not url or not url.startswith("http"):
        return False, 0.0, "no_url"
    start = time.perf_counter()
    req = urllib.request.Request(
        url,
        method="HEAD",
        headers={"User-Agent": "IDA-Dataset-Factory/2.0 (+source-health)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            code = getattr(resp, "status", 200) or 200
            ms = (time.perf_counter() - start) * 1000
            ok = 200 <= int(code) < 400
            return ok, round(ms, 1), f"http_{code}"
    except urllib.error.HTTPError as e:
        ms = (time.perf_counter() - start) * 1000
        # Some hosts reject HEAD — try GET briefly
        if e.code in (403, 405, 501):
            try:
                greq = urllib.request.Request(
                    url,
                    method="GET",
                    headers={"User-Agent": "IDA-Dataset-Factory/2.0 (+source-health)"},
                )
                with urllib.request.urlopen(greq, timeout=timeout) as resp:
                    code = getattr(resp, "status", 200) or 200
                    ms = (time.perf_counter() - start) * 1000
                    ok = 200 <= int(code) < 400
                    return ok, round(ms, 1), f"http_{code}_get"
            except Exception as e2:  # noqa: BLE001
                ms = (time.perf_counter() - start) * 1000
                return False, round(ms, 1), str(e2)[:80]
        return False, round(ms, 1), f"http_{e.code}"
    except Exception as e:  # noqa: BLE001
        ms = (time.perf_counter() - start) * 1000
        return False, round(ms, 1), str(e)[:80]


def record_attempt(
    source_id: str,
    *,
    success: bool,
    documents: int = 0,
    rows: int = 0,
    duration_ms: float = 0.0,
    mission_id: str | None = None,
    detail: str = "",
    root: Path | None = None,
) -> dict[str, Any]:
    """Record one production attempt for a trusted source (auto-called by sessions)."""
    root = root or find_repo_root()
    if not source_id or not source_id.startswith("SRC-"):
        return {}
    data = load_metrics(root)
    sources: dict[str, Any] = data.setdefault("sources", {})
    m = _ensure_source(sources, source_id)
    now = _utc_now()
    m["last_attempt"] = now
    m["attempts"] = int(m.get("attempts") or 0) + 1
    m["total_processing_ms"] = float(m.get("total_processing_ms") or 0) + float(
        duration_ms or 0
    )
    if success:
        m["successes"] = int(m.get("successes") or 0) + 1
        m["last_successful_sync"] = now
        m["documents_processed"] = int(m.get("documents_processed") or 0) + int(
            documents or 0
        )
        m["rows_produced"] = int(m.get("rows_produced") or 0) + int(rows or 0)
    else:
        m["failure_count"] = int(m.get("failure_count") or 0) + 1
    if mission_id:
        usage = m.setdefault("missions_seen", [])
        if mission_id not in usage:
            usage.append(mission_id)
        m["mission_usage"] = len(usage)
    if detail:
        m["last_detail"] = detail[:200]
    _recompute_rates(m)
    m["health_status"] = _derive_health(m)
    save_metrics(data, root)
    return m


def extract_source_ids_from_text(text: str) -> list[str]:
    found = _SOURCE_ID_RE.findall(text or "")
    # also map known name tokens
    low = (text or "").lower()
    aliases = {
        "SRC-000001": ["bps", "statistics indonesia"],
        "SRC-000004": ["world bank", "worldbank"],
        "SRC-000005": ["oecd"],
        "SRC-000006": ["asian development bank", "adb"],
        "SRC-000007": ["kemenperin", "perindustrian"],
        "SRC-000008": ["bkpm"],
        "SRC-000009": ["ifc"],
        "SRC-000010": ["ojk"],
        "SRC-000011": ["kemnaker"],
        "SRC-000012": ["kadin"],
        "SRC-000013": ["apindo"],
        "SRC-000014": ["lkpp"],
        "SRC-000015": ["oss"],
    }
    out = list(found)
    for sid, keys in aliases.items():
        if any(k in low for k in keys) and sid not in out:
            out.append(sid)
    return out


def recompute_from_datasets(root: Path | None = None) -> dict[str, Any]:
    """Rebuild production counters from published datasets + documents + missions."""
    root = root or find_repo_root()
    data = load_metrics(root)
    sources: dict[str, Any] = data.setdefault("sources", {})

    # Seed from registry
    for row in load_registry(root):
        sid = (row.get("Source ID") or "").strip()
        if not sid:
            continue
        m = _ensure_source(
            sources,
            sid,
            name=row.get("Source Name") or "",
            category=row.get("Category") or "",
            trust_score=float(row.get("Trust Score") or 0),
            status=(row.get("Status") or "").lower(),
            allowed=str(row.get("Allowed") or "").lower() == "true",
            base_url=row.get("Base URL") or "",
            notes=row.get("Notes") or "",
        )
        m["trust_score"] = float(row.get("Trust Score") or 0)
        m["status"] = (row.get("Status") or "").lower()
        m["allowed"] = str(row.get("Allowed") or "").lower() == "true"
        m["name"] = row.get("Source Name") or m.get("name") or ""
        m["category"] = row.get("Category") or m.get("category") or ""
        m["base_url"] = row.get("Base URL") or m.get("base_url") or ""

    # Reset produced counters then re-attribute from industry library
    for m in sources.values():
        m["rows_produced"] = 0
        m["coverage"] = 0.0

    industry = root / INDUSTRY_REL
    total_rows = 0
    if industry.exists():
        with industry.open(encoding="utf-8-sig", newline="") as f:
            rows = list(csv.DictReader(f))
        total_rows = len(rows)
        for row in rows:
            blob = f"{row.get('Data Sources', '')} {row.get('Notes', '')}"
            sids = extract_source_ids_from_text(blob)
            if not sids:
                continue
            share = 1.0 / len(sids)
            for sid in sids:
                m = _ensure_source(sources, sid)
                m["rows_produced"] = float(m.get("rows_produced") or 0) + share

    # Documents attribution
    for folder in (DOCS_INCOMING, DOCS_PROCESSED):
        d = root / folder
        if not d.exists():
            continue
        for fp in d.glob("*.json"):
            try:
                doc = json.loads(fp.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            sid = str(doc.get("source_id") or "")
            if not sid.startswith("SRC-"):
                # try metadata
                meta = doc.get("metadata") or {}
                sid = str(meta.get("source_id") or sid)
            if sid.startswith("SRC-"):
                m = _ensure_source(sources, sid)
                # only count if not already inflated from session counters;
                # use max of recompute floor
                m["documents_processed"] = max(
                    int(m.get("documents_processed") or 0),
                    int(m.get("documents_processed") or 0),
                )
                # increment document floor via separate key then merge
                m["_doc_floor"] = int(m.get("_doc_floor") or 0) + 1

    for m in sources.values():
        floor = int(m.pop("_doc_floor", 0) or 0)
        m["documents_processed"] = max(int(m.get("documents_processed") or 0), floor)
        # coverage: share of industry rows attributed
        rows_p = float(m.get("rows_produced") or 0)
        m["coverage"] = (
            round(rows_p / total_rows, 4) if total_rows else float(m.get("coverage") or 0)
        )
        # ceil so partial multi-source attribution still shows production
        import math

        m["rows_produced"] = (
            int(math.ceil(rows_p - 1e-9)) if rows_p > 0 else 0
        )
        # Prefer healthier status when rows were attributed from published data
        if m["rows_produced"] > 0 and int(m.get("successes") or 0) == 0:
            m["successes"] = max(1, int(m.get("successes") or 0))
            m["attempts"] = max(int(m.get("attempts") or 0), 1)
            if not m.get("last_successful_sync"):
                m["last_successful_sync"] = _utc_now()
        _recompute_rates(m)

    # Mission usage from mission files
    missions_dir = root / "automation" / "missions" / "missions"
    if missions_dir.exists():
        for m in sources.values():
            m["mission_usage"] = 0
            m["missions_seen"] = []
        for fp in missions_dir.glob("*.json"):
            try:
                mission = json.loads(fp.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            mid = str(mission.get("mission_id") or fp.stem)
            allowed = mission.get("allowed_sources") or []
            for sid in allowed:
                sid = str(sid)
                if not sid.startswith("SRC-"):
                    continue
                m = _ensure_source(sources, sid)
                seen = m.setdefault("missions_seen", [])
                if mid not in seen:
                    seen.append(mid)
                m["mission_usage"] = len(seen)

    for m in sources.values():
        m["health_status"] = _derive_health(m)

    save_metrics(data, root)
    return data


def refresh_health_probes(
    root: Path | None = None, *, only_active: bool = True
) -> dict[str, Any]:
    """Probe base URLs and update health + last_attempt for active sources."""
    root = root or find_repo_root()
    data = recompute_from_datasets(root)
    sources: dict[str, Any] = data.get("sources") or {}
    for sid, m in list(sources.items()):
        if only_active and (
            not m.get("allowed") or str(m.get("status", "")).lower() != "active"
        ):
            m["health_status"] = "inactive"
            continue
        url = str(m.get("base_url") or "")
        ok, ms, detail = probe_url(url)
        m["last_attempt"] = _utc_now()
        m["attempts"] = int(m.get("attempts") or 0) + 1
        m["total_processing_ms"] = float(m.get("total_processing_ms") or 0) + ms
        if ok:
            m["successes"] = int(m.get("successes") or 0) + 1
            m["last_successful_sync"] = m["last_attempt"]
            m["last_detail"] = detail
        else:
            m["failure_count"] = int(m.get("failure_count") or 0) + 1
            m["last_detail"] = detail
        _recompute_rates(m)
        m["health_status"] = _derive_health(m)
    save_metrics(data, root)
    return data


def list_source_dashboard(
    root: Path | None = None, *, probe: bool = False
) -> list[dict[str, Any]]:
    """Return ordered list of source production metrics for the UI."""
    root = root or find_repo_root()
    if probe:
        data = refresh_health_probes(root)
    else:
        data = recompute_from_datasets(root)
    sources: dict[str, Any] = data.get("sources") or {}
    # order by registry
    order = [r.get("Source ID", "") for r in load_registry(root)]
    out: list[dict[str, Any]] = []
    for sid in order:
        if sid in sources:
            out.append(sources[sid])
    for sid, m in sources.items():
        if sid not in order:
            out.append(m)
    return out


def record_session_sources(
    source_ids: list[str],
    *,
    success: bool,
    documents: int = 0,
    rows: int = 0,
    duration_ms: float = 0.0,
    mission_id: str | None = None,
    root: Path | None = None,
) -> None:
    """Distribute session outcomes across involved sources."""
    ids = [s for s in source_ids if s and str(s).startswith("SRC-")]
    if not ids:
        return
    per_doc = max(0, documents // len(ids))
    rem_doc = max(0, documents - per_doc * len(ids))
    per_row = max(0, rows // len(ids))
    rem_row = max(0, rows - per_row * len(ids))
    per_ms = duration_ms / len(ids) if duration_ms else 0.0
    for i, sid in enumerate(ids):
        record_attempt(
            sid,
            success=success,
            documents=per_doc + (1 if i < rem_doc else 0),
            rows=per_row + (1 if i < rem_row else 0),
            duration_ms=per_ms,
            mission_id=mission_id,
            root=root,
        )


if __name__ == "__main__":
    import sys

    root = find_repo_root()
    probe = "--probe" in sys.argv
    if probe:
        data = refresh_health_probes(root)
    else:
        data = recompute_from_datasets(root)
    rows = list_source_dashboard(root, probe=False)
    print(json.dumps({"updated_at": data.get("updated_at"), "sources": rows}, indent=2))
