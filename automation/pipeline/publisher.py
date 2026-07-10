"""Stage 9 — Publishing.

Append-only publication of approved candidates into domains/.
Never overwrites existing data. Always preserves IDs.
Always creates git-diff snapshot and a publish report.
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any

from automation.lib.io_utils import (
    append_csv_rows,
    git_diff_stat,
    git_status_porcelain,
    load_candidates,
    read_csv_headers,
    save_candidate,
    write_json,
)
from automation.lib.models import (
    PipelineStage,
    StageResult,
    ValidationStatus,
    utc_now_iso,
)

if TYPE_CHECKING:
    from automation.lib.models import CandidateRecord, PipelineContext

STAGE = PipelineStage.PUBLISHER.value


def _resolve_target_csv(ctx: "PipelineContext", target_dataset: str) -> Path:
    domains = ctx.paths.domains_root
    preferred = domains / "business_development" / f"{target_dataset}.csv"
    if preferred.exists() or preferred.parent.exists():
        return preferred
    matches = list(domains.glob(f"**/{target_dataset}.csv"))
    if matches:
        return matches[0]
    # default landing zone for new datasets under business_development
    preferred.parent.mkdir(parents=True, exist_ok=True)
    return preferred


def _row_for_dataset(candidate: "CandidateRecord", headers: list[str]) -> dict[str, Any]:
    """Build a publish row: domain payload + mandatory provenance columns."""
    row = candidate.with_provenance_on_payload()
    # If the target CSV has headers, only emit those columns (append_csv also enforces)
    if headers:
        return {h: row.get(h, candidate.payload.get(h, "")) for h in headers}
    return row


def run(ctx: "PipelineContext") -> StageResult:
    paths = ctx.paths
    controller = ctx.controller
    policies = ctx.config.get("policies", {})
    publishing = policies.get("publishing", {})

    may, reason = controller.may_publish()
    # Explicit orchestrator publish flag also required
    if not ctx.publish and not controller.is_publishing_enabled():
        may = False
        reason = reason if reason != "ok" else "publish_flag_false"

    # Schedule gate: only immediate or manual with explicit publish
    schedule = controller.publishing_schedule()
    if may and schedule not in {"immediate", "manual"}:
        # daily/weekly schedules defer unless orchestrator forces publish
        if not ctx.publish:
            may = False
            reason = f"schedule_deferred:{schedule}"

    approved = load_candidates(paths.queue_approved)
    if not may:
        result = StageResult(
            stage=STAGE,
            success=True,
            message=f"Publishing gated: {reason} ({len(approved)} approved waiting)",
            input_count=len(approved),
            output_count=0,
            details={"gated": True, "reason": reason, "schedule": schedule},
        )
        ctx.add_stage_result(result)
        return result

    if ctx.dry_run:
        result = StageResult(
            stage=STAGE,
            success=True,
            message=f"Dry-run publish: would append {len(approved)} row(s)",
            input_count=len(approved),
            output_count=0,
            details={"dry_run": True, "candidate_ids": [c.candidate_id for c in approved]},
        )
        artifact = paths.cache / f"{ctx.run_id}_publish_dry_run.json"
        write_json(
            artifact,
            {
                "run_id": ctx.run_id,
                "dry_run": True,
                "approved": [c.to_dict() for c in approved],
            },
        )
        result.artifacts = [str(artifact)]
        ctx.add_stage_result(result)
        return result

    published: list[dict[str, Any]] = []
    updated_datasets: set[str] = set()
    skipped: list[dict[str, Any]] = []

    # never_overwrite is always true by design
    assert publishing.get("never_overwrite", True) is True
    assert publishing.get("mode", "append_only") == "append_only"

    for candidate in approved:
        if not controller.can_accept_updates(1):
            skipped.append(
                {
                    "candidate_id": candidate.candidate_id,
                    "reason": "max_updates_per_day_reached",
                }
            )
            continue

        # Refuse to publish placeholder / zero-confidence rows even if approved
        if candidate.payload.get("placeholder") or candidate.provenance.confidence <= 0:
            skipped.append(
                {
                    "candidate_id": candidate.candidate_id,
                    "reason": "placeholder_or_zero_confidence",
                }
            )
            continue

        # Provenance mandatory
        prov = candidate.provenance
        if not all(
            [
                prov.source_id,
                prov.source_url,
                prov.retrieved_at,
                prov.extraction_version,
            ]
        ):
            skipped.append(
                {
                    "candidate_id": candidate.candidate_id,
                    "reason": "missing_provenance",
                }
            )
            continue

        target = _resolve_target_csv(ctx, candidate.target_dataset)
        headers = read_csv_headers(target)

        # Ensure provenance columns exist when creating a brand-new file
        if not headers:
            # Prefer payload keys + provenance
            headers = list(candidate.payload.keys()) + [
                "source_id",
                "source_url",
                "retrieved_at",
                "confidence",
                "extraction_version",
                "validation_status",
                "reviewer",
                "published_at",
            ]

        candidate.provenance.published_at = utc_now_iso()
        candidate.provenance.validation_status = ValidationStatus.PUBLISHED.value
        candidate.touch(STAGE)

        row = _row_for_dataset(candidate, headers)
        # preserve IDs: never rewrite entity_id in payload if already set
        append_csv_rows(target, [row], fieldnames=headers)

        updated_datasets.add(str(target.relative_to(paths.root)))
        controller.record_usage(updates=1)
        published.append(
            {
                "candidate_id": candidate.candidate_id,
                "entity_id": candidate.entity_id,
                "target": str(target.relative_to(paths.root)),
                "published_at": candidate.provenance.published_at,
            }
        )

        # Move out of approved queue into a published archive under review/
        archive_dir = paths.review / "published"
        save_candidate(archive_dir, candidate)
        approved_path = paths.queue_approved / f"{candidate.candidate_id}.json"
        approved_path.unlink(missing_ok=True)

    if ctx.report is not None:
        ctx.report.updated_datasets = sorted(updated_datasets)

    # Always generate git diff snapshot + report
    diff_stat = git_diff_stat(paths.root)
    status = git_status_porcelain(paths.root)
    publish_report = {
        "run_id": ctx.run_id,
        "published_at": utc_now_iso(),
        "published_count": len(published),
        "skipped": skipped,
        "updated_datasets": sorted(updated_datasets),
        "git_diff_stat": diff_stat,
        "git_status": status,
        "items": published,
        "mode": "append_only",
        "never_overwrite": True,
        "preserve_ids": True,
    }
    report_path = paths.reports / f"publish_{ctx.run_id}.json"
    write_json(report_path, publish_report)

    cache_path = paths.cache / f"{ctx.run_id}_publish.json"
    write_json(cache_path, publish_report)

    result = StageResult(
        stage=STAGE,
        success=True,
        message=(
            f"Published {len(published)} row(s) across "
            f"{len(updated_datasets)} dataset(s); skipped {len(skipped)}"
        ),
        input_count=len(approved),
        output_count=len(published),
        artifacts=[str(report_path), str(cache_path)],
        details={
            "updated_datasets": sorted(updated_datasets),
            "skipped": skipped,
        },
    )
    ctx.add_stage_result(result)
    return result
