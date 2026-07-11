"""Candidate lifecycle diagnostics — observe only.

Replays Integrity Guard rules rule-by-rule for evidence reporting.
Does NOT modify validation, thresholds, or publisher behavior.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Mapping, Optional

from automation.lib.paths import find_repo_root
from automation.quality.integrity_guard import (
    ID_FIELDS,
    ID_PATTERNS,
    _company_ids,
    _conf,
    _industry_ids,
    _load_index,
    _pain_ids,
    _stem,
    filter_append_rows,
    validate_row,
)

CONFIDENCE_THRESHOLD = 0.80  # integrity_guard fixed floor (observe only)

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
    "business_signal_library",
]


def _rule(
    name: str,
    status: str,
    *,
    input_val: Any = None,
    expected: Any = None,
    actual: Any = None,
    evidence: str = "",
) -> dict[str, Any]:
    return {
        "rule": name,
        "status": status,  # PASS | FAIL | SKIP | N/A
        "input": input_val,
        "expected": expected,
        "actual": actual,
        "evidence": evidence,
    }


def explain_integrity_rules(
    dataset_path: Path,
    row: Mapping[str, Any],
    *,
    repo_root: Path,
    existing_ids: Optional[set[str]] = None,
    batch_ids: Optional[set[str]] = None,
) -> list[dict[str, Any]]:
    """Evaluate every Integrity Guard rule independently (observe-only mirror)."""
    root = repo_root
    stem = _stem(dataset_path)
    rules: list[dict[str, Any]] = []
    id_field = ID_FIELDS.get(stem)
    batch_ids = batch_ids or set()

    # Schema / primary id
    if not id_field:
        rules.append(
            _rule(
                "schema_indexed_dataset",
                "PASS",
                input_val=stem,
                expected="known ID field or unindexed allow",
                actual="unindexed",
                evidence="ok_unindexed_dataset path",
            )
        )
        rules.append(
            _rule(
                "integrity_final",
                "PASS",
                evidence="validate_row short-circuit ok_unindexed_dataset",
            )
        )
        return rules

    rules.append(
        _rule(
            "schema_indexed_dataset",
            "PASS",
            input_val=stem,
            expected=id_field,
            actual=id_field,
            evidence=f"ID field mapped: {id_field}",
        )
    )

    eid = str(row.get(id_field) or "").strip()
    rules.append(
        _rule(
            "primary_id_present",
            "PASS" if eid else "FAIL",
            input_val=row.get(id_field),
            expected=f"non-empty {id_field}",
            actual=eid or "(empty)",
            evidence=f"{id_field}={eid!r}",
        )
    )

    pat = ID_PATTERNS.get(stem)
    if pat:
        ok_pat = bool(eid and pat.match(eid))
        rules.append(
            _rule(
                "primary_id_pattern",
                "PASS" if ok_pat else ("FAIL" if eid else "SKIP"),
                input_val=eid,
                expected=pat.pattern,
                actual=eid,
                evidence=f"pattern {pat.pattern} vs {eid!r}",
            )
        )
    else:
        rules.append(
            _rule(
                "primary_id_pattern",
                "N/A",
                input_val=eid,
                expected="no pattern for dataset",
                actual=eid,
                evidence="ID_PATTERNS has no entry",
            )
        )

    existing = (
        existing_ids
        if existing_ids is not None
        else (_load_index(dataset_path, id_field) if id_field else set())
    )
    in_batch = bool(eid and eid in batch_ids)
    in_existing = bool(eid and eid in existing)
    rules.append(
        _rule(
            "duplicate_id_in_batch",
            "FAIL" if in_batch else "PASS",
            input_val=eid,
            expected="id not already in this batch",
            actual="in_batch" if in_batch else "unique_in_batch",
            evidence=f"batch_ids_contains={in_batch}",
        )
    )
    rules.append(
        _rule(
            "duplicate_id_existing_dataset",
            "FAIL" if in_existing else "PASS",
            input_val=eid,
            expected="id not in existing CSV",
            actual="exists_in_csv" if in_existing else "new_id",
            evidence=f"existing_csv_contains={in_existing}; dataset_path={dataset_path.name}",
        )
    )

    conf = _conf(row)
    conf_ok = conf is None or conf >= CONFIDENCE_THRESHOLD
    rules.append(
        _rule(
            "confidence_threshold",
            "PASS" if conf_ok else "FAIL",
            input_val=conf,
            expected=f">= {CONFIDENCE_THRESHOLD}",
            actual=conf if conf is not None else "(missing → not blocked by conf rule)",
            evidence=f"threshold={CONFIDENCE_THRESHOLD}; conf={conf}",
        )
    )
    rules.append(
        _rule(
            "confidence_present",
            "PASS" if conf is not None else "N/A",
            input_val=conf,
            expected="optional numeric confidence in Notes/Data Sources/Confidence",
            actual=conf,
            evidence="integrity only fails when conf is present and < 0.80",
        )
    )

    # Relationship / FK rules
    if stem == "company_profile":
        iid = str(row.get("Industry ID") or "").strip()
        inds = _industry_ids(root)
        if iid:
            rules.append(
                _rule(
                    "relationship_industry_fk",
                    "PASS" if iid in inds else "FAIL",
                    input_val=iid,
                    expected="Industry ID in industry_library",
                    actual="found" if iid in inds else "missing",
                    evidence=f"Industry ID={iid}",
                )
            )
        else:
            has_name = bool(str(row.get("Industry") or "").strip())
            rules.append(
                _rule(
                    "relationship_industry_link",
                    "PASS" if has_name else "FAIL",
                    input_val=row.get("Industry"),
                    expected="Industry ID or Industry name",
                    actual="name_only" if has_name else "missing",
                    evidence="no Industry ID; Industry name check",
                )
            )
    elif stem == "pain_point_library":
        iid = str(row.get("Industry ID") or "").strip()
        inds = _industry_ids(root)
        rules.append(
            _rule(
                "relationship_industry_fk",
                "PASS" if iid and iid in inds else "FAIL",
                input_val=iid,
                expected="Industry ID in industry_library",
                actual=iid or "(empty)",
                evidence=f"in_registry={iid in inds if iid else False}",
            )
        )
    elif stem == "solution_library":
        pid = str(row.get("Related Pain ID") or "").strip()
        pains = _pain_ids(root)
        rules.append(
            _rule(
                "relationship_pain_fk",
                "PASS" if pid and pid in pains else "FAIL",
                input_val=pid,
                expected="Related Pain ID in pain_point_library",
                actual=pid or "(empty)",
                evidence=f"in_registry={pid in pains if pid else False}",
            )
        )
    elif stem == "case_study_library":
        cid = str(row.get("Company ID") or "").strip()
        comps = _company_ids(root)
        rules.append(
            _rule(
                "relationship_company_fk",
                "PASS" if cid and cid in comps else "FAIL",
                input_val=cid,
                expected="Company ID in company_profile",
                actual=cid or "(empty)",
                evidence=f"in_registry={cid in comps if cid else False}",
            )
        )
    elif stem == "opportunity_analysis":
        cid = str(row.get("Company ID") or "").strip()
        comps = _company_ids(root)
        if cid:
            rules.append(
                _rule(
                    "relationship_company_fk",
                    "PASS" if cid in comps else "FAIL",
                    input_val=cid,
                    expected="Company ID in company_profile when present",
                    actual=cid,
                    evidence=f"in_registry={cid in comps}",
                )
            )
        else:
            rules.append(
                _rule(
                    "relationship_company_fk",
                    "N/A",
                    input_val=None,
                    expected="optional when empty",
                    actual="(empty)",
                    evidence="no Company ID provided",
                )
            )
    else:
        rules.append(
            _rule(
                "relationship_fk",
                "N/A",
                input_val=stem,
                expected="no FK rules for this dataset",
                actual="n/a",
                evidence="integrity_guard has no FK branch for this stem",
            )
        )

    # Provenance
    blob = " ".join(
        str(row.get(k) or "")
        for k in ("Notes", "Data Sources", "Data Source", "References")
    )
    provenance_required = stem in {
        "industry_library",
        "company_profile",
        "product_catalog",
        "pain_point_library",
        "solution_library",
        "buyer_persona_library",
        "decision_maker_library",
        "regulation_library",
        "risk_library",
        "trend_library",
        "competitor_library",
    }
    has_src = "SRC-" in blob or "source" in blob.lower() or bool(
        str(
            row.get("Data Sources")
            or row.get("Data Source")
            or row.get("Information Source")
            or ""
        ).strip()
    )
    if not provenance_required:
        rules.append(
            _rule(
                "provenance_required",
                "N/A",
                evidence=f"dataset {stem} not in provenance-required set",
            )
        )
        rules.append(
            _rule(
                "provenance_present",
                "PASS" if has_src else "N/A",
                input_val=blob[:80],
                expected="optional",
                actual="present" if has_src else "absent",
                evidence=blob[:200],
            )
        )
    else:
        # fails only when provenance missing AND conf is None
        prov_fail = (not has_src) and conf is None
        rules.append(
            _rule(
                "provenance_required",
                "PASS" if not prov_fail else "FAIL",
                input_val={"has_source_marker": has_src, "confidence": conf},
                expected="SRC-/source text OR conf present",
                actual="fail" if prov_fail else "ok",
                evidence=blob[:200],
            )
        )
        rules.append(
            _rule(
                "provenance_present",
                "PASS" if has_src else "FAIL",
                input_val=blob[:80],
                expected="Notes/Data Sources contain source markers",
                actual="present" if has_src else "absent",
                evidence=blob[:200],
            )
        )

    # Freshness — not enforced by integrity_guard (report N/A with evidence)
    rules.append(
        _rule(
            "freshness",
            "N/A",
            input_val=row.get("Published Date") or row.get("Last Updated"),
            expected="not enforced by integrity_guard",
            actual=row.get("Published Date") or row.get("Last Updated") or "(none)",
            evidence="integrity_guard has no freshness rule",
        )
    )

    # Completeness of required id field already covered; general completeness N/A
    rules.append(
        _rule(
            "completeness_primary",
            "PASS" if eid else "FAIL",
            input_val=eid,
            expected="primary id present",
            actual=eid or "(empty)",
            evidence="primary id completeness",
        )
    )

    # Official final decision (source of truth)
    ok, reason = validate_row(
        dataset_path, row, repo_root=root, existing_ids=existing | batch_ids
    )
    rules.append(
        _rule(
            "integrity_final_validate_row",
            "PASS" if ok else "FAIL",
            input_val={id_field: eid, "confidence": conf},
            expected="validate_row ok",
            actual=reason,
            evidence=f"automation.quality.integrity_guard.validate_row → {reason}",
        )
    )
    return rules


def load_candidate_records(
    repo: Path,
    *,
    session: Optional[dict[str, Any]] = None,
) -> list[dict[str, Any]]:
    """Load full candidate records from queue + session production_trace."""
    by_id: dict[str, dict[str, Any]] = {}
    # Prefer queue files (full payload)
    for folder in (
        repo / "automation" / "queue" / "publish",
        repo / "automation" / "queue" / "pending",
        repo / "automation" / "queue" / "approved",
        repo / "automation" / "queue" / "rejected",
        repo / "automation" / "queue" / "candidates" / "pending",
        repo / "automation" / "queue" / "candidates" / "approved",
        repo / "automation" / "queue" / "candidates" / "rejected",
    ):
        if not folder.exists():
            continue
        for p in folder.glob("CAND-*.json"):
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
                cid = str(data.get("candidate_id") or p.stem)
                data["_queue_path"] = str(p.relative_to(repo))
                by_id[cid] = data
            except Exception:  # noqa: BLE001
                continue

    # Session / production_trace candidates (may lack payload)
    traces: list[dict[str, Any]] = []
    if session and isinstance(session.get("production_trace"), dict):
        traces.append(session["production_trace"])
    pt = repo / "automation" / "learning" / "state" / "production_trace.json"
    if pt.exists():
        try:
            traces.append(json.loads(pt.read_text(encoding="utf-8")))
        except Exception:  # noqa: BLE001
            pass

    for tr in traces:
        for c in tr.get("candidates") or []:
            if not isinstance(c, dict):
                continue
            cid = str(c.get("candidate_id") or "")
            if not cid:
                continue
            if cid in by_id:
                # merge status fields from trace
                by_id[cid]["_trace"] = c
            else:
                by_id[cid] = {
                    "candidate_id": cid,
                    "entity_id": c.get("entity_id"),
                    "target_dataset": c.get("dataset") or c.get("target_dataset"),
                    "canonical_name": c.get("entity") or c.get("name"),
                    "payload": {},
                    "provenance": {
                        "confidence": c.get("confidence"),
                        "source_id": c.get("source_id"),
                        "source_url": c.get("source_url"),
                    },
                    "metadata": {"document_id": c.get("document_id")},
                    "_trace": c,
                    "_queue_path": None,
                }

    # If session specifies candidate ids, prioritize those
    focus_ids: set[str] = set()
    if session:
        for c in (session.get("production_trace") or {}).get("candidates") or []:
            if isinstance(c, dict) and c.get("candidate_id"):
                focus_ids.add(str(c["candidate_id"]))
        kd = session.get("knowledge_delta") or {}
        if kd.get("candidate_id"):
            focus_ids.add(str(kd["candidate_id"]))

    records = list(by_id.values())
    if focus_ids:
        focused = [r for r in records if str(r.get("candidate_id")) in focus_ids]
        if focused:
            return focused
    return records


def analyze_candidate(
    cand: dict[str, Any],
    *,
    repo: Path,
    session: Optional[dict[str, Any]] = None,
    existing_cache: Optional[dict[str, set[str]]] = None,
) -> dict[str, Any]:
    """Full lifecycle + rule evaluation for one candidate."""
    existing_cache = existing_cache if existing_cache is not None else {}
    cid = str(cand.get("candidate_id") or "")
    payload = cand.get("payload") or {}
    prov = cand.get("provenance") or {}
    meta = cand.get("metadata") or {}
    trace = cand.get("_trace") or {}
    dataset = str(
        cand.get("target_dataset")
        or trace.get("dataset")
        or meta.get("dataset")
        or ""
    )
    # service_library maps to product_catalog.csv
    csv_stem = "product_catalog" if dataset == "service_library" else dataset
    csv_path = repo / "domains" / "business_development" / f"{csv_stem}.csv"

    document_id = (
        meta.get("document_id")
        or trace.get("document_id")
        or trace.get("source_document")
        or ""
    )
    mission_id = (
        meta.get("mission_id")
        or (session or {}).get("mission_id")
        or payload.get("Mission ID")
        or ""
    )
    session_id = meta.get("session_id") or (session or {}).get("session_id") or ""
    conf = prov.get("confidence")
    if conf is None:
        conf = _conf(payload)
    try:
        conf_f = float(conf) if conf is not None else None
    except (TypeError, ValueError):
        conf_f = None

    # Ensure payload has enough for integrity if empty but entity_id known
    row = dict(payload)
    if not row and cand.get("entity_id"):
        id_field = ID_FIELDS.get(csv_stem) or "ID"
        row[id_field] = cand.get("entity_id")
        if conf_f is not None:
            row["Confidence"] = conf_f
            row["Notes"] = f"confidence={conf_f}"

    id_field = ID_FIELDS.get(csv_stem)
    if csv_stem not in existing_cache and id_field and csv_path.exists():
        existing_cache[csv_stem] = _load_index(csv_path, id_field)
    existing = existing_cache.get(csv_stem) or set()

    rules: list[dict[str, Any]] = []
    if not csv_path.exists():
        rules.append(
            _rule(
                "dataset_csv_exists",
                "FAIL",
                input_val=str(csv_path),
                expected="CSV exists",
                actual="missing",
                evidence=f"path {csv_path} not found",
            )
        )
        integrity_ok = False
        integrity_reason = "dataset_csv_missing"
    elif not row:
        rules.append(
            _rule(
                "payload_present",
                "FAIL",
                evidence="candidate has no payload for integrity replay",
            )
        )
        integrity_ok = False
        integrity_reason = "missing_payload"
    else:
        rules.append(
            _rule(
                "dataset_csv_exists",
                "PASS",
                actual=str(csv_path.name),
                evidence="CSV present",
            )
        )
        rules.append(
            _rule(
                "payload_present",
                "PASS",
                evidence=f"payload fields={len(row)}",
            )
        )
        rules.extend(
            explain_integrity_rules(
                csv_path,
                row,
                repo_root=repo,
                existing_ids=existing,
            )
        )
        integrity_ok, integrity_reason = validate_row(
            csv_path, row, repo_root=repo, existing_ids=existing
        )

    # Failed rules (blocking)
    failed = [r for r in rules if r["status"] == "FAIL"]
    primary_block = None
    for r in rules:
        if r["rule"] == "integrity_final_validate_row" and r["status"] == "FAIL":
            primary_block = str(r.get("actual") or integrity_reason)
            break
    if not primary_block and failed:
        primary_block = failed[0]["rule"]

    dry_run = bool((session or {}).get("dry_run"))
    # Publish decision evidence
    trace_pub = str(trace.get("publish_status") or "")
    publish_attempted = not dry_run  # production publish path only when not dry_run
    if dry_run:
        publish_decision = "Skipped"
        publish_reason = "session_dry_run_true — publisher did not append"
    elif integrity_ok is False:
        publish_decision = "Rejected"
        publish_reason = f"integrity_guard:{primary_block or integrity_reason}"
    elif trace_pub == "published":
        publish_decision = "Published"
        publish_reason = "append succeeded"
    elif trace_pub in {"queued", "pending", "manual_review"}:
        publish_decision = "Queued" if trace_pub != "manual_review" else "Manual Review"
        publish_reason = f"publish_status={trace_pub}"
    else:
        publish_decision = "Rejected" if primary_block else "Queued"
        publish_reason = primary_block or f"publish_status={trace_pub or 'unknown'}"

    # False negative: single failing integrity rule, all other critical rules PASS
    critical_fail = [
        r
        for r in failed
        if r["rule"]
        not in {
            "provenance_present",  # may be soft when conf present
            "confidence_present",
            "freshness",
        }
    ]
    # Use integrity_final as authority
    final_fail = any(
        r["rule"] == "integrity_final_validate_row" and r["status"] == "FAIL"
        for r in rules
    )
    blocking_rules = [
        r["rule"]
        for r in rules
        if r["status"] == "FAIL"
        and r["rule"]
        not in {"integrity_final_validate_row", "provenance_present", "confidence_present", "freshness"}
    ]
    # Map final reason to rule
    reason = str(integrity_reason or "")
    if reason.startswith("duplicate_id"):
        blocking_rules = ["duplicate_id_existing_dataset"]
    elif reason.startswith("duplicate_id_in_batch"):
        blocking_rules = ["duplicate_id_in_batch"]
    elif reason.startswith("confidence_below"):
        blocking_rules = ["confidence_threshold"]
    elif reason.startswith("missing_provenance"):
        blocking_rules = ["provenance_required"]
    elif "fk" in reason or "industry" in reason or "pain" in reason or "company" in reason:
        blocking_rules = [r for r in blocking_rules if "relationship" in r] or blocking_rules

    potential_fn = bool(final_fail and len(set(blocking_rules)) == 1)

    return {
        "candidate_id": cid,
        "document_id": document_id,
        "mission_id": mission_id,
        "session_id": session_id,
        "dataset": dataset or csv_stem,
        "entity_id": cand.get("entity_id") or (payload.get(ID_FIELDS.get(csv_stem, "")) if csv_stem else ""),
        "entity": cand.get("canonical_name") or trace.get("entity") or payload.get("Signal Name"),
        "confidence": conf_f,
        "confidence_threshold": CONFIDENCE_THRESHOLD,
        "rules": rules,
        "failed_rules": [r["rule"] for r in failed],
        "blocking_rules": blocking_rules,
        "primary_block_reason": primary_block or integrity_reason,
        "integrity_ok": integrity_ok,
        "integrity_reason": integrity_reason,
        "dry_run": dry_run,
        "publish_attempted": publish_attempted,
        "publish_decision": publish_decision,
        "publish_reason": publish_reason,
        "trace_publish_status": trace_pub,
        "trace_reject_reason": trace.get("reject_reason"),
        "validation_status": trace.get("validation_status") or prov.get("validation_status"),
        "queue_path": cand.get("_queue_path"),
        "potential_false_negative": potential_fn,
        "false_negative_rule": blocking_rules[0] if potential_fn and blocking_rules else None,
        "payload_preview": {
            k: row.get(k)
            for k in list(row.keys())[:12]
        }
        if row
        else {},
    }


def aggregate_rule_stats(analyses: list[dict[str, Any]]) -> dict[str, Any]:
    total = max(1, len(analyses))
    blocked = [a for a in analyses if not a.get("integrity_ok")]
    reason_counter: Counter[str] = Counter()
    rule_counter: Counter[str] = Counter()
    for a in analyses:
        reason = str(a.get("primary_block_reason") or a.get("integrity_reason") or "")
        if not a.get("integrity_ok"):
            # normalize reason family
            if reason.startswith("duplicate_id"):
                family = "Duplicate"
            elif "confidence" in reason:
                family = "ConfidenceLow"
            elif "provenance" in reason:
                family = "MissingProvenance"
            elif "fk" in reason or "industry" in reason or "pain" in reason or "company" in reason:
                family = "MissingRelationship"
            elif "schema" in reason or "pattern" in reason or "primary_id" in reason:
                family = "SchemaError"
            elif reason:
                family = "Other"
            else:
                family = "Other"
            reason_counter[family] += 1
        for r in a.get("failed_rules") or []:
            rule_counter[r] += 1

    freq = []
    for family, n in reason_counter.most_common():
        freq.append(
            {
                "rule_family": family,
                "count": n,
                "pct": round(100.0 * n / total, 1),
            }
        )

    impacts = []
    for rule, n in rule_counter.most_common():
        confs = [
            float(a["confidence"])
            for a in analyses
            if rule in (a.get("failed_rules") or []) and a.get("confidence") is not None
        ]
        impacts.append(
            {
                "rule": rule,
                "candidates_affected": n,
                "rows_blocked": n,
                "pct_blocked": round(100.0 * n / total, 1),
                "average_confidence": round(sum(confs) / len(confs), 4) if confs else None,
            }
        )

    return {
        "total_candidates": len(analyses),
        "blocked": len(blocked),
        "passed_integrity": sum(1 for a in analyses if a.get("integrity_ok")),
        "frequency": freq,
        "rule_impact": impacts,
    }


def dataset_summary(analyses: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_ds: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for a in analyses:
        by_ds[str(a.get("dataset") or "unknown")].append(a)
    out = []
    for ds in DIAG_DATASETS + sorted(set(by_ds) - set(DIAG_DATASETS)):
        items = by_ds.get(ds) or []
        if not items and ds not in by_ds:
            continue
        reasons = Counter(
            str(a.get("primary_block_reason") or a.get("integrity_reason") or "none")
            for a in items
            if not a.get("integrity_ok")
        )
        top_rule = reasons.most_common(1)[0][0] if reasons else "—"
        confs = [float(a["confidence"]) for a in items if a.get("confidence") is not None]
        published = sum(1 for a in items if a.get("publish_decision") == "Published")
        rejected = sum(1 for a in items if a.get("publish_decision") == "Rejected" or not a.get("integrity_ok"))
        out.append(
            {
                "dataset": ds,
                "candidates": len(items),
                "published": published,
                "rejected": rejected,
                "top_rejection_rule": top_rule,
                "average_confidence": round(sum(confs) / len(confs), 4) if confs else None,
            }
        )
    return out


def run_candidate_lifecycle_diagnostics(
    repo_root: Path | None = None,
    *,
    session: Optional[dict[str, Any]] = None,
) -> dict[str, Any]:
    """Build full candidate lifecycle diagnostic bundle."""
    repo = repo_root or find_repo_root()
    if session is None:
        from automation.diagnostics.collector import collect_latest_session

        session = collect_latest_session(repo)

    cands = load_candidate_records(repo, session=session)
    existing_cache: dict[str, set[str]] = {}
    analyses = [
        analyze_candidate(c, repo=repo, session=session, existing_cache=existing_cache)
        for c in cands
    ]
    stats = aggregate_rule_stats(analyses)
    ds_sum = dataset_summary(analyses)
    false_negatives = [a for a in analyses if a.get("potential_false_negative")]

    # Root cause for candidate rejections (integrity), separate from dry_run gate
    blocked = [a for a in analyses if not a.get("integrity_ok")]
    reason_counts = Counter(
        str(a.get("primary_block_reason") or a.get("integrity_reason")) for a in blocked
    )
    family_counts = Counter()
    for a in blocked:
        reason = str(a.get("integrity_reason") or "")
        if reason.startswith("duplicate_id"):
            family_counts["duplicate_id"] += 1
        elif "confidence" in reason:
            family_counts["confidence_below_threshold"] += 1
        elif "provenance" in reason:
            family_counts["missing_provenance"] += 1
        elif "fk" in reason or "industry" in reason or "pain" in reason or "company" in reason:
            family_counts["relationship_fk"] += 1
        else:
            family_counts[reason or "other"] += 1
    top_family, top_n = (
        family_counts.most_common(1)[0] if family_counts else ("none", 0)
    )
    top_reason = top_family
    if top_family == "duplicate_id":
        top_reason = "duplicate_id (primary entity id already exists in target CSV)"
        examples = [str(a.get("integrity_reason")) for a in blocked if str(a.get("integrity_reason") or "").startswith("duplicate_id")]
        if examples:
            top_reason += f" — e.g. {examples[0]}"

    dry_run = bool((session or {}).get("dry_run"))
    return {
        "session_id": (session or {}).get("session_id"),
        "mission_id": (session or {}).get("mission_id"),
        "dry_run": dry_run,
        "candidates": analyses,
        "statistics": stats,
        "dataset_summary": ds_sum,
        "false_negatives": false_negatives,
        "root_cause": {
            "primary_integrity_block_reason": top_reason,
            "candidates_blocked_by_primary": top_n,
            "total_candidates": len(analyses),
            "integrity_blocked": len(blocked),
            "dry_run_blocked_publish": dry_run,
            "evidence": [
                f"session_id={(session or {}).get('session_id')}",
                f"dry_run={dry_run}",
                f"candidates_analyzed={len(analyses)}",
                f"integrity_blocked={len(blocked)}",
                f"top_family={top_family} count={top_n}",
                f"family_histogram={dict(family_counts)}",
                f"reason_histogram={dict(reason_counts)}",
                *[
                    f"candidate {a.get('candidate_id')} entity_id={a.get('entity_id')} "
                    f"reason={a.get('integrity_reason')} conf={a.get('confidence')}"
                    for a in blocked
                ],
            ],
            "could_continue_if_satisfied": (
                f"If rule/condition `{top_reason}` were satisfied for {top_n}/{len(analyses)} candidate(s), "
                f"integrity_guard.validate_row would return ok for those candidates "
                f"(publisher append still gated by session dry_run={dry_run})."
            ),
        },
    }
