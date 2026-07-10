"""Stage 7 — Entity Linking.

Resolves references (company_id, industry_id, product_id, ...) against
existing domain datasets. Unresolved links are flagged per policy.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from automation.lib.io_utils import read_csv_rows, write_json
from automation.lib.models import PipelineStage, StageResult

if TYPE_CHECKING:
    from automation.lib.models import CandidateRecord, PipelineContext

STAGE = PipelineStage.ENTITY_LINK.value


def _index_dataset(ctx: "PipelineContext", filename_stem: str, id_column: str) -> dict[str, dict[str, str]]:
    index: dict[str, dict[str, str]] = {}
    for path in ctx.paths.domains_root.glob(f"**/{filename_stem}.csv"):
        for row in read_csv_rows(path):
            key = (row.get(id_column) or "").strip()
            if key:
                index[key] = row
    return index


def _lookup(
    indexes: dict[str, dict[str, dict[str, str]]],
    dataset: str,
    entity_id: Optional[str],
) -> Optional[dict[str, str]]:
    if not entity_id:
        return None
    return indexes.get(dataset, {}).get(entity_id)


def run(ctx: "PipelineContext") -> StageResult:
    paths = ctx.paths
    policies = ctx.config.get("policies", {})
    link_cfg = policies.get("entity_linking", {})
    enabled = bool(link_cfg.get("enabled", True))
    unresolved_policy = str(link_cfg.get("unresolved_policy", "flag"))
    link_fields = list(
        link_cfg.get("link_fields")
        or [
            "company_id",
            "industry_id",
            "product_id",
            "opportunity_id",
            "competitor_id",
        ]
    )

    field_to_dataset = {
        "company_id": ("company_profile", "Company ID"),
        "industry_id": ("industry_library", "Industry ID"),
        "product_id": ("product_catalog", "Product ID"),
        "opportunity_id": ("opportunity_analysis", "Opportunity ID"),
        "competitor_id": ("competitor_library", "Competitor ID"),
    }

    indexes: dict[str, dict[str, dict[str, str]]] = {}
    if enabled:
        for field in link_fields:
            mapping = field_to_dataset.get(field)
            if not mapping:
                continue
            stem, id_col = mapping
            indexes[stem] = _index_dataset(ctx, stem, id_col)

    linked = 0
    unresolved_total = 0
    rejected_for_links: list[Any] = []
    remaining: list[Any] = []

    for candidate in ctx.candidates:
        candidate.touch(STAGE)
        if not enabled:
            remaining.append(candidate)
            continue

        links: dict[str, Any] = dict(candidate.links or {})
        unresolved: list[str] = []

        # Attempt links from payload keys (various casings)
        payload = candidate.payload
        for field in link_fields:
            mapping = field_to_dataset.get(field)
            if not mapping:
                continue
            stem, _id_col = mapping
            # find value in payload under several key styles
            value = (
                payload.get(field)
                or payload.get(field.replace("_", " ").title())
                or payload.get(field.upper())
            )
            if not value:
                continue
            value_str = str(value).strip()
            row = _lookup(indexes, stem, value_str)
            if row is None:
                unresolved.append(field)
                links[field] = {
                    "id": value_str,
                    "resolved": False,
                }
            else:
                links[field] = {
                    "id": value_str,
                    "resolved": True,
                    "dataset": stem,
                }
                linked += 1

        candidate.links = links
        unresolved_total += len(unresolved)

        if unresolved and unresolved_policy == "reject":
            candidate.rejection_reasons = list(
                set(candidate.rejection_reasons + [f"unresolved_link:{u}" for u in unresolved])
            )
            rejected_for_links.append(candidate)
        else:
            if unresolved and unresolved_policy == "flag":
                candidate.metadata["unresolved_links"] = unresolved
            remaining.append(candidate)

    if unresolved_policy == "reject":
        from automation.lib.io_utils import save_candidate
        from automation.lib.models import ValidationStatus

        for cand in rejected_for_links:
            cand.provenance.validation_status = ValidationStatus.INVALID.value
            save_candidate(paths.queue_rejected, cand)
        if ctx.report is not None:
            ctx.report.rows_rejected += len(rejected_for_links)

    ctx.candidates = remaining

    artifact = paths.cache / f"{ctx.run_id}_entity_links.json"
    write_json(
        artifact,
        {
            "run_id": ctx.run_id,
            "enabled": enabled,
            "linked_fields": linked,
            "unresolved_total": unresolved_total,
            "unresolved_policy": unresolved_policy,
            "candidates": [
                {
                    "candidate_id": c.candidate_id,
                    "links": c.links,
                    "unresolved": c.metadata.get("unresolved_links", []),
                }
                for c in remaining
            ],
        },
    )

    result = StageResult(
        stage=STAGE,
        success=True,
        message=(
            f"Entity linking complete: {linked} resolved field(s), "
            f"{unresolved_total} unresolved"
        ),
        input_count=len(remaining) + len(rejected_for_links),
        output_count=len(remaining),
        rejected_count=len(rejected_for_links),
        artifacts=[str(artifact)],
        details={
            "enabled": enabled,
            "unresolved_policy": unresolved_policy,
        },
    )
    ctx.add_stage_result(result)
    return result
