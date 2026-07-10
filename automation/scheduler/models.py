"""Shared models for the Continuous Learning Scheduler and Mission System."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Optional
from uuid import uuid4


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


class LearningStream(str, Enum):
    CONTINUOUS = "continuous"
    DIRECTED = "directed"
    MAINTENANCE = "maintenance"
    ONTOLOGY = "ontology"
    POLICY = "policy"


class MissionStatus(str, Enum):
    DRAFT = "Draft"
    QUEUED = "Queued"
    RUNNING = "Running"
    WAITING_REVIEW = "Waiting Review"
    COMPLETED = "Completed"
    PAUSED = "Paused"
    CANCELLED = "Cancelled"
    ARCHIVED = "Archived"


class MissionPriority(str, Enum):
    P0 = "P0"  # Critical
    P1 = "P1"  # High
    P2 = "P2"  # Medium
    P3 = "P3"  # Low
    P4 = "P4"  # Background


class TaskKind(str, Enum):
    CONTINUOUS = "continuous"
    DIRECTED = "directed"
    MAINTENANCE = "maintenance"
    ONTOLOGY = "ontology"
    POLICY = "policy"


PRIORITY_LABELS = {
    MissionPriority.P0: "Critical",
    MissionPriority.P1: "High",
    MissionPriority.P2: "Medium",
    MissionPriority.P3: "Low",
    MissionPriority.P4: "Background",
}


@dataclass
class LearningTask:
    """Unified learning queue item (continuous, directed, or maintenance)."""

    task_id: str
    title: str
    kind: str
    priority: str
    stream: str
    status: str = "queued"
    target_dataset: str = ""
    domain: str = ""
    mission_id: Optional[str] = None
    score: float = 0.0
    estimated_effort: float = 1.0
    progress: float = 0.0
    created_at: str = field(default_factory=utc_now_iso)
    updated_at: str = field(default_factory=utc_now_iso)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "LearningTask":
        return cls(
            task_id=str(data["task_id"]),
            title=str(data.get("title", "")),
            kind=str(data.get("kind", TaskKind.CONTINUOUS.value)),
            priority=str(data.get("priority", MissionPriority.P3.value)),
            stream=str(data.get("stream", LearningStream.CONTINUOUS.value)),
            status=str(data.get("status", "queued")),
            target_dataset=str(data.get("target_dataset", "")),
            domain=str(data.get("domain", "")),
            mission_id=data.get("mission_id"),
            score=float(data.get("score", 0.0)),
            estimated_effort=float(data.get("estimated_effort", 1.0)),
            progress=float(data.get("progress", 0.0)),
            created_at=str(data.get("created_at", utc_now_iso())),
            updated_at=str(data.get("updated_at", utc_now_iso())),
            metadata=dict(data.get("metadata") or {}),
        )


@dataclass
class Mission:
    """Directed Learning Mission."""

    mission_id: str
    title: str
    description: str
    priority: str
    requester: str
    created_at: str
    due_date: Optional[str] = None
    status: str = MissionStatus.DRAFT.value
    knowledge_targets: list[str] = field(default_factory=list)
    allowed_sources: list[str] = field(default_factory=list)
    policies: dict[str, Any] = field(default_factory=dict)
    estimated_effort: float = 1.0
    resource_allocation: float = 0.0
    progress: float = 0.0
    confidence: float = 0.0
    result: str = ""
    executive_summary: str = ""
    related_datasets: list[str] = field(default_factory=list)
    updated_at: str = field(default_factory=utc_now_iso)
    natural_language_request: str = ""
    contract_id: Optional[str] = None
    current_stage: str = "scheduled"
    current_dataset: str = ""
    documents_processed: int = 0
    entities_learned: int = 0
    knowledge_added: int = 0
    eta: Optional[str] = None

    @classmethod
    def create(
        cls,
        *,
        title: str,
        description: str,
        priority: str = MissionPriority.P2.value,
        requester: str = "human",
        knowledge_targets: Optional[list[str]] = None,
        allowed_sources: Optional[list[str]] = None,
        due_date: Optional[str] = None,
        natural_language_request: str = "",
        related_datasets: Optional[list[str]] = None,
    ) -> "Mission":
        mid = f"MIS-{utc_now_iso()[:10].replace('-', '')}-{uuid4().hex[:6].upper()}"
        return cls(
            mission_id=mid,
            title=title,
            description=description,
            priority=priority,
            requester=requester,
            created_at=utc_now_iso(),
            due_date=due_date,
            knowledge_targets=list(knowledge_targets or []),
            allowed_sources=list(allowed_sources or []),
            related_datasets=list(related_datasets or []),
            natural_language_request=natural_language_request or description,
            status=MissionStatus.DRAFT.value,
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Mission":
        return cls(
            mission_id=str(data["mission_id"]),
            title=str(data.get("title", "")),
            description=str(data.get("description", "")),
            priority=str(data.get("priority", MissionPriority.P2.value)),
            requester=str(data.get("requester", "human")),
            created_at=str(data.get("created_at", utc_now_iso())),
            due_date=data.get("due_date"),
            status=str(data.get("status", MissionStatus.DRAFT.value)),
            knowledge_targets=list(data.get("knowledge_targets") or []),
            allowed_sources=list(data.get("allowed_sources") or []),
            policies=dict(data.get("policies") or {}),
            estimated_effort=float(data.get("estimated_effort", 1.0)),
            resource_allocation=float(data.get("resource_allocation", 0.0)),
            progress=float(data.get("progress", 0.0)),
            confidence=float(data.get("confidence", 0.0)),
            result=str(data.get("result", "")),
            executive_summary=str(data.get("executive_summary", "")),
            related_datasets=list(data.get("related_datasets") or []),
            updated_at=str(data.get("updated_at", utc_now_iso())),
            natural_language_request=str(data.get("natural_language_request", "")),
            contract_id=data.get("contract_id"),
            current_stage=str(data.get("current_stage", "scheduled")),
            current_dataset=str(data.get("current_dataset", "")),
            documents_processed=int(data.get("documents_processed", 0)),
            entities_learned=int(data.get("entities_learned", 0)),
            knowledge_added=int(data.get("knowledge_added", 0)),
            eta=data.get("eta"),
        )


@dataclass
class LearningContract:
    """Permanent learning contract created from a Directed Learning request."""

    contract_id: str
    mission_id: str
    objective: str
    knowledge_scope: list[str]
    priority: str
    allowed_sources: list[str]
    resource_allocation: float
    deadline: Optional[str]
    expected_deliverables: list[str]
    review_requirement: bool
    requester: str
    created_at: str
    natural_language_request: str = ""
    status: str = "active"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_mission(
        cls,
        mission: Mission,
        *,
        resource_allocation: float,
        expected_deliverables: Optional[list[str]] = None,
        review_requirement: bool = True,
    ) -> "LearningContract":
        cid = f"CTR-{mission.mission_id.replace('MIS-', '')}"
        return cls(
            contract_id=cid,
            mission_id=mission.mission_id,
            objective=mission.description or mission.title,
            knowledge_scope=list(mission.knowledge_targets),
            priority=mission.priority,
            allowed_sources=list(mission.allowed_sources),
            resource_allocation=resource_allocation,
            deadline=mission.due_date,
            expected_deliverables=list(
                expected_deliverables
                or [
                    "Knowledge delta report",
                    "Mission summary",
                    "Updated related datasets (via review)",
                ]
            ),
            review_requirement=review_requirement,
            requester=mission.requester,
            created_at=utc_now_iso(),
            natural_language_request=mission.natural_language_request,
            status="active",
        )


@dataclass
class AllocationSnapshot:
    continuous: float
    directed: float
    maintenance: float
    ontology: float
    policy: float
    profile: str
    updated_at: str = field(default_factory=utc_now_iso)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def as_percent_map(self) -> dict[str, float]:
        return {
            "continuous": self.continuous,
            "directed": self.directed,
            "maintenance": self.maintenance,
            "ontology": self.ontology,
            "policy": self.policy,
        }


@dataclass
class SchedulerEvent:
    ts: str
    event: str
    stream: str
    detail: str
    mission_id: Optional[str] = None
    task_id: Optional[str] = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
