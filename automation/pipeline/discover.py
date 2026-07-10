"""Stage 1 — Source Discovery.

Identifies trusted sources eligible for acquisition in this run.
No network I/O in Phase 1; reads configuration + source registry only.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from automation.lib.io_utils import utc_stamp, write_json
from automation.lib.models import PipelineStage, StageResult

if TYPE_CHECKING:
    from automation.lib.models import PipelineContext

STAGE = PipelineStage.DISCOVER.value


def run(ctx: "PipelineContext") -> StageResult:
    """Discover allowed, trusted sources for the run."""
    controller = ctx.controller
    paths = ctx.paths

    trusted = controller.trusted_sources()
    max_sources = int(
        ctx.config.get("policies", {})
        .get("limits", {})
        .get("max_sources_per_run", 10)
    )
    selected = trusted[:max_sources]

    discovered = []
    for row in selected:
        source_id = row.get("Source ID", "")
        base_url = row.get("Base URL", "")
        if base_url and not controller.is_domain_allowed(base_url):
            continue
        discovered.append(
            {
                "source_id": source_id,
                "source_name": row.get("Source Name", ""),
                "base_url": base_url,
                "category": row.get("Category", ""),
                "country": row.get("Country", ""),
                "trust_score": row.get("Trust Score", ""),
                "update_frequency": row.get("Update Frequency", ""),
                "status": row.get("Status", ""),
                "allowed": row.get("Allowed", ""),
                "discovered_at": utc_stamp(),
                "stage": STAGE,
            }
        )

    ctx.discovered_sources = discovered
    if ctx.report is not None:
        ctx.report.rows_discovered = len(discovered)

    artifact = paths.cache / f"{ctx.run_id}_discovered_sources.json"
    if not ctx.dry_run:
        write_json(artifact, {"run_id": ctx.run_id, "sources": discovered})
    else:
        # dry-run still writes cache artifact for reproducibility of the plan
        write_json(
            artifact,
            {
                "run_id": ctx.run_id,
                "dry_run": True,
                "sources": discovered,
            },
        )

    result = StageResult(
        stage=STAGE,
        success=True,
        message=f"Discovered {len(discovered)} trusted source(s)",
        input_count=len(trusted),
        output_count=len(discovered),
        artifacts=[str(artifact)],
        details={"source_ids": [s["source_id"] for s in discovered]},
    )
    ctx.add_stage_result(result)
    return result
