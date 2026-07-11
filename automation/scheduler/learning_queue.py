"""Unified learning queue: continuous, directed, maintenance, ontology, policy."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

from .config_loader import read_json, resolve_path, write_json
from .models import LearningTask, LearningStream, TaskKind, utc_now_iso


class LearningQueue:
    def __init__(self, config: dict[str, Any]):
        self.config = config
        self.path: Path = resolve_path(
            config, "learning_queue", "automation/scheduler/state/learning_queue.json"
        )

    def load(self) -> list[LearningTask]:
        raw = read_json(self.path, {"tasks": []})
        tasks = [LearningTask.from_dict(t) for t in raw.get("tasks") or []]
        return tasks

    def save(self, tasks: list[LearningTask]) -> None:
        write_json(
            self.path,
            {
                "updated_at": utc_now_iso(),
                "count": len(tasks),
                "tasks": [t.to_dict() for t in tasks],
            },
        )

    def upsert(self, task: LearningTask) -> list[LearningTask]:
        tasks = self.load()
        found = False
        for i, t in enumerate(tasks):
            if t.task_id == task.task_id:
                task.updated_at = utc_now_iso()
                tasks[i] = task
                found = True
                break
        if not found:
            tasks.append(task)
        self.save(tasks)
        return tasks

    def remove(self, task_id: str) -> list[LearningTask]:
        tasks = [t for t in self.load() if t.task_id != task_id]
        self.save(tasks)
        return tasks

    def get(self, task_id: str) -> Optional[LearningTask]:
        for t in self.load():
            if t.task_id == task_id:
                return t
        return None

    def seed_continuous_catalog(self) -> list[LearningTask]:
        """Ensure continuous catalog tasks exist in the queue."""
        catalog = self.config.get("continuous_catalog") or []
        tasks = self.load()
        existing = {t.task_id for t in tasks}
        for item in catalog:
            tid = str(item.get("task_id") or "")
            if not tid or tid in existing:
                continue
            task = LearningTask(
                task_id=tid,
                title=str(item.get("title") or tid),
                kind=TaskKind.CONTINUOUS.value,
                priority=str(item.get("priority") or "P3"),
                stream=LearningStream.CONTINUOUS.value,
                status="queued",
                target_dataset=str(item.get("target_dataset") or ""),
                domain=str(item.get("domain") or ""),
                estimated_effort=float(item.get("estimated_effort") or 1.0),
                metadata={
                    "source": "continuous_catalog",
                    "enterprise_function": str(
                        item.get("enterprise_function") or "multi"
                    ),
                },
            )
            tasks.append(task)
            existing.add(tid)
        self.save(tasks)
        return tasks

    def by_kind(self, kind: str) -> list[LearningTask]:
        return [t for t in self.load() if t.kind == kind]

    def snapshot(self) -> dict[str, Any]:
        tasks = self.load()
        counts: dict[str, int] = {}
        for t in tasks:
            counts[t.kind] = counts.get(t.kind, 0) + 1
        return {
            "total": len(tasks),
            "by_kind": counts,
            "queued": sum(1 for t in tasks if t.status == "queued"),
            "running": sum(1 for t in tasks if t.status == "running"),
            "tasks": [t.to_dict() for t in tasks],
        }
