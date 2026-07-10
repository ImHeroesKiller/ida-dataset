"""Priority Engine — scores unified learning queue tasks for selection."""

from __future__ import annotations

from typing import Any

from .models import LearningTask, MissionPriority


class PriorityEngine:
    def __init__(self, config: dict[str, Any]):
        self.config = config
        pri = config.get("priorities") or {}
        self.weights = {
            code: float((meta or {}).get("weight", 10))
            for code, meta in pri.items()
        }
        # defaults if config incomplete
        for code, w in {
            MissionPriority.P0.value: 1000,
            MissionPriority.P1.value: 500,
            MissionPriority.P2.value: 200,
            MissionPriority.P3.value: 50,
            MissionPriority.P4.value: 10,
        }.items():
            self.weights.setdefault(code, w)

    def score(self, task: LearningTask, *, allocation_pct: float = 0.0) -> float:
        base = self.weights.get(task.priority, 10.0)
        # Slight boost for directed when allocation favors directed
        stream_boost = 1.0
        if task.kind == "directed" and allocation_pct >= 50:
            stream_boost = 1.15
        if task.kind == "continuous" and allocation_pct >= 50:
            stream_boost = 1.10
        # Prefer incomplete progress mid-flight
        progress_factor = 1.0 + (0.2 if 0 < task.progress < 100 else 0.0)
        # Lower effort slightly preferred for continuous gap fills
        effort = max(task.estimated_effort, 0.1)
        score = (base * stream_boost * progress_factor) / effort
        return round(score, 4)

    def rank(
        self,
        tasks: list[LearningTask],
        *,
        allocation: dict[str, float] | None = None,
    ) -> list[LearningTask]:
        allocation = allocation or {}
        ranked: list[LearningTask] = []
        for t in tasks:
            pct = float(allocation.get(t.stream, allocation.get(t.kind, 0)))
            t.score = self.score(t, allocation_pct=pct)
            ranked.append(t)
        ranked.sort(key=lambda x: (-x.score, x.created_at))
        return ranked

    def select_executable(
        self,
        tasks: list[LearningTask],
        *,
        allocation: dict[str, float] | None = None,
        limit: int = 1,
    ) -> list[LearningTask]:
        queued = [t for t in tasks if t.status in {"queued", "running", "ready"}]
        ranked = self.rank(queued, allocation=allocation)
        return ranked[: max(limit, 0)]
