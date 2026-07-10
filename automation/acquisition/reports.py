"""Generate production observability reports from a ProductionTrace dict."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root


def write_production_reports(
    trace: dict[str, Any],
    *,
    repo_root: Path | None = None,
) -> dict[str, str]:
    """Write reports/production/*.md from real trace data."""
    root = repo_root or find_repo_root()
    out = root / "reports" / "production"
    out.mkdir(parents=True, exist_ok=True)
    written: dict[str, str] = {}

    def w(name: str, body: str) -> None:
        path = out / name
        path.write_text(body.rstrip() + "\n", encoding="utf-8", newline="\n")
        written[name] = str(path.relative_to(root))

    mission = trace.get("mission") or "—"
    sid = trace.get("session_id") or "—"
    mid = trace.get("mission_id") or "—"
    started = trace.get("started_at") or ""
    finished = trace.get("finished_at") or utc_now_iso()
    summary = trace.get("summary") or {}
    publish = trace.get("publish") or {}
    connectors = trace.get("connectors") or []
    documents = trace.get("documents") or []
    candidates = trace.get("candidates") or []
    stages = trace.get("stages") or []
    chains = trace.get("evidence_chains") or []
    dq = trace.get("document_queue") or {}

    # production_trace.md
    lines = [
        "# Production Trace",
        "",
        f"**Generated:** {utc_now_iso()}",
        f"**Mission:** {mission}",
        f"**Mission ID:** `{mid}`",
        f"**Session ID:** `{sid}`",
        f"**Started:** {started}",
        f"**Finished:** {finished}",
        "",
        "## Pipeline timeline",
        "",
        "| Stage | Status | Duration (ms) | Docs | Rows | Errors |",
        "|-------|--------|--------------:|-----:|-----:|--------|",
    ]
    for st in stages:
        errs = "; ".join(st.get("errors") or [])[:80] or "—"
        lines.append(
            f"| {st.get('name')} | {st.get('status')} | {st.get('duration_ms', 0)} | "
            f"{st.get('documents', 0)} | {st.get('rows', 0)} | {errs} |"
        )
    lines += [
        "",
        "## Summary",
        "",
        f"- Documents discovered: **{summary.get('documents_discovered', 0)}**",
        f"- Documents downloaded: **{summary.get('documents_downloaded', 0)}**",
        f"- Candidates extracted: **{summary.get('candidates_extracted', 0)}**",
        f"- Candidates validated: **{summary.get('candidates_validated', 0)}**",
        f"- Candidates rejected: **{summary.get('candidates_rejected', 0)}**",
        f"- Rows published: **{summary.get('rows_published', 0)}**",
        f"- Duplicates: **{summary.get('rows_duplicate', 0)}**",
        "",
    ]
    w("production_trace.md", "\n".join(lines))

    # connector_summary.md
    cl = [
        "# Connector Summary",
        "",
        f"**Session:** `{sid}` · **Mission:** {mission}",
        "",
        "| Connector | Status | HTTP | Elapsed (ms) | Discovered | Downloaded | Skipped | Rejected | Retries | Error |",
        "|-----------|--------|------|-------------:|-----------:|-----------:|--------:|---------:|--------:|-------|",
    ]
    for c in connectors:
        cl.append(
            f"| {c.get('name') or c.get('connector_id')} | {c.get('status')} | "
            f"{c.get('http_status') or '—'} | {c.get('elapsed_ms', 0)} | "
            f"{c.get('documents_discovered', 0)} | {c.get('documents_downloaded', 0)} | "
            f"{c.get('skipped', 0)} | {c.get('rejected', 0)} | {c.get('retry_count', 0)} | "
            f"{(c.get('error') or '—')[:60]} |"
        )
    if not connectors:
        cl.append("| — | — | — | 0 | 0 | 0 | 0 | 0 | 0 | no connectors ran |")
    cl += ["", "## Details", ""]
    for c in connectors:
        cl.append(f"### {c.get('name') or c.get('connector_id')}")
        cl.append("")
        cl.append(f"- connector_id: `{c.get('connector_id')}`")
        cl.append(f"- source_id: `{c.get('source_id')}`")
        cl.append(f"- last_successful_sync: {c.get('last_successful_sync') or '—'}")
        cl.append(f"- urls_sample: {', '.join((c.get('urls') or [])[:3]) or '—'}")
        cl.append("")
    w("connector_summary.md", "\n".join(cl))

    # document_pipeline.md
    dl = [
        "# Document Pipeline",
        "",
        f"**Session:** `{sid}`",
        "",
        "## Queue counts",
        "",
        f"| State | Count |",
        f"|-------|------:|",
        f"| queued | {dq.get('queued', 0)} |",
        f"| processing | {dq.get('processing', 0)} |",
        f"| completed | {dq.get('completed', 0)} |",
        f"| failed | {dq.get('failed', 0)} |",
        f"| duplicates | {dq.get('duplicates', 0)} |",
        "",
        "## Documents",
        "",
        "| Document ID | Source | Connector | Type | Status | Size | URL |",
        "|-------------|--------|-----------|------|--------|-----:|-----|",
    ]
    for d in documents:
        dl.append(
            f"| `{d.get('document_id')}` | {d.get('source_id')} | {d.get('connector_id')} | "
            f"{d.get('content_type') or d.get('document_type') or '—'} | {d.get('status')} | "
            f"{d.get('size') or d.get('bytes') or 0} | {(d.get('url') or '')[:80]} |"
        )
    if not documents:
        dl.append("| — | — | — | — | — | 0 | none |")
    w("document_pipeline.md", "\n".join(dl))

    # candidate_pipeline.md
    candl = [
        "# Candidate Pipeline",
        "",
        f"**Session:** `{sid}`",
        "",
        f"Extracted **{publish.get('extracted', 0)}** · "
        f"Validated **{publish.get('validated', 0)}** · "
        f"Rejected **{publish.get('rejected', 0)}**",
        "",
        "| Candidate | Entity | Dataset | Confidence | Validation | Publish | Document | Reject reason |",
        "|-----------|--------|---------|------------|------------|---------|----------|---------------|",
    ]
    for c in candidates:
        candl.append(
            f"| `{c.get('candidate_id')}` | {c.get('entity') or c.get('name')} | "
            f"{c.get('dataset')} | {c.get('confidence')} | {c.get('validation_status')} | "
            f"{c.get('publish_status')} | `{c.get('document_id') or '—'}` | "
            f"{(c.get('reject_reason') or '—')[:50]} |"
        )
    if not candidates:
        candl.append("| — | — | — | — | — | — | — | none |")
    # evidence snippets
    candl += ["", "## Evidence snippets", ""]
    for c in candidates:
        snip = c.get("evidence_snippet") or ""
        if snip:
            candl.append(f"### `{c.get('candidate_id')}`")
            candl.append("")
            candl.append(f"> {snip[:500]}")
            candl.append("")
    w("candidate_pipeline.md", "\n".join(candl))

    # publish_pipeline.md
    pl = [
        "# Publish Pipeline",
        "",
        f"**Session:** `{sid}`",
        "",
        "## Balance",
        "",
        f"| Metric | Count |",
        f"|--------|------:|",
        f"| Extracted | {publish.get('extracted', 0)} |",
        f"| Validated | {publish.get('validated', 0)} |",
        f"| Rejected | {publish.get('rejected', 0)} |",
        f"| Queued | {publish.get('queued', 0)} |",
        f"| Published | {publish.get('published', 0)} |",
        f"| Duplicate | {publish.get('duplicate', 0)} |",
        f"| Skipped | {publish.get('skipped', 0)} |",
        "",
        f"Balance OK: **{publish.get('balance_ok', False)}**",
        "",
        "Identity: `extracted = validated + rejected`",
        "",
        "## By dataset",
        "",
    ]
    by_ds = publish.get("by_dataset") or {}
    if by_ds:
        pl.append("| Dataset | Rows |")
        pl.append("|---------|-----:|")
        for ds, n in by_ds.items():
            pl.append(f"| {ds} | {n} |")
    else:
        pl.append("_No rows published._")
    w("publish_pipeline.md", "\n".join(pl))

    # evidence_trace.md
    el = [
        "# Evidence Trace",
        "",
        f"**Session:** `{sid}`",
        "",
        "Every published row → candidate → document → connector → source.",
        "",
    ]
    if not chains:
        el.append("_No published evidence chains in this session._")
    for ch in chains:
        el += [
            f"## {ch.get('entity') or ch.get('entity_id')}",
            "",
            f"- **Dataset row:** `{ch.get('entity_id')}` · {ch.get('entity')} ({ch.get('dataset')})",
            f"- **Candidate:** `{ch.get('candidate_id')}`",
            f"- **Document:** `{ch.get('document_id')}` · {ch.get('document_title')}",
            f"- **Connector:** {ch.get('connector_name')} (`{ch.get('connector_id')}`)",
            f"- **Source:** {ch.get('source_name')} (`{ch.get('source_id')}`)",
            f"- **URL:** {ch.get('url')}",
            f"- **Confidence:** {ch.get('confidence')}",
            "",
        ]
        if ch.get("evidence_snippet"):
            el.append(f"> {ch['evidence_snippet'][:500]}")
            el.append("")
    w("evidence_trace.md", "\n".join(el))

    # runtime_statistics.md
    total_ms = sum(float(st.get("duration_ms") or 0) for st in stages)
    rl = [
        "# Runtime Statistics",
        "",
        f"**Session:** `{sid}`",
        f"**Mission:** {mission}",
        f"**Total stage time (ms):** {round(total_ms, 1)}",
        "",
        "## Stage durations",
        "",
        "| Stage | ms | Status |",
        "|-------|---:|--------|",
    ]
    for st in stages:
        rl.append(f"| {st.get('name')} | {st.get('duration_ms', 0)} | {st.get('status')} |")
    rl += [
        "",
        "## Counters",
        "",
        "```json",
        json.dumps(
            {
                "summary": summary,
                "publish": publish,
                "document_queue": dq,
                "exports": trace.get("exports"),
                "git": trace.get("git"),
            },
            indent=2,
            ensure_ascii=False,
        ),
        "```",
        "",
    ]
    w("runtime_statistics.md", "\n".join(rl))

    # also store session-scoped copies
    if sid and sid != "—":
        sess_dir = out / "sessions" / str(sid)
        sess_dir.mkdir(parents=True, exist_ok=True)
        for name in written:
            src = out / name
            (sess_dir / name).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")

    return written
