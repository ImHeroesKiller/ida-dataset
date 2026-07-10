"""Bridge: Scheduler / Planner requests → Connector Manager.

Planner never imports connectors directly. It asks the bridge/manager.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

from .manager import ConnectorManager
from .types import SearchQuery


class SchedulerBridge:
    """Owned by orchestration layer; enforces request → manager → queue path."""

    def __init__(self, repo_root: Path | None = None):
        self.manager = ConnectorManager(repo_root=repo_root)

    def request_documents(
        self,
        query: str,
        *,
        limit: int = 10,
        connector_ids: Optional[list[str]] = None,
        mission_id: Optional[str] = None,
        planner_request_id: Optional[str] = None,
        dry_run: bool = True,
        acquire: bool = True,
    ) -> dict[str, Any]:
        q = SearchQuery(
            query=query,
            limit=limit,
            mission_id=mission_id,
            planner_request_id=planner_request_id,
            dry_run=dry_run,
            metadata={
                "mission_id": mission_id,
                "planner_request_id": planner_request_id,
            },
        )
        results = self.manager.search(q, connector_ids=connector_ids)
        documents = []
        if acquire:
            for res in results[:limit]:
                try:
                    doc = self.manager.acquire(res, mission_id=mission_id)
                    documents.append(doc.to_dict())
                except Exception as exc:  # noqa: BLE001
                    documents.append(
                        {
                            "error": str(exc),
                            "url": res.url,
                            "connector_id": res.connector_id,
                        }
                    )
        return {
            "query": query,
            "results": [r.to_dict() for r in results],
            "documents": documents,
            "queue": self.manager.queue.counts(),
            "dry_run": dry_run,
            "path": "Scheduler/Planner → Policy → ConnectorManager → DocumentQueue",
        }
