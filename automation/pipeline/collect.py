"""Stage 2 — Document Collection.

Fetches raw documents from discovered sources.
Phase 1: placeholder collector — no network crawl.
Honors controller crawling_enabled and document limits.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from automation.lib.io_utils import utc_stamp, write_json
from automation.lib.models import PipelineStage, StageResult, utc_now_iso

if TYPE_CHECKING:
    from automation.lib.models import PipelineContext

STAGE = PipelineStage.COLLECT.value


def _placeholder_document(source: dict[str, Any], index: int) -> dict[str, Any]:
    """Synthetic document stub for architecture validation.

    Replace with search API / browser automation integrations later.
    """
    source_id = source.get("source_id", "SRC-UNKNOWN")
    base_url = source.get("base_url", "")
    return {
        "document_id": f"DOC-{source_id}-{index:04d}",
        "source_id": source_id,
        "source_url": f"{base_url.rstrip('/')}/placeholder/{index}",
        "title": f"Placeholder document {index} from {source.get('source_name')}",
        "content_type": "text/plain",
        "retrieved_at": utc_now_iso(),
        "local_path": None,
        "bytes": 0,
        "status": "placeholder",
        "notes": "Phase 1 placeholder — no external fetch performed.",
    }


def run(ctx: "PipelineContext") -> StageResult:
    controller = ctx.controller
    paths = ctx.paths
    sources = ctx.discovered_sources

    may, reason = controller.may_crawl()
    collected: list[dict[str, Any]] = []
    skipped_reason = None

    if not may:
        skipped_reason = reason
        # Stage is not skipped in the pipeline sense — it runs and records a no-op.
        result = StageResult(
            stage=STAGE,
            success=True,
            message=f"Collection gated by controller: {reason}",
            input_count=len(sources),
            output_count=0,
            details={"gated": True, "reason": reason},
        )
        ctx.collected_documents = []
        ctx.add_stage_result(result)
        return result

    # Phase 1: emit at most one placeholder document per discovered source
    for source in sources:
        if not controller.can_accept_documents(1):
            skipped_reason = "max_documents_reached"
            break
        doc = _placeholder_document(source, 1)
        # Persist raw placeholder metadata (not real content)
        raw_meta = paths.raw_documents / f"{doc['document_id']}.json"
        if not ctx.dry_run or True:
            write_json(raw_meta, doc)
            doc["local_path"] = str(raw_meta)
        collected.append(doc)
        controller.record_usage(documents=1)

    ctx.collected_documents = collected
    if ctx.report is not None:
        ctx.report.rows_collected = len(collected)

    artifact = paths.cache / f"{ctx.run_id}_collected_documents.json"
    write_json(
        artifact,
        {
            "run_id": ctx.run_id,
            "dry_run": ctx.dry_run,
            "documents": collected,
            "notes": skipped_reason,
        },
    )

    result = StageResult(
        stage=STAGE,
        success=True,
        message=f"Collected {len(collected)} document stub(s)",
        input_count=len(sources),
        output_count=len(collected),
        artifacts=[str(artifact)],
        details={"placeholder": True, "skipped_reason": skipped_reason},
    )
    ctx.add_stage_result(result)
    return result
