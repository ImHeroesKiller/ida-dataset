"""Manufacturing Controller — continuous knowledge demand → dynamic missions."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional

from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root
from automation.manufacturing.capacity import collect_capacity
from automation.manufacturing.economics import collect_economics
from automation.manufacturing.knowledge_gap import evaluate_dataset, rank_datasets
from automation.manufacturing.modes import detect_mode, mode_mission_prefix
from automation.manufacturing.targets import load_dynamic_targets

# Datasets the factory manufactures (aligned with mission catalog)
MANUFACTURED_DATASETS = [
    "industry_library",
    "company_profile",
    "product_catalog",
    "service_library",
    "pain_point_library",
    "solution_library",
    "framework_library",
    "case_study_library",
    "opportunity_analysis",
    "competitor_library",
    "business_signal_library",
    "buyer_persona_library",
    "decision_maker_library",
    "regulation_library",
    "risk_library",
    "trend_library",
    "discovery_question_library",
]


# Mission templates driven by knowledge demand (not a finish line).
# Enterprise-function-aware topics are preferred via enterprise_functions module;
# these remain fallbacks when taxonomy is unavailable.
_TOPIC_HINTS = {
    "industry_library": [
        "Manufacturing Industry Indonesia",
        "Financial Services Industry Indonesia",
        "Digital Economy Indonesia",
        "Healthcare Services Indonesia",
        "Logistics Industry Indonesia",
        "Energy Industry Indonesia",
    ],
    "company_profile": [
        "Manufacturing Companies Indonesia",
        "Banking Companies Indonesia",
        "Technology Companies Indonesia",
        "Logistics Companies Indonesia",
    ],
    "product_catalog": [
        "Manufacturing Products Indonesia",
        "Digital Products Indonesia",
        "Industrial Equipment Catalog",
    ],
    "service_library": [
        "Managed IT Services Indonesia",
        "BPO Services Indonesia",
        "Logistics Services Indonesia",
        "HR Outsourcing Indonesia",
    ],
    "business_signal_library": [
        "New OECD Publications",
        "World Bank Indonesia Reports",
        "OJK Regulatory Signals",
        "ILO Labor Signals",
        "NIST Cybersecurity Signals",
    ],
    "pain_point_library": [
        "Manufacturing Pain Points Indonesia",
        "Finance Operations Pain Points",
        "IT Security Pain Points",
        "HR Recruitment Pain Points",
        "Supply Chain Pain Points",
    ],
    "solution_library": [
        "Predictive Maintenance Solutions",
        "Digital Banking Solutions",
        "Cybersecurity Solutions",
        "Procurement Automation Solutions",
    ],
    "framework_library": [
        "NIST Cybersecurity Framework",
        "ISO Quality Frameworks",
        "OECD Governance Frameworks",
        "ILO Labor Frameworks",
        "GRI ESG Frameworks",
    ],
    "buyer_persona_library": [
        "HR Director Buyer Persona Indonesia",
        "CFO Finance Buyer Persona Indonesia",
        "IT Director Buyer Persona Indonesia",
        "Plant Manager Buyer Persona Indonesia",
        "Procurement Head Buyer Persona Indonesia",
        "Legal Counsel Buyer Persona Indonesia",
    ],
    "decision_maker_library": [
        "Finance Decision Maker Patterns Indonesia",
        "IT Decision Maker Patterns Indonesia",
        "Operations Decision Maker Patterns Indonesia",
        "HR Decision Maker Patterns Indonesia",
    ],
    "regulation_library": [
        "OJK Financial Regulations",
        "Kemnaker Employment Regulations",
        "Tax Regulations Indonesia",
        "Data Privacy Regulations",
        "Environmental Regulations Indonesia",
        "Procurement Regulations LKPP",
    ],
    "risk_library": [
        "Cybersecurity Risk Indonesia",
        "Treasury Liquidity Risk",
        "Supply Chain Risk Manufacturing",
        "Employment Relations Risk",
        "ESG Climate Risk",
    ],
    "trend_library": [
        "Cybersecurity Trends",
        "Treasury Digitalization Trends",
        "Manufacturing Automation Trends",
        "Recruitment Trends Indonesia",
        "ESG Reporting Trends",
        "AI Enterprise Adoption Trends",
    ],
    "competitor_library": [
        "Competitor Landscape Manufacturing Indonesia",
        "Competitor Landscape Banking Indonesia",
        "Competitor Landscape Technology Indonesia",
    ],
}


def _counts(repo: Path) -> dict[str, int]:
    import csv

    bd = repo / "domains" / "business_development"

    def n(name: str, *, service: bool | None = None) -> int:
        p = bd / f"{name}.csv"
        if name == "service_library":
            p = bd / "product_catalog.csv"
        if not p.exists():
            return 0
        with p.open(encoding="utf-8-sig", newline="") as f:
            rows = list(csv.DictReader(f))
        if service is True:
            return sum(1 for r in rows if "service" in (r.get("Product Type") or "").lower())
        if service is False:
            return sum(1 for r in rows if "service" not in (r.get("Product Type") or "").lower())
        return len(rows)

    return {
        "industry_library": n("industry_library"),
        "company_profile": n("company_profile"),
        "product_catalog": n("product_catalog", service=False),
        "service_library": n("service_library", service=True),
        "pain_point_library": n("pain_point_library"),
        "solution_library": n("solution_library"),
        "framework_library": n("framework_library"),
        "case_study_library": n("case_study_library"),
        "opportunity_analysis": n("opportunity_analysis"),
        "competitor_library": n("competitor_library"),
        "business_signal_library": n("business_signal_library"),
        "buyer_persona_library": n("buyer_persona_library"),
        "decision_maker_library": n("decision_maker_library"),
        "regulation_library": n("regulation_library"),
        "risk_library": n("risk_library"),
        "trend_library": n("trend_library"),
        "discovery_question_library": n("discovery_question_library"),
    }


def _pick_topic(dataset: str, mode: str, evaluation: dict[str, Any]) -> str:
    # Prefer enterprise-function-balanced topic (all functions, not BD-only)
    try:
        from automation.manufacturing.enterprise_functions import (
            enrich_mission_instruction,
        )

        enriched = enrich_mission_instruction(
            dataset,
            "",
            current_rows=int(evaluation.get("current_rows") or 0),
        )
        topic = str(enriched.get("title") or "")
        if topic:
            prefix = mode_mission_prefix(mode)
            if mode == "MAINTENANCE":
                return f"{prefix} {topic}"
            if mode == "CONTINUOUS":
                return f"{prefix} publications for {topic}"
            return f"{prefix} {topic}"
    except Exception:  # noqa: BLE001
        pass
    hints = _TOPIC_HINTS.get(dataset) or [dataset.replace("_", " ").title()]
    # rotate by row count for variety across enterprise contexts
    idx = int(evaluation.get("current_rows") or 0) % len(hints)
    topic = hints[idx]
    prefix = mode_mission_prefix(mode)
    if mode == "MAINTENANCE":
        return f"{prefix} {topic}"
    if mode == "CONTINUOUS":
        return f"{prefix} publications for {topic}"
    return f"{prefix} {topic}"


def _should_pause(economics: dict[str, Any], evaluations: list[dict[str, Any]]) -> dict[str, Any]:
    """Pause only for real operational reasons — never numeric target alone."""
    # No trusted knowledge signal: all universe gaps zero AND no empty datasets
    total_opp = sum(int(e.get("knowledge_opportunity") or 0) for e in evaluations)
    if total_opp <= 0 and all(int(e.get("current_rows") or 0) > 0 for e in evaluations):
        # still continuous — signals may publish tomorrow
        return {"pause": False, "reason": "continue_awaiting_new_publications"}
    return {"pause": False, "reason": "manufacturing_active"}


class ManufacturingController:
    def __init__(self, repo_root: Path | None = None):
        self.repo_root = repo_root or find_repo_root()

    def evaluate(self) -> dict[str, Any]:
        counts = _counts(self.repo_root)
        evaluations = rank_datasets(
            MANUFACTURED_DATASETS, counts=counts, repo_root=self.repo_root
        )
        mode = detect_mode(evaluations)
        economics = collect_economics(self.repo_root)
        capacity = collect_capacity(self.repo_root)
        pause = _should_pause(economics, evaluations)
        targets = load_dynamic_targets(self.repo_root)

        # Dynamic mission proposals (never empty while work exists)
        # Balanced across Enterprise Function × Dataset knowledge gaps.
        missions: list[dict[str, Any]] = []
        for e in evaluations[:8]:
            ds = e["dataset"]
            ef_meta: dict[str, Any] = {}
            try:
                from automation.manufacturing.enterprise_functions import (
                    enrich_mission_instruction,
                )

                ef_meta = enrich_mission_instruction(
                    ds,
                    "",
                    current_rows=int(e.get("current_rows") or 0),
                )
            except Exception:  # noqa: BLE001
                ef_meta = {}
            topic = _pick_topic(ds, mode["mode"], e)
            instruction = (
                f"{topic} — continuous knowledge manufacturing for {ds} "
                f"(gap_score={e.get('knowledge_gap_score')}, "
                f"universe_remaining={e.get('universe_gap')}, mode={mode['mode']}"
                f", enterprise_function={ef_meta.get('enterprise_function') or 'multi'})"
            )
            if ef_meta.get("instruction"):
                instruction = (
                    f"{ef_meta['instruction']}; dataset_gap={e.get('knowledge_gap_score')}; "
                    f"mode={mode['mode']}"
                )
                if ef_meta.get("title"):
                    # Keep mode prefix from _pick_topic when useful
                    topic = str(ef_meta["title"])
            missions.append(
                {
                    "dataset": ds,
                    "title": topic,
                    "instruction": instruction,
                    "mode": mode["mode"],
                    "knowledge_gap_score": e.get("knowledge_gap_score"),
                    "universe_gap": e.get("universe_gap"),
                    "current_rows": e.get("current_rows"),
                    "stretch_target": (e.get("profile") or {}).get("stretch_target"),
                    "minimum_target": (e.get("profile") or {}).get("minimum_target"),
                    "hard_limit": (e.get("profile") or {}).get("hard_limit"),
                    "enterprise_function": ef_meta.get("enterprise_function"),
                    "enterprise_function_name": ef_meta.get("enterprise_function_name"),
                    "discovery_queries": ef_meta.get("discovery_queries") or [],
                    "function_gap_score": ef_meta.get("function_gap_score"),
                    "priority_reason": (
                        f"mode={mode['mode']}; gap_score={e.get('knowledge_gap_score')}; "
                        f"opportunity={e.get('knowledge_opportunity')}; "
                        f"enterprise_function={ef_meta.get('enterprise_function') or 'multi'}"
                    ),
                }
            )

        top = evaluations[0] if evaluations else {}
        top_mission = missions[0] if missions else None

        state = {
            "version": "1.0",
            "updated_at": utc_now_iso(),
            "continuous_manufacturing": True,
            "never_stop_at_numeric_target": bool(
                targets.get("never_stop_at_numeric_target", True)
            ),
            "mode": mode,
            "pause": pause,
            "counts": counts,
            "evaluations": evaluations,
            "proposed_missions": missions,
            "selected_mission": top_mission,
            "economics": economics,
            "capacity": capacity,
            "growth": {
                "growth_velocity": capacity.get("growth_velocity_rows_per_day"),
                "coverage_velocity": capacity.get("rows_per_day"),
                "freshness_velocity": None,
                "knowledge_produced_total": sum(counts.values()),
            },
            "top_dataset": top.get("dataset"),
            "knowledge_gap_summary": {
                "highest_gap_dataset": top.get("dataset"),
                "highest_gap_score": top.get("knowledge_gap_score"),
                "total_universe_remaining": sum(
                    int(e.get("universe_gap") or 0) for e in evaluations
                ),
            },
            "governance": (
                "IDA Dataset Factory has no predefined finish line. "
                "Success is knowledge growth, coverage, freshness, confidence, quality. "
                "Business Development is one enterprise function among the full taxonomy."
            ),
        }
        # Enterprise function generalization metrics (additive; freeze-compliant)
        try:
            from automation.manufacturing.enterprise_functions import (
                build_enterprise_state,
            )

            state["enterprise_functions"] = build_enterprise_state(self.repo_root)
        except Exception:  # noqa: BLE001
            state["enterprise_functions"] = {"error": "unavailable"}
        return state

    def persist(self, state: dict[str, Any] | None = None) -> dict[str, Any]:
        state = state or self.evaluate()
        path = (
            self.repo_root
            / "automation"
            / "learning"
            / "state"
            / "manufacturing_state.json"
        )
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(state, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        try:
            from automation.manufacturing.reports import write_manufacturing_reports

            write_manufacturing_reports(state, repo_root=self.repo_root)
        except Exception:  # noqa: BLE001
            pass
        try:
            from automation.manufacturing.enterprise_functions import (
                write_enterprise_reports,
                run_enterprise_generalization,
            )

            # Persist full enterprise snapshot + markdown reports
            run_enterprise_generalization(self.repo_root)
            if state.get("enterprise_functions"):
                write_enterprise_reports(
                    state.get("enterprise_functions"), repo_root=self.repo_root
                )
        except Exception:  # noqa: BLE001
            pass
        return state

    def next_mission(self) -> dict[str, Any]:
        state = self.persist()
        return {
            "ok": True,
            "mode": state.get("mode"),
            "selected": state.get("selected_mission"),
            "proposed": state.get("proposed_missions"),
            "pause": state.get("pause"),
            "knowledge_gap_summary": state.get("knowledge_gap_summary"),
            "capacity": state.get("capacity"),
            "economics": state.get("economics"),
        }


def run_manufacturing_cycle(repo_root: Path | None = None) -> dict[str, Any]:
    return ManufacturingController(repo_root=repo_root).persist()
