"""Human controller layer for the Knowledge Acquisition System.

All safety rails live here. Pipeline stages must consult the controller
before performing side effects (crawl, extract, publish).
"""

from __future__ import annotations

import csv
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Mapping, MutableMapping, Optional, Sequence
from urllib.parse import urlparse

from .config import deep_merge, get_nested
from .models import CandidateRecord


@dataclass
class ControllerSnapshot:
    """Serializable view of controller decisions for logs/reports."""

    crawling_enabled: bool
    extraction_enabled: bool
    publishing_enabled: bool
    approval_mode: str
    review_required: bool
    confidence_threshold: float
    max_documents: int
    max_rows_per_day: int
    max_updates_per_day: int
    domain_whitelist: list[str]
    domain_blacklist: list[str]
    publishing_schedule: str
    trusted_source_ids: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "crawling_enabled": self.crawling_enabled,
            "extraction_enabled": self.extraction_enabled,
            "publishing_enabled": self.publishing_enabled,
            "approval_mode": self.approval_mode,
            "review_required": self.review_required,
            "confidence_threshold": self.confidence_threshold,
            "max_documents": self.max_documents,
            "max_rows_per_day": self.max_rows_per_day,
            "max_updates_per_day": self.max_updates_per_day,
            "domain_whitelist": self.domain_whitelist,
            "domain_blacklist": self.domain_blacklist,
            "publishing_schedule": self.publishing_schedule,
            "trusted_source_ids": self.trusted_source_ids,
        }


@dataclass
class HumanController:
    """Human-in-the-loop control surface.

    Enable/disable crawling, extraction, publishing.
    Select trusted sources, limit domains, whitelist/blacklist,
    enforce max documents / rows/day / updates/day, confidence threshold,
    approval mode, review requirement, and publishing schedule.
    """

    config: MutableMapping[str, Any]
    source_registry_path: Path
    _usage: dict[str, Any] = field(default_factory=dict)
    _runtime_overrides: dict[str, Any] = field(default_factory=dict)

    # ------------------------------------------------------------------
    # Config accessors
    # ------------------------------------------------------------------
    @property
    def policies(self) -> Mapping[str, Any]:
        return self.config.get("policies", {})

    @property
    def sources_cfg(self) -> Mapping[str, Any]:
        return self.config.get("sources", {})

    def _feature(self, name: str, default: bool = False) -> bool:
        if name in self._runtime_overrides:
            return bool(self._runtime_overrides[name])
        return bool(get_nested(self.policies, "features", name, default=default))

    # Enable / Disable
    def is_crawling_enabled(self) -> bool:
        return self._feature("crawling_enabled", False)

    def is_extraction_enabled(self) -> bool:
        return self._feature("extraction_enabled", False)

    def is_publishing_enabled(self) -> bool:
        return self._feature("publishing_enabled", False)

    def enable(self, feature: str) -> None:
        key = f"{feature}_enabled" if not feature.endswith("_enabled") else feature
        self._runtime_overrides[key] = True

    def disable(self, feature: str) -> None:
        key = f"{feature}_enabled" if not feature.endswith("_enabled") else feature
        self._runtime_overrides[key] = False

    def set_override(self, key: str, value: Any) -> None:
        self._runtime_overrides[key] = value

    def apply_overrides(self, overrides: Mapping[str, Any]) -> None:
        deep_merge(self._runtime_overrides, dict(overrides))

    # Approval / review
    def approval_mode(self) -> str:
        if "approval_mode" in self._runtime_overrides:
            return str(self._runtime_overrides["approval_mode"])
        return str(self.policies.get("approval_mode", "manual"))

    def review_required(self) -> bool:
        if "review_required" in self._runtime_overrides:
            return bool(self._runtime_overrides["review_required"])
        return bool(self.policies.get("review_required", True))

    def confidence_threshold(self) -> float:
        if "confidence_threshold" in self._runtime_overrides:
            return float(self._runtime_overrides["confidence_threshold"])
        return float(self.policies.get("confidence_threshold", 0.8))

    def publishing_schedule(self) -> str:
        if "publishing_schedule" in self._runtime_overrides:
            return str(self._runtime_overrides["publishing_schedule"])
        return str(
            get_nested(self.policies, "publishing", "schedule", default="manual")
        )

    # Limits
    def max_documents(self) -> int:
        return int(
            self._runtime_overrides.get(
                "max_documents",
                get_nested(self.policies, "limits", "max_documents", default=100),
            )
        )

    def max_rows_per_day(self) -> int:
        return int(
            self._runtime_overrides.get(
                "max_rows_per_day",
                get_nested(self.policies, "limits", "max_rows_per_day", default=200),
            )
        )

    def max_updates_per_day(self) -> int:
        return int(
            self._runtime_overrides.get(
                "max_updates_per_day",
                get_nested(self.policies, "limits", "max_updates_per_day", default=50),
            )
        )

    # Domain controls
    def domain_whitelist(self) -> list[str]:
        override = self._runtime_overrides.get("domain_whitelist")
        if override is not None:
            return list(override)
        return list(get_nested(self.sources_cfg, "domains", "whitelist", default=[]) or [])

    def domain_blacklist(self) -> list[str]:
        override = self._runtime_overrides.get("domain_blacklist")
        if override is not None:
            return list(override)
        return list(get_nested(self.sources_cfg, "domains", "blacklist", default=[]) or [])

    def is_domain_allowed(self, url_or_domain: str) -> bool:
        host = url_or_domain.lower().strip()
        if "://" in host:
            host = urlparse(host).hostname or host
        host = host.lstrip("www.")

        blacklist = {d.lower().lstrip("www.") for d in self.domain_blacklist()}
        if host in blacklist or any(host.endswith("." + b) for b in blacklist):
            return False

        whitelist = {d.lower().lstrip("www.") for d in self.domain_whitelist()}
        if not whitelist:
            return True
        return host in whitelist or any(host.endswith("." + w) for w in whitelist)

    # ------------------------------------------------------------------
    # Source registry
    # ------------------------------------------------------------------
    def load_source_registry(self) -> list[dict[str, str]]:
        path = self.source_registry_path
        if not path.exists():
            return []
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return list(csv.DictReader(handle))

    def trusted_sources(
        self,
        *,
        min_trust: Optional[float] = None,
        allowed_only: bool = True,
    ) -> list[dict[str, str]]:
        threshold = (
            min_trust
            if min_trust is not None
            else float(
                get_nested(
                    self.sources_cfg, "defaults", "trust_score_min", default=0.7
                )
            )
        )
        selected: list[dict[str, str]] = []
        for row in self.load_source_registry():
            allowed = str(row.get("Allowed", "")).strip().lower() in {
                "1",
                "true",
                "yes",
                "y",
            }
            status = str(row.get("Status", "")).strip().lower()
            try:
                trust = float(row.get("Trust Score", 0) or 0)
            except ValueError:
                trust = 0.0
            if allowed_only and not allowed:
                continue
            if status and status not in {"active", "enabled"}:
                continue
            if trust < threshold:
                continue
            base_url = row.get("Base URL", "")
            if base_url and not self.is_domain_allowed(base_url):
                continue
            selected.append(row)
        return selected

    def is_source_trusted(self, source_id: str) -> bool:
        trusted_ids = {r.get("Source ID") for r in self.trusted_sources()}
        return source_id in trusted_ids

    def get_source(self, source_id: str) -> Optional[dict[str, str]]:
        for row in self.load_source_registry():
            if row.get("Source ID") == source_id:
                return row
        return None

    # ------------------------------------------------------------------
    # Daily usage / rate limits
    # ------------------------------------------------------------------
    def _today_key(self) -> str:
        return date.today().isoformat()

    def _usage_bucket(self) -> dict[str, int]:
        key = self._today_key()
        if key not in self._usage:
            self._usage[key] = {"rows": 0, "updates": 0, "documents": 0}
        return self._usage[key]

    def record_usage(self, *, rows: int = 0, updates: int = 0, documents: int = 0) -> None:
        bucket = self._usage_bucket()
        bucket["rows"] += rows
        bucket["updates"] += updates
        bucket["documents"] += documents

    def can_accept_documents(self, count: int = 1) -> bool:
        bucket = self._usage_bucket()
        return (bucket["documents"] + count) <= self.max_documents()

    def can_accept_rows(self, count: int = 1) -> bool:
        bucket = self._usage_bucket()
        return (bucket["rows"] + count) <= self.max_rows_per_day()

    def can_accept_updates(self, count: int = 1) -> bool:
        bucket = self._usage_bucket()
        return (bucket["updates"] + count) <= self.max_updates_per_day()

    # ------------------------------------------------------------------
    # Decision helpers for stages
    # ------------------------------------------------------------------
    def may_crawl(self) -> tuple[bool, str]:
        if not self.is_crawling_enabled():
            return False, "crawling_disabled"
        if not self.can_accept_documents(1):
            return False, "max_documents_reached"
        return True, "ok"

    def may_extract(self) -> tuple[bool, str]:
        if not self.is_extraction_enabled():
            return False, "extraction_disabled"
        if not self.can_accept_rows(1):
            return False, "max_rows_per_day_reached"
        return True, "ok"

    def may_publish(self) -> tuple[bool, str]:
        if not self.is_publishing_enabled():
            return False, "publishing_disabled"
        schedule = self.publishing_schedule()
        if schedule != "immediate" and schedule != "manual":
            # daily/weekly still require explicit publish flag from orchestrator
            pass
        if self.review_required() and self.approval_mode() == "manual":
            # publisher stage will only consume approved queue
            pass
        if not self.can_accept_updates(1):
            return False, "max_updates_per_day_reached"
        return True, "ok"

    def passes_confidence(self, confidence: float) -> bool:
        return float(confidence) >= self.confidence_threshold()

    def auto_approve_allowed(self) -> bool:
        """True only when approval_mode is automatic AND review_required is false."""
        return self.approval_mode() == "automatic" and not self.review_required()

    def evaluate_candidate_for_rejection(
        self, candidate: CandidateRecord
    ) -> list[str]:
        """Return rejection reasons (empty list means not rejected by controller)."""
        reasons: list[str] = []
        if not self.is_source_trusted(candidate.provenance.source_id):
            reasons.append("no_trusted_source")
        if not self.passes_confidence(candidate.provenance.confidence):
            reasons.append("confidence_below_threshold")
        if candidate.provenance.source_url and not self.is_domain_allowed(
            candidate.provenance.source_url
        ):
            reasons.append("domain_not_allowed")
        return reasons

    def snapshot(self) -> ControllerSnapshot:
        trusted = self.trusted_sources()
        return ControllerSnapshot(
            crawling_enabled=self.is_crawling_enabled(),
            extraction_enabled=self.is_extraction_enabled(),
            publishing_enabled=self.is_publishing_enabled(),
            approval_mode=self.approval_mode(),
            review_required=self.review_required(),
            confidence_threshold=self.confidence_threshold(),
            max_documents=self.max_documents(),
            max_rows_per_day=self.max_rows_per_day(),
            max_updates_per_day=self.max_updates_per_day(),
            domain_whitelist=self.domain_whitelist(),
            domain_blacklist=self.domain_blacklist(),
            publishing_schedule=self.publishing_schedule(),
            trusted_source_ids=[r.get("Source ID", "") for r in trusted],
        )
