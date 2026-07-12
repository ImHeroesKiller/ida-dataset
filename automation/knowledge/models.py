"""Knowledge manufacturing models — additive, schema-compatible.

Quality metadata is never written into domain CSV columns.
It rides on CandidateRecord.metadata and enrichment queue sidecars.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any, Optional

from automation.lib.models import utc_now_iso


class EnrichmentStatus(str, Enum):
    """Operator-facing enrichment lifecycle."""

    COMPLETE = "complete"  # meets publish completeness
    NEEDS_ENRICHMENT = "needs_enrichment"
    ENRICHING = "enriching"
    FAILED = "failed"
    SKIPPED = "skipped"


class QualityValidationStatus(str, Enum):
    """Quality-layer validation (orthogonal to pipeline ValidationStatus)."""

    PASS = "pass"
    FAIL_MANDATORY = "fail_mandatory"
    FAIL_COMPLETENESS = "fail_completeness"
    FAIL_CONFIDENCE = "fail_confidence"
    PENDING = "pending"


class PublishDisposition(str, Enum):
    """Where the quality gate routes a candidate."""

    PUBLISH = "publish"
    ENRICHMENT_QUEUE = "enrichment_queue"
    REJECT = "reject"


@dataclass
class FieldPresence:
    """Single-field completeness observation."""

    field: str
    present: bool
    value_preview: str = ""
    mandatory: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class QualityAssessment:
    """Per-row quality scores — stored outside domain CSVs."""

    target_dataset: str
    completeness: float
    confidence: float
    enrichment_status: str
    validation_status: str
    disposition: str
    mandatory_present: int = 0
    mandatory_total: int = 0
    mandatory_missing: list[str] = field(default_factory=list)
    fields: list[FieldPresence] = field(default_factory=list)
    scored_fields: int = 0
    filled_fields: int = 0
    reasons: list[str] = field(default_factory=list)
    assessed_at: str = field(default_factory=utc_now_iso)
    policy_version: str = "1.0"

    def to_dict(self) -> dict[str, Any]:
        return {
            "target_dataset": self.target_dataset,
            "completeness": round(self.completeness, 4),
            "confidence": round(self.confidence, 4),
            "enrichment_status": self.enrichment_status,
            "validation_status": self.validation_status,
            "disposition": self.disposition,
            "mandatory_present": self.mandatory_present,
            "mandatory_total": self.mandatory_total,
            "mandatory_missing": list(self.mandatory_missing),
            "fields": [f.to_dict() for f in self.fields],
            "scored_fields": self.scored_fields,
            "filled_fields": self.filled_fields,
            "reasons": list(self.reasons),
            "assessed_at": self.assessed_at,
            "policy_version": self.policy_version,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "QualityAssessment":
        fields_raw = data.get("fields") or []
        fields = [
            FieldPresence(
                field=str(f.get("field", "")),
                present=bool(f.get("present")),
                value_preview=str(f.get("value_preview") or "")[:80],
                mandatory=bool(f.get("mandatory")),
            )
            for f in fields_raw
            if isinstance(f, dict)
        ]
        return cls(
            target_dataset=str(data.get("target_dataset") or ""),
            completeness=float(data.get("completeness") or 0.0),
            confidence=float(data.get("confidence") or 0.0),
            enrichment_status=str(
                data.get("enrichment_status")
                or EnrichmentStatus.NEEDS_ENRICHMENT.value
            ),
            validation_status=str(
                data.get("validation_status") or QualityValidationStatus.PENDING.value
            ),
            disposition=str(
                data.get("disposition") or PublishDisposition.ENRICHMENT_QUEUE.value
            ),
            mandatory_present=int(data.get("mandatory_present") or 0),
            mandatory_total=int(data.get("mandatory_total") or 0),
            mandatory_missing=list(data.get("mandatory_missing") or []),
            fields=fields,
            scored_fields=int(data.get("scored_fields") or 0),
            filled_fields=int(data.get("filled_fields") or 0),
            reasons=list(data.get("reasons") or []),
            assessed_at=str(data.get("assessed_at") or utc_now_iso()),
            policy_version=str(data.get("policy_version") or "1.0"),
        )


# --- Forward-compatible atom/graph stubs (used in later commits) ---


class AtomType(str, Enum):
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    TABLE = "table"
    BULLET = "bullet"
    FAQ = "faq"
    METADATA = "metadata"
    CAPTION = "caption"
    SECTION = "section"


@dataclass
class KnowledgeAtom:
    """Semantic unit derived from a document (many atoms per document)."""

    atom_id: str
    document_id: str
    atom_type: str
    text: str
    heading_path: list[str] = field(default_factory=list)
    order: int = 0
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=utc_now_iso)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class GraphEntity:
    """Node in the internal knowledge graph."""

    entity_id: str
    entity_type: str
    name: str
    attributes: dict[str, Any] = field(default_factory=dict)
    confidence: float = 0.0
    sources: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class GraphRelationship:
    """Edge in the internal knowledge graph."""

    relationship_id: str
    subject_id: str
    predicate: str
    object_id: str
    confidence: float = 0.0
    sources: list[str] = field(default_factory=list)
    attributes: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
