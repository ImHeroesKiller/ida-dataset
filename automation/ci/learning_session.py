#!/usr/bin/env python3
"""Learning Session CI job — executed by GitHub Actions.

Runs one continuous-learning session using the existing architecture:

  Scheduler → Planner → Policy → Connector → Pipeline → Review → Publisher → Telemetry

Execution model only: sessions run in GHA, not inside the dashboard process.
Persists full session records under automation/sessions/YYYY-MM-DD/.

Exit codes: 0 success | 1 failure | 2 config
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Optional

_REPO = Path(__file__).resolve().parents[2]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))

from automation.ci import (  # noqa: E402
    EXIT_CONFIG_ERROR,
    EXIT_SUCCESS,
    EXIT_VALIDATION_ERROR,
)
from automation.ci.common import (  # noqa: E402
    RunContext,
    add_common_args,
    find_repo_root,
    load_environment_config,
    report_header,
    resolve_dry_run,
    resolve_environment,
    stamp,
    write_json_log,
    write_markdown_report,
)
from automation.learning import growth, journal  # noqa: E402
from automation.learning.live_runtime import run_live_session  # noqa: E402
from automation.learning.session_store import (  # noqa: E402
    append_event,
    empty_session,
    finalize_session,
    list_sessions,
    new_session_id,
    save_session,
    session_path,
    sessions_root,
)
from automation.scheduler.scheduler import ContinuousLearningScheduler  # noqa: E402


def _github_meta() -> dict[str, Any]:
    return {
        "run_id": os.environ.get("GITHUB_RUN_ID"),
        "run_number": os.environ.get("GITHUB_RUN_NUMBER"),
        "workflow": os.environ.get("GITHUB_WORKFLOW"),
        "workflow_ref": os.environ.get("GITHUB_WORKFLOW_REF"),
        "actor": os.environ.get("GITHUB_ACTOR"),
        "event_name": os.environ.get("GITHUB_EVENT_NAME"),
        "sha": os.environ.get("GITHUB_SHA"),
        "ref": os.environ.get("GITHUB_REF"),
        "repository": os.environ.get("GITHUB_REPOSITORY"),
        "server_url": os.environ.get("GITHUB_SERVER_URL", "https://github.com"),
    }


def _resolve_trigger(event_name: str | None, explicit: str | None) -> str:
    if explicit:
        return explicit
    if event_name == "schedule":
        return "schedule"
    if event_name == "workflow_dispatch":
        return "manual"
    if event_name == "repository_dispatch":
        return "mission"
    return event_name or "manual"


def run_session(
    *,
    repo_root: Path,
    environment: str,
    dry_run: bool,
    instruction: str,
    mission: str | None,
    trigger: str,
    pace: float,
    auto_approve: bool,
    publish: bool,
    dataset: str | None = None,
) -> dict[str, Any]:
    """Execute one learning session and persist SESSION-*.json."""
    session_id = new_session_id()
    gh = _github_meta()
    session = empty_session(
        session_id=session_id,
        mission=mission or instruction,
        instruction=instruction,
        trigger=trigger,
        dry_run=dry_run,
        environment=environment,
        github=gh,
    )
    session["mission_id"] = None
    save_session(session, repo_root)

    # Mark activity for any local observers (not required on Vercel)
    journal.write_activity(
        {
            "status": "running",
            "session_id": session_id,
            "progress": 1,
            "current_thought": f"GitHub Actions learning session {session_id}",
            "current_task": "Starting learning session",
            "updated_at": session["start_time"],
            "execution_model": "github_actions",
        },
        repo_root=repo_root,
    )

    append_event(
        session,
        "Session",
        f"Learning session {session_id} started via {trigger}",
        stage="session",
        progress=1,
        status="started",
        current_task="Session bootstrap",
    )
    append_event(
        session,
        "Scheduler",
        "Continuous Learning Scheduler tick (GHA execution)",
        stage="scheduler",
        progress=5,
        status="started",
    )
    save_session(session, repo_root)

    planner_output: dict[str, Any] | None = None
    connector_output: dict[str, Any] | None = None
    sched_tick: dict[str, Any] | None = None

    try:
        # Scheduler always exists; tick records continuous allocation.
        sched = ContinuousLearningScheduler(repo_root=repo_root)
        sched_tick = sched.tick(dry_run=True)
        session["telemetry"]["scheduler_tick"] = {
            "ok": True,
            "allocation": (sched_tick.get("state") or {}).get("allocation"),
            "dispatched": sched_tick.get("dispatched"),
        }
        append_event(
            session,
            "Scheduler",
            "Scheduler tick complete — continuous learning allocated",
            stage="scheduler",
            progress=12,
            status="completed",
            meta={"allocation": session["telemetry"]["scheduler_tick"].get("allocation")},
        )
        save_session(session, repo_root)

        # Resolve target dataset from selector / instruction (coverage libraries)
        target_dataset = dataset or "industry_library"
        try:
            from automation.acquisition.dataset_routing import (
                resolve_dataset_from_instruction,
            )

            target_dataset = resolve_dataset_from_instruction(
                instruction, explicit=dataset, default=target_dataset
            )
        except Exception:  # noqa: BLE001
            pass

        # Run the frozen live session body (same engines; GHA execution only).
        # skip_lock: GHA job is the exclusive executor; no dashboard spawn.
        live = run_live_session(
            instruction=instruction,
            dataset=target_dataset,
            auto_approve=auto_approve and not dry_run,
            publish=publish and not dry_run,
            pace=pace,
            repo_root=repo_root,
            correlation_id=f"GHA-{gh.get('run_id') or session_id}",
            skip_lock=True,
        )

        # Merge journal events from live runtime session if present
        live_sid = live.get("session_id")
        if live_sid:
            live_events = journal.load_session(str(live_sid), repo_root=repo_root)
            for ev in live_events:
                # Re-tag with GHA session id for dashboard replay
                tagged = dict(ev)
                tagged["gha_session_id"] = session_id
                tagged["legacy_session_id"] = live_sid
                session["events"].append(tagged)
                session["logs"].append(
                    f"[{tagged.get('ts')}] {tagged.get('verb')}: {tagged.get('detail')}"
                )

        session["mission_id"] = live.get("mission_id")
        session["legacy_session_id"] = live_sid
        session["correlation_id"] = live.get("correlation_id")

        planner_output = {
            "gaps_focus": live.get("industry_name") or instruction,
            "dataset": live.get("dataset") or target_dataset,
            "snapshot": live.get("snapshot"),
        }
        connector_output = {
            "document_id": live.get("document_id"),
            "ok": bool(live.get("ok")),
            "error": live.get("error"),
        }
        acq = live.get("acquisition") or {}
        production_trace = live.get("production_trace") or acq.get("production_trace") or {}
        publish_balance = (
            live.get("publish_balance")
            or acq.get("publish")
            or (production_trace.get("publish") or {})
        )
        knowledge_delta = {
            "added": int(
                live.get("knowledge_added")
                if live.get("knowledge_added") is not None
                else (1 if live.get("published") else 0)
            ),
            "updated": 0,
            "rejected": int(
                publish_balance.get("rejected")
                or acq.get("candidates_rejected")
                or 0
            )
            + (
                1
                if live.get("error")
                in {
                    "no_document",
                    "no_documents_discovered",
                    "no_documents_downloaded",
                    "no_candidates_extracted",
                }
                else 0
            ),
            "industry_id": live.get("industry_id"),
            "industry_name": live.get("industry_name"),
            "candidate_id": live.get("candidate_id"),
            "document_id": live.get("document_id"),
            "connector_id": live.get("connector_id"),
            "source_id": live.get("source_id"),
            "published": bool(live.get("published")),
            "pending_review": bool(live.get("pending_review")),
            "documents_discovered": acq.get("documents_discovered"),
            "documents_downloaded": acq.get("documents_downloaded"),
            "candidates_extracted": acq.get("candidates_extracted")
            or publish_balance.get("extracted"),
            "candidates_validated": acq.get("candidates_validated")
            or publish_balance.get("validated"),
            "candidates_rejected": publish_balance.get("rejected"),
            "publish_queued": publish_balance.get("queued"),
            "publish_published": publish_balance.get("published"),
            "publish_duplicate": publish_balance.get("duplicate"),
            "publish_skipped": publish_balance.get("skipped"),
            "publish_by_dataset": publish_balance.get("by_dataset"),
            "connectors": acq.get("connectors") or production_trace.get("connectors"),
            "evidence_chains": acq.get("evidence_chains")
            or production_trace.get("evidence_chains"),
            "document_queue": acq.get("document_queue")
            or production_trace.get("document_queue"),
            "last_connector": production_trace.get("last_connector"),
            "last_document": production_trace.get("last_document"),
            "last_published_entity": production_trace.get("last_published_entity")
            or live.get("industry_name"),
        }
        publish_summary = {
            "published": bool(live.get("published")),
            "dry_run": dry_run,
            "dataset": live.get("dataset") or target_dataset,
            "entity": live.get("industry_name"),
            "rows_published": int(publish_balance.get("published") or knowledge_delta["added"]),
            "extracted": publish_balance.get("extracted"),
            "validated": publish_balance.get("validated"),
            "rejected": publish_balance.get("rejected"),
            "queued": publish_balance.get("queued"),
            "duplicate": publish_balance.get("duplicate"),
            "skipped": publish_balance.get("skipped"),
            "by_dataset": publish_balance.get("by_dataset"),
            "balance_ok": publish_balance.get("balance_ok"),
            "blocked_reason": None
            if live.get("ok")
            else (live.get("message") or live.get("error")),
        }

        session["planner_output"] = planner_output
        session["connector_output"] = {
            **connector_output,
            "connectors": knowledge_delta.get("connectors"),
            "documents_discovered": knowledge_delta.get("documents_discovered"),
            "documents_downloaded": knowledge_delta.get("documents_downloaded"),
        }
        session["knowledge_delta"] = knowledge_delta
        session["publish_summary"] = publish_summary
        session["production_trace"] = production_trace
        session["console"] = live.get("console") or ""
        session["knowledge_added"] = int(knowledge_delta["added"])
        session["knowledge_updated"] = int(knowledge_delta["updated"])
        session["knowledge_rejected"] = int(knowledge_delta["rejected"])
        session["telemetry"]["live_result"] = {
            k: live.get(k)
            for k in (
                "ok",
                "session_id",
                "mission_id",
                "published",
                "duration_ms",
                "error",
                "message",
                "knowledge_added",
            )
        }
        session["telemetry"]["growth"] = live.get("growth")
        session["telemetry"]["snapshot"] = live.get("snapshot")
        session["telemetry"]["publish_balance"] = publish_balance
        session["telemetry"]["production_summary"] = (
            production_trace.get("summary") if isinstance(production_trace, dict) else {}
        )

        # EPIC-1: ensure source health metrics recompute after every session
        try:
            from automation.lib.source_health import recompute_from_datasets

            recompute_from_datasets(repo_root)
        except Exception:  # noqa: BLE001
            pass

        if live.get("ok"):
            pb = publish_balance or {}
            summary = (
                f"Session completed · published={session['knowledge_added']} "
                f"extracted={pb.get('extracted', session.get('knowledge_delta', {}).get('candidates_extracted'))} "
                f"validated={pb.get('validated')} rejected={pb.get('rejected')} "
                f"docs={acq.get('documents_downloaded')} "
                f"entity={live.get('industry_name') or '—'}"
            )
            if dry_run:
                summary += " · dry_run"
            finalize_session(
                session,
                status="completed",
                summary=summary,
                repo_root=repo_root,
            )
        else:
            err = {
                "error": live.get("error") or "session_failed",
                "message": live.get("message") or "Learning session failed",
                "failure": live.get("failure"),
            }
            finalize_session(
                session,
                status="failed",
                summary=err["message"],
                errors=[err],
                repo_root=repo_root,
            )

    except Exception as exc:  # noqa: BLE001
        finalize_session(
            session,
            status="failed",
            summary=str(exc),
            errors=[{"error": type(exc).__name__, "message": str(exc)}],
            repo_root=repo_root,
        )

    # Growth snapshot for dashboard KPIs
    try:
        growth.snapshot_today(repo_root)
    except Exception:  # noqa: BLE001
        pass

    # Progressive publish ONLY when the in-session acquisition path did not already
    # publish and the publish queue still has candidates (prevents double-publish /
    # empty-queue noise). One publish path per session.
    publish_q = repo_root / "automation" / "queue" / "publish"
    queue_pending = (
        list(publish_q.glob("*.json")) if publish_q.exists() else []
    )
    already_published = int(session.get("knowledge_added") or 0) > 0 or bool(
        (session.get("publish_summary") or {}).get("published")
    )
    if (
        not dry_run
        and session.get("status") == "completed"
        and queue_pending
        and not already_published
    ):
        try:
            import subprocess

            subprocess.run(
                [sys.executable, "automation/ci/progressive_publish.py"],
                cwd=str(repo_root),
                check=False,
                timeout=600,
                env={**os.environ, "PYTHONUNBUFFERED": "1"},
            )
        except Exception:  # noqa: BLE001
            pass
    elif not dry_run and session.get("status") == "completed":
        # Explicit single-publish telemetry (no second publisher)
        session.setdefault("telemetry", {})["publish_once"] = {
            "already_published_in_session": already_published,
            "publish_queue_remaining": len(queue_pending),
            "progressive_publish_skipped": True,
        }

    journal.write_activity(
        {
            "status": "idle" if session.get("status") == "completed" else "error",
            "session_id": session_id,
            "mission_id": session.get("mission_id"),
            "progress": 100 if session.get("status") == "completed" else 0,
            "current_thought": session.get("summary"),
            "current_task": "Idle" if session.get("status") == "completed" else "Failed",
            "last_learned": (session.get("knowledge_delta") or {}).get("industry_name"),
            "updated_at": session.get("end_time"),
            "execution_model": "github_actions",
            "last_error": (session.get("errors") or [None])[0],
        },
        repo_root=repo_root,
    )

    final_path = session_path(session_id, repo_root)
    return {
        "ok": session.get("status") == "completed",
        "session_id": session_id,
        "status": session.get("status"),
        "session": session,
        "session_file": str(final_path.relative_to(repo_root)),
    }


def build_report(ctx: RunContext, result: dict[str, Any]) -> str:
    session = result.get("session") or {}
    lines = report_header(ctx, "Learning Session Report")
    lines += [
        f"- **Session ID:** `{session.get('session_id')}`",
        f"- **Status:** `{session.get('status')}`",
        f"- **Trigger:** `{session.get('trigger')}`",
        f"- **Mission:** {session.get('mission')}",
        f"- **Duration (s):** {session.get('duration_seconds')}",
        f"- **Knowledge added:** {session.get('knowledge_added')}",
        f"- **Knowledge updated:** {session.get('knowledge_updated')}",
        f"- **Knowledge rejected:** {session.get('knowledge_rejected')}",
        "",
        "## Summary",
        "",
        str(session.get("summary") or "—"),
        "",
        "## Errors",
        "",
    ]
    errors = session.get("errors") or []
    if not errors:
        lines.append("_None_")
    else:
        for e in errors:
            lines.append(f"- `{json.dumps(e, ensure_ascii=False)[:500]}`")
    lines += ["", "## Architecture (unchanged)", ""]
    for step in session.get("architecture") or []:
        lines.append(f"1. {step}")
    lines.append("")
    return "\n".join(lines)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Run one IDA learning session (GHA)")
    add_common_args(parser)
    parser.add_argument(
        "--instruction",
        default=None,
        help="Learning instruction / mission text",
    )
    parser.add_argument(
        "--mission",
        default=None,
        help="Alias for instruction (mission trigger)",
    )
    parser.add_argument(
        "--trigger",
        default=None,
        choices=["schedule", "manual", "mission", "hourly", "daily"],
        help="How this session was triggered",
    )
    parser.add_argument("--pace", type=float, default=0.15, help="Event pace (CI: fast)")
    parser.add_argument(
        "--pending-review",
        action="store_true",
        help="Do not auto-approve candidates",
    )
    parser.add_argument(
        "--no-publish",
        action="store_true",
        help="Skip dataset publish even when not dry-run",
    )
    args = parser.parse_args(argv)

    try:
        environment = resolve_environment(args.environment)
        repo_root = Path(args.repo_root) if args.repo_root else find_repo_root()
        env_config = load_environment_config(repo_root, environment)
        dry_run = resolve_dry_run(args, env_config, default=True)
    except (ValueError, FileNotFoundError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        return EXIT_CONFIG_ERROR

    raw_instruction = (
        (args.instruction or args.mission or os.environ.get("IDA_LEARNING_INSTRUCTION") or "")
        .strip()
    )
    trigger = _resolve_trigger(os.environ.get("GITHUB_EVENT_NAME"), args.trigger)
    if trigger == "hourly":
        trigger = "schedule"
    if trigger == "daily":
        trigger = "schedule"

    # Dynamic mission selection (P0-4): no hardcoded default when auto/schedule
    selector_meta: dict[str, Any] = {}
    try:
        from automation.scheduler.mission_selector import (
            is_default_or_empty_instruction,
            select_next_mission,
        )

        if is_default_or_empty_instruction(raw_instruction) or trigger == "schedule":
            selector_meta = select_next_mission(repo_root)
            selected = (selector_meta or {}).get("selected") or {}
            instruction = str(
                selected.get("instruction")
                or raw_instruction
                or "Produce Industry Dataset — expand industry_library toward product target"
            )
            selector_meta["applied"] = True
        else:
            instruction = raw_instruction
            selector_meta = {"applied": False, "reason": "explicit_mission_provided"}
    except Exception as exc:  # noqa: BLE001
        instruction = (
            raw_instruction
            or "Produce Industry Dataset — expand industry_library toward product target"
        )
        selector_meta = {"applied": False, "error": str(exc)}

    mission = (args.mission or instruction).strip()

    ctx = RunContext(
        name="learning",
        repo_root=repo_root,
        environment=environment,
        dry_run=dry_run,
        env_config=env_config,
    )
    ctx.messages.append(f"instruction={instruction[:120]}")
    ctx.messages.append(f"trigger={trigger}")
    if selector_meta:
        ctx.messages.append(
            f"mission_selector={selector_meta.get('selected', {}).get('batch_id', selector_meta)}"
        )
        ctx.metrics["mission_selector"] = selector_meta

    # Publish only when env allows and not dry-run
    allow_publish = bool(env_config.get("allow_publish")) and not dry_run
    publish = allow_publish and not args.no_publish
    auto_approve = not args.pending_review

    selected_dataset = None
    try:
        selected_dataset = (selector_meta.get("selected") or {}).get("dataset")
    except Exception:  # noqa: BLE001
        selected_dataset = None

    result = run_session(
        repo_root=repo_root,
        environment=environment,
        dry_run=dry_run,
        instruction=instruction,
        mission=mission,
        trigger=trigger,
        pace=args.pace,
        auto_approve=auto_approve,
        publish=publish,
        dataset=selected_dataset,
    )

    session = result.get("session") or {}
    ctx.metrics.update(
        {
            "session_id": session.get("session_id"),
            "status": session.get("status"),
            "knowledge_added": session.get("knowledge_added"),
            "knowledge_updated": session.get("knowledge_updated"),
            "knowledge_rejected": session.get("knowledge_rejected"),
            "duration_seconds": session.get("duration_seconds"),
            "events": len(session.get("events") or []),
        }
    )

    reports_dir = repo_root / "reports" / "learning"
    log_path = reports_dir / f"learning_session_{stamp()}.json"
    md_path = reports_dir / f"learning_session_{stamp()}.md"

    ok = bool(result.get("ok"))
    exit_code = EXIT_SUCCESS if ok else EXIT_VALIDATION_ERROR
    ctx.finish(exit_code, "success" if ok else "failed")
    write_json_log(log_path, ctx, extra={"session": {
        k: session.get(k)
        for k in (
            "session_id",
            "status",
            "start_time",
            "end_time",
            "duration_seconds",
            "knowledge_added",
            "knowledge_updated",
            "knowledge_rejected",
            "summary",
            "mission",
            "errors",
        )
    }})
    write_markdown_report(md_path, build_report(ctx, result), ctx)

    # Index of recent sessions for quick dashboard reads
    index = {
        "updated_at": session.get("end_time") or session.get("start_time"),
        "sessions": list_sessions(repo_root, limit=50),
    }
    index_path = sessions_root(repo_root) / "index.json"
    index_path.write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    # Machine-readable stdout for GHA step outputs
    kd = session.get("knowledge_delta") or {}
    ps = session.get("publish_summary") or {}
    print(
        json.dumps(
            {
                "ok": ok,
                "session_id": session.get("session_id"),
                "status": session.get("status"),
                "duration_seconds": session.get("duration_seconds"),
                "knowledge_added": session.get("knowledge_added"),
                "knowledge_updated": session.get("knowledge_updated"),
                "knowledge_rejected": session.get("knowledge_rejected"),
                "documents_discovered": kd.get("documents_discovered"),
                "documents_downloaded": kd.get("documents_downloaded"),
                "candidates_extracted": kd.get("candidates_extracted"),
                "candidates_validated": kd.get("candidates_validated"),
                "publish": {
                    "extracted": ps.get("extracted"),
                    "validated": ps.get("validated"),
                    "rejected": ps.get("rejected"),
                    "queued": ps.get("queued"),
                    "published": ps.get("rows_published") or session.get("knowledge_added"),
                    "duplicate": ps.get("duplicate"),
                    "skipped": ps.get("skipped"),
                    "by_dataset": ps.get("by_dataset"),
                },
                "last_connector": kd.get("last_connector"),
                "last_document": kd.get("last_document"),
                "last_published_entity": kd.get("last_published_entity"),
                "summary": session.get("summary"),
                "dry_run": dry_run,
                "environment": environment,
            },
            ensure_ascii=False,
        )
    )
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
