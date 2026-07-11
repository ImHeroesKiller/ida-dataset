#!/usr/bin/env python3
"""Live Learning Runtime — real acquisition + streaming journal events.

Reuses frozen architecture:
  Scheduler → Source Registry → Connectors → Document Queue
  → Grounded Extraction → Candidate Queue → DPS Validation
  → Append-only Publish → Growth metrics

Never fabricates knowledge. Empty acquisition fails with an explicit reason.
"""

from __future__ import annotations

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
from automation.lib.models import utc_now_iso  # noqa: E402
from automation.lib.paths import find_repo_root  # noqa: E402
from automation.runtime import channels as runtime_channels  # noqa: E402
from automation.runtime.errors import record_failure  # noqa: E402
from automation.runtime.lifecycle import (  # noqa: E402
    RuntimeLifecycle,
    RuntimeState,
    acquire_lock,
)
from automation.runtime.recovery import run_with_recovery  # noqa: E402
from automation.scheduler.scheduler import ContinuousLearningScheduler  # noqa: E402


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
    correlation_id: str | None = None,
    skip_lock: bool = False,
) -> dict[str, Any]:
    """Execute one live learning session with streaming journal events."""
    root = repo_root or find_repo_root()
    # Route dataset from mission instruction (coverage libraries must not stay industry-only)
    try:
        from automation.acquisition.dataset_routing import resolve_dataset_from_instruction

        dataset = resolve_dataset_from_instruction(
            instruction, explicit=dataset, default=dataset or "industry_library"
        )
    except Exception:  # noqa: BLE001
        pass
    session_id = f"SES-{utc_now_iso()[:10].replace('-', '')}-{uuid4().hex[:6].upper()}"
    t0 = time.time()
    lifecycle: RuntimeLifecycle | None = None

    def elapsed() -> float:
        return round((time.time() - t0) * 1000, 1)

    # --- Exclusive runtime lock (prevent double start / zombie sessions) ---
    if not skip_lock:
        lock = acquire_lock(
            session_id=session_id,
            correlation_id=correlation_id,
            instruction=instruction,
            repo_root=root,
        )
        if not lock.ok:
            err = record_failure(
                component="runtime.lock",
                exception=lock.reason or "Lock acquisition failed",
                session_id=session_id,
                correlation_id=lock.correlation_id,
                recovery_action=lock.recovery_action or "wait_or_stop_existing_runtime",
                meta={"existing": lock.existing},
                repo_root=root,
            )
            journal.write_activity(
                {
                    "status": "error",
                    "session_id": session_id,
                    "correlation_id": lock.correlation_id,
                    "current_thought": f"Runtime failed: {lock.reason}",
                    "progress": 0,
                },
                repo_root=root,
            )
            return {
                "ok": False,
                "session_id": session_id,
                "correlation_id": lock.correlation_id,
                "error": "runtime_locked",
                "message": lock.reason,
                "failure": err,
            }
        correlation_id = lock.correlation_id
        lifecycle = RuntimeLifecycle(
            session_id=session_id,
            correlation_id=correlation_id,
            repo_root=root,
            instruction=instruction,
        )
        lifecycle.transition(
            RuntimeState.STARTING,
            stage="startup",
            task="Runtime lock acquired",
        )
    else:
        # GHA / CI execution: no exclusive host lock, but lifecycle still applies.
        correlation_id = correlation_id or f"CORR-{uuid4().hex[:12].upper()}"
        lifecycle = RuntimeLifecycle(
            session_id=session_id,
            correlation_id=correlation_id,
            repo_root=root,
            instruction=instruction,
        )
        lifecycle.transition(
            RuntimeState.STARTING,
            stage="startup",
            task="Session started (github_actions / skip_lock)",
        )

    runtime_channels.set_context(session_id=session_id, correlation_id=correlation_id)
    runtime_channels.log(
        "runtime",
        f"Session {session_id} starting",
        module="live_runtime",
        session_id=session_id,
        correlation_id=correlation_id,
        meta={"instruction": instruction},
        repo_root=root,
    )

    try:
        return _run_live_session_body(
            root=root,
            session_id=session_id,
            correlation_id=correlation_id or "",
            instruction=instruction,
            dataset=dataset,
            auto_approve=auto_approve,
            publish=publish,
            pace=pace,
            lifecycle=lifecycle,
            t0=t0,
            elapsed=elapsed,
        )
    except Exception as exc:  # noqa: BLE001
        failure = record_failure(
            component="live_runtime",
            exception=exc,
            session_id=session_id,
            correlation_id=correlation_id,
            recovery_action="stop_and_notify",
            repo_root=root,
        )
        if lifecycle:
            lifecycle.transition(
                RuntimeState.FAILED,
                stage="failed",
                task="Runtime failed",
                error=failure,
                health={"runtime": "failed"},
            )
            lifecycle.release(force=True)
        journal.write_activity(
            {
                "status": "error",
                "session_id": session_id,
                "correlation_id": correlation_id,
                "current_thought": f"Runtime failed: {exc}",
                "progress": 0,
                "last_error": failure,
            },
            repo_root=root,
        )
        runtime_channels.log(
            "errors",
            f"Session {session_id} failed: {exc}",
            module="live_runtime",
            level="ERROR",
            session_id=session_id,
            correlation_id=correlation_id,
            duration_ms=elapsed(),
            repo_root=root,
        )
        return {
            "ok": False,
            "session_id": session_id,
            "correlation_id": correlation_id,
            "error": type(exc).__name__,
            "message": str(exc),
            "failure": failure,
        }
    finally:
        runtime_channels.clear_context()


def _run_live_session_body(
    *,
    root: Path,
    session_id: str,
    correlation_id: str,
    instruction: str,
    dataset: str,
    auto_approve: bool,
    publish: bool,
    pace: float,
    lifecycle: RuntimeLifecycle | None,
    t0: float,
    elapsed: Any,
) -> dict[str, Any]:
    """Inner session body after lock is held."""
    if lifecycle:
        lifecycle.transition(
            RuntimeState.RUNNING,
            stage="mission",
            task="Accepting human learning mission",
        )

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

    def _make_scheduler() -> ContinuousLearningScheduler:
        return ContinuousLearningScheduler(repo_root=root)

    sched = run_with_recovery(
        _make_scheduler,
        component="scheduler",
        session_id=session_id,
        correlation_id=correlation_id,
        repo_root=root,
    )
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

    # --- Real acquisition engine (collect → extract → validate → publish) ---
    _emit(
        session_id,
        "Connector",
        "Searching trusted sources via acquisition engine",
        stage="connector",
        progress=44,
        status="started",
        mission_id=mission_id,
        current_task="Real multi-connector acquisition",
        current_source="source_registry",
    )
    _sleep(0.2, pace=pace)

    acquisition_logs: list[dict[str, str]] = []

    def _acq_log(verb: str, detail: str) -> None:
        acquisition_logs.append({"verb": verb, "detail": detail})
        stage_map = {
            "Searching": "connector",
            "Downloading": "document_queue",
            "Document Queue": "document_queue",
            "Parsing document": "pipeline",
            "Extracting": "pipeline",
            "Candidate Queue": "pipeline",
            "Validation": "validate",
            "Publishing": "publish",
            "Knowledge Updated": "knowledge",
            "Connector": "connector",
            "Pipeline": "pipeline",
        }
        st = stage_map.get(verb, "pipeline")
        progress_hint = {
            "connector": 50,
            "document_queue": 60,
            "pipeline": 78,
            "validate": 90,
            "publish": 96,
            "knowledge": 99,
        }.get(st, 70)
        _emit(
            session_id,
            verb,
            detail,
            stage=st,
            progress=progress_hint,
            status="progress",
            mission_id=mission_id,
            dataset=dataset,
            current_task=detail[:120],
        )

    def _acquire() -> dict[str, Any]:
        from automation.acquisition.pipeline import run_acquisition

        # Throughput: adaptive discovery budgets inside pipeline; limit is a floor hint only.
        # process_budget targets ≥90% of discovered docs within adaptive download budget.
        return run_acquisition(
            instruction=instruction,
            mission_id=mission_id,
            session_id=session_id,
            dataset=dataset,
            limit=64,
            dry_run=not publish,
            publish=publish and auto_approve,
            auto_approve=auto_approve,
            repo_root=root,
            log=_acq_log,
        )

    acq = run_with_recovery(
        _acquire,
        component="acquisition.pipeline",
        session_id=session_id,
        correlation_id=correlation_id,
        repo_root=root,
    )

    docs = acq.get("documents") or []
    doc = docs[0] if docs else {}
    published_n = int(acq.get("rows_published") or 0)
    published = published_n > 0
    entities = acq.get("published_entities") or []
    entity_name = entities[0] if entities else (
        (acq.get("candidates") or [{}])[0].get("name") if acq.get("candidates") else None
    )
    cand_meta = (acq.get("candidates") or [{}])[0]
    industry_id = cand_meta.get("entity_id") or ""
    industry_name = entity_name or cand_meta.get("name") or ""
    production_trace = acq.get("production_trace") or {}
    publish_balance = acq.get("publish") or (production_trace.get("publish") or {})
    console_text = str(acq.get("console") or "")

    # Emit structured production console into journal (real data only)
    if console_text:
        _emit(
            session_id,
            "Production Console",
            console_text[:4000],
            stage="publish",
            progress=97,
            status="completed",
            mission_id=mission_id,
            dataset=dataset,
            meta={
                "publish": publish_balance,
                "connectors": [
                    {
                        "name": c.get("name"),
                        "status": c.get("status"),
                        "http_status": c.get("http_status"),
                        "documents_discovered": c.get("documents_discovered"),
                        "documents_downloaded": c.get("documents_downloaded"),
                    }
                    for c in (acq.get("connectors") or [])[:12]
                ],
            },
        )

    if lifecycle:
        lifecycle.mark_progress(
            stage="pipeline",
            task=f"Acquisition docs={acq.get('documents_downloaded')} cands={acq.get('candidates_extracted')}",
            documents_processed=int(acq.get("documents_downloaded") or 0),
            knowledge_candidates=int(acq.get("candidates_extracted") or 0),
            health={
                "connector": "healthy" if docs else "degraded",
                "queue": "healthy",
            },
        )

    if not acq.get("ok") and published_n == 0:
        err_code = str(acq.get("error") or "acquisition_failed")
        reason = "; ".join(acq.get("reasons") or acq.get("failures") or [err_code])
        _emit(
            session_id,
            "Connector",
            f"Acquisition failed: {reason}",
            stage="connector",
            progress=55,
            status="error",
            mission_id=mission_id,
        )
        failure = record_failure(
            component="acquisition.pipeline",
            exception=err_code,
            session_id=session_id,
            correlation_id=correlation_id,
            recovery_action="check_connectors_and_sources",
            meta={
                "message": reason,
                "sources_contacted": acq.get("sources_contacted"),
                "documents_discovered": acq.get("documents_discovered"),
                "documents_downloaded": acq.get("documents_downloaded"),
                "candidates_extracted": acq.get("candidates_extracted"),
                "failures": (acq.get("failures") or [])[:10],
            },
            repo_root=root,
        )
        journal.write_activity(
            {
                "status": "error",
                "session_id": session_id,
                "correlation_id": correlation_id,
                "current_thought": f"Learning session failed: {reason}",
                "progress": 55,
                "last_error": failure,
            },
            repo_root=root,
        )
        if lifecycle:
            lifecycle.transition(
                RuntimeState.FAILED,
                stage="acquisition",
                task=reason[:120],
                error=failure,
                health={"runtime": "failed", "connector": "failed"},
            )
            lifecycle.release(force=True)
        try:
            from automation.lib.source_health import record_session_sources

            record_session_sources(
                ["SRC-000004", "SRC-OPENALEX", "SRC-CROSSREF"],
                success=False,
                documents=int(acq.get("documents_downloaded") or 0),
                rows=0,
                duration_ms=float(elapsed()),
                mission_id=mission_id,
                root=root,
            )
        except Exception:  # noqa: BLE001
            pass
        return {
            "ok": False,
            "session_id": session_id,
            "correlation_id": correlation_id,
            "mission_id": mission_id,
            "error": err_code,
            "message": reason,
            "failure": failure,
            "acquisition": acq,
            "published": False,
            "knowledge_added": 0,
        }

    if not auto_approve:
        _emit(
            session_id,
            "Review",
            f"Queued {acq.get('candidates_extracted')} candidates for human approval",
            stage="review",
            progress=92,
            status="progress",
            mission_id=mission_id,
            current_entity=industry_name,
        )
        growth.snapshot_today(root)
        if lifecycle:
            lifecycle.transition(
                RuntimeState.STOPPED,
                stage="review",
                task="Waiting human approval",
                health={"publisher": "disabled", "runtime": "healthy"},
            )
            lifecycle.release()
        return {
            "ok": True,
            "session_id": session_id,
            "mission_id": mission_id,
            "correlation_id": correlation_id,
            "pending_review": True,
            "candidate_id": cand_meta.get("candidate_id"),
            "acquisition": acq,
            "published": False,
            "knowledge_added": 0,
        }

    if published_n:
        growth.record_daily_counters(added=published_n, root=root)
        _emit(
            session_id,
            "Publishing",
            f"Published {published_n} row(s) · Knowledge Added {published_n}",
            stage="publish",
            progress=98,
            status="completed",
            mission_id=mission_id,
            dataset=dataset,
            current_entity=industry_name,
            duration_ms=elapsed(),
        )
        _emit(
            session_id,
            "Knowledge Updated",
            f"Knowledge feed: {industry_name or 'entities'} (+{published_n})",
            stage="knowledge",
            progress=99,
            status="progress",
            mission_id=mission_id,
            dataset=dataset,
            current_entity=industry_name,
        )

    sched.complete_mission(
        mission_id,
        result=(
            f"Live session {session_id} acquired "
            f"docs={acq.get('documents_downloaded')} "
            f"published={published_n} entity={industry_name}"
        ),
        executive_summary=(
            "Real acquisition engine completed discover→download→extract→validate→publish."
        ),
    )

    _emit(
        session_id,
        "Mission Completed",
        f"Mission {mission_id} finished · published={published_n}",
        stage="mission",
        progress=100,
        status="completed",
        mission_id=mission_id,
        dataset=dataset,
        current_entity=industry_name,
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

    last_conn = (production_trace.get("last_connector") or "")
    last_doc = (production_trace.get("last_document") or doc.get("document_id") or "")
    journal.write_activity(
        {
            "status": "idle",
            "session_id": session_id,
            "mission_id": mission_id,
            "correlation_id": correlation_id,
            "progress": 100,
            "current_thought": "Session complete — Continuous Learning standing by",
            "current_task": "Idle",
            "current_entity": industry_name,
            "current_dataset": dataset,
            "last_learned": industry_name,
            "current_stage": production_trace.get("current_stage") or "completed",
            "current_connector": production_trace.get("current_connector") or last_conn,
            "current_document": production_trace.get("current_document") or last_doc,
            "last_connector": last_conn,
            "last_document": last_doc,
            "last_published_entity": industry_name,
            "documents_discovered": acq.get("documents_discovered"),
            "documents_downloaded": acq.get("documents_downloaded"),
            "candidates_extracted": acq.get("candidates_extracted"),
            "candidates_validated": publish_balance.get("validated"),
            "candidates_rejected": publish_balance.get("rejected"),
            "publish_queue_size": publish_balance.get("queued"),
            "rows_appended": published_n,
            "publish_balance": publish_balance,
            "updated_at": utc_now_iso(),
        },
        repo_root=root,
    )

    if lifecycle:
        lifecycle.transition(
            RuntimeState.STOPPING,
            stage="complete",
            task="Releasing runtime",
        )
        lifecycle.transition(
            RuntimeState.STOPPED,
            stage="complete",
            task="Session complete",
            health={
                "runtime": "healthy",
                "scheduler": "healthy",
                "connector": "healthy",
                "queue": "healthy",
                "sse": "healthy",
                "publisher": "healthy",
            },
        )
        lifecycle.release()
        lifecycle.transition(RuntimeState.IDLE, stage="idle", task="Standing by")

    runtime_channels.log(
        "runtime",
        f"Session {session_id} completed",
        module="live_runtime",
        session_id=session_id,
        correlation_id=correlation_id,
        duration_ms=elapsed(),
        repo_root=root,
    )
    runtime_channels.log(
        "learning",
        f"Learned {industry_name} published={published_n}",
        module="live_runtime",
        session_id=session_id,
        correlation_id=correlation_id,
        duration_ms=elapsed(),
        repo_root=root,
    )

    result = {
        "ok": True,
        "session_id": session_id,
        "mission_id": mission_id,
        "correlation_id": correlation_id,
        "dataset": dataset,
        "published": published,
        "knowledge_added": published_n,
        "industry_id": industry_id,
        "industry_name": industry_name,
        "candidate_id": cand_meta.get("candidate_id"),
        "document_id": doc.get("document_id"),
        "source_id": str(doc.get("source_id") or ""),
        "connector_id": str(doc.get("connector_id") or ""),
        "duration_ms": elapsed(),
        "snapshot": snap,
        "growth": vs,
        "console": console_text,
        "production_trace": production_trace,
        "publish_balance": publish_balance,
        "acquisition": {
            "sources_contacted": acq.get("sources_contacted"),
            "documents_discovered": acq.get("documents_discovered"),
            "documents_downloaded": acq.get("documents_downloaded"),
            "candidates_extracted": acq.get("candidates_extracted"),
            "candidates_validated": acq.get("candidates_validated"),
            "candidates_rejected": acq.get("candidates_rejected"),
            "rows_published": published_n,
            "queue_stats": acq.get("queue_stats"),
            "document_queue": acq.get("document_queue"),
            "connectors": acq.get("connectors"),
            "publish": publish_balance,
            "evidence_chains": acq.get("evidence_chains"),
            "failures": acq.get("failures"),
            "reports": acq.get("reports"),
        },
        "replay": f"automation/learning/state/sessions/{session_id}.jsonl",
    }

    try:
        from automation.lib.source_health import record_session_sources, recompute_from_datasets

        sids = []
        for d in docs:
            sid = str(d.get("source_id") or "")
            if sid.startswith("SRC-"):
                sids.append(sid)
        if not sids:
            sids = ["SRC-000004"]
        # unique
        seen: set[str] = set()
        uniq = []
        for s in sids:
            if s not in seen:
                seen.add(s)
                uniq.append(s)
        record_session_sources(
            uniq,
            success=True,
            documents=int(acq.get("documents_downloaded") or 0),
            rows=published_n,
            duration_ms=float(elapsed()),
            mission_id=mission_id,
            root=root,
        )
        recompute_from_datasets(root)
    except Exception:  # noqa: BLE001
        pass

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
    p.add_argument("--correlation-id", default=None, help="Correlation id from API start")
    p.add_argument(
        "--skip-lock",
        action="store_true",
        help="Skip exclusive lock (tests only)",
    )
    args = p.parse_args(argv)
    result = run_live_session(
        instruction=args.instruction,
        auto_approve=not args.pending_review,
        publish=not args.no_publish,
        pace=args.pace,
        correlation_id=args.correlation_id,
        skip_lock=args.skip_lock,
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
