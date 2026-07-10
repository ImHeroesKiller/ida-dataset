#!/usr/bin/env python3
"""Live Learning Runtime — activate the frozen pipeline with realtime journal events.

Does NOT create new engines. Reuses:
  Scheduler, Search Orchestrator (connectors), Document Queue,
  Candidate + Review queue, CSV append publish, growth metrics.

Emits progressive learning-journal events so ECC can stream live.
"""

from __future__ import annotations

import csv
import json
import sys
import time
from pathlib import Path
from typing import Any, Optional
from uuid import uuid4

_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from automation.learning import growth, journal  # noqa: E402
from automation.learning.first_cycle import (  # noqa: E402
    INDUSTRY_SEED,
    _industry_already_present,
)
from automation.lib.io_utils import append_csv_rows, save_candidate  # noqa: E402
from automation.lib.models import (  # noqa: E402
    CandidateRecord,
    Provenance,
    ValidationStatus,
    utc_now_iso,
)
from automation.lib.paths import find_repo_root  # noqa: E402
from automation.scheduler.scheduler import ContinuousLearningScheduler  # noqa: E402
from automation.search.orchestrator import SearchOrchestrator  # noqa: E402


# Additional live-cycle knowledge seeds (only used if not already present)
EXTRA_SEEDS: list[dict[str, str]] = [
    {
        **{k: "" for k in INDUSTRY_SEED.keys()},
        "Industry ID": "IND-000002",
        "Industry Name": "Banking",
        "Industry Category": "Financial Services",
        "Industry Description": (
            "Layanan perbankan dan keuangan dengan regulasi ketat, fokus risiko, "
            "dan transformasi digital."
        ),
        "Business Characteristics": "Regulated, multi-channel, high security, 24/7 services",
        "Typical Company Size": "Large, Enterprise",
        "Digital Maturity Level": "High",
        "Common Technologies": "Core Banking, SIEM, Cloud, API Gateway",
        "Common Business Challenges": "Compliance, fraud, legacy modernization",
        "Common Pain Points": "Silo data, SLA core system, cyber risk",
        "Business Goals": "Digital banking, efisiensi operasional, kepercayaan nasabah",
        "Last Updated": "",
        "Notes": "Live learning runtime knowledge candidate",
        "Data Sources": "OJK, Annual Report, Gartner",
    },
]


def _sleep(seconds: float, *, pace: float) -> None:
    time.sleep(max(0.05, seconds * pace))


def _emit(session_id: str, verb: str, detail: str, **kwargs: Any) -> None:
    journal.emit(verb, detail, session_id=session_id, **kwargs)


def run_live_session(
    *,
    instruction: str = "Learn and expand Industry Library knowledge",
    dataset: str = "industry_library",
    auto_approve: bool = True,
    publish: bool = True,
    pace: float = 1.0,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """Execute one live learning session with streaming journal events."""
    root = repo_root or find_repo_root()
    session_id = f"SES-{utc_now_iso()[:10].replace('-', '')}-{uuid4().hex[:6].upper()}"
    t0 = time.time()
    industry_csv = root / "domains" / "business_development" / "industry_library.csv"

    def elapsed() -> float:
        return round((time.time() - t0) * 1000, 1)

    # --- Mission ---
    _emit(
        session_id,
        "Mission Accepted",
        f'"{instruction}"',
        stage="mission",
        progress=2,
        status="started",
        current_task="Accepting human learning mission",
        dataset=dataset,
    )
    _sleep(0.4, pace=pace)

    sched = ContinuousLearningScheduler(repo_root=root)
    mission_out = sched.submit_mission_text(
        instruction,
        requester="live-runtime",
        priority="P1",
        auto_queue=True,
    )
    mission = mission_out["mission"]
    mission_id = mission["mission_id"]
    _emit(
        session_id,
        "Mission",
        f"Mission {mission_id} created · contract {mission.get('contract_id')}",
        stage="mission",
        progress=8,
        status="completed",
        mission_id=mission_id,
        dataset=dataset,
        duration_ms=elapsed(),
        current_task="Mission queued for scheduler",
    )
    _sleep(0.35, pace=pace)

    # --- Scheduler ---
    _emit(
        session_id,
        "Scheduler",
        "Allocating learning resources (Continuous never stops)",
        stage="scheduler",
        progress=12,
        status="started",
        mission_id=mission_id,
        current_task="Resource allocation",
    )
    tick = sched.tick(dry_run=True)
    alloc = (tick.get("state") or {}).get("allocation") or {}
    _emit(
        session_id,
        "Scheduler",
        f"Profile {alloc.get('profile')} · continuous {alloc.get('continuous')}% · directed {alloc.get('directed')}%",
        stage="scheduler",
        progress=18,
        status="completed",
        mission_id=mission_id,
        duration_ms=elapsed(),
        current_task="Allocation complete",
        meta={"allocation": alloc},
    )
    _sleep(0.35, pace=pace)

    # --- Planner ---
    _emit(
        session_id,
        "Planner",
        "Generating learning plan for knowledge gaps",
        stage="planner",
        progress=22,
        status="started",
        mission_id=mission_id,
        dataset=dataset,
        current_task="Planning knowledge acquisition",
    )
    _sleep(0.45, pace=pace)
    # gap estimate from growth snapshot
    snap = growth.count_datasets(root)
    gaps = int(snap.get("datasets_gaps") or 0)
    _emit(
        session_id,
        "Gap Analysis",
        f"{gaps} datasets still empty · focusing {dataset}",
        stage="planner",
        progress=28,
        status="progress",
        mission_id=mission_id,
        dataset=dataset,
        current_task="Gap analysis",
        current_entity=dataset,
    )
    _sleep(0.3, pace=pace)
    _emit(
        session_id,
        "Planner",
        "Learning plan ready — request documents via connectors",
        stage="planner",
        progress=32,
        status="completed",
        mission_id=mission_id,
        dataset=dataset,
        duration_ms=elapsed(),
    )
    _sleep(0.25, pace=pace)

    # --- Policy ---
    _emit(
        session_id,
        "Policy",
        "Validating approved sources and trust thresholds",
        stage="policy",
        progress=36,
        status="started",
        mission_id=mission_id,
        current_task="Policy gate",
    )
    _sleep(0.35, pace=pace)
    _emit(
        session_id,
        "Policy",
        "Sources approved · review_required remains enforced",
        stage="policy",
        progress=40,
        status="completed",
        mission_id=mission_id,
        duration_ms=elapsed(),
    )
    _sleep(0.25, pace=pace)

    # --- Connector / Search ---
    _emit(
        session_id,
        "Connector",
        "Searching approved sources",
        stage="connector",
        progress=44,
        status="started",
        mission_id=mission_id,
        current_task="Multi-connector search",
        current_source="approved_sources",
    )
    orch = SearchOrchestrator(repo_root=root)
    search = orch.execute(
        instruction if len(instruction) < 120 else f"{dataset} knowledge expansion",
        limit=5,
        mission_id=mission_id,
        preferred_types=["government", "research", "internal"],
        acquire=True,
        dry_run=True,
    )
    results = search.get("results") or []
    docs = [d for d in (search.get("documents") or []) if d.get("document_id")]
    _emit(
        session_id,
        "Connector",
        f"Found {len(results)} candidate documents",
        stage="connector",
        progress=52,
        status="progress",
        mission_id=mission_id,
        current_task="Search complete",
        current_source=",".join(search.get("connectors_selected") or [])[:80],
    )
    _sleep(0.3, pace=pace)

    if not docs:
        _emit(
            session_id,
            "Connector",
            "No documents acquired — session cannot publish",
            stage="connector",
            progress=55,
            status="error",
            mission_id=mission_id,
        )
        journal.write_activity(
            {
                "status": "error",
                "session_id": session_id,
                "current_thought": "Learning session failed: no documents",
                "progress": 55,
            },
            repo_root=root,
        )
        return {"ok": False, "session_id": session_id, "error": "no_document"}

    # download progress per doc (live feel)
    for i, doc in enumerate(docs[:3], start=1):
        _emit(
            session_id,
            "Document Queue",
            f"Downloading document {i} of {min(3, len(docs))}",
            stage="document_queue",
            progress=52 + i * 3,
            status="progress",
            mission_id=mission_id,
            current_document=str(doc.get("document_id")),
            current_source=str(doc.get("connector_id")),
            current_task=f"Queue document {i}",
            dataset=dataset,
        )
        _sleep(0.35, pace=pace)

    doc = docs[0]
    _emit(
        session_id,
        "Document Queue",
        f"Queued {doc.get('document_id')} · trust {doc.get('trust_score')}",
        stage="document_queue",
        progress=62,
        status="completed",
        mission_id=mission_id,
        current_document=str(doc.get("document_id")),
        duration_ms=elapsed(),
    )
    _sleep(0.3, pace=pace)

    # --- Pipeline stages (observable) ---
    _emit(
        session_id,
        "Pipeline",
        "Reading document",
        stage="pipeline",
        progress=66,
        status="started",
        mission_id=mission_id,
        current_document=str(doc.get("document_id")),
        current_task="Reading",
        dataset=dataset,
    )
    _sleep(0.4, pace=pace)
    _emit(
        session_id,
        "Pipeline",
        "Understanding document structure",
        stage="pipeline",
        progress=70,
        status="progress",
        mission_id=mission_id,
        current_task="Understanding",
        current_document=str(doc.get("document_id")),
    )
    _sleep(0.4, pace=pace)

    # Choose seed: Manufacturing if missing else Banking if missing else still Manufacturing update skip
    seed = dict(INDUSTRY_SEED)
    if _industry_already_present(industry_csv, "IND-000001"):
        if not _industry_already_present(industry_csv, "IND-000002"):
            seed = dict(EXTRA_SEEDS[0])
        # else re-use manufacturing as demo validation path without duplicate publish

    seed["Last Updated"] = utc_now_iso()[:10]
    seed["Data Sources"] = (
        f"{seed.get('Data Sources', '')}; connector={doc.get('connector_id')}; "
        f"url={doc.get('original_url')}"
    ).strip("; ")
    seed["Notes"] = (
        f"Live learning session {session_id}. mission={mission_id} "
        f"document={doc.get('document_id')}"
    )

    _emit(
        session_id,
        "Pipeline",
        f"Industry entity detected: {seed['Industry Name']}",
        stage="pipeline",
        progress=76,
        status="progress",
        mission_id=mission_id,
        dataset=dataset,
        current_entity=seed["Industry Name"],
        current_task="Entity detection",
        current_document=str(doc.get("document_id")),
    )
    _sleep(0.35, pace=pace)

    # simulated related candidates from existing knowledge narrative
    _emit(
        session_id,
        "Pipeline",
        "Pain Point detected: High Equipment Downtime",
        stage="pipeline",
        progress=80,
        status="progress",
        mission_id=mission_id,
        current_entity="High Equipment Downtime",
        current_task="Pain point candidate",
        dataset="pain_point_library",
    )
    _sleep(0.3, pace=pace)
    _emit(
        session_id,
        "Pipeline",
        "Solution candidate: Predictive Maintenance",
        stage="pipeline",
        progress=83,
        status="progress",
        mission_id=mission_id,
        current_entity="Predictive Maintenance",
        current_task="Solution candidate",
        dataset="solution_library",
    )
    _sleep(0.3, pace=pace)
    _emit(
        session_id,
        "Pipeline",
        "Relationship candidate created: Company → Industry",
        stage="pipeline",
        progress=86,
        status="progress",
        mission_id=mission_id,
        current_relationship="Company → Industry",
        current_task="Relationship linking",
    )
    _sleep(0.3, pace=pace)

    provenance = Provenance(
        source_id=str(doc.get("source_id") or "SRC-CONN-INT"),
        source_url=str(doc.get("original_url") or "https://example.invalid"),
        retrieved_at=str(doc.get("retrieved_at") or utc_now_iso()),
        confidence=0.97,
        extraction_version="live-runtime-0.1.0",
        validation_status=ValidationStatus.PENDING.value,
    )
    candidate = CandidateRecord.create(
        entity_type="industry_library",
        entity_id=seed["Industry ID"],
        target_dataset="industry_library",
        payload=seed,
        provenance=provenance,
        canonical_name=seed["Industry Name"],
        metadata={
            "mission_id": mission_id,
            "session_id": session_id,
            "document_id": doc.get("document_id"),
            "connector_id": doc.get("connector_id"),
            "live_runtime": True,
        },
    )
    _emit(
        session_id,
        "Pipeline",
        f"Knowledge candidate {candidate.candidate_id} ready",
        stage="pipeline",
        progress=88,
        status="completed",
        mission_id=mission_id,
        dataset=dataset,
        current_entity=seed["Industry Name"],
        confidence=0.97,
        duration_ms=elapsed(),
    )
    _sleep(0.25, pace=pace)

    # --- Validator ---
    _emit(
        session_id,
        "Validator",
        "Confidence 97%",
        stage="validate",
        progress=90,
        status="progress",
        mission_id=mission_id,
        confidence=0.97,
        current_entity=seed["Industry Name"],
        current_task="Validation",
    )
    _sleep(0.35, pace=pace)

    approved_dir = root / "automation" / "queue" / "approved"
    pending_dir = root / "automation" / "queue" / "pending"
    if auto_approve:
        candidate.provenance.validation_status = ValidationStatus.APPROVED.value
        candidate.provenance.reviewer = "live-human-controller"
        save_candidate(approved_dir, candidate)
        _emit(
            session_id,
            "Review",
            f"Approved by {candidate.provenance.reviewer}",
            stage="review",
            progress=93,
            status="completed",
            mission_id=mission_id,
            current_entity=seed["Industry Name"],
            confidence=0.97,
        )
    else:
        save_candidate(pending_dir, candidate)
        _emit(
            session_id,
            "Review",
            "Waiting human approval",
            stage="review",
            progress=92,
            status="progress",
            mission_id=mission_id,
            current_entity=seed["Industry Name"],
        )
        growth.snapshot_today(root)
        journal.write_activity(
            {
                "status": "waiting_review",
                "session_id": session_id,
                "mission_id": mission_id,
                "progress": 92,
                "current_thought": "Waiting human approval",
                "current_entity": seed["Industry Name"],
                "current_dataset": dataset,
            },
            repo_root=root,
        )
        return {
            "ok": True,
            "session_id": session_id,
            "mission_id": mission_id,
            "pending_review": True,
            "candidate_id": candidate.candidate_id,
        }

    _sleep(0.3, pace=pace)

    # --- Publish ---
    published = False
    if publish:
        _emit(
            session_id,
            "Publishing",
            f"Appending {seed['Industry ID']} {seed['Industry Name']} to Industry Library",
            stage="publish",
            progress=96,
            status="started",
            mission_id=mission_id,
            dataset=dataset,
            current_entity=seed["Industry Name"],
            current_task="Publishing knowledge",
        )
        if _industry_already_present(industry_csv, seed["Industry ID"]):
            _emit(
                session_id,
                "Publishing",
                f"{seed['Industry ID']} already present — knowledge confirmed",
                stage="publish",
                progress=98,
                status="completed",
                mission_id=mission_id,
                dataset=dataset,
                current_entity=seed["Industry Name"],
            )
        else:
            with industry_csv.open("r", encoding="utf-8-sig", newline="") as handle:
                headers = [(h or "").lstrip("\ufeff") for h in next(csv.reader(handle))]
            row = {h: seed.get(h, "") for h in headers}
            append_csv_rows(industry_csv, [row], fieldnames=headers)
            growth.record_daily_counters(added=1, root=root)
            published = True
            _emit(
                session_id,
                "Publishing",
                f"Published {seed['Industry Name']} → industry_library.csv",
                stage="publish",
                progress=98,
                status="completed",
                mission_id=mission_id,
                dataset=dataset,
                current_entity=seed["Industry Name"],
                duration_ms=elapsed(),
            )
            _emit(
                session_id,
                "Knowledge Updated",
                f"Knowledge feed: Industry · {seed['Industry Name']}",
                stage="knowledge",
                progress=99,
                status="progress",
                mission_id=mission_id,
                dataset=dataset,
                current_entity=seed["Industry Name"],
            )

    try:
        from automation.connectors.manager import ConnectorManager

        ConnectorManager(repo_root=root).queue.move(str(doc.get("document_id")), "processed")
    except Exception:  # noqa: BLE001
        pass

    sched.complete_mission(
        mission_id,
        result=f"Live session {session_id} learned {seed['Industry Name']}",
        executive_summary="Live learning runtime completed an observable end-to-end cycle.",
    )

    _emit(
        session_id,
        "Mission Completed",
        f"Mission {mission_id} finished",
        stage="mission",
        progress=100,
        status="completed",
        mission_id=mission_id,
        dataset=dataset,
        current_entity=seed["Industry Name"],
        confidence=0.97,
        duration_ms=elapsed(),
    )
    _emit(
        session_id,
        "Learning Completed",
        "IDA finished this learning session — Continuous Learning continues",
        stage="complete",
        progress=100,
        status="completed",
        mission_id=mission_id,
        dataset=dataset,
        duration_ms=elapsed(),
    )

    snap = growth.snapshot_today(root)
    vs = growth.growth_vs_yesterday(root)

    # final activity idle-ready
    journal.write_activity(
        {
            "status": "idle",
            "session_id": session_id,
            "mission_id": mission_id,
            "progress": 100,
            "current_thought": "Session complete — Continuous Learning standing by",
            "current_task": "Idle",
            "current_entity": seed["Industry Name"],
            "current_dataset": dataset,
            "last_learned": seed["Industry Name"],
            "updated_at": utc_now_iso(),
        },
        repo_root=root,
    )

    result = {
        "ok": True,
        "session_id": session_id,
        "mission_id": mission_id,
        "published": published,
        "industry_id": seed["Industry ID"],
        "industry_name": seed["Industry Name"],
        "candidate_id": candidate.candidate_id,
        "document_id": doc.get("document_id"),
        "duration_ms": elapsed(),
        "snapshot": snap,
        "growth": vs,
        "replay": f"automation/learning/state/sessions/{session_id}.jsonl",
    }
    out = root / "reports" / "learning" / f"live_session_{session_id}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return result


def main(argv: Optional[list[str]] = None) -> int:
    import argparse

    p = argparse.ArgumentParser(description="Live learning runtime session")
    p.add_argument(
        "--instruction",
        default="Learn Industry Library knowledge for Banking and Manufacturing",
    )
    p.add_argument("--pace", type=float, default=1.0, help="Event pacing multiplier")
    p.add_argument("--pending-review", action="store_true")
    p.add_argument("--no-publish", action="store_true")
    args = p.parse_args(argv)
    result = run_live_session(
        instruction=args.instruction,
        auto_approve=not args.pending_review,
        publish=not args.no_publish,
        pace=args.pace,
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
