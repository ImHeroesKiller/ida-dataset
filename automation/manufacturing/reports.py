"""Manufacturing intelligence reports."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root


def write_manufacturing_reports(
    state: dict[str, Any],
    *,
    repo_root: Path | None = None,
) -> dict[str, str]:
    root = repo_root or find_repo_root()
    out = root / "reports" / "manufacturing"
    out.mkdir(parents=True, exist_ok=True)
    written: dict[str, str] = {}

    def w(name: str, body: str) -> None:
        p = out / name
        p.write_text(body.rstrip() + "\n", encoding="utf-8", newline="\n")
        written[name] = str(p.relative_to(root))

    mode = state.get("mode") or {}
    evals = state.get("evaluations") or []
    cap = state.get("capacity") or {}
    eco = state.get("economics") or {}
    missions = state.get("proposed_missions") or []
    growth = state.get("growth") or {}

    # knowledge_gap.md
    lines = [
        "# Knowledge Gap",
        "",
        f"**Generated:** {utc_now_iso()}",
        f"**Mode:** {mode.get('mode')} — {mode.get('reason')}",
        "",
        "Multi-dimensional gaps (not coverage-only).",
        "",
        "| Dataset | Rows | Min gap | Stretch gap | Universe rem. | Gap score | Density | Conf gap | Fresh gap |",
        "|---------|-----:|--------:|------------:|--------------:|----------:|--------:|---------:|----------:|",
    ]
    for e in evals:
        lines.append(
            f"| {e.get('dataset')} | {e.get('current_rows')} | {e.get('minimum_gap')} | "
            f"{e.get('stretch_gap')} | {e.get('universe_gap')} | {e.get('knowledge_gap_score')} | "
            f"{e.get('knowledge_density')} | {e.get('confidence_gap')} | {e.get('freshness_gap')} |"
        )
    w("knowledge_gap.md", "\n".join(lines))

    # knowledge_universe.md
    ul = [
        "# Knowledge Universe",
        "",
        "Dynamic estimates — hard_limit is null (no artificial ceiling).",
        "",
        "| Dataset | Current | Estimated universe | Remaining | Fill % | Method |",
        "|---------|--------:|-------------------:|----------:|-------:|--------|",
    ]
    for e in evals:
        u = e.get("universe") or {}
        ul.append(
            f"| {e.get('dataset')} | {e.get('current_rows')} | {u.get('estimated_universe')} | "
            f"{u.get('remaining_estimate')} | {u.get('fill_pct')} | {u.get('method')} |"
        )
    w("knowledge_universe.md", "\n".join(ul))

    # production_capacity.md
    w(
        "production_capacity.md",
        "\n".join(
            [
                "# Production Capacity",
                "",
                f"| Metric | Value |",
                f"|--------|------:|",
                f"| Rows/hour | {cap.get('rows_per_hour')} |",
                f"| Rows/day | {cap.get('rows_per_day')} |",
                f"| Rows/week | {cap.get('rows_per_week')} |",
                f"| Rows/month | {cap.get('rows_per_month')} |",
                f"| Documents/hour | {cap.get('documents_per_hour')} |",
                f"| Candidates/hour | {cap.get('candidates_per_hour')} |",
                f"| Growth velocity (rows/day) | {cap.get('growth_velocity_rows_per_day')} |",
                f"| Sessions 24h | {cap.get('sessions_24h')} |",
                f"| Rows this week | {cap.get('rows_this_week')} |",
                f"| Rows this month | {cap.get('rows_this_month')} |",
                "",
            ]
        ),
    )

    # growth_velocity.md
    w(
        "growth_velocity.md",
        "\n".join(
            [
                "# Growth Velocity",
                "",
                f"- Growth velocity: **{growth.get('growth_velocity')}** rows/day",
                f"- Coverage velocity: **{growth.get('coverage_velocity')}** rows/day capacity",
                f"- Knowledge produced (all datasets): **{growth.get('knowledge_produced_total')}**",
                "",
                "```json",
                json.dumps(cap, indent=2, ensure_ascii=False),
                "```",
                "",
            ]
        ),
    )

    # factory_economics.md
    w(
        "factory_economics.md",
        "\n".join(
            [
                "# Factory Economics",
                "",
                f"| Metric | Value |",
                f"|--------|------:|",
                f"| Bandwidth (bytes) | {eco.get('bandwidth_bytes')} |",
                f"| API requests | {eco.get('api_requests')} |",
                f"| Cache hit rate | {eco.get('cache_hit_rate')} |",
                f"| Rows produced | {eco.get('rows_produced')} |",
                f"| Documents processed | {eco.get('documents_processed')} |",
                f"| Rows per API call | {eco.get('rows_per_api_call')} |",
                f"| Rows per GB | {eco.get('rows_per_gb')} |",
                f"| Est. production cost (USD proxy) | {eco.get('estimated_production_cost_usd')} |",
                f"| Knowledge ROI | {eco.get('knowledge_roi')} |",
                "",
                "## Top sources by rows",
                "",
                "```json",
                json.dumps(eco.get("rows_per_source") or [], indent=2, ensure_ascii=False),
                "```",
                "",
            ]
        ),
    )

    # continuous_production.md
    w(
        "continuous_production.md",
        "\n".join(
            [
                "# Continuous Production",
                "",
                "**Governance:** IDA Dataset Factory has no predefined finish line.",
                "",
                f"- Mode: **{mode.get('mode')}**",
                f"- Reason: {mode.get('reason')}",
                f"- Never stop at numeric target: **{state.get('never_stop_at_numeric_target')}**",
                f"- Pause: {state.get('pause')}",
                "",
                "The factory continues while trusted, validated knowledge still exists.",
                "It only slows for: no updates, API quota, rate limits, backoff, maintenance.",
                "",
                f"Selected mission: **{(state.get('selected_mission') or {}).get('title')}**",
                "",
                (state.get("selected_mission") or {}).get("instruction") or "",
                "",
            ]
        ),
    )

    # scheduler_decisions.md
    sl = [
        "# Scheduler Decisions",
        "",
        "Manufacturing controller proposals (highest-value knowledge demand).",
        "",
        "| # | Mode | Dataset | Title | Gap score | Universe rem. |",
        "|--:|------|---------|-------|----------:|--------------:|",
    ]
    for i, m in enumerate(missions[:12], 1):
        sl.append(
            f"| {i} | {m.get('mode')} | {m.get('dataset')} | {m.get('title')} | "
            f"{m.get('knowledge_gap_score')} | {m.get('universe_gap')} |"
        )
    sl += ["", "## Decision chain", "", "```", 
           "Biggest knowledge gap → Trusted source → Discovery → Best connector → High-value docs → Collect → Validate → Publish → Repeat",
           "```", ""]
    w("scheduler_decisions.md", "\n".join(sl))

    return written
