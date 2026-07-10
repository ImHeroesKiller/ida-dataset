"""Repository path resolution for KAS."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping


def find_repo_root(start: Path | None = None) -> Path:
    """Locate repository root by walking up until VERSION or .git is found."""
    current = (start or Path.cwd()).resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "VERSION").exists() or (candidate / ".git").exists():
            if (candidate / "domains").exists() or (candidate / "automation").exists():
                return candidate
            if (candidate / ".git").exists():
                return candidate
    return current


@dataclass(frozen=True)
class RepoPaths:
    """Resolved filesystem paths used by the pipeline."""

    root: Path
    automation_root: Path
    config_dir: Path
    queue_pending: Path
    queue_approved: Path
    queue_rejected: Path
    logs: Path
    reports: Path
    cache: Path
    raw_documents: Path
    review: Path
    source_registry: Path
    domains_root: Path

    @classmethod
    def from_policies(
        cls,
        policies: Mapping[str, Any],
        root: Path | None = None,
    ) -> "RepoPaths":
        repo_root = root or find_repo_root()
        path_cfg = policies.get("paths", {})

        def resolve(key: str, default: str) -> Path:
            rel = path_cfg.get(key, default)
            path = Path(rel)
            return path if path.is_absolute() else repo_root / path

        return cls(
            root=repo_root,
            automation_root=resolve("automation_root", "automation"),
            config_dir=(repo_root / "automation" / "config"),
            queue_pending=resolve("queue_pending", "automation/queue/pending"),
            queue_approved=resolve("queue_approved", "automation/queue/approved"),
            queue_rejected=resolve("queue_rejected", "automation/queue/rejected"),
            logs=resolve("logs", "automation/logs"),
            reports=resolve("reports", "automation/reports"),
            cache=resolve("cache", "automation/cache"),
            raw_documents=resolve("raw_documents", "automation/raw_documents"),
            review=resolve("review", "automation/review"),
            source_registry=resolve(
                "source_registry", "metadata/source_registry.csv"
            ),
            domains_root=resolve("domains_root", "domains"),
        )

    def ensure(self) -> None:
        """Create runtime directories if missing."""
        for path in (
            self.queue_pending,
            self.queue_approved,
            self.queue_rejected,
            self.logs,
            self.reports,
            self.cache,
            self.raw_documents,
            self.review,
        ):
            path.mkdir(parents=True, exist_ok=True)
