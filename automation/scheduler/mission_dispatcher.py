"""Mission dispatcher — converts human requests into missions + queue tasks + contracts."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Optional

from .config_loader import read_json, resolve_path, write_json
from .models import (
    LearningContract,
    LearningStream,
    LearningTask,
    Mission,
    MissionPriority,
    MissionStatus,
    TaskKind,
    utc_now_iso,
)


# Lightweight NL → structured mission heuristics (no LLM)
_NL_PATTERNS: list[tuple[re.Pattern[str], dict[str, Any]]] = [
    (
        re.compile(r"\bSAP\b|\bERP\b", re.I),
        {
            "title": "Learn SAP ERP",
            "targets": ["Product", "Technology", "Framework", "Pain Point"],
            "datasets": ["product_catalog", "framework_library", "pain_point_library"],
            "priority": MissionPriority.P1.value,
        },
    ),
    (
        re.compile(r"telkom", re.I),
        {
            "title": "Prepare for Telkom meeting",
            "targets": ["Company", "Opportunity", "Competitor", "Industry"],
            "datasets": ["company_profile", "opportunity_analysis", "competitor_library"],
            "priority": MissionPriority.P0.value,
        },
    ),
    (
        re.compile(r"mining|pertambangan", re.I),
        {
            "title": "Study Indonesian Mining Industry",
            "targets": ["Industry", "Company", "Regulation", "Pain Point"],
            "datasets": ["industry_library", "company_profile", "pain_point_library"],
            "priority": MissionPriority.P1.value,
        },
    ),
    (
        re.compile(r"\bPLN\b|listrik", re.I),
        {
            "title": "Study Annual Report PLN",
            "targets": ["Company", "Document", "KPI", "Risk"],
            "datasets": ["company_profile", "case_study_library"],
            "priority": MissionPriority.P1.value,
        },
    ),
    (
        re.compile(r"gartner|technology trends", re.I),
        {
            "title": "Study Gartner Technology Trends",
            "targets": ["Technology", "Framework", "Business Signal"],
            "datasets": ["framework_library", "business_signal_library"],
            "priority": MissionPriority.P2.value,
        },
    ),
    (
        re.compile(r"cyber|keamanan|security regulation", re.I),
        {
            "title": "Focus on cyber security regulations",
            "targets": ["Regulation", "Standard", "Risk"],
            "datasets": ["framework_library", "pain_point_library"],
            "priority": MissionPriority.P1.value,
        },
    ),
]


class MissionDispatcher:
    def __init__(self, config: dict[str, Any]):
        self.config = config
        self.active_dir: Path = resolve_path(
            config, "missions_active", "automation/missions/missions"
        )
        self.history_dir: Path = resolve_path(
            config, "missions_history", "automation/missions/history"
        )
        self.contracts_dir: Path = resolve_path(
            config, "missions_contracts", "automation/missions/contracts"
        )
        self.templates_dir: Path = resolve_path(
            config, "missions_templates", "automation/missions/templates"
        )
        for d in (
            self.active_dir,
            self.history_dir,
            self.contracts_dir,
            self.templates_dir,
        ):
            d.mkdir(parents=True, exist_ok=True)

    def _mission_path(self, mission_id: str, *, history: bool = False) -> Path:
        base = self.history_dir if history else self.active_dir
        return base / f"{mission_id}.json"

    def save_mission(self, mission: Mission) -> Path:
        mission.updated_at = utc_now_iso()
        path = self._mission_path(mission.mission_id)
        write_json(path, mission.to_dict())
        return path

    def load_mission(self, mission_id: str) -> Optional[Mission]:
        path = self._mission_path(mission_id)
        if not path.exists():
            hist = self._mission_path(mission_id, history=True)
            if not hist.exists():
                return None
            return Mission.from_dict(read_json(hist, {}))
        return Mission.from_dict(read_json(path, {}))

    def list_missions(self, *, include_history: bool = False) -> list[Mission]:
        missions: list[Mission] = []
        for path in sorted(self.active_dir.glob("MIS-*.json")):
            missions.append(Mission.from_dict(read_json(path, {})))
        if include_history:
            for path in sorted(self.history_dir.glob("MIS-*.json")):
                missions.append(Mission.from_dict(read_json(path, {})))
        return missions

    def parse_natural_language(
        self,
        text: str,
        *,
        requester: str = "human",
        priority: Optional[str] = None,
    ) -> Mission:
        """Convert a natural human instruction into a structured Mission (no LLM)."""
        text = (text or "").strip()
        matched: Optional[dict[str, Any]] = None
        for pattern, meta in _NL_PATTERNS:
            if pattern.search(text):
                matched = meta
                break

        if matched:
            title = str(matched["title"])
            targets = list(matched.get("targets") or [])
            datasets = list(matched.get("datasets") or [])
            pri = priority or str(matched.get("priority") or MissionPriority.P2.value)
            description = f"Directed learning mission derived from: {text}"
        else:
            # Generic mission from free text
            title = text[:80] if text else "Untitled learning mission"
            if len(text) > 80:
                title = title.rsplit(" ", 1)[0] + "…"
            targets = ["Knowledge"]
            datasets = []
            pri = priority or MissionPriority.P2.value
            description = text

        mission = Mission.create(
            title=title,
            description=description,
            priority=pri,
            requester=requester,
            knowledge_targets=targets,
            related_datasets=datasets,
            natural_language_request=text,
        )
        return mission

    def create_contract(
        self,
        mission: Mission,
        *,
        resource_allocation: float,
        review_requirement: bool = True,
    ) -> LearningContract:
        contract = LearningContract.from_mission(
            mission,
            resource_allocation=resource_allocation,
            review_requirement=review_requirement,
        )
        write_json(self.contracts_dir / f"{contract.contract_id}.json", contract.to_dict())
        mission.contract_id = contract.contract_id
        return contract

    def enqueue_mission(
        self,
        mission: Mission,
        *,
        resource_allocation: float = 30.0,
    ) -> tuple[Mission, LearningContract, LearningTask]:
        """Activate mission: contract + queue task + status Queued."""
        if mission.status == MissionStatus.DRAFT.value:
            mission.status = MissionStatus.QUEUED.value
        contract = self.create_contract(
            mission, resource_allocation=resource_allocation
        )
        mission.resource_allocation = resource_allocation
        mission.current_stage = "queued_for_scheduler"
        self.save_mission(mission)

        task = LearningTask(
            task_id=f"DIR-{mission.mission_id}",
            title=mission.title,
            kind=TaskKind.DIRECTED.value,
            priority=mission.priority,
            stream=LearningStream.DIRECTED.value,
            status="queued",
            target_dataset=(mission.related_datasets[0] if mission.related_datasets else ""),
            domain="",
            mission_id=mission.mission_id,
            estimated_effort=mission.estimated_effort,
            metadata={
                "contract_id": contract.contract_id,
                "knowledge_targets": mission.knowledge_targets,
            },
        )
        return mission, contract, task

    def archive_mission(self, mission: Mission) -> Path:
        mission.status = MissionStatus.ARCHIVED.value
        mission.updated_at = utc_now_iso()
        active = self._mission_path(mission.mission_id)
        hist = self._mission_path(mission.mission_id, history=True)
        write_json(hist, mission.to_dict())
        if active.exists():
            active.unlink()
        return hist

    def update_status(self, mission_id: str, status: str, **fields: Any) -> Optional[Mission]:
        mission = self.load_mission(mission_id)
        if not mission:
            return None
        mission.status = status
        for k, v in fields.items():
            if hasattr(mission, k):
                setattr(mission, k, v)
        self.save_mission(mission)
        return mission
