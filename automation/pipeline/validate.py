"""Stage 5 — Validation.

Rejects candidates that fail trust, confidence, schema, URL, or reference checks.
Rejected records are written to automation/queue/rejected/.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any, Optional
from urllib.parse import urlparse

from automation.lib.io_utils import read_csv_headers, save_candidate, write_json
from automation.lib.models import PipelineStage, StageResult, ValidationStatus

if TYPE_CHECKING:
    from automation.lib.models import CandidateRecord, PipelineContext

STAGE = PipelineStage.VALIDATE.value


def _parse_iso(ts: str) -> Optional[datetime]:
    if not ts:
        return None
    try:
        # support trailing Z
        cleaned = ts.replace("Z", "+00:00")
        return datetime.fromisoformat(cleaned)
    except ValueError:
        return None


def _url_looks_valid(url: str) -> bool:
    if not url:
        return False
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return False
    if not parsed.netloc:
        return False
    # Phase 1: structural check only (no network HEAD)
    return True


def _dataset_path(ctx: "PipelineContext", target_dataset: str) -> Any:
    # Prefer business_development domain for BD libraries
    domains = ctx.paths.domains_root
    preferred = domains / "business_development" / f"{target_dataset}.csv"
    if preferred.exists():
        return preferred
    # search other domains
    matches = list(domains.glob(f"**/{target_dataset}.csv"))
    return matches[0] if matches else preferred


def _validate_one(ctx: "PipelineContext", candidate: "CandidateRecord") -> list[str]:
    policies = ctx.config.get("policies", {})
    rules = policies.get("validation", {})
    reasons: list[str] = []

    # Controller-level trust / confidence / domain
    reasons.extend(ctx.controller.evaluate_candidate_for_rejection(candidate))

    # Required fields
    if rules.get("reject_missing_required_fields", True):
        required = list(rules.get("required_fields") or [])
        snapshot = {
            "entity_type": candidate.entity_type,
            "entity_id": candidate.entity_id,
            "source_id": candidate.provenance.source_id,
            "source_url": candidate.provenance.source_url,
            "retrieved_at": candidate.provenance.retrieved_at,
            "confidence": candidate.provenance.confidence,
            "extraction_version": candidate.provenance.extraction_version,
        }
        for field in required:
            value = snapshot.get(field)
            if value is None or value == "":
                reasons.append(f"missing_required_field:{field}")

    # Broken URL (structural)
    if rules.get("reject_broken_url", True):
        if not _url_looks_valid(candidate.provenance.source_url):
            reasons.append("broken_url")

    # Outdated information
    if rules.get("reject_outdated", True):
        max_age = int(rules.get("outdated_after_days", 365))
        retrieved = _parse_iso(candidate.provenance.retrieved_at)
        if retrieved is None:
            reasons.append("outdated_or_invalid_retrieved_at")
        else:
            if retrieved.tzinfo is None:
                retrieved = retrieved.replace(tzinfo=timezone.utc)
            age_days = (datetime.now(timezone.utc) - retrieved).days
            if age_days > max_age:
                reasons.append("outdated_information")

    # Schema mismatch — payload keys that are not in target CSV headers are flagged
    # only when the target has a non-empty schema beyond provenance columns.
    if rules.get("reject_schema_mismatch", True):
        dataset_file = _dataset_path(ctx, candidate.target_dataset)
        headers = read_csv_headers(dataset_file)
        if headers:
            # Allow provenance + internal keys; domain keys must match if present
            internal = {
                "placeholder",
                "document_id",
                "title",
                "source_id",
                "source_url",
                "retrieved_at",
                "confidence",
                "extraction_version",
                "validation_status",
                "reviewer",
                "published_at",
            }
            header_set = set(headers)
            unknown = [
                k
                for k in candidate.payload.keys()
                if k not in header_set and k not in internal
            ]
            # Placeholder-only payloads are not schema-mismatched domain rows;
            # they fail later on confidence / publish gates instead.
            if unknown and not candidate.payload.get("placeholder"):
                reasons.append(f"schema_mismatch:{','.join(sorted(unknown))}")

    # Invalid references in links (if already present)
    if rules.get("reject_invalid_references", True):
        for key, value in (candidate.links or {}).items():
            if value in (None, "", [], {}):
                reasons.append(f"invalid_reference:{key}")

    # No trusted source already covered by controller; reinforce policy flag
    if rules.get("require_trusted_source", True):
        if "no_trusted_source" not in reasons and not ctx.controller.is_source_trusted(
            candidate.provenance.source_id
        ):
            reasons.append("no_trusted_source")

    if rules.get("reject_below_confidence", True):
        if not ctx.controller.passes_confidence(candidate.provenance.confidence):
            if "confidence_below_threshold" not in reasons:
                reasons.append("confidence_below_threshold")

    return sorted(set(reasons))


def run(ctx: "PipelineContext") -> StageResult:
    paths = ctx.paths
    valid: list = []
    rejected: list = []

    for candidate in ctx.candidates:
        reasons = _validate_one(ctx, candidate)
        candidate.touch(STAGE)
        if reasons:
            candidate.rejection_reasons = reasons
            candidate.provenance.validation_status = ValidationStatus.INVALID.value
            rejected.append(candidate)
            save_candidate(paths.queue_rejected, candidate)
        else:
            candidate.provenance.validation_status = ValidationStatus.VALID.value
            valid.append(candidate)

    ctx.candidates = valid
    if ctx.report is not None:
        ctx.report.rows_validated = len(valid)
        ctx.report.rows_rejected += len(rejected)

    artifact = paths.cache / f"{ctx.run_id}_validation.json"
    write_json(
        artifact,
        {
            "run_id": ctx.run_id,
            "valid": [c.candidate_id for c in valid],
            "rejected": [
                {
                    "candidate_id": c.candidate_id,
                    "reasons": c.rejection_reasons,
                }
                for c in rejected
            ],
        },
    )

    result = StageResult(
        stage=STAGE,
        success=True,
        message=f"Validated {len(valid)} candidate(s); rejected {len(rejected)}",
        input_count=len(valid) + len(rejected),
        output_count=len(valid),
        rejected_count=len(rejected),
        artifacts=[str(artifact)],
    )
    ctx.add_stage_result(result)
    return result
