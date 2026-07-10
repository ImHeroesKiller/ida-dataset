#!/usr/bin/env python3
"""Review summary CI job.

Reads automation/review/ and queue folders.
Generates review_summary.md.
No publishing.

Exit codes: 0 success | 2 config
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Optional

_REPO = Path(__file__).resolve().parents[2]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))

from automation.ci import EXIT_CONFIG_ERROR, EXIT_SUCCESS  # noqa: E402
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
from automation.lib.io_utils import load_candidates  # noqa: E402


def load_json_if_exists(path: Path) -> Any:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def collect_review_state(root: Path, env_config: dict[str, Any]) -> dict[str, Any]:
    paths = env_config.get("paths", {})
    pending_dir = root / paths.get("queue_pending", "automation/queue/pending")
    approved_dir = root / paths.get("queue_approved", "automation/queue/approved")
    rejected_dir = root / paths.get("queue_rejected", "automation/queue/rejected")
    review_dir = root / paths.get("automation_review", "automation/review")

    pending = load_candidates(pending_dir)
    approved = load_candidates(approved_dir)
    rejected = load_candidates(rejected_dir)
    manifest = load_json_if_exists(review_dir / "review_queue.json")

    def summarize(cands):
        rows = []
        for c in cands:
            rows.append(
                {
                    "candidate_id": c.candidate_id,
                    "entity_id": c.entity_id,
                    "target_dataset": c.target_dataset,
                    "canonical_name": c.canonical_name,
                    "confidence": c.provenance.confidence,
                    "source_id": c.provenance.source_id,
                    "validation_status": c.provenance.validation_status,
                    "reviewer": c.provenance.reviewer,
                }
            )
        return rows

    datasets_affected = sorted(
        {
            c.target_dataset
            for c in (*pending, *approved, *rejected)
            if c.target_dataset
        }
    )

    confidences = [c.provenance.confidence for c in (*pending, *approved)]
    avg_conf = (
        round(sum(confidences) / len(confidences), 4) if confidences else None
    )

    return {
        "pending_count": len(pending),
        "approved_count": len(approved),
        "rejected_count": len(rejected),
        "pending": summarize(pending),
        "approved": summarize(approved),
        "rejected": summarize(rejected),
        "datasets_affected": datasets_affected,
        "average_confidence": avg_conf,
        "manifest_present": manifest is not None,
        "manifest_count": (manifest or {}).get("count"),
        "review_dir": str(review_dir.relative_to(root)),
    }


def build_markdown(ctx: RunContext, state: dict[str, Any]) -> str:
    lines = report_header(ctx, "Review Summary")
    lines += [
        "## Queue Snapshot",
        "",
        f"| Queue | Count |",
        f"| --- | ---: |",
        f"| Pending | {state['pending_count']} |",
        f"| Approved | {state['approved_count']} |",
        f"| Rejected | {state['rejected_count']} |",
        f"| Average confidence (pending+approved) | {state['average_confidence']} |",
        "",
        "## Datasets Affected",
        "",
    ]
    if state["datasets_affected"]:
        for ds in state["datasets_affected"]:
            lines.append(f"- `{ds}`")
    else:
        lines.append("- (none)")
    lines.append("")

    def section(title: str, rows: list[dict[str, Any]]) -> None:
        lines.append(f"## {title}")
        lines.append("")
        if not rows:
            lines.append("_Empty_")
            lines.append("")
            return
        lines.append("| Candidate | Dataset | Entity | Confidence | Status |")
        lines.append("| --- | --- | --- | ---: | --- |")
        for r in rows:
            lines.append(
                f"| `{r['candidate_id']}` | `{r['target_dataset']}` | "
                f"`{r['entity_id']}` | {r['confidence']} | {r['validation_status']} |"
            )
        lines.append("")

    section("Pending", state["pending"])
    section("Approved", state["approved"])
    section("Rejected", state["rejected"])

    lines += [
        "## Guardrails",
        "",
        "- This workflow does **not** publish.",
        "- Use `publish.yml` only after human approval.",
        f"- Review directory: `{state['review_dir']}`",
        "",
    ]
    return "\n".join(lines)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="IDA review summary CI job")
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
        name="review",
        repo_root=root,
        environment=environment,
        dry_run=dry_run,
        env_config=env_config,
    )

    state = collect_review_state(root, env_config)
    ctx.metrics = {
        "pending": state["pending_count"],
        "approved": state["approved_count"],
        "rejected": state["rejected_count"],
        "datasets_affected": len(state["datasets_affected"]),
        "average_confidence": state["average_confidence"],
    }
    ctx.finish(EXIT_SUCCESS)

    report_dir = root / env_config.get("paths", {}).get(
        "review_reports", "reports/review"
    )
    ts = stamp()
    md_path = report_dir / "review_summary.md"
    log_path = report_dir / f"review_{ts}.json"

    write_markdown_report(md_path, build_markdown(ctx, state), ctx)
    write_json_log(log_path, ctx, extra={"state": state})

    print(
        f"Review summary: pending={state['pending_count']} "
        f"approved={state['approved_count']} rejected={state['rejected_count']}"
    )
    print(f"Wrote {md_path}")
    return EXIT_SUCCESS


if __name__ == "__main__":
    raise SystemExit(main())
