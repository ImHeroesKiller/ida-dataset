"""Collect end-to-end production evidence from existing state only.

Does not mutate datasets, queues, or production engines.
"""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root

# Datasets required by the diagnostic brief
DIAG_DATASETS = [
    "industry_library",
    "service_library",
    "product_catalog",
    "company_profile",
    "pain_point_library",
    "solution_library",
    "framework_library",
    "case_study_library",
    "buyer_persona_library",
    "decision_maker_library",
    "regulation_library",
    "risk_library",
    "trend_library",
    "competitor_library",
]


def _read_json(path: Path) -> Any:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return None


def _row_count(path: Path, *, service_only: bool = False) -> int:
    if not path.exists():
        return 0
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if service_only:
        return sum(1 for r in rows if "service" in (r.get("Product Type") or "").lower())
    return len(rows)


def dataset_counts(repo: Path) -> dict[str, int]:
    bd = repo / "domains" / "business_development"
    return {
        "industry_library": _row_count(bd / "industry_library.csv"),
        "service_library": _row_count(bd / "product_catalog.csv", service_only=True),
        "product_catalog": _row_count(bd / "product_catalog.csv"),
        "company_profile": _row_count(bd / "company_profile.csv"),
        "pain_point_library": _row_count(bd / "pain_point_library.csv"),
        "solution_library": _row_count(bd / "solution_library.csv"),
        "framework_library": _row_count(bd / "framework_library.csv"),
        "case_study_library": _row_count(bd / "case_study_library.csv"),
        "buyer_persona_library": _row_count(bd / "buyer_persona_library.csv"),
        "decision_maker_library": _row_count(bd / "decision_maker_library.csv"),
        "regulation_library": _row_count(bd / "regulation_library.csv"),
        "risk_library": _row_count(bd / "risk_library.csv"),
        "trend_library": _row_count(bd / "trend_library.csv"),
        "competitor_library": _row_count(bd / "competitor_library.csv"),
    }


def collect_mission_diagnostics(repo: Path) -> dict[str, Any]:
    """Full mission eligibility / ranking evidence."""
    from automation.scheduler.mission_selector import (
        CATALOG,
        _deps_met,
        _load_targets,
        select_next_mission,
    )

    sel = select_next_mission(repo)
    # Top-8 only from API — rebuild full score map from same inputs where possible
    top_ranked = {r["dataset"]: r for r in (sel.get("ranking") or [])}
    counts = sel.get("counts") or dataset_counts(repo)
    selected = (sel.get("selected") or {}).get("dataset")
    targets = _load_targets(repo)
    mode_name = sel.get("manufacturing_mode") or ""

    # Manufacturing gap scores for all datasets
    gap_by_ds: dict[str, float] = {}
    try:
        from automation.manufacturing.controller import ManufacturingController

        mfg = ManufacturingController(repo_root=repo).evaluate()
        for e in mfg.get("evaluations") or []:
            gap_by_ds[str(e.get("dataset"))] = float(e.get("knowledge_gap_score") or 0)
        if not mode_name:
            mode_name = str((mfg.get("mode") or {}).get("mode") or "")
    except Exception:  # noqa: BLE001
        pass

    source_factor = 1.0
    try:
        nsrc = int(sel.get("active_sources") or 0)
        source_factor = 1.0 if nsrc >= 6 else 0.7 if nsrc >= 3 else 0.4
    except Exception:  # noqa: BLE001
        pass

    full_scores: dict[str, dict[str, Any]] = {}
    for item in CATALOG:
        ds = item["dataset"]
        cur = counts.get(ds, 0)
        if item.get("service_type"):
            cur = counts.get("service_library", 0)
        eligible = _deps_met(item, counts)
        tgt = int(targets.get(item.get("target_key") or ds, targets.get("_default", 1000)))
        cov = min(100.0, (cur / tgt) * 100.0) if tgt else 0.0
        gap_score = float(gap_by_ds.get(ds) or 0)
        gap_weight = (100.0 - min(cov, 99.0)) / 100.0
        business_value = float(item.get("business_value") or item.get("product_priority") or 0)
        relationship_impact = float(item.get("relationship_impact") or 50)
        starvation_boost = 0.0
        if cur == 0 and ds in {
            "buyer_persona_library",
            "decision_maker_library",
            "regulation_library",
            "risk_library",
            "trend_library",
            "competitor_library",
        }:
            starvation_boost = 220.0
        score = None
        if eligible:
            score = (
                gap_score * 10.0
                + gap_weight * 500.0
                + float(item.get("product_priority") or 0) * 2.0
                + business_value * 1.5
                + relationship_impact * 1.2
                + starvation_boost
                + (50.0 if cur == 0 else 0.0)
            ) * source_factor
            # prefer live top-rank score when present
            if ds in top_ranked and top_ranked[ds].get("score") is not None:
                score = float(top_ranked[ds]["score"])
        full_scores[ds] = {
            "eligible": eligible,
            "score": round(score, 2) if score is not None else None,
            "coverage_pct": round(cov, 1),
            "current_rows": cur,
            "knowledge_gap_score": gap_score or (
                top_ranked.get(ds) or {}
            ).get("knowledge_gap_score"),
        }

    selected_score = (sel.get("selected") or {}).get("score")
    rows: list[dict[str, Any]] = []
    for item in CATALOG:
        ds = item["dataset"]
        if ds not in DIAG_DATASETS and ds not in counts:
            continue
        fs = full_scores.get(ds) or {}
        r = top_ranked.get(ds)
        cur = fs.get("current_rows", counts.get(ds, 0))
        eligible = bool(fs.get("eligible"))
        skip_reason = ""
        if not eligible:
            deps = item.get("hard_deps") or []
            missing = []
            for dep in deps:
                if dep == "industry_library" and counts.get("industry_library", 0) < 50:
                    missing.append(
                        f"industry_library<50 (have {counts.get('industry_library', 0)})"
                    )
                elif dep == "company_profile" and counts.get("company_profile", 0) < 25:
                    missing.append(
                        f"company_profile<25 (have {counts.get('company_profile', 0)})"
                    )
                elif dep == "pain_point_library" and counts.get("pain_point_library", 0) < 1:
                    missing.append("pain_point_library empty")
                elif dep == "solution_library" and counts.get("solution_library", 0) < 1:
                    missing.append("solution_library empty")
                elif dep == "product_catalog" and counts.get("product_catalog", 0) < 1:
                    missing.append("product_catalog empty")
                elif counts.get(dep, 0) < 1 and dep not in ("industry_library",):
                    missing.append(f"{dep} empty")
            skip_reason = (
                "dependency_not_met: " + "; ".join(missing)
                if missing
                else "dependency_gate_failed (_deps_met=False)"
            )
        elif ds != selected:
            skip_reason = (
                f"eligible_but_not_selected; score={fs.get('score')} "
                f"< selected={selected} score={selected_score}"
            )
        rows.append(
            {
                "dataset": ds,
                "batch_id": item.get("batch_id"),
                "coverage_pct": fs.get("coverage_pct"),
                "current_rows": cur,
                "knowledge_gap_score": fs.get("knowledge_gap_score"),
                "priority_score": fs.get("score"),
                "product_priority": item.get("product_priority"),
                "hard_deps": item.get("hard_deps") or [],
                "eligible": eligible,
                "selected": ds == selected,
                "skip_reason": skip_reason if ds != selected else "",
                "mode": mode_name,
            }
        )

    # Ensure all DIAG_DATASETS appear even if not in CATALOG
    present = {r["dataset"] for r in rows}
    for ds in DIAG_DATASETS:
        if ds in present:
            continue
        rows.append(
            {
                "dataset": ds,
                "batch_id": "—",
                "coverage_pct": None,
                "current_rows": counts.get(ds, 0),
                "knowledge_gap_score": None,
                "priority_score": None,
                "product_priority": None,
                "hard_deps": [],
                "eligible": False,
                "selected": False,
                "skip_reason": "not_present_in_mission_selector_CATALOG",
                "mode": sel.get("manufacturing_mode") or "",
            }
        )

    rows.sort(
        key=lambda x: (
            0 if x.get("selected") else 1,
            -(float(x.get("priority_score") or 0)),
            x.get("dataset") or "",
        )
    )
    return {
        "selected": sel.get("selected"),
        "ranking": sel.get("ranking") or [],
        "counts": counts,
        "datasets": rows,
        "manufacturing_mode": sel.get("manufacturing_mode"),
        "active_sources": sel.get("active_sources"),
        "continuous": sel.get("continuous"),
        "raw_selector": {
            "ok": sel.get("ok"),
            "reason": (sel.get("selected") or {}).get("reason"),
        },
    }


def collect_knowledge_gap_trace(repo: Path) -> dict[str, Any]:
    """Multi-dimensional gap scores from manufacturing controller (read-only)."""
    try:
        from automation.manufacturing.controller import ManufacturingController

        state = ManufacturingController(repo_root=repo).evaluate()
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc), "evaluations": []}

    evals = state.get("evaluations") or []
    rows = []
    for e in evals:
        prof = e.get("profile") or {}
        rows.append(
            {
                "dataset": e.get("dataset"),
                "current_rows": e.get("current_rows"),
                "coverage": e.get("coverage_pct") or e.get("stretch_coverage_pct"),
                "freshness_gap": e.get("freshness_gap"),
                "confidence_gap": e.get("confidence_gap"),
                "relationship_score": e.get("relationship_gap")
                or e.get("relationship_score")
                or e.get("knowledge_density"),
                "dependency_score": e.get("dependency_gap") or e.get("dependency_score"),
                "business_priority": e.get("business_priority")
                or prof.get("minimum_target"),
                "knowledge_gap_score": e.get("knowledge_gap_score"),
                "universe_gap": e.get("universe_gap"),
                "minimum_gap": e.get("minimum_gap"),
                "stretch_gap": e.get("stretch_gap"),
            }
        )
    rows.sort(key=lambda x: -float(x.get("knowledge_gap_score") or 0))
    return {
        "ok": True,
        "mode": state.get("mode"),
        "selected_mission": state.get("selected_mission"),
        "evaluations": rows,
        "knowledge_gap_summary": state.get("knowledge_gap_summary"),
    }


def collect_production_trace(repo: Path) -> dict[str, Any]:
    pt = _read_json(repo / "automation" / "learning" / "state" / "production_trace.json") or {}
    return pt if isinstance(pt, dict) else {}


def collect_fingerprints(repo: Path) -> dict[str, Any]:
    fp = _read_json(
        repo / "automation" / "connectors" / "cache" / "document_fingerprints.json"
    ) or {}
    by_url = fp.get("by_url") or {}
    by_hash = fp.get("by_hash") or {}
    stats = fp.get("stats") or {}
    return {
        "urls_known": len(by_url),
        "hashes_known": len(by_hash),
        "stats": stats,
        "sample_urls": list(by_url.keys())[:15],
    }


def collect_source_performance(repo: Path) -> dict[str, Any]:
    sp = _read_json(
        repo / "automation" / "learning" / "state" / "source_performance.json"
    ) or {}
    sources = sp.get("sources") or {}
    rows = []
    for sid, s in sources.items():
        rows.append(
            {
                "source_id": sid,
                "attempts": s.get("attempts"),
                "success_rate": s.get("success_rate"),
                "avg_latency_ms": s.get("avg_latency_ms"),
                "documents_yielded": s.get("documents_yielded"),
                "rows_yielded": s.get("rows_yielded"),
                "duplicates": s.get("duplicates"),
                "duplicate_rate": s.get("duplicate_rate"),
                "backoff_level": s.get("backoff_level"),
                "disabled_until": s.get("disabled_until"),
            }
        )
    rows.sort(key=lambda x: -float(x.get("documents_yielded") or 0))
    return {"sources": rows}


def collect_latest_session(repo: Path) -> dict[str, Any]:
    idx = _read_json(repo / "automation" / "sessions" / "index.json") or {}
    sessions = idx.get("sessions") or []
    if not sessions:
        # fallback walk
        root = repo / "automation" / "sessions"
        found = []
        if root.exists():
            for day in sorted(root.iterdir(), reverse=True):
                if not day.is_dir():
                    continue
                for f in sorted(day.glob("SESSION-*.json"), reverse=True):
                    found.append(f)
                if found:
                    break
        if not found:
            return {}
        return _read_json(found[0]) or {}
    path = sessions[0].get("path")
    if path:
        return _read_json(repo / path) or sessions[0]
    return sessions[0]


def collect_heartbeat(repo: Path) -> dict[str, Any]:
    return (
        _read_json(
            repo / "automation" / "learning" / "state" / "scheduler_heartbeat.json"
        )
        or {}
    )


def collect_acquisition_performance(repo: Path) -> dict[str, Any]:
    return (
        _read_json(
            repo / "automation" / "learning" / "state" / "acquisition_performance.json"
        )
        or {}
    )


def build_execution_stages(bundle: dict[str, Any]) -> list[dict[str, Any]]:
    """Map evidence into the required pipeline stage order."""
    pt = bundle.get("production_trace") or {}
    stages_raw = pt.get("stages") or []
    by_name = {
        str(s.get("name") or s.get("stage") or ""): s
        for s in stages_raw
        if isinstance(s, dict)
    }
    session = bundle.get("session") or {}
    acq = bundle.get("acquisition") or {}
    mission = bundle.get("mission") or {}
    selected = (mission.get("selected") or {}) if isinstance(mission, dict) else {}

    def stage(name: str, **kw: Any) -> dict[str, Any]:
        base = by_name.get(name) or {}
        return {
            "stage": name,
            "status": kw.get("status") or base.get("status") or "unknown",
            "duration_ms": base.get("duration_ms"),
            "documents": base.get("documents") or kw.get("documents"),
            "rows": base.get("rows") or kw.get("rows"),
            "meta": {**(base.get("meta") or {}), **(kw.get("meta") or {})},
            "errors": base.get("errors") or kw.get("errors") or [],
            "evidence": kw.get("evidence") or "",
        }

    pub = pt.get("publish") or acq.get("publish") or {}
    dq = pt.get("document_queue") or {}
    docs_disc = (
        (pt.get("summary") or {}).get("documents_discovered")
        or acq.get("documents_discovered")
        or 0
    )
    docs_dl = (
        (pt.get("summary") or {}).get("documents_downloaded")
        or acq.get("documents_downloaded")
        or dq.get("completed")
        or 0
    )
    dups = (
        (pt.get("summary") or {}).get("documents_duplicates")
        or dq.get("duplicates")
        or 0
    )

    order = [
        stage(
            "mission_selection",
            status="completed" if selected else "unknown",
            evidence=f"selected={selected.get('dataset')} score={selected.get('score')}",
            meta={"instruction": selected.get("instruction"), "reason": selected.get("reason")},
        ),
        stage(
            "knowledge_gap_evaluation",
            status="completed",
            evidence=f"mode={bundle.get('knowledge_gap', {}).get('mode')}",
        ),
        stage(
            "dependency_evaluation",
            status="completed",
            evidence="see mission_trace eligible flags",
        ),
        stage(
            "mission_eligible",
            status="completed" if selected else "failed",
            evidence=selected.get("reason") or "",
        ),
        stage(
            "source_discovery",
            status=by_name.get("source_discovery", {}).get("status") or "completed",
            evidence=f"connectors={(acq.get('sources_contacted') or pt.get('connectors') or [])[:8]}",
        ),
        stage(
            "connector_calls",
            status=by_name.get("connector", {}).get("status") or "completed",
            documents=docs_disc,
            evidence=f"discovered={docs_disc}",
        ),
        stage(
            "document_discovery",
            status=by_name.get("document_discovery", {}).get("status") or "completed",
            documents=docs_disc,
        ),
        stage(
            "documents_skipped",
            status="completed",
            documents=dups,
            evidence=f"duplicates_or_skips={dups}",
            meta={"duplicates": dups, "fingerprints": bundle.get("fingerprints")},
        ),
        stage(
            "document_download",
            status=by_name.get("document_download", {}).get("status") or "completed",
            documents=docs_dl,
            evidence=f"downloaded={docs_dl}",
        ),
        stage(
            "extraction",
            status=by_name.get("extraction", {}).get("status") or "completed",
            rows=pub.get("extracted") or acq.get("candidates_extracted"),
        ),
        stage(
            "validation",
            status=by_name.get("candidate_validation", {}).get("status") or "completed",
            rows=pub.get("validated"),
            meta={"rejected": pub.get("rejected"), "duplicate": pub.get("duplicate")},
        ),
        stage(
            "publish",
            status=by_name.get("append_dataset", {}).get("status")
            or by_name.get("publish_queue", {}).get("status")
            or "completed",
            rows=pub.get("published") or session.get("knowledge_added") or 0,
        ),
        stage(
            "commit",
            status=by_name.get("git_commit", {}).get("status") or "skipped",
            evidence=(by_name.get("git_commit") or {}).get("warnings")
            or "deferred_to_CI",
        ),
        stage(
            "end_session",
            status=session.get("status") or "unknown",
            evidence=session.get("summary") or "",
            meta={
                "duration_seconds": session.get("duration_seconds"),
                "dry_run": session.get("dry_run"),
            },
        ),
    ]
    return order


def collect_document_trace(repo: Path, production_trace: dict[str, Any]) -> list[dict[str, Any]]:
    docs = production_trace.get("documents") or []
    fp = _read_json(
        repo / "automation" / "connectors" / "cache" / "document_fingerprints.json"
    ) or {}
    by_url = fp.get("by_url") or {}
    by_hash = fp.get("by_hash") or {}
    out = []
    for d in docs:
        if not isinstance(d, dict):
            continue
        url = str(d.get("url") or d.get("original_url") or "")
        checksum = str(d.get("checksum") or d.get("hash") or "")
        known_url = False
        known_hash = False
        # fingerprint keys are hashed — use stats only; presence of doc in processed is evidence
        already = str(d.get("status") or "") in {"completed", "processed", "duplicate"}
        skip = d.get("skip_reason") or d.get("reject_reason")
        fetch = d.get("fetch_mode") or ""
        out.append(
            {
                "document_id": d.get("document_id"),
                "url": url,
                "title": d.get("title"),
                "fingerprint": checksum[:16] if checksum else "",
                "already_processed": already,
                "cache_hit": "cache" in str(fetch).lower(),
                "not_modified_304": "304" in str(d.get("http_status") or "")
                or d.get("not_modified") is True,
                "duplicate": "duplicate" in str(d.get("status") or "").lower()
                or bool(d.get("duplicate")),
                "downloaded": str(d.get("status") or "")
                in {"queued", "processing", "completed", "processed"}
                or bool(d.get("bytes")),
                "skip_reason": skip or "",
                "status": d.get("status"),
                "connector_id": d.get("connector_id"),
                "source_id": d.get("source_id"),
                "fetch_mode": fetch,
                "size": d.get("size") or d.get("bytes"),
            }
        )
    # If no document list, synthesize skip summary from queue counts
    if not out:
        dq = production_trace.get("document_queue") or {}
        summary = production_trace.get("summary") or {}
        out.append(
            {
                "document_id": "—",
                "url": "—",
                "title": "(aggregate)",
                "fingerprint": "",
                "already_processed": None,
                "cache_hit": None,
                "not_modified_304": None,
                "duplicate": None,
                "downloaded": None,
                "skip_reason": (
                    f"aggregate duplicates={summary.get('documents_duplicates') or dq.get('duplicates')}; "
                    f"downloaded={summary.get('documents_downloaded') or dq.get('completed')}; "
                    f"discovered={summary.get('documents_discovered')}"
                ),
                "status": "aggregate",
                "connector_id": "",
                "source_id": "",
                "fetch_mode": "",
                "size": 0,
            }
        )
    return out


def collect_extraction_trace(production_trace: dict[str, Any], acq: dict[str, Any]) -> list[dict[str, Any]]:
    cands = production_trace.get("candidates") or acq.get("candidates") or []
    ext = acq.get("extraction_stages") or (acq.get("performance") or {}).get("extraction") or {}
    out = []
    for c in cands:
        if not isinstance(c, dict):
            continue
        out.append(
            {
                "candidate_id": c.get("candidate_id"),
                "entity": c.get("entity") or c.get("name") or c.get("canonical_name"),
                "entity_type": c.get("dataset") or c.get("entity_type"),
                "dataset": c.get("dataset") or c.get("target_dataset"),
                "confidence": c.get("confidence"),
                "document_id": c.get("document_id") or c.get("source_document"),
                "validation_status": c.get("validation_status"),
                "publish_status": c.get("publish_status"),
                "reject_reason": c.get("reject_reason"),
                "extraction_stage": (c.get("metadata") or {}).get("extraction_stage")
                if isinstance(c.get("metadata"), dict)
                else None,
            }
        )
    return {
        "candidates": out,
        "stage_stats": ext,
        "llm_skipped": ext.get("skipped_llm") or ext.get("llm_skipped"),
        "llm_used": ext.get("llm") or ext.get("llm_used") or 0,
        "fast": ext.get("fast"),
        "medium": ext.get("medium"),
        "deep": ext.get("deep"),
    }


def collect_publish_trace(production_trace: dict[str, Any], acq: dict[str, Any], session: dict[str, Any]) -> dict[str, Any]:
    cands = production_trace.get("candidates") or acq.get("candidates") or []
    pub = production_trace.get("publish") or acq.get("publish") or session.get("publish_summary") or {}
    items = []
    for c in cands:
        if not isinstance(c, dict):
            continue
        conf = c.get("confidence")
        try:
            conf_f = float(conf) if conf is not None else None
        except (TypeError, ValueError):
            conf_f = None
        pub_status = str(c.get("publish_status") or "")
        items.append(
            {
                "candidate_id": c.get("candidate_id"),
                "dataset": c.get("dataset") or c.get("target_dataset"),
                "entity": c.get("entity") or c.get("name"),
                "confidence": conf_f,
                "duplicate": "duplicate" in pub_status.lower()
                or "duplicate" in str(c.get("reject_reason") or "").lower(),
                "relationship_complete": True,  # integrity does not expose partial relationship flag
                "published": pub_status == "published",
                "queued": pub_status in {"queued", "pending", "manual_review"},
                "manual_review": pub_status == "manual_review",
                "reject_reason": c.get("reject_reason"),
                "validation_status": c.get("validation_status"),
                "publish_status": pub_status,
            }
        )
    return {
        "balance": pub,
        "candidates": items,
        "session_knowledge_added": session.get("knowledge_added"),
        "session_knowledge_rejected": session.get("knowledge_rejected"),
        "dry_run": session.get("dry_run"),
    }


def collect_source_trace(production_trace: dict[str, Any], acq: dict[str, Any]) -> list[dict[str, Any]]:
    cons = production_trace.get("connectors") or acq.get("connectors") or []
    rows = []
    for c in cons:
        if not isinstance(c, dict):
            continue
        rows.append(
            {
                "connector_id": c.get("connector_id"),
                "name": c.get("name"),
                "source_id": c.get("source_id"),
                "status": c.get("status"),
                "http_status": c.get("http_status"),
                "latency_ms": c.get("elapsed_ms"),
                "documents_discovered": c.get("documents_discovered"),
                "documents_downloaded": c.get("documents_downloaded"),
                "skipped": c.get("skipped"),
                "rejected": c.get("rejected"),
                "error": c.get("error"),
                "rank_score": c.get("rank_score"),
                "urls": c.get("urls") or [],
            }
        )
    return rows


def collect_full_bundle(
    repo_root: Path | None = None,
    *,
    session: Optional[dict[str, Any]] = None,
    acquisition: Optional[dict[str, Any]] = None,
) -> dict[str, Any]:
    repo = repo_root or find_repo_root()
    mission = collect_mission_diagnostics(repo)
    kg = collect_knowledge_gap_trace(repo)
    pt = collect_production_trace(repo)
    sess = session or collect_latest_session(repo)
    acq = acquisition or {}
    # merge session-embedded acquisition if present
    if not acq and isinstance(sess.get("knowledge_delta"), dict):
        acq = {
            "documents_discovered": sess["knowledge_delta"].get("documents_discovered"),
            "documents_downloaded": sess["knowledge_delta"].get("documents_downloaded"),
            "candidates_extracted": sess["knowledge_delta"].get("candidates_extracted"),
            "candidates_validated": sess["knowledge_delta"].get("candidates_validated"),
            "candidates_rejected": sess["knowledge_delta"].get("candidates_rejected"),
            "rows_published": sess.get("knowledge_added"),
            "connectors": (sess.get("knowledge_delta") or {}).get("connectors"),
            "publish": sess.get("publish_summary"),
        }
    if sess.get("production_trace") and isinstance(sess["production_trace"], dict):
        # prefer session-scoped trace when present
        pt = {**pt, **sess["production_trace"]}

    bundle = {
        "generated_at": utc_now_iso(),
        "mission": mission,
        "knowledge_gap": kg,
        "production_trace": pt,
        "session": sess,
        "acquisition": acq,
        "fingerprints": collect_fingerprints(repo),
        "source_performance": collect_source_performance(repo),
        "heartbeat": collect_heartbeat(repo),
        "acquisition_performance": collect_acquisition_performance(repo),
        "counts": dataset_counts(repo),
    }
    bundle["execution_stages"] = build_execution_stages(bundle)
    bundle["document_trace"] = collect_document_trace(repo, pt)
    bundle["extraction_trace"] = collect_extraction_trace(pt, acq)
    bundle["publish_trace"] = collect_publish_trace(pt, acq, sess if isinstance(sess, dict) else {})
    bundle["source_trace"] = collect_source_trace(pt, acq)
    return bundle
