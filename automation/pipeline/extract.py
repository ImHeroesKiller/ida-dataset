"""Stage 3 — Content Extraction.

Transforms collected documents into candidate knowledge rows.
Phase 1: placeholder extractor — no LLM / parser integration.
Honors controller extraction_enabled and row limits.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from automation.lib.io_utils import write_json
from automation.lib.models import (
    CandidateRecord,
    PipelineStage,
    Provenance,
    StageResult,
    utc_now_iso,
)

if TYPE_CHECKING:
    from automation.lib.models import PipelineContext

STAGE = PipelineStage.EXTRACT.value


def _placeholder_candidates(
    document: dict[str, Any],
    *,
    extraction_version: str,
    target_dataset: str,
) -> list[CandidateRecord]:
    """Create architecture-validation candidates without inventing domain facts.

    Payload intentionally empty of business claims — only structural placeholders
    with full provenance. Future extractors (LLM / rules) plug in here.
    """
    source_id = str(document.get("source_id", ""))
    source_url = str(document.get("source_url", ""))
    retrieved_at = str(document.get("retrieved_at") or utc_now_iso())
    entity_id = f"PLACEHOLDER-{document.get('document_id', 'UNKNOWN')}"

    provenance = Provenance(
        source_id=source_id,
        source_url=source_url,
        retrieved_at=retrieved_at,
        confidence=0.0,  # placeholder extraction has zero factual confidence
        extraction_version=extraction_version,
        validation_status="pending",
        reviewer=None,
        published_at=None,
    )

    candidate = CandidateRecord.create(
        entity_type=target_dataset,
        entity_id=entity_id,
        target_dataset=target_dataset,
        payload={
            # Domain fields intentionally omitted — no hallucinated facts.
            "placeholder": True,
            "document_id": document.get("document_id"),
            "title": document.get("title"),
        },
        provenance=provenance,
        canonical_name=str(document.get("title") or entity_id),
        metadata={
            "extraction_backend": "none",
            "phase": "1",
            "note": "Placeholder candidate; not suitable for publication.",
        },
    )
    candidate.touch(STAGE)
    return [candidate]


def run(ctx: "PipelineContext") -> StageResult:
    controller = ctx.controller
    paths = ctx.paths
    documents = ctx.collected_documents
    policies = ctx.config.get("policies", {})
    extraction_cfg = policies.get("extraction", {})
    extraction_version = str(extraction_cfg.get("version", "0.1.0-phase1"))
    targets = list(
        extraction_cfg.get("target_datasets") or ["company_profile"]
    )
    target_dataset = targets[0] if targets else "company_profile"

    may, reason = controller.may_extract()
    candidates: list[CandidateRecord] = []

    if not may:
        result = StageResult(
            stage=STAGE,
            success=True,
            message=f"Extraction gated by controller: {reason}",
            input_count=len(documents),
            output_count=0,
            details={"gated": True, "reason": reason},
        )
        ctx.candidates = []
        ctx.add_stage_result(result)
        return result

    for document in documents:
        if not controller.can_accept_rows(1):
            break
        # Phase 1 never fabricates real entities; still produces structure for pipeline test
        batch = _placeholder_candidates(
            document,
            extraction_version=extraction_version,
            target_dataset=target_dataset,
        )
        for cand in batch:
            candidates.append(cand)
            controller.record_usage(rows=1)

    ctx.candidates = candidates
    if ctx.report is not None:
        ctx.report.rows_extracted = len(candidates)

    artifact = paths.cache / f"{ctx.run_id}_extracted_candidates.json"
    write_json(
        artifact,
        {
            "run_id": ctx.run_id,
            "extraction_version": extraction_version,
            "backend": extraction_cfg.get("backend", "none"),
            "candidates": [c.to_dict() for c in candidates],
        },
    )

    result = StageResult(
        stage=STAGE,
        success=True,
        message=f"Extracted {len(candidates)} candidate stub(s)",
        input_count=len(documents),
        output_count=len(candidates),
        artifacts=[str(artifact)],
        details={
            "placeholder": True,
            "extraction_version": extraction_version,
            "backend": extraction_cfg.get("backend", "none"),
        },
    )
    ctx.add_stage_result(result)
    return result
