"""Write reports/diagnostics/* from collected evidence."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional

from automation.diagnostics.analyzer import analyze_root_cause
from automation.diagnostics.collector import collect_full_bundle
from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root


def _w(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body.rstrip() + "\n", encoding="utf-8", newline="\n")


def _md_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for r in rows:
        cells = [str(c if c is not None else "—").replace("|", "\\|")[:120] for c in r]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def write_diagnostics_bundle(
    *,
    repo_root: Path | None = None,
    session: Optional[dict[str, Any]] = None,
    acquisition: Optional[dict[str, Any]] = None,
) -> dict[str, str]:
    """Generate all Phase 1–10 diagnostic reports. Observe-only."""
    root = repo_root or find_repo_root()
    out = root / "reports" / "diagnostics"
    out.mkdir(parents=True, exist_ok=True)

    bundle = collect_full_bundle(
        root, session=session, acquisition=acquisition
    )
    rca = analyze_root_cause(bundle)
    written: dict[str, str] = {}

    # Persist machine-readable bundle
    state_path = (
        root / "automation" / "learning" / "state" / "diagnostics_last.json"
    )
    try:
        state_path.parent.mkdir(parents=True, exist_ok=True)
        # slim bundle for disk (drop huge nested if any)
        slim = {
            "generated_at": bundle.get("generated_at"),
            "mission": bundle.get("mission"),
            "knowledge_gap": {
                "mode": (bundle.get("knowledge_gap") or {}).get("mode"),
                "evaluations": (bundle.get("knowledge_gap") or {}).get("evaluations"),
                "selected_mission": (bundle.get("knowledge_gap") or {}).get(
                    "selected_mission"
                ),
            },
            "execution_stages": bundle.get("execution_stages"),
            "source_trace": bundle.get("source_trace"),
            "document_trace": bundle.get("document_trace"),
            "extraction_trace": bundle.get("extraction_trace"),
            "publish_trace": bundle.get("publish_trace"),
            "session": {
                k: (bundle.get("session") or {}).get(k)
                for k in (
                    "session_id",
                    "status",
                    "start_time",
                    "end_time",
                    "duration_seconds",
                    "mission",
                    "instruction",
                    "knowledge_added",
                    "knowledge_rejected",
                    "summary",
                    "dry_run",
                    "trigger",
                )
            },
            "fingerprints": bundle.get("fingerprints"),
            "root_cause": rca,
            "production_trace_summary": (bundle.get("production_trace") or {}).get(
                "summary"
            ),
            "publish_balance": ((bundle.get("production_trace") or {}).get("publish")),
        }
        state_path.write_text(
            json.dumps(slim, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    except Exception:  # noqa: BLE001
        pass

    gen = bundle.get("generated_at") or utc_now_iso()
    mission = (bundle.get("mission") or {}).get("selected") or {}
    session = bundle.get("session") or {}
    pt = bundle.get("production_trace") or {}
    summary = pt.get("summary") or {}

    # --- mission_trace.md ---
    mrows = []
    for d in (bundle.get("mission") or {}).get("datasets") or []:
        mrows.append(
            [
                d.get("dataset"),
                d.get("current_rows"),
                d.get("coverage_pct"),
                d.get("knowledge_gap_score"),
                d.get("priority_score"),
                d.get("eligible"),
                d.get("selected"),
                d.get("skip_reason") or "—",
            ]
        )
    body = "\n".join(
        [
            "# Mission Trace",
            "",
            f"**Generated:** {gen}",
            f"**Selected:** `{mission.get('dataset')}` · score={mission.get('score')}",
            f"**Reason:** {mission.get('reason')}",
            f"**Instruction:** {mission.get('instruction')}",
            "",
            "## All datasets",
            "",
            _md_table(
                [
                    "Dataset",
                    "Rows",
                    "Coverage%",
                    "Gap score",
                    "Priority score",
                    "Eligible",
                    "Selected",
                    "Skip reason",
                ],
                mrows,
            ),
            "",
            "## Evidence",
            "",
            f"- Manufacturing mode: `{(bundle.get('mission') or {}).get('manufacturing_mode')}`",
            f"- Active sources: `{(bundle.get('mission') or {}).get('active_sources')}`",
            f"- Continuous: `{(bundle.get('mission') or {}).get('continuous')}`",
            "",
        ]
    )
    p = out / "mission_trace.md"
    _w(p, body)
    written["mission_trace.md"] = str(p.relative_to(root))

    # --- knowledge_gap_trace.md ---
    kg = bundle.get("knowledge_gap") or {}
    grows = []
    for e in kg.get("evaluations") or []:
        grows.append(
            [
                e.get("dataset"),
                e.get("current_rows"),
                e.get("coverage"),
                e.get("freshness_gap"),
                e.get("relationship_score"),
                e.get("dependency_score"),
                e.get("business_priority"),
                e.get("knowledge_gap_score"),
            ]
        )
    body = "\n".join(
        [
            "# Knowledge Gap Trace",
            "",
            f"**Generated:** {gen}",
            f"**Mode:** `{kg.get('mode')}`",
            f"**Selected mission:** `{(kg.get('selected_mission') or {}).get('dataset') or (kg.get('selected_mission') or {}).get('title')}`",
            "",
            "Sorted by knowledge_gap_score descending.",
            "",
            _md_table(
                [
                    "Dataset",
                    "Rows",
                    "Coverage",
                    "Freshness gap",
                    "Relationship",
                    "Dependency",
                    "Business priority",
                    "Overall gap score",
                ],
                grows,
            ),
            "",
            f"Summary: `{kg.get('knowledge_gap_summary')}`",
            "",
        ]
    )
    p = out / "knowledge_gap_trace.md"
    _w(p, body)
    written["knowledge_gap_trace.md"] = str(p.relative_to(root))

    # --- scheduler_trace.md ---
    hb = bundle.get("heartbeat") or {}
    mode = kg.get("mode") or {}
    if isinstance(mode, dict):
        mode_name = mode.get("mode") or mode
    else:
        mode_name = mode
    body = "\n".join(
        [
            "# Scheduler Trace",
            "",
            f"**Generated:** {gen}",
            "",
            "## Current mode",
            "",
            f"`{mode_name}`",
            "",
            "## Current mission",
            "",
            f"- Dataset: `{mission.get('dataset')}`",
            f"- Title: `{mission.get('title')}`",
            f"- Instruction: {mission.get('instruction')}",
            f"- Reason: {mission.get('reason')}",
            "",
            "## Heartbeat",
            "",
            _md_table(
                ["Field", "Value"],
                [
                    ["status", hb.get("status")],
                    ["last_heartbeat", hb.get("last_heartbeat")],
                    ["last_success", hb.get("last_success")],
                    ["last_failure", hb.get("last_failure")],
                    ["current_job", hb.get("current_job")],
                    ["job_duration_seconds", hb.get("job_duration_seconds")],
                    ["last_error", hb.get("last_error")],
                ],
            ),
            "",
            "## Missions not selected (eligible or not)",
            "",
            _md_table(
                ["Dataset", "Eligible", "Score", "Skip / not-selected reason"],
                [
                    [
                        d.get("dataset"),
                        d.get("eligible"),
                        d.get("priority_score"),
                        d.get("skip_reason") or "—",
                    ]
                    for d in ((bundle.get("mission") or {}).get("datasets") or [])
                    if not d.get("selected")
                ],
            ),
            "",
            "## Next mission (rank #2 if any)",
            "",
        ]
    )
    ranking = (bundle.get("mission") or {}).get("ranking") or []
    if len(ranking) > 1:
        nxt = ranking[1]
        body += f"- `{nxt.get('dataset')}` score={nxt.get('score')} cov={nxt.get('coverage_pct')}\n"
    else:
        body += "- —\n"
    p = out / "scheduler_trace.md"
    _w(p, body)
    written["scheduler_trace.md"] = str(p.relative_to(root))

    # --- source_trace.md ---
    srows = []
    for s in bundle.get("source_trace") or []:
        srows.append(
            [
                s.get("name") or s.get("connector_id"),
                s.get("source_id"),
                s.get("status"),
                s.get("http_status"),
                s.get("latency_ms"),
                s.get("documents_discovered"),
                s.get("documents_downloaded"),
                s.get("skipped"),
                s.get("error") or "—",
            ]
        )
    body = "\n".join(
        [
            "# Source Trace",
            "",
            f"**Generated:** {gen}",
            f"**Mission dataset:** `{mission.get('dataset')}`",
            "",
            "## Connectors contacted (last production trace)",
            "",
            _md_table(
                [
                    "Connector",
                    "Source",
                    "Status",
                    "HTTP",
                    "Latency ms",
                    "Discovered",
                    "Downloaded",
                    "Skipped",
                    "Error",
                ],
                srows or [["—", "—", "—", "—", "—", "—", "—", "—", "no connector rows in trace"]],
            ),
            "",
            "## Adaptive source performance history",
            "",
            _md_table(
                [
                    "Source",
                    "Attempts",
                    "Success rate",
                    "Avg latency",
                    "Docs",
                    "Rows",
                    "Dup rate",
                    "Backoff",
                ],
                [
                    [
                        s.get("source_id"),
                        s.get("attempts"),
                        s.get("success_rate"),
                        s.get("avg_latency_ms"),
                        s.get("documents_yielded"),
                        s.get("rows_yielded"),
                        s.get("duplicate_rate"),
                        s.get("backoff_level"),
                    ]
                    for s in ((bundle.get("source_performance") or {}).get("sources") or [])[
                        :25
                    ]
                ]
                or [["—"] * 8],
            ),
            "",
        ]
    )
    p = out / "source_trace.md"
    _w(p, body)
    written["source_trace.md"] = str(p.relative_to(root))

    # --- document_trace.md ---
    drows = []
    for d in bundle.get("document_trace") or []:
        drows.append(
            [
                d.get("document_id"),
                (d.get("url") or "")[:60],
                d.get("fingerprint"),
                d.get("already_processed"),
                d.get("cache_hit"),
                d.get("not_modified_304"),
                d.get("duplicate"),
                d.get("downloaded"),
                d.get("skip_reason") or d.get("status") or "—",
            ]
        )
    fp = bundle.get("fingerprints") or {}
    body = "\n".join(
        [
            "# Document Trace",
            "",
            f"**Generated:** {gen}",
            "",
            f"- Fingerprint URLs known: **{fp.get('urls_known')}**",
            f"- Fingerprint hashes known: **{fp.get('hashes_known')}**",
            f"- Fingerprint stats: `{fp.get('stats')}`",
            f"- Trace summary: discovered={summary.get('documents_discovered')} "
            f"downloaded={summary.get('documents_downloaded')} "
            f"duplicates={summary.get('documents_duplicates')}",
            "",
            _md_table(
                [
                    "Document ID",
                    "URL",
                    "Fingerprint",
                    "Already processed",
                    "Cache hit",
                    "304",
                    "Duplicate",
                    "Downloaded",
                    "Skip reason / status",
                ],
                drows,
            ),
            "",
        ]
    )
    p = out / "document_trace.md"
    _w(p, body)
    written["document_trace.md"] = str(p.relative_to(root))

    # --- extraction_trace.md ---
    et = bundle.get("extraction_trace") or {}
    if isinstance(et, dict):
        erows = []
        for c in et.get("candidates") or []:
            erows.append(
                [
                    c.get("candidate_id"),
                    c.get("entity"),
                    c.get("entity_type") or c.get("dataset"),
                    c.get("confidence"),
                    c.get("extraction_stage"),
                    c.get("validation_status"),
                    c.get("publish_status"),
                ]
            )
        body = "\n".join(
            [
                "# Extraction Trace",
                "",
                f"**Generated:** {gen}",
                "",
                f"- Stage stats: `{et.get('stage_stats')}`",
                f"- Fast: `{et.get('fast')}` · Medium: `{et.get('medium')}` · Deep: `{et.get('deep')}`",
                f"- LLM used: `{et.get('llm_used')}` · LLM skipped: `{et.get('llm_skipped')}`",
                "",
                _md_table(
                    [
                        "Candidate",
                        "Entity",
                        "Type/Dataset",
                        "Confidence",
                        "Stage",
                        "Validation",
                        "Publish",
                    ],
                    erows or [["—"] * 7],
                ),
                "",
            ]
        )
    else:
        body = f"# Extraction Trace\n\n**Generated:** {gen}\n\n_No extraction evidence._\n"
    p = out / "extraction_trace.md"
    _w(p, body)
    written["extraction_trace.md"] = str(p.relative_to(root))

    # --- publish_trace.md ---
    pubt = bundle.get("publish_trace") or {}
    prows = []
    for c in pubt.get("candidates") or []:
        prows.append(
            [
                c.get("candidate_id"),
                c.get("dataset"),
                c.get("confidence"),
                c.get("duplicate"),
                c.get("relationship_complete"),
                c.get("published"),
                c.get("queued"),
                c.get("manual_review"),
                c.get("reject_reason") or "—",
            ]
        )
    body = "\n".join(
        [
            "# Publish Trace",
            "",
            f"**Generated:** {gen}",
            "",
            f"- Balance: `{pubt.get('balance')}`",
            f"- Session knowledge_added: `{pubt.get('session_knowledge_added')}`",
            f"- Session knowledge_rejected: `{pubt.get('session_knowledge_rejected')}`",
            f"- dry_run: `{pubt.get('dry_run')}`",
            "",
            _md_table(
                [
                    "Candidate ID",
                    "Dataset",
                    "Confidence",
                    "Duplicate",
                    "Relationships",
                    "Published",
                    "Queue",
                    "Manual review",
                    "Reject reason",
                ],
                prows or [["—"] * 9],
            ),
            "",
        ]
    )
    p = out / "publish_trace.md"
    _w(p, body)
    written["publish_trace.md"] = str(p.relative_to(root))

    # --- session_trace.md ---
    stages = bundle.get("execution_stages") or []
    srows = [
        [
            s.get("stage"),
            s.get("status"),
            s.get("duration_ms"),
            s.get("documents"),
            s.get("rows"),
            (s.get("evidence") or "")[:80],
        ]
        for s in stages
    ]
    body = "\n".join(
        [
            "# Session Trace",
            "",
            f"**Generated:** {gen}",
            "",
            "## Session summary",
            "",
            _md_table(
                ["Field", "Value"],
                [
                    ["session_id", session.get("session_id")],
                    ["status", session.get("status")],
                    ["mission", session.get("mission")],
                    ["trigger", session.get("trigger")],
                    ["dry_run", session.get("dry_run")],
                    ["duration_seconds", session.get("duration_seconds")],
                    ["knowledge_added", session.get("knowledge_added")],
                    ["knowledge_rejected", session.get("knowledge_rejected")],
                    ["summary", session.get("summary")],
                    ["start_time", session.get("start_time")],
                    ["end_time", session.get("end_time")],
                ],
            ),
            "",
            "## Pipeline stages",
            "",
            _md_table(
                ["Stage", "Status", "Duration ms", "Documents", "Rows", "Evidence"],
                srows,
            ),
            "",
            "## Funnel",
            "",
            _md_table(
                ["Metric", "Value"],
                [
                    ["documents_discovered", summary.get("documents_discovered")],
                    ["documents_downloaded", summary.get("documents_downloaded")],
                    ["documents_duplicates", summary.get("documents_duplicates")],
                    ["candidates_extracted", summary.get("candidates_extracted")],
                    ["candidates_validated", summary.get("candidates_validated")],
                    ["candidates_rejected", summary.get("candidates_rejected")],
                    ["rows_published", summary.get("rows_published")],
                ],
            ),
            "",
            f"**Next mission (rank #2):** `{(ranking[1].get('dataset') if len(ranking) > 1 else '—')}`",
            "",
        ]
    )
    p = out / "session_trace.md"
    _w(p, body)
    written["session_trace.md"] = str(p.relative_to(root))

    # --- root_cause_analysis.md ---
    body = "\n".join(
        [
            "# Root Cause Analysis",
            "",
            f"**Generated:** {gen}",
            f"**Session:** `{rca.get('session_id')}`",
            f"**Mission:** `{rca.get('mission_id')}`",
            "",
            "> Diagnostics only. No fixes. Evidence only.",
            "",
            "## Why no new rows?",
            "",
            rca.get("why_no_new_rows") or "—",
            "",
            "## Exactly which stage stopped production?",
            "",
            f"**`{rca.get('stop_stage')}`**",
            "",
            "## What condition caused it?",
            "",
            f"**`{rca.get('condition')}`**",
            "",
            "## What module decided it?",
            "",
            f"**`{rca.get('module')}`**",
            "",
            "## What evidence proves it?",
            "",
            *[f"- {e}" for e in (rca.get("evidence") or ["—"])],
            "",
            "## Metrics snapshot",
            "",
            "```json",
            json.dumps(rca.get("metrics") or {}, indent=2, ensure_ascii=False),
            "```",
            "",
            "## Findings",
            "",
        ]
    )
    for i, fnd in enumerate(rca.get("findings") or [], 1):
        body += f"### Finding {i}\n\n{fnd.get('claim')}\n\n"
        for e in fnd.get("evidence") or []:
            body += f"- `{e}`\n"
        body += "\n"
    if rca.get("failed_stages"):
        body += "## Failed stages (from execution trace)\n\n"
        body += "```json\n" + json.dumps(rca["failed_stages"], indent=2) + "\n```\n"
    p = out / "root_cause_analysis.md"
    _w(p, body)
    written["root_cause_analysis.md"] = str(p.relative_to(root))

    return written
