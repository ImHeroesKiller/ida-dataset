"""Continuous Learning Scheduler — single entry point above Planner.

Nothing starts the Planner directly. Humans create missions; continuous
catalog seeds gap-closing tasks; the scheduler allocates resources and
dispatches the highest-priority executable work into the controlled pipeline path.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any, Optional

from .config_loader import load_learning_config, resolve_path, write_json
from .learning_queue import LearningQueue
from .mission_dispatcher import MissionDispatcher
from .models import (
    LearningStream,
    Mission,
    MissionStatus,
    SchedulerEvent,
    utc_now_iso,
)
from .priority_engine import PriorityEngine
from .resource_allocator import ResourceAllocator
from .scheduler_metrics import SchedulerMetrics


class ContinuousLearningScheduler:
    """Central orchestrator for Continuous + Directed learning."""

    def __init__(self, repo_root: Path | None = None, config: dict[str, Any] | None = None):
        self.config = config or load_learning_config(repo_root)
        self.repo_root = Path(self.config["_repo_root"])
        self.allocator = ResourceAllocator(self.config)
        self.priority = PriorityEngine(self.config)
        self.queue = LearningQueue(self.config)
        self.missions = MissionDispatcher(self.config)
        self.metrics = SchedulerMetrics(self.config)
        self.state_path = resolve_path(
            self.config, "scheduler_state", "automation/scheduler/state/scheduler_state.json"
        )
        self.reports_dir = resolve_path(
            self.config, "learning_reports", "reports/learning"
        )
        self.reports_dir.mkdir(parents=True, exist_ok=True)
        (self.state_path.parent).mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # Telemetry helpers
    # ------------------------------------------------------------------
    def _emit(
        self,
        event: str,
        detail: str,
        *,
        stream: str = "system",
        mission_id: str | None = None,
        task_id: str | None = None,
    ) -> None:
        self.metrics.record_event(
            SchedulerEvent(
                ts=utc_now_iso(),
                event=event,
                stream=stream,
                detail=detail,
                mission_id=mission_id,
                task_id=task_id,
            )
        )

    def _refresh_knowledge_growth(self) -> dict[str, Any]:
        domains = self.repo_root / "domains"
        total = 0
        populated = 0
        if domains.exists():
            for path in domains.rglob("*.csv"):
                total += 1
                try:
                    text = path.read_text(encoding="utf-8-sig")
                    rows = list(csv.reader(text.splitlines()))
                    if len(rows) > 1:
                        populated += 1
                except OSError:
                    continue
        coverage = round((populated / total) * 100, 1) if total else 0.0
        self.metrics.set_knowledge_growth(
            populated=populated, total=total, coverage_pct=coverage
        )
        return {
            "datasets_total": total,
            "datasets_populated": populated,
            "coverage_pct": coverage,
        }

    # ------------------------------------------------------------------
    # Mission API (human instruction entry)
    # ------------------------------------------------------------------
    def submit_mission_text(
        self,
        text: str,
        *,
        requester: str = "human",
        priority: Optional[str] = None,
        auto_queue: bool = True,
    ) -> dict[str, Any]:
        """Human natural-language mission → structured mission + contract."""
        mission = self.missions.parse_natural_language(
            text, requester=requester, priority=priority
        )
        self.missions.save_mission(mission)
        self._emit(
            "mission_created",
            f"Mission {mission.mission_id}: {mission.title}",
            stream="directed",
            mission_id=mission.mission_id,
        )

        result: dict[str, Any] = {"mission": mission.to_dict(), "contract": None, "task": None}
        if auto_queue:
            result.update(self.queue_mission(mission.mission_id))
        return result

    def queue_mission(self, mission_id: str) -> dict[str, Any]:
        mission = self.missions.load_mission(mission_id)
        if not mission:
            raise ValueError(f"Mission not found: {mission_id}")

        # Allocation snapshot to stamp resource share
        all_missions = self.missions.list_missions()
        allocation = self.allocator.allocate(all_missions + [mission])
        default_pct = float(
            (self.config.get("scheduler") or {}).get("default_mission_allocation_pct", 30)
        )
        share = min(allocation.directed, default_pct) if allocation.directed else default_pct

        mission, contract, task = self.missions.enqueue_mission(
            mission, resource_allocation=share
        )
        self.queue.upsert(task)
        self.metrics.update_allocation(allocation)
        self._emit(
            "mission_dispatched",
            f"Queued {mission.mission_id} with directed allocation hint {share}%",
            stream="directed",
            mission_id=mission.mission_id,
            task_id=task.task_id,
        )
        self._emit(
            "learning_contract_created",
            f"Contract {contract.contract_id} for {mission.mission_id}",
            stream="directed",
            mission_id=mission.mission_id,
        )
        return {
            "mission": mission.to_dict(),
            "contract": contract.to_dict(),
            "task": task.to_dict(),
            "allocation": allocation.to_dict(),
        }

    # ------------------------------------------------------------------
    # Scheduler tick
    # ------------------------------------------------------------------
    def tick(self, *, dry_run: bool = True) -> dict[str, Any]:
        """One scheduler cycle. Always keeps continuous learning alive."""
        if not self.config.get("enabled", True):
            self._emit("scheduler_disabled", "Scheduler disabled in learning.yaml")
            return {"ok": False, "reason": "scheduler_disabled"}

        # Continuous Learning never stops — always re-seed catalog
        self.queue.seed_continuous_catalog()
        self._emit(
            "continuous_learning_active",
            "Continuous learning catalog ensured in queue",
            stream="continuous",
        )

        missions = self.missions.list_missions()
        allocation = self.allocator.allocate(missions)
        self.metrics.update_allocation(allocation)
        self._emit(
            "allocation_updated",
            f"profile={allocation.profile} continuous={allocation.continuous}% directed={allocation.directed}%",
            stream="system",
        )

        growth = self._refresh_knowledge_growth()
        tasks = self.queue.load()
        selected = self.priority.select_executable(
            tasks,
            allocation=allocation.as_percent_map(),
            limit=int((self.config.get("scheduler") or {}).get("max_tasks_per_tick", 5)),
        )

        dispatched: list[dict[str, Any]] = []
        for task in selected:
            task.status = "running"
            task.progress = max(task.progress, 5.0)
            task.updated_at = utc_now_iso()
            self.queue.upsert(task)

            if task.kind == "directed" and task.mission_id:
                self.missions.update_status(
                    task.mission_id,
                    MissionStatus.RUNNING.value,
                    current_stage="scheduler_selected",
                    current_dataset=task.target_dataset,
                    progress=max(task.progress, 5.0),
                )
                self._emit(
                    "planner_handoff_directed",
                    f"Scheduler selected directed task {task.task_id} → Planner path",
                    stream="directed",
                    mission_id=task.mission_id,
                    task_id=task.task_id,
                )
                self.metrics.bump(directed_cycles=1, tasks_dispatched=1)
            else:
                self._emit(
                    "planner_selected_continuous",
                    f"Scheduler selected continuous task {task.title} ({task.target_dataset})",
                    stream="continuous",
                    task_id=task.task_id,
                )
                self.metrics.bump(continuous_cycles=1, tasks_dispatched=1)

            # Architecture handoff (no crawler/LLM): mark as waiting for planner/pipeline
            # under human-controlled KAS — dry_run records intent only.
            stage = "awaiting_planner"
            if dry_run:
                stage = "dry_run_scheduled"
                task.progress = min(task.progress + 10.0, 40.0)
                task.status = "queued"  # return to queue after dry intent
                self._emit(
                    "dry_run_tick",
                    f"Dry-run: would invoke Planner for {task.task_id} (policies still apply)",
                    stream=task.stream,
                    mission_id=task.mission_id,
                    task_id=task.task_id,
                )
            else:
                # Real handoff flag — actual planner remains external KAS module
                task.metadata["handoff"] = "knowledge_planner"
                task.metadata["policy_required"] = True
                task.metadata["review_required"] = True
                task.status = "awaiting_planner"
                task.progress = min(task.progress + 15.0, 60.0)
                self._emit(
                    "pipeline_handoff",
                    f"Task {task.task_id} handed to Planner → Policy → Pipeline → Review → Publisher",
                    stream=task.stream,
                    mission_id=task.mission_id,
                    task_id=task.task_id,
                )

            task.updated_at = utc_now_iso()
            self.queue.upsert(task)
            dispatched.append(
                {
                    "task": task.to_dict(),
                    "stage": stage,
                    "dry_run": dry_run,
                }
            )

        self.metrics.bump(ticks=1)
        state = {
            "last_tick_at": utc_now_iso(),
            "dry_run": dry_run,
            "allocation": allocation.to_dict(),
            "dispatched": dispatched,
            "knowledge_growth": growth,
            "rules": self.config.get("rules") or {},
        }
        write_json(self.state_path, state)

        # Always reaffirm continuous learning remains active after directed work
        self._emit(
            "continuous_learning_resumed",
            "Continuous learning remains active after tick",
            stream="continuous",
        )

        report = self.write_tick_report(state)
        return {
            "ok": True,
            "state": state,
            "report": str(report),
            "dashboard": self.dashboard(),
        }

    def write_tick_report(self, state: dict[str, Any]) -> Path:
        ts = utc_now_iso().replace(":", "").replace("-", "")
        path = self.reports_dir / f"scheduler_tick_{ts}.json"
        write_json(path, state)
        # also latest pointer
        write_json(self.reports_dir / "latest_tick.json", state)
        return path

    def complete_mission(
        self,
        mission_id: str,
        *,
        result: str = "",
        executive_summary: str = "",
    ) -> dict[str, Any]:
        mission = self.missions.update_status(
            mission_id,
            MissionStatus.COMPLETED.value,
            progress=100.0,
            result=result or "Mission completed via scheduler",
            executive_summary=executive_summary or "",
            current_stage="completed",
        )
        if not mission:
            raise ValueError(f"Mission not found: {mission_id}")
        # remove directed task
        self.queue.remove(f"DIR-{mission_id}")
        self.metrics.bump(missions_completed=1)
        self._emit(
            "mission_completed",
            f"Mission {mission_id} completed; continuous learning continues",
            stream="directed",
            mission_id=mission_id,
        )
        self._emit(
            "continuous_learning_resumed",
            "Continuous learning active after mission completion",
            stream="continuous",
        )
        report = self._write_mission_report(mission)
        return {"mission": mission.to_dict(), "report": str(report)}

    def _write_mission_report(self, mission: Mission) -> Path:
        path = self.reports_dir / f"mission_{mission.mission_id}.json"
        write_json(
            path,
            {
                "type": "mission_report",
                "generated_at": utc_now_iso(),
                "mission": mission.to_dict(),
                "architecture": "Scheduler → Planner → Policy → Pipeline → Review → Publisher",
            },
        )
        # markdown brief
        md = self.reports_dir / f"mission_{mission.mission_id}.md"
        md.write_text(
            "\n".join(
                [
                    f"# Mission Report — {mission.title}",
                    "",
                    f"- **Mission ID:** `{mission.mission_id}`",
                    f"- **Priority:** {mission.priority}",
                    f"- **Status:** {mission.status}",
                    f"- **Requester:** {mission.requester}",
                    f"- **Progress:** {mission.progress}%",
                    f"- **Confidence:** {mission.confidence}",
                    f"- **Contract:** {mission.contract_id or '—'}",
                    "",
                    "## Objective",
                    "",
                    mission.description,
                    "",
                    "## Knowledge Targets",
                    "",
                ]
                + ([f"- {t}" for t in mission.knowledge_targets] or ["- —"])
                + [
                    "",
                    "## Related Datasets",
                    "",
                ]
                + ([f"- `{d}`" for d in mission.related_datasets] or ["- —"])
                + [
                    "",
                    "## Result",
                    "",
                    mission.result or "Waiting for first execution",
                    "",
                    "## Executive Summary",
                    "",
                    mission.executive_summary or "Placeholder — awaiting review pack",
                    "",
                    "## Architecture",
                    "",
                    "Scheduler is the single entry point. Continuous learning never stops.",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        return path

    def write_growth_report(self) -> Path:
        growth = self._refresh_knowledge_growth()
        path = self.reports_dir / "learning_growth_report.json"
        write_json(
            path,
            {
                "type": "learning_growth_report",
                "generated_at": utc_now_iso(),
                "growth": growth,
                "metrics": self.metrics.load(),
            },
        )
        md = self.reports_dir / "learning_growth_report.md"
        md.write_text(
            "\n".join(
                [
                    "# Learning Growth Report",
                    "",
                    f"- Generated: {utc_now_iso()}",
                    f"- Datasets total: {growth['datasets_total']}",
                    f"- Datasets populated: {growth['datasets_populated']}",
                    f"- Coverage: {growth['coverage_pct']}%",
                    "",
                    "Continuous Learning remains active.",
                    "",
                ]
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        return path

    def dashboard(self) -> dict[str, Any]:
        missions = self.missions.list_missions()
        allocation = self.allocator.allocate(missions)
        queue_snap = self.queue.snapshot()
        selected = self.priority.select_executable(
            self.queue.load(),
            allocation=allocation.as_percent_map(),
            limit=1,
        )
        current_task = selected[0].to_dict() if selected else None
        return self.metrics.dashboard_snapshot(
            allocation=allocation,
            missions=missions,
            queue_snapshot=queue_snap,
            current_task=current_task,
        )
