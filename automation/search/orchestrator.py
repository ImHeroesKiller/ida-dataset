"""Search Orchestrator — Planner request → connectors → document queue.

Never extracts knowledge. Only acquires documents.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

from automation.connectors.manager import ConnectorManager
from automation.connectors.types import SearchQuery
from automation.lib.paths import find_repo_root

from .query_history import QueryHistory
from .query_planner import QueryPlanner
from .search_cache import SearchCache
from .source_selector import SourceSelector


class SearchOrchestrator:
    def __init__(self, repo_root: Path | None = None):
        self.repo_root = repo_root or find_repo_root()
        self.manager = ConnectorManager(repo_root=self.repo_root)
        self.planner = QueryPlanner()
        self.selector = SourceSelector()
        paths = self.manager.config.get("paths") or {}
        cache_root = self.repo_root / paths.get(
            "search_cache", "automation/search/cache"
        )
        self.cache = SearchCache(cache_root)
        self.history = QueryHistory(cache_root / "query_history.jsonl")

    def execute(
        self,
        raw_query: str,
        *,
        limit: int = 10,
        mission_id: Optional[str] = None,
        preferred_types: Optional[list[str]] = None,
        acquire: bool = True,
        dry_run: bool = True,
    ) -> dict[str, Any]:
        plan = self.planner.plan(
            raw_query,
            limit=limit,
            mission_id=mission_id,
            preferred_types=preferred_types,
        )
        connectors = self.manager.list_connectors()
        selected = self.selector.select(
            connectors, preferred_types=preferred_types, limit=8
        )

        cache_key = f"{plan.query}|{plan.limit}|{','.join(selected)}"
        cached = self.cache.get(cache_key)
        if cached:
            self.history.add(
                {
                    "query": plan.query,
                    "cached": True,
                    "connectors": selected,
                    "result_count": len(cached.get("results") or []),
                }
            )
            return {**cached, "cached": True}

        q = SearchQuery(
            query=plan.query,
            limit=plan.limit,
            mission_id=mission_id,
            planner_request_id=plan.planner_request_id,
            dry_run=dry_run,
            metadata={
                "mission_id": mission_id,
                "planner_request_id": plan.planner_request_id,
            },
        )
        results = self.manager.search(q, connector_ids=selected)
        documents = []
        if acquire:
            for res in results[: plan.limit]:
                try:
                    documents.append(
                        self.manager.acquire(res, mission_id=mission_id).to_dict()
                    )
                except Exception as exc:  # noqa: BLE001
                    documents.append({"error": str(exc), "url": res.url})

        payload = {
            "plan": self.planner.to_dict(plan),
            "connectors_selected": selected,
            "results": [r.to_dict() for r in results],
            "documents": documents,
            "queue": self.manager.queue.counts(),
            "cached": False,
            "path": "Planner → Policy → ConnectorManager → DocumentQueue",
            "note": "No knowledge extraction performed",
        }
        self.cache.set(cache_key, payload)
        self.history.add(
            {
                "query": plan.query,
                "cached": False,
                "connectors": selected,
                "result_count": len(results),
                "documents": len(documents),
            }
        )
        return payload
