"""Query planner — normalizes Planner search intents (no extraction)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class PlannedQuery:
    query: str
    limit: int = 10
    preferred_types: list[str] | None = None
    mission_id: Optional[str] = None
    planner_request_id: Optional[str] = None


class QueryPlanner:
    def plan(
        self,
        raw: str,
        *,
        limit: int = 10,
        mission_id: Optional[str] = None,
        preferred_types: list[str] | None = None,
    ) -> PlannedQuery:
        q = " ".join((raw or "").split()).strip()
        return PlannedQuery(
            query=q,
            limit=max(1, min(limit, 50)),
            preferred_types=preferred_types,
            mission_id=mission_id,
            planner_request_id=f"PQ-{abs(hash(q)) % 10_000_000:07d}",
        )

    def to_dict(self, plan: PlannedQuery) -> dict[str, Any]:
        return {
            "query": plan.query,
            "limit": plan.limit,
            "preferred_types": plan.preferred_types or [],
            "mission_id": plan.mission_id,
            "planner_request_id": plan.planner_request_id,
        }
