"""Dataset Quality Engine — completeness, confidence, enrichment disposition.

Additive only:
- Does not mutate domain CSV schemas
- Does not rewrite frozen pipeline stages
- Quality metadata attaches to CandidateRecord.metadata["quality"] or sidecars

Usage:
    from automation.knowledge.quality import assess_row, assess_candidate

    qa = assess_row("company_profile", {"Company Name": "Acme", "Industry": "Banking"})
    # qa.completeness, qa.disposition → publish | enrichment_queue | reject
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping, Optional, Sequence, Union

from automation.knowledge.mandatory_fields import (
    load_quality_config,
    mandatory_fields_for,
    thresholds,
)
from automation.knowledge.models import (
    EnrichmentStatus,
    FieldPresence,
    PublishDisposition,
    QualityAssessment,
    QualityValidationStatus,
)
from automation.lib.paths import find_repo_root

try:
    from automation.lib.models import CandidateRecord
except Exception:  # noqa: BLE001
    CandidateRecord = Any  # type: ignore


def _empty_tokens(repo_root: Optional[Path] = None) -> set[str]:
    cfg = load_quality_config(repo_root)
    comp = cfg.get("completeness") or {}
    tokens = comp.get("empty_tokens") if isinstance(comp, dict) else None
    if isinstance(tokens, list) and tokens:
        return {str(t) for t in tokens}
    return {"", "-", "n/a", "N/A", "unknown", "Unknown", "null", "None"}


def _ignore_fields(repo_root: Optional[Path] = None) -> set[str]:
    cfg = load_quality_config(repo_root)
    comp = cfg.get("completeness") or {}
    ign = comp.get("ignore_fields") if isinstance(comp, dict) else None
    if isinstance(ign, list):
        return {str(x) for x in ign}
    return {
        "Notes",
        "Last Updated",
        "Data Sources",
        "Data Source",
        "extraction_version",
        "validation_status",
        "reviewer",
        "published_at",
        "source_id",
        "source_url",
        "retrieved_at",
        "confidence",
    }


def is_empty(value: Any, *, empty_tokens: Optional[set[str]] = None) -> bool:
    """True when value is missing for completeness scoring."""
    if value is None:
        return True
    if isinstance(value, (list, dict)):
        return len(value) == 0
    s = str(value).strip()
    tokens = empty_tokens if empty_tokens is not None else _empty_tokens()
    return s in tokens


def _dataset_headers(
    target_dataset: str,
    *,
    repo_root: Optional[Path] = None,
) -> list[str]:
    root = repo_root or find_repo_root()
    path = root / "domains" / "business_development" / f"{target_dataset}.csv"
    if not path.exists():
        matches = list((root / "domains").glob(f"**/{target_dataset}.csv"))
        path = matches[0] if matches else path
    if not path.exists():
        return []
    try:
        import csv

        with path.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.reader(f)
            row = next(reader, None)
            return [c.strip() for c in (row or []) if c.strip()]
    except Exception:  # noqa: BLE001
        return []


def _payload_lookup(payload: Mapping[str, Any], field: str) -> Any:
    """Case-sensitive first, then case-insensitive key match."""
    if field in payload:
        return payload[field]
    lower = field.lower()
    for k, v in payload.items():
        if str(k).lower() == lower:
            return v
    return None


def _tracked_fields(
    target_dataset: str,
    *,
    repo_root: Optional[Path] = None,
) -> list[str]:
    """Optional fields counted even when empty (operator completeness view)."""
    cfg = load_quality_config(repo_root)
    block = cfg.get("tracked_fields") or {}
    if isinstance(block, dict):
        raw = block.get(target_dataset)
        if isinstance(raw, list):
            return [str(x).strip() for x in raw if str(x).strip()]
    return []


def score_completeness(
    target_dataset: str,
    payload: Mapping[str, Any],
    *,
    scored_field_names: Optional[Sequence[str]] = None,
    repo_root: Optional[Path] = None,
) -> tuple[float, list[FieldPresence], int, int]:
    """Return (completeness 0–1, field observations, filled, scored).

    Scored set (default) = mandatory ∪ payload keys ∪ tracked_fields.
    Does **not** penalize every empty CSV column never attempted.
    """
    root = repo_root or find_repo_root()
    empty = _empty_tokens(root)
    ignore = _ignore_fields(root)
    mandatory = set(mandatory_fields_for(target_dataset, repo_root=root))

    if scored_field_names:
        fields = [f for f in scored_field_names if f and f not in ignore]
    else:
        fields: list[str] = []
        seen: set[str] = set()

        def _add(name: str) -> None:
            n = (name or "").strip()
            if not n or n in ignore or n in seen:
                return
            seen.add(n)
            fields.append(n)

        for m in mandatory:
            _add(m)
        for k in payload.keys():
            _add(str(k))
        for t in _tracked_fields(target_dataset, repo_root=root):
            _add(t)
        # If still empty, fall back to dataset headers (edge case)
        if not fields:
            for h in _dataset_headers(target_dataset, repo_root=root):
                _add(h)

    observations: list[FieldPresence] = []
    filled = 0
    for name in fields:
        val = _payload_lookup(payload, name)
        present = not is_empty(val, empty_tokens=empty)
        if present:
            filled += 1
        preview = "" if is_empty(val, empty_tokens=empty) else str(val)[:80]
        observations.append(
            FieldPresence(
                field=name,
                present=present,
                value_preview=preview,
                mandatory=name in mandatory,
            )
        )

    scored = len(fields)
    completeness = (filled / scored) if scored else 0.0
    return completeness, observations, filled, scored


def assess_row(
    target_dataset: str,
    payload: Mapping[str, Any],
    *,
    confidence: float = 0.0,
    scored_field_names: Optional[Sequence[str]] = None,
    repo_root: Optional[Path] = None,
) -> QualityAssessment:
    """Full quality assessment for a dataset row payload."""
    root = repo_root or find_repo_root()
    thr = thresholds(repo_root=root)
    empty = _empty_tokens(root)
    mandatory = mandatory_fields_for(target_dataset, repo_root=root)

    completeness, observations, filled, scored = score_completeness(
        target_dataset,
        payload,
        scored_field_names=scored_field_names,
        repo_root=root,
    )

    missing = [
        f
        for f in mandatory
        if is_empty(_payload_lookup(payload, f), empty_tokens=empty)
    ]
    mandatory_present = len(mandatory) - len(missing)
    conf = float(confidence or 0.0)
    reasons: list[str] = []

    if missing:
        reasons.append(f"mandatory_missing:{','.join(missing)}")
    if completeness < thr["min_completeness_to_publish"]:
        reasons.append(
            f"completeness_below_threshold:{completeness:.2f}<{thr['min_completeness_to_publish']}"
        )
    if conf < thr["min_confidence_to_publish"]:
        reasons.append(
            f"confidence_below_threshold:{conf:.2f}<{thr['min_confidence_to_publish']}"
        )

    # Disposition
    if missing:
        validation = QualityValidationStatus.FAIL_MANDATORY.value
        disposition = PublishDisposition.ENRICHMENT_QUEUE.value
        enrichment = EnrichmentStatus.NEEDS_ENRICHMENT.value
    elif completeness < thr["min_completeness_to_publish"]:
        validation = QualityValidationStatus.FAIL_COMPLETENESS.value
        disposition = PublishDisposition.ENRICHMENT_QUEUE.value
        enrichment = EnrichmentStatus.NEEDS_ENRICHMENT.value
    elif conf < thr["min_confidence_to_publish"]:
        validation = QualityValidationStatus.FAIL_CONFIDENCE.value
        # Confidence failure stays enrichment (re-extract / re-source), not hard reject
        disposition = PublishDisposition.ENRICHMENT_QUEUE.value
        enrichment = EnrichmentStatus.NEEDS_ENRICHMENT.value
    else:
        validation = QualityValidationStatus.PASS.value
        disposition = PublishDisposition.PUBLISH.value
        enrichment = EnrichmentStatus.COMPLETE.value
        reasons = []

    cfg = load_quality_config(root)
    policy_version = str(cfg.get("version") or "1.0")

    return QualityAssessment(
        target_dataset=target_dataset,
        completeness=completeness,
        confidence=conf,
        enrichment_status=enrichment,
        validation_status=validation,
        disposition=disposition,
        mandatory_present=mandatory_present,
        mandatory_total=len(mandatory),
        mandatory_missing=missing,
        fields=observations,
        scored_fields=scored,
        filled_fields=filled,
        reasons=reasons,
        policy_version=policy_version,
    )


def assess_candidate(
    candidate: Any,
    *,
    repo_root: Optional[Path] = None,
) -> QualityAssessment:
    """Assess a CandidateRecord; attach result to candidate.metadata['quality']."""
    payload = getattr(candidate, "payload", None) or {}
    if not isinstance(payload, Mapping):
        payload = {}
    target = str(getattr(candidate, "target_dataset", "") or "")
    prov = getattr(candidate, "provenance", None)
    conf = float(getattr(prov, "confidence", 0.0) or 0.0) if prov else 0.0
    qa = assess_row(
        target,
        payload,
        confidence=conf,
        repo_root=repo_root,
    )
    meta = getattr(candidate, "metadata", None)
    if isinstance(meta, dict):
        meta["quality"] = qa.to_dict()
    return qa


def may_publish_directly(assessment: QualityAssessment) -> bool:
    return assessment.disposition == PublishDisposition.PUBLISH.value


def completeness_report_lines(assessment: QualityAssessment) -> list[str]:
    """Human-readable completeness breakdown (for reports / console)."""
    lines = [
        f"Dataset: {assessment.target_dataset}",
        f"Completeness: {assessment.completeness:.0%}",
        f"Confidence: {assessment.confidence:.2f}",
        f"Mandatory: {assessment.mandatory_present}/{assessment.mandatory_total}",
        f"Disposition: {assessment.disposition}",
        f"Enrichment: {assessment.enrichment_status}",
        f"Validation: {assessment.validation_status}",
        "",
        "Fields:",
    ]
    for f in assessment.fields:
        mark = "✓" if f.present else "✗"
        mand = " (required)" if f.mandatory else ""
        lines.append(f"  {f.field} {mark}{mand}")
    if assessment.reasons:
        lines.append("")
        lines.append("Reasons:")
        for r in assessment.reasons:
            lines.append(f"  - {r}")
    return lines
