"""Query planner — normalizes Planner search intents (no extraction).

Supports enterprise-function context so discovery is not BD-only.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class PlannedQuery:
    query: str
    limit: int = 10
    preferred_types: list[str] | None = None
    mission_id: Optional[str] = None
    planner_request_id: Optional[str] = None
    enterprise_function: Optional[str] = None
    related_queries: list[str] = field(default_factory=list)


class QueryPlanner:
    def plan(
        self,
        raw: str,
        *,
        limit: int = 10,
        mission_id: Optional[str] = None,
        preferred_types: list[str] | None = None,
        enterprise_function: Optional[str] = None,
        dataset: Optional[str] = None,
    ) -> PlannedQuery:
        q = " ".join((raw or "").split()).strip()
        related: list[str] = []
        ef = enterprise_function
        # Auto-enrich with function-scoped site: queries when context present
        if ef or dataset:
            try:
                from automation.manufacturing.enterprise_functions import (
                    build_discovery_queries,
                    select_function_for_dataset,
                )

                ds = dataset or "industry_library"
                if not ef:
                    picked = select_function_for_dataset(ds)
                    ef = str(picked.get("id") or "") or None
                if ef:
                    related = build_discovery_queries(
                        dataset=ds,
                        enterprise_function=ef,
                        base_query=q,
                        limit=5,
                    )
                    # Prefer first related query when raw is empty/generic
                    if not q and related:
                        q = related[0]
            except Exception:  # noqa: BLE001
                related = []
        return PlannedQuery(
            query=q,
            limit=max(1, min(limit, 50)),
            preferred_types=preferred_types,
            mission_id=mission_id,
            planner_request_id=f"PQ-{abs(hash(q)) % 10_000_000:07d}",
            enterprise_function=ef,
            related_queries=related,
        )

    def to_dict(self, plan: PlannedQuery) -> dict[str, Any]:
        return {
            "query": plan.query,
            "limit": plan.limit,
            "preferred_types": plan.preferred_types or [],
            "mission_id": plan.mission_id,
            "planner_request_id": plan.planner_request_id,
            "enterprise_function": plan.enterprise_function,
            "related_queries": plan.related_queries or [],
        }
