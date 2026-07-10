"""Scheduler metrics and brain telemetry snapshots."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .config_loader import read_json, resolve_path, write_json
from .models import AllocationSnapshot, Mission, SchedulerEvent, utc_now_iso


class SchedulerMetrics:
    def __init__(self, config: dict[str, Any]):
        self.config = config
        self.path: Path = resolve_path(
            config, "metrics", "automation/scheduler/state/metrics.json"
        )
        self.events_path: Path = self.path.parent / "events.jsonl"
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def load(self) -> dict[str, Any]:
        return read_json(
            self.path,
            {
                "updated_at": None,
                "ticks": 0,
                "tasks_dispatched": 0,
                "missions_completed": 0,
                "continuous_cycles": 0,
                "directed_cycles": 0,
                "allocation": None,
                "brain_health": "waiting",
                "knowledge_growth": {
                    "datasets_populated": 0,
                    "datasets_total": 0,
                    "coverage_pct": 0,
                },
                "learning_history": [],
            },
        )

    def save(self, data: dict[str, Any]) -> None:
        data["updated_at"] = utc_now_iso()
        write_json(self.path, data)

    def record_event(self, event: SchedulerEvent) -> None:
        self.events_path.parent.mkdir(parents=True, exist_ok=True)
        with self.events_path.open("a", encoding="utf-8", newline="\n") as handle:
            import json

            handle.write(json.dumps(event.to_dict(), ensure_ascii=False) + "\n")
        data = self.load()
        history = list(data.get("learning_history") or [])
        history.append(event.to_dict())
        data["learning_history"] = history[-200:]
        self.save(data)

    def recent_events(self, limit: int = 50) -> list[dict[str, Any]]:
        if not self.events_path.exists():
            return list((self.load().get("learning_history") or [])[-limit:])
        lines = self.events_path.read_text(encoding="utf-8").splitlines()
        import json

        events = []
        for line in lines[-limit:]:
            line = line.strip()
            if not line:
                continue
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                continue
        return events

    def update_allocation(self, allocation: AllocationSnapshot) -> None:
        data = self.load()
        data["allocation"] = allocation.to_dict()
        self.save(data)

    def bump(self, **counters: int) -> dict[str, Any]:
        data = self.load()
        for key, value in counters.items():
            data[key] = int(data.get(key) or 0) + int(value)
        self.save(data)
        return data

    def set_knowledge_growth(
        self, *, populated: int, total: int, coverage_pct: float
    ) -> None:
        data = self.load()
        data["knowledge_growth"] = {
            "datasets_populated": populated,
            "datasets_total": total,
            "coverage_pct": coverage_pct,
        }
        # Brain health heuristic
        if total == 0:
            data["brain_health"] = "waiting"
        elif coverage_pct >= 50:
            data["brain_health"] = "healthy"
        elif coverage_pct >= 15:
            data["brain_health"] = "learning"
        else:
            data["brain_health"] = "nascent"
        self.save(data)

    def dashboard_snapshot(
        self,
        *,
        allocation: AllocationSnapshot | None,
        missions: list[Mission],
        queue_snapshot: dict[str, Any],
        current_task: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        data = self.load()
        running = [m for m in missions if m.status == "Running"]
        current_mission = running[0].to_dict() if running else None
        if not current_mission:
            queued = [m for m in missions if m.status == "Queued"]
            current_mission = queued[0].to_dict() if queued else None

        return {
            "updated_at": utc_now_iso(),
            "brain_health": data.get("brain_health", "waiting"),
            "knowledge_growth": data.get("knowledge_growth"),
            "learning_allocation": (
                allocation.to_dict()
                if allocation
                else data.get("allocation")
            ),
            "current_mission": current_mission,
            "current_task": current_task,
            "mission_queue": [
                m.to_dict()
                for m in missions
                if m.status in {"Draft", "Queued", "Running", "Waiting Review", "Paused"}
            ],
            "continuous_learning_queue": [
                t
                for t in (queue_snapshot.get("tasks") or [])
                if t.get("kind") == "continuous"
            ],
            "learning_timeline": self.recent_events(30),
            "knowledge_feed": self.recent_events(20),
            "brain_activity": {
                "ticks": data.get("ticks", 0),
                "tasks_dispatched": data.get("tasks_dispatched", 0),
                "continuous_cycles": data.get("continuous_cycles", 0),
                "directed_cycles": data.get("directed_cycles", 0),
                "missions_completed": data.get("missions_completed", 0),
            },
            "learning_history": (data.get("learning_history") or [])[-50:],
            "queue": queue_snapshot,
            "placeholders": {
                "reasoning_coverage": "Waiting for first execution",
                "decision_coverage": "Waiting for first execution",
            },
            "architecture": {
                "entry": "ContinuousLearningScheduler",
                "flow": [
                    "Scheduler",
                    "PriorityEngine",
                    "Planner",
                    "Policy",
                    "Pipeline",
                    "Review",
                    "Publisher",
                    "Telemetry",
                ],
                "rules": self.config.get("rules") or {},
            },
        }
