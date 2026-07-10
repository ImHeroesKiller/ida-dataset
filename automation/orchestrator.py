"""Pipeline orchestrator — runs stages in fixed order without skipping."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any, Optional, Sequence
from uuid import uuid4

# Ensure repository root is on sys.path when executed as a script
_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from automation.lib.config import load_config
from automation.lib.controller import HumanController
from automation.lib.io_utils import utc_stamp, write_json, write_text
from automation.lib.logging_utils import log_event, setup_logger
from automation.lib.models import PipelineContext, RunReport, utc_now_iso
from automation.lib.paths import RepoPaths
from automation.pipeline import STAGE_MODULES, STAGE_ORDER


def build_context(
    *,
    profile: str = "dry_run",
    dry_run: Optional[bool] = None,
    publish: Optional[bool] = None,
    overrides: Optional[dict[str, Any]] = None,
    root: Optional[Path] = None,
) -> PipelineContext:
    config = load_config(root=root)
    policies = config["policies"]
    paths = RepoPaths.from_policies(policies, root=root)
    paths.ensure()

    controller = HumanController(
        config=config,
        source_registry_path=paths.source_registry,
    )
    if overrides:
        controller.apply_overrides(overrides)

    scheduler = config.get("scheduler", {})
    profiles = scheduler.get("profiles") or {}
    profile_cfg = profiles.get(profile) or {}

    if dry_run is None:
        dry_run = bool(profile_cfg.get("dry_run", True))
    if publish is None:
        publish = bool(profile_cfg.get("publish", False))

    run_id = f"RUN-{utc_stamp()}-{uuid4().hex[:6].upper()}"
    report = RunReport(
        run_id=run_id,
        started_at=utc_now_iso(),
        profile=profile,
        dry_run=dry_run,
    )

    return PipelineContext(
        run_id=run_id,
        config=config,
        paths=paths,
        controller=controller,
        dry_run=dry_run,
        publish=publish,
        report=report,
    )


def resolve_stages(profile: str, config: dict[str, Any]) -> list[str]:
    scheduler = config.get("scheduler", {})
    profiles = scheduler.get("profiles") or {}
    profile_cfg = profiles.get(profile) or {}
    stages = list(profile_cfg.get("stages") or STAGE_ORDER)

    # Enforce fixed order: filter to known stages and sort by STAGE_ORDER index
    order_index = {name: i for i, name in enumerate(STAGE_ORDER)}
    unknown = [s for s in stages if s not in order_index]
    if unknown:
        raise ValueError(f"Unknown stages in profile '{profile}': {unknown}")
    stages_sorted = sorted(stages, key=lambda s: order_index[s])

    # Full pipeline profiles must not skip stages between first and last requested
    if profile in {"dry_run", "full_pipeline"}:
        if stages_sorted != STAGE_ORDER:
            raise ValueError(
                f"Profile '{profile}' must include all stages in order; got {stages_sorted}"
            )
    return stages_sorted


def run_pipeline(
    *,
    profile: str = "dry_run",
    dry_run: Optional[bool] = None,
    publish: Optional[bool] = None,
    overrides: Optional[dict[str, Any]] = None,
    root: Optional[Path] = None,
    stages: Optional[Sequence[str]] = None,
) -> PipelineContext:
    ctx = build_context(
        profile=profile,
        dry_run=dry_run,
        publish=publish,
        overrides=overrides,
        root=root,
    )
    logger = setup_logger(
        "ida.kas",
        ctx.paths.logs,
        run_id=ctx.run_id,
        level=str(
            ctx.config.get("policies", {}).get("logging", {}).get("level", "INFO")
        ),
    )

    stage_list = list(stages) if stages else resolve_stages(profile, ctx.config)

    log_event(
        logger,
        "pipeline_start",
        run_id=ctx.run_id,
        profile=profile,
        dry_run=ctx.dry_run,
        publish=ctx.publish,
        stages=stage_list,
        controller=ctx.controller.snapshot().to_dict(),
    )

    try:
        for stage_name in stage_list:
            module = STAGE_MODULES[stage_name]
            log_event(logger, "stage_start", stage=stage_name, run_id=ctx.run_id)
            result = module.run(ctx)
            log_event(
                logger,
                "stage_end",
                stage=stage_name,
                run_id=ctx.run_id,
                success=result.success,
                stage_message=result.message,
                input_count=result.input_count,
                output_count=result.output_count,
                rejected_count=result.rejected_count,
            )
            if not result.success:
                raise RuntimeError(f"Stage {stage_name} failed: {result.message}")
    finally:
        if ctx.report is not None:
            ctx.report.finished_at = utc_now_iso()
            report_path = ctx.paths.reports / f"run_{ctx.run_id}.json"
            write_json(report_path, ctx.report.to_dict())
            _write_daily_markdown(ctx)
            log_event(
                logger,
                "pipeline_end",
                run_id=ctx.run_id,
                report=str(report_path),
            )

    return ctx


def _write_daily_markdown(ctx: PipelineContext) -> None:
    """Generate human-readable daily report fragment."""
    if ctx.report is None:
        return
    r = ctx.report
    day = (r.started_at or utc_now_iso())[:10]
    path = ctx.paths.reports / f"daily_{day}.md"
    lines = [
        f"# Daily Report — {day}",
        "",
        f"## Run `{r.run_id}`",
        "",
        f"- Profile: `{r.profile}`",
        f"- Dry run: `{r.dry_run}`",
        f"- Started: {r.started_at}",
        f"- Finished: {r.finished_at}",
        "",
        "### Metrics",
        "",
        f"| Metric | Count |",
        f"| --- | ---: |",
        f"| Rows discovered | {r.rows_discovered} |",
        f"| Rows collected | {r.rows_collected} |",
        f"| Rows extracted | {r.rows_extracted} |",
        f"| Rows validated | {r.rows_validated} |",
        f"| Rows approved | {r.rows_approved} |",
        f"| Rows rejected | {r.rows_rejected} |",
        f"| Duplicates | {r.duplicates} |",
        "",
        "### Updated datasets",
        "",
    ]
    if r.updated_datasets:
        for ds in r.updated_datasets:
            lines.append(f"- `{ds}`")
    else:
        lines.append("- (none)")
    lines.append("")
    lines.append("### Stage results")
    lines.append("")
    for stage in r.stage_results:
        lines.append(
            f"- **{stage.get('stage')}**: {stage.get('message')} "
            f"(in={stage.get('input_count')}, out={stage.get('output_count')}, "
            f"rejected={stage.get('rejected_count')})"
        )
    lines.append("")
    # append if file exists
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    if existing:
        content = existing.rstrip() + "\n\n" + "\n".join(lines) + "\n"
    else:
        content = "\n".join(lines) + "\n"
    write_text(path, content)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ida-kas",
        description=(
            "IDA Knowledge Acquisition System — human-controlled pipeline. "
            "No stage may be skipped in full profiles."
        ),
    )
    sub = parser.add_subparsers(dest="command", required=True)

    run_p = sub.add_parser("run", help="Run a pipeline profile")
    run_p.add_argument(
        "--profile",
        default="dry_run",
        choices=["dry_run", "full_pipeline", "review_only", "publish_only"],
        help="Scheduler profile name",
    )
    run_p.add_argument(
        "--dry-run",
        action="store_true",
        default=None,
        help="Force dry-run mode",
    )
    run_p.add_argument(
        "--no-dry-run",
        action="store_true",
        help="Disable dry-run mode",
    )
    run_p.add_argument(
        "--publish",
        action="store_true",
        help="Allow publisher stage to write (still gated by policies)",
    )
    run_p.add_argument(
        "--enable-crawling",
        action="store_true",
        help="Runtime override: enable crawling",
    )
    run_p.add_argument(
        "--enable-extraction",
        action="store_true",
        help="Runtime override: enable extraction",
    )
    run_p.add_argument(
        "--enable-publishing",
        action="store_true",
        help="Runtime override: enable publishing",
    )
    run_p.add_argument(
        "--approval-mode",
        choices=["automatic", "semi_automatic", "manual"],
        help="Runtime override for approval mode",
    )
    run_p.add_argument(
        "--confidence-threshold",
        type=float,
        help="Runtime override for confidence threshold",
    )
    run_p.add_argument(
        "--max-documents",
        type=int,
        help="Runtime override for max documents",
    )
    run_p.add_argument(
        "--max-rows-per-day",
        type=int,
        help="Runtime override for max rows per day",
    )
    run_p.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Repository root (defaults to auto-detect)",
    )

    ctrl = sub.add_parser("controller", help="Show human controller snapshot")
    ctrl.add_argument("--root", type=Path, default=None)

    rev = sub.add_parser("review", help="Apply a human review decision")
    rev.add_argument("--candidate-id", required=True)
    rev.add_argument(
        "--action",
        required=True,
        choices=[
            "approve",
            "reject",
            "edit",
            "merge",
            "skip",
            "bulk_approve",
            "bulk_reject",
        ],
    )
    rev.add_argument("--reviewer", required=True)
    rev.add_argument("--reason", default="")
    rev.add_argument(
        "--ids",
        nargs="*",
        help="Additional candidate IDs for bulk actions",
    )
    rev.add_argument("--root", type=Path, default=None)

    sub.add_parser("stages", help="List pipeline stages in order")

    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    if args.command == "stages":
        for i, name in enumerate(STAGE_ORDER, 1):
            print(f"{i}. {name}")
        return 0

    if args.command == "controller":
        ctx = build_context(root=args.root)
        snap = ctx.controller.snapshot().to_dict()
        write_json  # keep import used
        import json

        print(json.dumps(snap, indent=2))
        return 0

    if args.command == "review":
        from automation.pipeline import reviewer as reviewer_mod

        ctx = build_context(profile="review_only", dry_run=False, root=args.root)
        if args.action in {"bulk_approve", "bulk_reject"}:
            ids = [args.candidate_id, *(args.ids or [])]
            results = reviewer_mod.bulk_apply(
                ctx,
                candidate_ids=ids,
                action=args.action,
                reviewer=args.reviewer,
                reason=args.reason,
            )
            import json

            print(json.dumps(results, indent=2))
        else:
            result = reviewer_mod.apply_decision(
                ctx,
                candidate_id=args.candidate_id,
                action=args.action,
                reviewer=args.reviewer,
                reason=args.reason,
            )
            import json

            print(json.dumps(result, indent=2))
        return 0

    if args.command == "run":
        dry_run: Optional[bool]
        if args.no_dry_run:
            dry_run = False
        elif args.dry_run:
            dry_run = True
        else:
            dry_run = None

        overrides: dict[str, Any] = {}
        if args.enable_crawling:
            overrides["crawling_enabled"] = True
        if args.enable_extraction:
            overrides["extraction_enabled"] = True
        if args.enable_publishing:
            overrides["publishing_enabled"] = True
        if args.approval_mode:
            overrides["approval_mode"] = args.approval_mode
        if args.confidence_threshold is not None:
            overrides["confidence_threshold"] = args.confidence_threshold
        if args.max_documents is not None:
            overrides["max_documents"] = args.max_documents
        if args.max_rows_per_day is not None:
            overrides["max_rows_per_day"] = args.max_rows_per_day

        ctx = run_pipeline(
            profile=args.profile,
            dry_run=dry_run,
            publish=bool(args.publish),
            overrides=overrides or None,
            root=args.root,
        )
        print(f"Run complete: {ctx.run_id}")
        if ctx.report:
            print(
                f"discovered={ctx.report.rows_discovered} "
                f"collected={ctx.report.rows_collected} "
                f"extracted={ctx.report.rows_extracted} "
                f"validated={ctx.report.rows_validated} "
                f"approved={ctx.report.rows_approved} "
                f"rejected={ctx.report.rows_rejected} "
                f"duplicates={ctx.report.duplicates}"
            )
        return 0

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
