"""Shared types for the IDA Knowledge Network connector framework."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Optional
from uuid import uuid4


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


class ConnectorHealth(str, Enum):
    HEALTHY = "healthy"
    IDLE = "idle"
    DEGRADED = "degraded"
    RATE_LIMITED = "rate_limited"
    ERROR = "error"
    DISABLED = "disabled"
    UNKNOWN = "unknown"


class DocumentStatus(str, Enum):
    INCOMING = "incoming"
    PROCESSING = "processing"
    PROCESSED = "processed"
    FAILED = "failed"


@dataclass
class SearchQuery:
    query: str
    limit: int = 10
    domains: list[str] = field(default_factory=list)
    mission_id: Optional[str] = None
    planner_request_id: Optional[str] = None
    dry_run: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class SearchResult:
    result_id: str
    connector_id: str
    source_id: str
    title: str
    url: str
    snippet: str = ""
    trust_score: float = 0.0
    retrieved_at: str = field(default_factory=utc_now_iso)
    dry_run: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def create(cls, **kwargs: Any) -> "SearchResult":
        kwargs.setdefault("result_id", f"RES-{uuid4().hex[:10].upper()}")
        return cls(**kwargs)


@dataclass
class DocumentRef:
    """Queued document metadata — never written into domain datasets directly."""

    document_id: str
    connector_id: str
    source_id: str
    trust_score: float
    retrieved_at: str
    original_url: str
    checksum: str
    version: str
    title: str = ""
    content_type: str = "application/octet-stream"
    local_path: Optional[str] = None
    status: str = DocumentStatus.INCOMING.value
    dry_run: bool = True
    mission_id: Optional[str] = None
    planner_request_id: Optional[str] = None
    bytes: int = 0
    notes: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def create(cls, **kwargs: Any) -> "DocumentRef":
        kwargs.setdefault("document_id", f"DOC-{uuid4().hex[:12].upper()}")
        kwargs.setdefault("retrieved_at", utc_now_iso())
        kwargs.setdefault("version", "1")
        kwargs.setdefault("checksum", "")
        return cls(**kwargs)


@dataclass
class ConnectorEvent:
    ts: str
    event: str
    connector_id: str
    detail: str
    level: str = "info"
    document_id: Optional[str] = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class HealthReport:
    connector_id: str
    health: str
    latency_ms: Optional[float] = None
    success_rate: Optional[float] = None
    documents_retrieved: int = 0
    errors: int = 0
    message: str = ""
    last_check: str = field(default_factory=utc_now_iso)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
