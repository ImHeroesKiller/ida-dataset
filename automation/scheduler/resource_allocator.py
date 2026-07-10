"""Resource allocation for Continuous vs Directed learning streams.

Allocation ratios are loaded from config — never hardcoded in logic.
Continuous Learning never stops (minimum continuous share always applied).
"""

from __future__ import annotations

from typing import Any, Iterable, Optional

from .models import AllocationSnapshot, Mission, MissionPriority, MissionStatus, utc_now_iso


class ResourceAllocator:
    def __init__(self, config: dict[str, Any]):
        self.config = config
        self.allocation_cfg = config.get("allocation") or {}

    def _profile_for_missions(self, missions: Iterable[Mission]) -> str:
        active = [
            m
            for m in missions
            if m.status
            in {
                MissionStatus.QUEUED.value,
                MissionStatus.RUNNING.value,
                MissionStatus.WAITING_REVIEW.value,
            }
        ]
        if not active:
            return "idle"
        if any(m.priority == MissionPriority.P0.value for m in active):
            return "critical_mission"
        if any(m.priority == MissionPriority.P1.value for m in active):
            return "high_mission"
        return "default"

    def allocate(
        self,
        missions: Iterable[Mission],
        *,
        override_profile: Optional[str] = None,
    ) -> AllocationSnapshot:
        profile = override_profile or self._profile_for_missions(missions)
        ratios = dict(self.allocation_cfg.get(profile) or self.allocation_cfg.get("default") or {})

        continuous = float(ratios.get("continuous", 70))
        directed = float(ratios.get("directed", 30))
        maintenance = float(ratios.get("maintenance", 0))
        ontology = float(ratios.get("ontology", 0))
        policy = float(ratios.get("policy", 0))

        # Continuous Learning never stops — enforce minimum floor of 1% if enabled
        streams = self.config.get("streams") or {}
        if (streams.get("continuous") or {}).get("never_stop", True):
            continuous = max(continuous, 1.0)

        total = continuous + directed + maintenance + ontology + policy
        if total <= 0:
            continuous, directed = 70.0, 30.0
            total = 100.0

        # Normalize to 100
        factor = 100.0 / total
        snap = AllocationSnapshot(
            continuous=round(continuous * factor, 2),
            directed=round(directed * factor, 2),
            maintenance=round(maintenance * factor, 2),
            ontology=round(ontology * factor, 2),
            policy=round(policy * factor, 2),
            profile=profile,
            updated_at=utc_now_iso(),
        )
        return snap

    def directed_share_for_mission(
        self,
        mission: Mission,
        allocation: AllocationSnapshot,
        active_directed_count: int,
    ) -> float:
        """Slice of directed pool assigned to one mission."""
        if active_directed_count <= 0:
            return 0.0
        # Priority weighting within directed pool
        weights = {
            MissionPriority.P0.value: 8,
            MissionPriority.P1.value: 4,
            MissionPriority.P2.value: 2,
            MissionPriority.P3.value: 1,
            MissionPriority.P4.value: 0.5,
        }
        w = weights.get(mission.priority, 1)
        # Caller may sum weights; here equal split fallback with weight hint
        base = allocation.directed / max(active_directed_count, 1)
        return round(base * (w / 2.0 if w > 2 else 1.0), 2)
