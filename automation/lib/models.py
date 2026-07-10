"""Core data models for the Knowledge Acquisition System."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Mapping, MutableMapping, Optional
from uuid import uuid4


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


class ValidationStatus(str, Enum):
    PENDING = "pending"
    VALID = "valid"
    INVALID = "invalid"
    DUPLICATE = "duplicate"
    REJECTED = "rejected"
    APPROVED = "approved"
    PUBLISHED = "published"
    SKIPPED = "skipped"


class ReviewAction(str, Enum):
    APPROVE = "approve"
    REJECT = "reject"
    EDIT = "edit"
    MERGE = "merge"
    SKIP = "skip"
    BULK_APPROVE = "bulk_approve"
    BULK_REJECT = "bulk_reject"


class PipelineStage(str, Enum):
    DISCOVER = "discover"
    COLLECT = "collect"
    EXTRACT = "extract"
    NORMALIZE = "normalize"
    VALIDATE = "validate"
    DEDUPLICATE = "deduplicate"
    ENTITY_LINK = "entity_link"
    REVIEWER = "reviewer"
    PUBLISHER = "publisher"


PROVENANCE_FIELD_NAMES = (
    "source_id",
    "source_url",
    "retrieved_at",
    "confidence",
    "extraction_version",
    "validation_status",
    "reviewer",
    "published_at",
)


@dataclass
class Provenance:
    """Mandatory provenance for every candidate / published row."""

    source_id: str
    source_url: str
    retrieved_at: str
    confidence: float
    extraction_version: str
    validation_status: str = ValidationStatus.PENDING.value
    reviewer: Optional[str] = None
    published_at: Optional[str] = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "Provenance":
        return cls(
            source_id=str(data.get("source_id", "")),
            source_url=str(data.get("source_url", "")),
            retrieved_at=str(data.get("retrieved_at", "")),
            confidence=float(data.get("confidence", 0.0)),
            extraction_version=str(data.get("extraction_version", "")),
            validation_status=str(
                data.get("validation_status", ValidationStatus.PENDING.value)
            ),
            reviewer=data.get("reviewer"),
            published_at=data.get("published_at"),
        )


@dataclass
class CandidateRecord:
    """A single knowledge candidate flowing through the pipeline."""

    candidate_id: str
    entity_type: str
    entity_id: str
    target_dataset: str
    payload: dict[str, Any]
    provenance: Provenance
    canonical_name: str = ""
    links: dict[str, Any] = field(default_factory=dict)
    rejection_reasons: list[str] = field(default_factory=list)
    duplicate_of: Optional[str] = None
    stage_history: list[str] = field(default_factory=list)
    created_at: str = field(default_factory=utc_now_iso)
    updated_at: str = field(default_factory=utc_now_iso)
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def create(
        cls,
        *,
        entity_type: str,
        entity_id: str,
        target_dataset: str,
        payload: Mapping[str, Any],
        provenance: Provenance,
        canonical_name: str = "",
        metadata: Optional[Mapping[str, Any]] = None,
    ) -> "CandidateRecord":
        return cls(
            candidate_id=f"CAND-{uuid4().hex[:12].upper()}",
            entity_type=entity_type,
            entity_id=entity_id,
            target_dataset=target_dataset,
            payload=dict(payload),
            provenance=provenance,
            canonical_name=canonical_name or str(payload.get("name", entity_id)),
            metadata=dict(metadata or {}),
        )

    def touch(self, stage: str | PipelineStage | None = None) -> None:
        self.updated_at = utc_now_iso()
        if stage is not None:
            stage_name = stage.value if isinstance(stage, PipelineStage) else stage
            self.stage_history.append(stage_name)

    def to_dict(self) -> dict[str, Any]:
        return {
            "candidate_id": self.candidate_id,
            "entity_type": self.entity_type,
            "entity_id": self.entity_id,
            "target_dataset": self.target_dataset,
            "canonical_name": self.canonical_name,
            "payload": self.payload,
            "provenance": self.provenance.to_dict(),
            "links": self.links,
            "rejection_reasons": self.rejection_reasons,
            "duplicate_of": self.duplicate_of,
            "stage_history": self.stage_history,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "CandidateRecord":
        return cls(
            candidate_id=str(data["candidate_id"]),
            entity_type=str(data.get("entity_type", "")),
            entity_id=str(data.get("entity_id", "")),
            target_dataset=str(data.get("target_dataset", "")),
            payload=dict(data.get("payload") or {}),
            provenance=Provenance.from_mapping(data.get("provenance") or {}),
            canonical_name=str(data.get("canonical_name", "")),
            links=dict(data.get("links") or {}),
            rejection_reasons=list(data.get("rejection_reasons") or []),
            duplicate_of=data.get("duplicate_of"),
            stage_history=list(data.get("stage_history") or []),
            created_at=str(data.get("created_at", utc_now_iso())),
            updated_at=str(data.get("updated_at", utc_now_iso())),
            metadata=dict(data.get("metadata") or {}),
        )

    def entity_key(self) -> str:
        return f"{self.entity_type}:{self.entity_id}".lower()

    def with_provenance_on_payload(self) -> dict[str, Any]:
        """Merge domain payload with mandatory provenance columns for publishing."""
        row = dict(self.payload)
        for key, value in self.provenance.to_dict().items():
            row[key] = value
        return row


@dataclass
class StageResult:
    """Outcome of a single pipeline stage."""

    stage: str
    success: bool
    message: str = ""
    input_count: int = 0
    output_count: int = 0
    rejected_count: int = 0
    artifacts: list[str] = field(default_factory=list)
    details: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class RunReport:
    """Aggregated metrics for a pipeline run / daily report."""

    run_id: str
    started_at: str
    finished_at: Optional[str] = None
    profile: str = "manual"
    dry_run: bool = True
    rows_discovered: int = 0
    rows_collected: int = 0
    rows_extracted: int = 0
    rows_normalized: int = 0
    rows_validated: int = 0
    rows_approved: int = 0
    rows_rejected: int = 0
    duplicates: int = 0
    updated_datasets: list[str] = field(default_factory=list)
    stage_results: list[dict[str, Any]] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class PipelineContext:
    """Shared mutable context passed through all stages."""

    run_id: str
    config: MutableMapping[str, Any]
    paths: Any  # RepoPaths (avoid circular typing issues at runtime)
    controller: Any  # HumanController
    dry_run: bool = True
    publish: bool = False
    candidates: list[CandidateRecord] = field(default_factory=list)
    discovered_sources: list[dict[str, Any]] = field(default_factory=list)
    collected_documents: list[dict[str, Any]] = field(default_factory=list)
    report: Optional[RunReport] = None
    state: dict[str, Any] = field(default_factory=dict)

    def add_stage_result(self, result: StageResult) -> None:
        if self.report is None:
            return
        self.report.stage_results.append(result.to_dict())
