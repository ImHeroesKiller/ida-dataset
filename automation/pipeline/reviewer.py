"""Stage 8 — Human Review Queue.

Every candidate is placed in the review surface before publishing.
Supports approve / reject / edit / merge / skip / bulk actions.
No automatic publishing unless controller.auto_approve_allowed().
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING, Any, Iterable, Optional, Sequence

from automation.lib.io_utils import (
    load_candidate,
    load_candidates,
    move_candidate,
    save_candidate,
    write_json,
)
from automation.lib.models import (
    PipelineStage,
    ReviewAction,
    StageResult,
    ValidationStatus,
    utc_now_iso,
)

if TYPE_CHECKING:
    from automation.lib.models import CandidateRecord, PipelineContext

STAGE = PipelineStage.REVIEWER.value


def _review_index_path(review_dir: Path) -> Path:
    return review_dir / "review_queue.json"


def _decisions_path(review_dir: Path) -> Path:
    return review_dir / "decisions.jsonl"


def _write_review_manifest(
    review_dir: Path,
    candidates: Sequence["CandidateRecord"],
    *,
    run_id: str,
) -> Path:
    """Human-readable review queue index."""
    items = []
    for c in candidates:
        items.append(
            {
                "candidate_id": c.candidate_id,
                "entity_type": c.entity_type,
                "entity_id": c.entity_id,
                "target_dataset": c.target_dataset,
                "canonical_name": c.canonical_name,
                "confidence": c.provenance.confidence,
                "source_id": c.provenance.source_id,
                "source_url": c.provenance.source_url,
                "validation_status": c.provenance.validation_status,
                "payload_preview": c.payload,
                "links": c.links,
                "actions": [a.value for a in ReviewAction],
                "queue_file": f"../queue/pending/{c.candidate_id}.json",
            }
        )
    path = _review_index_path(review_dir)
    write_json(
        path,
        {
            "run_id": run_id,
            "generated_at": utc_now_iso(),
            "count": len(items),
            "instructions": {
                "approve": "Move candidate to queue/approved after human confirmation",
                "reject": "Move candidate to queue/rejected with reason",
                "edit": "Modify payload fields then approve",
                "merge": "Merge into an existing entity then reject duplicate",
                "skip": "Leave in pending for a later review cycle",
                "bulk_approve": "Approve all listed candidate_ids",
                "bulk_reject": "Reject all listed candidate_ids",
            },
            "items": items,
        },
    )
    return path


def enqueue_for_review(
    ctx: "PipelineContext",
    candidates: Sequence["CandidateRecord"],
) -> list[Path]:
    paths = []
    for candidate in candidates:
        candidate.provenance.validation_status = ValidationStatus.PENDING.value
        candidate.touch(STAGE)
        path = save_candidate(ctx.paths.queue_pending, candidate)
        paths.append(path)
    return paths


def apply_decision(
    ctx: "PipelineContext",
    *,
    candidate_id: str,
    action: str | ReviewAction,
    reviewer: str,
    reason: str = "",
    edits: Optional[dict[str, Any]] = None,
    merge_into: Optional[str] = None,
) -> dict[str, Any]:
    """Apply a single human review decision. Returns decision audit record."""
    action_value = action.value if isinstance(action, ReviewAction) else str(action)
    pending_path = ctx.paths.queue_pending / f"{candidate_id}.json"
    if not pending_path.exists():
        return {
            "ok": False,
            "candidate_id": candidate_id,
            "error": "not_found_in_pending",
        }

    candidate = load_candidate(pending_path)
    candidate.provenance.reviewer = reviewer
    candidate.touch(STAGE)
    candidate.metadata["review_action"] = action_value
    candidate.metadata["review_reason"] = reason
    candidate.metadata["reviewed_at"] = utc_now_iso()

    if action_value in {ReviewAction.EDIT.value, "edit"} and edits:
        candidate.payload.update(edits)
        candidate.metadata["edited_fields"] = sorted(edits.keys())

    if action_value in {ReviewAction.MERGE.value, "merge"}:
        candidate.metadata["merge_into"] = merge_into
        candidate.rejection_reasons = list(
            set(candidate.rejection_reasons + ["merged"])
        )
        candidate.provenance.validation_status = ValidationStatus.REJECTED.value
        save_candidate(ctx.paths.queue_rejected, candidate)
        pending_path.unlink(missing_ok=True)
        status = "rejected_merged"
    elif action_value in {
        ReviewAction.APPROVE.value,
        ReviewAction.BULK_APPROVE.value,
        "approve",
        "bulk_approve",
    }:
        candidate.provenance.validation_status = ValidationStatus.APPROVED.value
        save_candidate(ctx.paths.queue_approved, candidate)
        pending_path.unlink(missing_ok=True)
        status = "approved"
    elif action_value in {
        ReviewAction.REJECT.value,
        ReviewAction.BULK_REJECT.value,
        "reject",
        "bulk_reject",
    }:
        if reason:
            candidate.rejection_reasons = list(
                set(candidate.rejection_reasons + [reason])
            )
        candidate.provenance.validation_status = ValidationStatus.REJECTED.value
        save_candidate(ctx.paths.queue_rejected, candidate)
        pending_path.unlink(missing_ok=True)
        status = "rejected"
    elif action_value in {ReviewAction.SKIP.value, "skip"}:
        save_candidate(ctx.paths.queue_pending, candidate)
        status = "skipped"
    else:
        return {
            "ok": False,
            "candidate_id": candidate_id,
            "error": f"unknown_action:{action_value}",
        }

    decision = {
        "ok": True,
        "candidate_id": candidate_id,
        "action": action_value,
        "reviewer": reviewer,
        "reason": reason,
        "status": status,
        "decided_at": utc_now_iso(),
    }
    # append audit trail
    decisions = _decisions_path(ctx.paths.review)
    decisions.parent.mkdir(parents=True, exist_ok=True)
    with decisions.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(decision, ensure_ascii=False) + "\n")
    return decision


def bulk_apply(
    ctx: "PipelineContext",
    *,
    candidate_ids: Iterable[str],
    action: str,
    reviewer: str,
    reason: str = "",
) -> list[dict[str, Any]]:
    results = []
    for cid in candidate_ids:
        results.append(
            apply_decision(
                ctx,
                candidate_id=cid,
                action=action,
                reviewer=reviewer,
                reason=reason,
            )
        )
    return results


def run(ctx: "PipelineContext") -> StageResult:
    """Enqueue candidates for human review (or auto-approve if explicitly allowed)."""
    paths = ctx.paths
    controller = ctx.controller
    candidates = list(ctx.candidates)

    approved_count = 0
    pending_count = 0
    auto = controller.auto_approve_allowed()

    if auto:
        for candidate in candidates:
            candidate.provenance.validation_status = ValidationStatus.APPROVED.value
            candidate.provenance.reviewer = "auto"
            candidate.metadata["review_action"] = ReviewAction.APPROVE.value
            candidate.metadata["auto_approved"] = True
            candidate.touch(STAGE)
            save_candidate(paths.queue_approved, candidate)
            approved_count += 1
        manifest = None
        message = f"Auto-approved {approved_count} candidate(s) (approval_mode=automatic)"
    else:
        # Always human review path by default
        enqueue_for_review(ctx, candidates)
        pending_count = len(candidates)
        manifest = _write_review_manifest(
            paths.review, candidates, run_id=ctx.run_id
        )
        message = (
            f"Queued {pending_count} candidate(s) for human review "
            f"(mode={controller.approval_mode()}, review_required={controller.review_required()})"
        )

    if ctx.report is not None:
        ctx.report.rows_approved += approved_count

    # Also list anything already pending from prior runs
    existing_pending = load_candidates(paths.queue_pending)
    existing_approved = load_candidates(paths.queue_approved)

    artifact = paths.cache / f"{ctx.run_id}_review.json"
    write_json(
        artifact,
        {
            "run_id": ctx.run_id,
            "auto_approve": auto,
            "newly_pending": pending_count,
            "newly_approved": approved_count,
            "queue_pending_total": len(existing_pending),
            "queue_approved_total": len(existing_approved),
            "manifest": str(manifest) if manifest else None,
            "supported_actions": [a.value for a in ReviewAction],
        },
    )

    # Candidates leave in-memory flow here; publisher reads from approved queue
    ctx.candidates = []
    ctx.state["review_manifest"] = str(manifest) if manifest else None

    result = StageResult(
        stage=STAGE,
        success=True,
        message=message,
        input_count=pending_count + approved_count,
        output_count=pending_count + approved_count,
        artifacts=[str(artifact)] + ([str(manifest)] if manifest else []),
        details={
            "auto_approve": auto,
            "approval_mode": controller.approval_mode(),
            "review_required": controller.review_required(),
        },
    )
    ctx.add_stage_result(result)
    return result
