"""Discovery analytics reports under reports/discovery/."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root


def write_discovery_reports(
    analytics: dict[str, Any],
    *,
    repo_root: Path | None = None,
) -> dict[str, str]:
    root = repo_root or find_repo_root()
    out = root / "reports" / "discovery"
    out.mkdir(parents=True, exist_ok=True)
    written: dict[str, str] = {}

    def w(name: str, body: str) -> None:
        p = out / name
        p.write_text(body.rstrip() + "\n", encoding="utf-8", newline="\n")
        written[name] = str(p.relative_to(root))

    sid = analytics.get("session_id") or "—"
    mid = analytics.get("mission_id") or "—"

    # provider_statistics
    lines = [
        "# Provider Statistics",
        "",
        f"**Generated:** {utc_now_iso()}",
        f"**Session:** `{sid}` · **Mission:** `{mid}`",
        "",
        f"Queries executed: **{analytics.get('queries_executed', 0)}**",
        f"URLs discovered: **{analytics.get('urls_discovered', 0)}**",
        f"URLs accepted: **{analytics.get('urls_accepted', 0)}**",
        f"URLs rejected: **{analytics.get('urls_rejected', 0)}**",
        "",
        "| Provider | Type | Queries | URLs | Cache hits | ms | Status |",
        "|----------|------|--------:|-----:|-----------:|---:|--------|",
    ]
    for p in analytics.get("providers") or []:
        lines.append(
            f"| {p.get('name')} | {p.get('api_type')} | {p.get('queries', 0)} | "
            f"{p.get('urls', 0)} | {p.get('cache_hits', 0)} | {p.get('elapsed_ms', 0)} | "
            f"{p.get('status')} |"
        )
    w("provider_statistics.md", "\n".join(lines))

    # provider_health
    hl = [
        "# Provider Health",
        "",
        f"**Session:** `{sid}`",
        "",
        "| Provider | Health | Credentials | Message |",
        "|----------|--------|-------------|---------|",
    ]
    for p in analytics.get("providers") or []:
        h = p.get("health") or {}
        hl.append(
            f"| {p.get('name')} | {h.get('status') if isinstance(h, dict) else h} | "
            f"{p.get('credentials_available')} | "
            f"{(h.get('message') if isinstance(h, dict) else '') or '—'} |"
        )
    w("provider_health.md", "\n".join(hl))

    # query_statistics
    ql = [
        "# Query Statistics",
        "",
        f"**Session:** `{sid}`",
        "",
        "| Provider | Query | URLs | ms | Cached |",
        "|----------|-------|-----:|---:|--------|",
    ]
    for q in (analytics.get("query_stats") or [])[:80]:
        ql.append(
            f"| {q.get('provider_id')} | `{(q.get('query') or '')[:80]}` | "
            f"{q.get('urls', 0)} | {q.get('elapsed_ms', 0)} | {q.get('cached', False)} |"
        )
    w("query_statistics.md", "\n".join(ql))

    # reputation_scores
    rl = [
        "# Reputation Scores",
        "",
        "Trusted sources ranked for discovery targeting.",
        "",
        "| Rank | Source | Reputation | Authority | Rank score |",
        "|-----:|--------|-----------:|----------:|-----------:|",
    ]
    for i, s in enumerate(analytics.get("reputation_top") or [], 1):
        rl.append(
            f"| {i} | {s.get('name') or s.get('id')} | {s.get('reputation')} | "
            f"{s.get('authority')} | {s.get('score')} |"
        )
    w("reputation_scores.md", "\n".join(rl))

    # accepted_urls
    al = [
        "# Accepted URLs",
        "",
        "Only domains present in Trusted Source Registry.",
        "",
        "| URL | Source | Provider | Title |",
        "|-----|--------|----------|-------|",
    ]
    for a in analytics.get("accepted_urls") or []:
        al.append(
            f"| {(a.get('url') or '')[:90]} | {a.get('source_id')} | "
            f"{a.get('provider_id')} | {(a.get('title') or '')[:60]} |"
        )
    if not analytics.get("accepted_urls"):
        al.append("| — | — | — | none |")
    w("accepted_urls.md", "\n".join(al))

    # rejected_urls
    jl = [
        "# Rejected URLs",
        "",
        "Rejected by trusted-source filter (blogs, social, non-registry domains, duplicates).",
        "",
        "| URL | Reason | Host | Provider |",
        "|-----|--------|------|----------|",
    ]
    for r in analytics.get("rejected_urls") or []:
        jl.append(
            f"| {(r.get('url') or '')[:80]} | {r.get('reason')} | "
            f"{r.get('host')} | {r.get('provider_id')} |"
        )
    if not analytics.get("rejected_urls"):
        jl.append("| — | — | — | none |")
    w("rejected_urls.md", "\n".join(jl))

    # trusted_source_usage
    usage: dict[str, int] = {}
    for a in analytics.get("accepted_urls") or []:
        sid = str(a.get("source_id") or "unknown")
        usage[sid] = usage.get(sid, 0) + 1
    tl = [
        "# Trusted Source Usage",
        "",
        "Accepted discovery URLs attributed to trusted registry sources.",
        "",
        "| Source ID | Accepted URLs |",
        "|-----------|--------------:|",
    ]
    for sid, n in sorted(usage.items(), key=lambda x: -x[1]):
        tl.append(f"| {sid} | {n} |")
    if not usage:
        tl.append("| — | 0 |")
    gap = analytics.get("knowledge_gap") or {}
    tl += [
        "",
        "## Knowledge gap",
        "",
        f"- Dataset: `{gap.get('dataset')}`",
        f"- Current: {gap.get('current_rows')}",
        f"- Target: {gap.get('target_rows')}",
        f"- Gap: {gap.get('gap_rows')}",
        f"- Coverage: {gap.get('coverage_pct')}%",
        "",
        "> Search engines are discovery tools only. Knowledge is extracted solely from trusted sources.",
        "",
    ]
    w("trusted_source_usage.md", "\n".join(tl))

    return written
