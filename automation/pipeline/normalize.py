"""Stage 4 — Normalization.

Standardizes candidate payloads: casing, whitespace, ID formats, field names.
Does not invent data. Operates only on existing candidate fields.
"""

from __future__ import annotations

import re
from typing import TYPE_CHECKING, Any

from automation.lib.io_utils import write_json
from automation.lib.models import PipelineStage, StageResult

if TYPE_CHECKING:
    from automation.lib.models import PipelineContext

STAGE = PipelineStage.NORMALIZE.value


def _collapse_ws(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def _normalize_value(value: Any) -> Any:
    if isinstance(value, str):
        return _collapse_ws(value)
    if isinstance(value, dict):
        return {str(k).strip(): _normalize_value(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_normalize_value(v) for v in value]
    return value


def _normalize_entity_id(entity_id: str) -> str:
    cleaned = _collapse_ws(entity_id).upper().replace(" ", "-")
    cleaned = re.sub(r"[^A-Z0-9_\-]", "", cleaned)
    return cleaned


def run(ctx: "PipelineContext") -> StageResult:
    paths = ctx.paths
    normalized_count = 0

    for candidate in ctx.candidates:
        candidate.entity_id = _normalize_entity_id(candidate.entity_id)
        candidate.entity_type = _collapse_ws(candidate.entity_type).lower().replace(
            " ", "_"
        )
        candidate.target_dataset = _collapse_ws(
            candidate.target_dataset
        ).lower().replace(" ", "_")
        candidate.canonical_name = _collapse_ws(candidate.canonical_name)
        candidate.payload = _normalize_value(candidate.payload)

        # Normalize provenance URL whitespace only — do not rewrite host/path
        if candidate.provenance.source_url:
            candidate.provenance.source_url = candidate.provenance.source_url.strip()
        if candidate.provenance.source_id:
            candidate.provenance.source_id = _collapse_ws(
                candidate.provenance.source_id
            ).upper()

        candidate.touch(STAGE)
        normalized_count += 1

    if ctx.report is not None:
        ctx.report.rows_normalized = normalized_count

    artifact = paths.cache / f"{ctx.run_id}_normalized_candidates.json"
    write_json(
        artifact,
        {
            "run_id": ctx.run_id,
            "count": normalized_count,
            "candidates": [c.to_dict() for c in ctx.candidates],
        },
    )

    result = StageResult(
        stage=STAGE,
        success=True,
        message=f"Normalized {normalized_count} candidate(s)",
        input_count=normalized_count,
        output_count=normalized_count,
        artifacts=[str(artifact)],
    )
    ctx.add_stage_result(result)
    return result
