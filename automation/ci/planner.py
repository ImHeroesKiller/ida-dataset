#!/usr/bin/env python3
"""Knowledge Planner CI job.

Runs Knowledge Planner, Gap Analyzer, and Priority Engine over the
repository inventory. Never modifies datasets. Never publishes.

Exit codes: 0 success | 2 config | 3 policy
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

_REPO = Path(__file__).resolve().parents[2]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))

from automation.ci import (  # noqa: E402
    EXIT_CONFIG_ERROR,
    EXIT_POLICY_VIOLATION,
    EXIT_SUCCESS,
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


@dataclass
class DatasetGap:
    path: str
    dataset: str
    domain: str
    row_count: int
    is_placeholder: bool
    priority_score: float
    reasons: list[str] = field(default_factory=list)
    recommended_actions: list[str] = field(default_factory=list)


def count_csv_rows(path: Path) -> int:
    try:
        text = path.read_text(encoding="utf-8-sig")
        reader = csv.reader(text.splitlines())
        rows = list(reader)
        if not rows:
            return 0
        return max(0, len(rows) - 1)
    except (OSError, UnicodeDecodeError, csv.Error):
        return -1


def inventory_datasets(root: Path) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    domains = root / "domains"
    if not domains.exists():
        return items
    for path in sorted(domains.rglob("*.csv")):
        rel = str(path.relative_to(root))
        domain = path.relative_to(domains).parts[0] if path.relative_to(domains).parts else ""
        rows = count_csv_rows(path)
        items.append(
            {
                "path": rel,
                "dataset": path.stem,
                "domain": domain,
                "row_count": rows,
                "is_placeholder": rows == 0,
            }
        )
    return items


def analyze_gaps(
    inventory: list[dict[str, Any]],
    *,
    gap_threshold: int,
    weights: dict[str, float],
) -> list[DatasetGap]:
    """Gap Analyzer + Priority Engine."""
    w_empty = float(weights.get("emptiness", 0.5))
    w_rel = float(weights.get("relationships", 0.3))
    w_strat = float(weights.get("strategic", 0.2))

    # Strategic weight boost for core BD datasets
    strategic_boost = {
        "company_profile": 1.0,
        "opportunity_analysis": 0.95,
        "product_catalog": 0.9,
        "industry_library": 0.85,
        "pain_point_library": 0.8,
        "solution_library": 0.8,
        "competitor_library": 0.75,
        "discovery_question_library": 0.7,
        "case_study_library": 0.65,
        "business_signal_library": 0.6,
        "framework_library": 0.55,
    }

    gaps: list[DatasetGap] = []
    for item in inventory:
        reasons: list[str] = []
        actions: list[str] = []
        row_count = int(item["row_count"])
        dataset = item["dataset"]

        emptiness = 1.0 if row_count <= 0 else max(0.0, 1.0 - (row_count / max(gap_threshold, 1)))
        if row_count < 0:
            emptiness = 1.0
            reasons.append("unreadable_csv")
            actions.append("Fix file encoding/format")
        elif row_count == 0:
            reasons.append("placeholder_header_only")
            actions.append("Populate via KAS review queue (human-approved)")
        elif row_count < gap_threshold:
            reasons.append(f"below_threshold:{row_count}<{gap_threshold}")
            actions.append("Expand coverage for this dataset")

        # Relationship density proxy: core entities without satellite data
        rel_gap = 0.0
        if dataset == "company_profile" and row_count > 0:
            # if companies exist but opportunity is thin, raise relationship gap
            rel_gap = 0.3
            reasons.append("relationship_coverage_unknown")
        if item["is_placeholder"]:
            rel_gap = max(rel_gap, 0.5)

        strat = strategic_boost.get(dataset, 0.3 if item["domain"] == "business_development" else 0.1)

        score = (w_empty * emptiness) + (w_rel * rel_gap) + (w_strat * strat)
        score = round(min(1.0, score), 4)

        if reasons:
            gaps.append(
                DatasetGap(
                    path=item["path"],
                    dataset=dataset,
                    domain=item["domain"],
                    row_count=row_count,
                    is_placeholder=bool(item["is_placeholder"]),
                    priority_score=score,
                    reasons=reasons,
                    recommended_actions=actions or ["Review with Knowledge Planner"],
                )
            )

    gaps.sort(key=lambda g: g.priority_score, reverse=True)
    return gaps


def knowledge_plan(gaps: list[DatasetGap], inventory: list[dict[str, Any]]) -> dict[str, Any]:
    """Knowledge Planner synthesis."""
    total = len(inventory)
    placeholders = sum(1 for i in inventory if i["is_placeholder"])
    populated = total - placeholders
    top = gaps[:10]
    return {
        "summary": {
            "datasets_total": total,
            "datasets_populated": populated,
            "datasets_placeholder": placeholders,
            "gaps_identified": len(gaps),
        },
        "focus_areas": [
            {
                "dataset": g.dataset,
                "domain": g.domain,
                "priority_score": g.priority_score,
                "actions": g.recommended_actions,
            }
            for g in top
        ],
        "next_sprint_candidates": [g.dataset for g in top[:5]],
        "principles": [
            "Human-in-the-loop acquisition only",
            "No autonomous crawling or LLM extraction in this workflow",
            "Never modify production datasets from planner",
        ],
    }


def build_markdown(
    ctx: RunContext,
    plan: dict[str, Any],
    gaps: list[DatasetGap],
    inventory: list[dict[str, Any]],
) -> str:
    lines = report_header(ctx, "Planning Report")
    s = plan["summary"]
    lines += [
        "## Knowledge Planner Summary",
        "",
        f"| Metric | Value |",
        f"| --- | ---: |",
        f"| Datasets total | {s['datasets_total']} |",
        f"| Populated | {s['datasets_populated']} |",
        f"| Placeholder (header only) | {s['datasets_placeholder']} |",
        f"| Gaps identified | {s['gaps_identified']} |",
        "",
        "## Priority Engine — Top Gaps",
        "",
    ]
    if not gaps:
        lines.append("No gaps identified under current thresholds.")
        lines.append("")
    else:
        lines.append("| Priority | Dataset | Domain | Rows | Reasons |")
        lines.append("| ---: | --- | --- | ---: | --- |")
        for g in gaps[:20]:
            lines.append(
                f"| {g.priority_score:.2f} | `{g.dataset}` | {g.domain} | "
                f"{g.row_count} | {', '.join(g.reasons)} |"
            )
        lines.append("")

    lines += [
        "## Recommended Next Sprint Candidates",
        "",
    ]
    for name in plan.get("next_sprint_candidates") or []:
        lines.append(f"- `{name}`")
    lines += [
        "",
        "## Inventory",
        "",
        "| Dataset | Domain | Rows | Placeholder |",
        "| --- | --- | ---: | --- |",
    ]
    for item in inventory:
        lines.append(
            f"| `{item['dataset']}` | {item['domain']} | {item['row_count']} | "
            f"{item['is_placeholder']} |"
        )
    lines += [
        "",
        "## Guardrails",
        "",
        "- Never modify datasets from this workflow.",
        "- Never publish from this workflow.",
        "- Acquisition remains human-controlled via KAS.",
        "",
    ]
    return "\n".join(lines)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="IDA Knowledge Planner CI job")
    add_common_args(parser)
    args = parser.parse_args(argv)

    try:
        environment = resolve_environment(args.environment)
    except ValueError as exc:
        print(f"CONFIG ERROR: {exc}", file=sys.stderr)
        return EXIT_CONFIG_ERROR

    root = find_repo_root(args.repo_root)
    try:
        env_config = load_environment_config(root, environment)
    except FileNotFoundError as exc:
        print(f"CONFIG ERROR: {exc}", file=sys.stderr)
        return EXIT_CONFIG_ERROR

    dry_run = resolve_dry_run(args, env_config, default=True)
    ctx = RunContext(
        name="planner",
        repo_root=root,
        environment=environment,
        dry_run=dry_run,
        env_config=env_config,
    )

    # Policy: planner must not publish
    if env_config.get("allow_publish") and False:
        pass  # never publish here

    planner_cfg = env_config.get("planner", {})
    gap_threshold = int(planner_cfg.get("gap_threshold_rows", 5))
    weights = dict(planner_cfg.get("priority_weights") or {})

    inventory = inventory_datasets(root)
    gaps = analyze_gaps(inventory, gap_threshold=gap_threshold, weights=weights)
    plan = knowledge_plan(gaps, inventory)

    ctx.metrics = {
        **plan["summary"],
        "gap_threshold_rows": gap_threshold,
        "top_priority": gaps[0].priority_score if gaps else 0,
    }
    ctx.messages.append("Planner completed without dataset mutations")
    ctx.finish(EXIT_SUCCESS)

    report_dir = root / env_config.get("paths", {}).get(
        "planner_reports", "reports/planner"
    )
    ts = stamp()
    md_path = report_dir / "planning_report.md"
    json_path = report_dir / "planning_report.json"
    log_path = report_dir / f"planner_{ts}.json"

    payload = {
        "plan": plan,
        "gaps": [
            {
                "path": g.path,
                "dataset": g.dataset,
                "domain": g.domain,
                "row_count": g.row_count,
                "is_placeholder": g.is_placeholder,
                "priority_score": g.priority_score,
                "reasons": g.reasons,
                "recommended_actions": g.recommended_actions,
            }
            for g in gaps
        ],
        "inventory": inventory,
        "run": ctx.to_log_dict(),
    }

    write_markdown_report(md_path, build_markdown(ctx, plan, gaps, inventory), ctx)
    # planning_report.json is a required artifact
    json_path.parent.mkdir(parents=True, exist_ok=True)
    if not (dry_run and env_config.get("dry_run_skip_reports")):
        json_path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        ctx.artifacts.append(str(json_path))
    write_json_log(log_path, ctx, extra={"plan_summary": plan["summary"]})

    print(f"Planning complete: {plan['summary']}")
    print(f"Wrote {md_path} and {json_path}")
    return EXIT_SUCCESS


if __name__ == "__main__":
    raise SystemExit(main())
