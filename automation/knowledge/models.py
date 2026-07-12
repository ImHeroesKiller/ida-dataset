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


# --- Knowledge Graph manufacturing models (additive) ---


class AtomType(str, Enum):
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    TABLE = "table"
    BULLET = "bullet"
    FAQ = "faq"
    METADATA = "metadata"
    CAPTION = "caption"
    SECTION = "section"


class AtomStatus(str, Enum):
    ACTIVE = "ACTIVE"
    SUPERSEDED = "SUPERSEDED"
    MERGED = "MERGED"
    ARCHIVED = "ARCHIVED"


class EntityStatus(str, Enum):
    ACTIVE = "ACTIVE"
    MERGED = "MERGED"
    SUPERSEDED = "SUPERSEDED"
    ARCHIVED = "ARCHIVED"


@dataclass
class KnowledgeAtom:
    """Persistent semantic unit — many atoms per document.

    Atoms are the first stage of knowledge manufacturing.
    Dataset rows are produced later from the entity graph, not from atoms alone.
    API surface from Commit 1 remains valid; new fields are optional/defaulted.
    """

    atom_id: str
    document_id: str
    atom_type: str
    text: str
    source: str = ""
    source_url: str = ""
    section: str = ""
    heading_path: list[str] = field(default_factory=list)
    order: int = 0
    timestamp: str = field(default_factory=utc_now_iso)
    confidence: float = 0.0
    provenance: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=utc_now_iso)
    # Commit 2 revisions (additive)
    knowledge_score: float = 0.0
    normalized_text: str = ""
    original_text: str = ""
    language: str = ""
    document_type: str = ""
    mime_type: str = ""
    publisher: str = ""
    published_date: str = ""
    crawl_date: str = ""
    parser_version: str = ""
    extractor_version: str = ""
    status: str = AtomStatus.ACTIVE.value
    paragraph_index: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "atom_id": self.atom_id,
            "document_id": self.document_id,
            "atom_type": self.atom_type,
            "text": self.text,
            "source": self.source,
            "source_url": self.source_url,
            "section": self.section,
            "heading_path": list(self.heading_path),
            "order": self.order,
            "timestamp": self.timestamp,
            "confidence": self.confidence,
            "provenance": dict(self.provenance),
            "metadata": dict(self.metadata),
            "created_at": self.created_at,
            "knowledge_score": self.knowledge_score,
            "normalized_text": self.normalized_text,
            "original_text": self.original_text or self.text,
            "language": self.language,
            "document_type": self.document_type,
            "mime_type": self.mime_type,
            "publisher": self.publisher,
            "published_date": self.published_date,
            "crawl_date": self.crawl_date,
            "parser_version": self.parser_version,
            "extractor_version": self.extractor_version,
            "status": self.status,
            "paragraph_index": self.paragraph_index,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "KnowledgeAtom":
        text = str(data.get("text") or "")
        return cls(
            atom_id=str(data.get("atom_id") or ""),
            document_id=str(data.get("document_id") or ""),
            atom_type=str(data.get("atom_type") or AtomType.PARAGRAPH.value),
            text=text,
            source=str(data.get("source") or ""),
            source_url=str(data.get("source_url") or ""),
            section=str(data.get("section") or ""),
            heading_path=list(data.get("heading_path") or []),
            order=int(data.get("order") or 0),
            timestamp=str(data.get("timestamp") or utc_now_iso()),
            confidence=float(data.get("confidence") or 0.0),
            provenance=dict(data.get("provenance") or {}),
            metadata=dict(data.get("metadata") or {}),
            created_at=str(data.get("created_at") or utc_now_iso()),
            knowledge_score=float(data.get("knowledge_score") or 0.0),
            normalized_text=str(data.get("normalized_text") or ""),
            original_text=str(data.get("original_text") or text),
            language=str(data.get("language") or ""),
            document_type=str(data.get("document_type") or ""),
            mime_type=str(data.get("mime_type") or ""),
            publisher=str(data.get("publisher") or ""),
            published_date=str(data.get("published_date") or ""),
            crawl_date=str(data.get("crawl_date") or ""),
            parser_version=str(data.get("parser_version") or ""),
            extractor_version=str(data.get("extractor_version") or ""),
            status=str(data.get("status") or AtomStatus.ACTIVE.value),
            paragraph_index=int(data.get("paragraph_index") or data.get("order") or 0),
        )


@dataclass
class GraphEntity:
    """Canonical entity — permanent foundation of the Knowledge Graph.

    Relationships are NOT attached in Commit 2.
    """

    entity_id: str
    entity_type: str
    canonical_name: str
    aliases: list[str] = field(default_factory=list)
    knowledge_score: float = 0.0
    confidence: float = 0.0
    first_seen: str = field(default_factory=utc_now_iso)
    last_seen: str = field(default_factory=utc_now_iso)
    sources: list[str] = field(default_factory=list)
    atom_ids: list[str] = field(default_factory=list)
    document_ids: list[str] = field(default_factory=list)
    status: str = EntityStatus.ACTIVE.value
    attributes: dict[str, Any] = field(default_factory=dict)
    provenance: dict[str, Any] = field(default_factory=dict)
    created_session: str = ""
    updated_session: str = ""
    created_at: str = field(default_factory=utc_now_iso)
    updated_at: str = field(default_factory=utc_now_iso)
    # Soft-merge pointer when SUPERSEDED/MERGED
    merged_into: str = ""

    @property
    def name(self) -> str:
        return self.canonical_name

    def to_dict(self) -> dict[str, Any]:
        return {
            "entity_id": self.entity_id,
            "entity_type": self.entity_type,
            "canonical_name": self.canonical_name,
            "name": self.canonical_name,
            "aliases": list(self.aliases),
            "knowledge_score": self.knowledge_score,
            "confidence": self.confidence,
            "first_seen": self.first_seen,
            "last_seen": self.last_seen,
            "sources": list(self.sources),
            "atom_ids": list(self.atom_ids),
            "document_ids": list(self.document_ids),
            "status": self.status,
            "attributes": dict(self.attributes),
            "provenance": dict(self.provenance),
            "created_session": self.created_session,
            "updated_session": self.updated_session,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "merged_into": self.merged_into,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "GraphEntity":
        cname = str(data.get("canonical_name") or data.get("name") or "").strip()
        now = utc_now_iso()
        return cls(
            entity_id=str(data.get("entity_id") or ""),
            entity_type=str(data.get("entity_type") or ""),
            canonical_name=cname,
            aliases=list(data.get("aliases") or []),
            knowledge_score=float(data.get("knowledge_score") or 0.0),
            confidence=float(data.get("confidence") or 0.0),
            first_seen=str(data.get("first_seen") or data.get("created_at") or now),
            last_seen=str(data.get("last_seen") or data.get("updated_at") or now),
            sources=list(data.get("sources") or []),
            atom_ids=list(data.get("atom_ids") or []),
            document_ids=list(data.get("document_ids") or []),
            status=str(data.get("status") or EntityStatus.ACTIVE.value),
            attributes=dict(data.get("attributes") or {}),
            provenance=dict(data.get("provenance") or {}),
            created_session=str(data.get("created_session") or ""),
            updated_session=str(data.get("updated_session") or ""),
            created_at=str(data.get("created_at") or now),
            updated_at=str(data.get("updated_at") or now),
            merged_into=str(data.get("merged_into") or ""),
        )


# Alias used in docs / public API
CanonicalEntity = GraphEntity


@dataclass
class GraphRelationship:
    """Edge in the internal knowledge graph."""

    relationship_id: str
    source_entity: str  # subject entity_id
    target_entity: str  # object entity_id
    relationship_type: str  # predicate
    confidence: float = 0.0
    provenance: dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default_factory=utc_now_iso)
    sources: list[str] = field(default_factory=list)
    attributes: dict[str, Any] = field(default_factory=dict)

    # Back-compat aliases
    @property
    def subject_id(self) -> str:
        return self.source_entity

    @property
    def object_id(self) -> str:
        return self.target_entity

    @property
    def predicate(self) -> str:
        return self.relationship_type

    def to_dict(self) -> dict[str, Any]:
        return {
            "relationship_id": self.relationship_id,
            "source_entity": self.source_entity,
            "target_entity": self.target_entity,
            "relationship_type": self.relationship_type,
            "subject_id": self.source_entity,
            "object_id": self.target_entity,
            "predicate": self.relationship_type,
            "confidence": self.confidence,
            "provenance": dict(self.provenance),
            "timestamp": self.timestamp,
            "sources": list(self.sources),
            "attributes": dict(self.attributes),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "GraphRelationship":
        return cls(
            relationship_id=str(data.get("relationship_id") or ""),
            source_entity=str(
                data.get("source_entity") or data.get("subject_id") or ""
            ),
            target_entity=str(
                data.get("target_entity") or data.get("object_id") or ""
            ),
            relationship_type=str(
                data.get("relationship_type") or data.get("predicate") or ""
            ),
            confidence=float(data.get("confidence") or 0.0),
            provenance=dict(data.get("provenance") or {}),
            timestamp=str(data.get("timestamp") or utc_now_iso()),
            sources=list(data.get("sources") or []),
            attributes=dict(data.get("attributes") or {}),
        )
