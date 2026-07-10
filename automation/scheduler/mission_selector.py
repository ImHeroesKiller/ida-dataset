"""Dynamic mission selector — chooses next production mission without hardcoding.

Priority order (factory reliability sprint):
  Lowest Coverage → Highest Product Priority → Dependency Matrix
  → Trusted Source Availability → Factory Capacity → Mission Queue

Industry remains continuous only when it remains the highest-scoring eligible mission.
"""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from automation.lib.paths import find_repo_root

# Product priority (higher = more strategic for roadmap)
# Aligns with PRODUCTION_BATCH_LIBRARY official order after baselines.
CATALOG: list[dict[str, Any]] = [
    {
        "batch_id": "Batch-001",
        "dataset": "industry_library",
        "target_key": "industry_library",
        "path": "domains/business_development/industry_library.csv",
        "title": "Produce Industry Dataset",
        "instruction": "Produce Industry Dataset — expand industry_library toward product target",
        "product_priority": 100,
        "hard_deps": [],
        "min_baseline": 0,
    },
    {
        "batch_id": "Batch-002",
        "dataset": "service_library",
        "target_key": "service_library",
        "path": "domains/business_development/product_catalog.csv",
        "title": "Produce Service Dataset",
        "instruction": "Produce Service Dataset — expand service-type rows in product_catalog",
        "product_priority": 95,
        "hard_deps": ["industry_library"],
        "min_baseline": 50,  # industry baseline
        "service_type": True,
    },
    {
        "batch_id": "Batch-003",
        "dataset": "product_catalog",
        "target_key": "product_catalog",
        "path": "domains/business_development/product_catalog.csv",
        "title": "Produce Product Dataset",
        "instruction": "Produce Product Dataset — expand non-service product_catalog rows",
        "product_priority": 94,
        "hard_deps": ["industry_library"],
        "min_baseline": 50,
    },
    {
        "batch_id": "Batch-004",
        "dataset": "company_profile",
        "target_key": "company_profile",
        "path": "domains/business_development/company_profile.csv",
        "title": "Produce Company Dataset",
        "instruction": "Produce Company Dataset — expand company_profile toward product target",
        "product_priority": 93,
        "hard_deps": ["industry_library"],
        "min_baseline": 50,
    },
    {
        "batch_id": "Batch-005",
        "dataset": "pain_point_library",
        "target_key": "pain_point_library",
        "path": "domains/business_development/pain_point_library.csv",
        "title": "Produce Pain Point Dataset",
        "instruction": "Produce Pain Point Dataset — expand pain_point_library",
        "product_priority": 92,
        "hard_deps": ["industry_library", "company_profile"],
        "min_baseline": 25,
    },
    {
        "batch_id": "Batch-006",
        "dataset": "solution_library",
        "target_key": "solution_library",
        "path": "domains/business_development/solution_library.csv",
        "title": "Produce Solution Dataset",
        "instruction": "Produce Solution Dataset — expand solution_library linked to pains",
        "product_priority": 91,
        "hard_deps": ["pain_point_library"],
        "min_baseline": 25,
    },
    {
        "batch_id": "Batch-007",
        "dataset": "framework_library",
        "target_key": "framework_library",
        "path": "domains/business_development/framework_library.csv",
        "title": "Produce Framework Dataset",
        "instruction": "Produce Framework Dataset — expand framework_library",
        "product_priority": 80,
        "hard_deps": ["solution_library"],
        "min_baseline": 10,
    },
    {
        "batch_id": "Batch-008",
        "dataset": "case_study_library",
        "target_key": "case_study_library",
        "path": "domains/business_development/case_study_library.csv",
        "title": "Produce Case Study Dataset",
        "instruction": "Produce Case Study Dataset — expand case_study_library",
        "product_priority": 78,
        "hard_deps": ["company_profile", "solution_library"],
        "min_baseline": 25,
    },
    {
        "batch_id": "Batch-009",
        "dataset": "buyer_persona_library",
        "target_key": "buyer_persona_library",
        "path": "domains/business_development/discovery_question_library.csv",  # interim store until dedicated CSV
        "title": "Produce Buyer Persona Dataset",
        "instruction": "Produce Buyer Persona Dataset — structured buyer personas (Batch-009)",
        "product_priority": 96,  # next official empty class — high
        "hard_deps": ["industry_library", "company_profile"],
        "min_baseline": 25,
        "logical_only": True,  # may not have dedicated CSV yet
    },
    {
        "batch_id": "Batch-011",
        "dataset": "regulation_library",
        "target_key": "regulation_library",
        "path": "",
        "title": "Produce Regulation Dataset",
        "instruction": "Produce Regulation Dataset — regulation knowledge for industries (Batch-011)",
        "product_priority": 88,
        "hard_deps": ["industry_library"],
        "min_baseline": 50,
        "logical_only": True,
    },
    {
        "batch_id": "Batch-012",
        "dataset": "opportunity_analysis",
        "target_key": "opportunity_analysis",
        "path": "domains/business_development/opportunity_analysis.csv",
        "title": "Produce Opportunity Dataset",
        "instruction": "Produce Opportunity Dataset — expand opportunity_analysis with valid company FKs",
        "product_priority": 75,
        "hard_deps": ["company_profile", "pain_point_library", "solution_library"],
        "min_baseline": 25,
    },
    {
        "batch_id": "Batch-015",
        "dataset": "competitor_library",
        "target_key": "competitor_library",
        "path": "domains/business_development/competitor_library.csv",
        "title": "Produce Competitor Dataset",
        "instruction": "Produce Competitor Dataset — expand competitor_library",
        "product_priority": 70,
        "hard_deps": ["company_profile", "product_catalog"],
        "min_baseline": 20,
    },
]


def _load_targets(repo: Path) -> dict[str, int]:
    targets: dict[str, int] = {"_default": 100}
    p = repo / "automation/config/product_targets.yaml"
    if not p.exists():
        return targets
    in_t = False
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("targets:"):
            in_t = True
            continue
        if in_t:
            if line and not line[0].isspace() and not line.strip().startswith("#"):
                break
            m = re.match(r"\s+([A-Za-z0-9_]+):\s*(\d+)", line)
            if m:
                targets[m.group(1)] = int(m.group(2))
    return targets


def _row_count(path: Path, *, service_only: bool = False, non_service_only: bool = False) -> int:
    if not path.exists():
        return 0
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if service_only:
        return sum(1 for r in rows if "service" in (r.get("Product Type") or "").lower())
    if non_service_only:
        return sum(1 for r in rows if "service" not in (r.get("Product Type") or "").lower())
    return len(rows)


def _counts(repo: Path) -> dict[str, int]:
    bd = repo / "domains/business_development"
    return {
        "industry_library": _row_count(bd / "industry_library.csv"),
        "company_profile": _row_count(bd / "company_profile.csv"),
        "product_catalog": _row_count(bd / "product_catalog.csv"),
        "service_library": _row_count(bd / "product_catalog.csv", service_only=True),
        "pain_point_library": _row_count(bd / "pain_point_library.csv"),
        "solution_library": _row_count(bd / "solution_library.csv"),
        "framework_library": _row_count(bd / "framework_library.csv"),
        "case_study_library": _row_count(bd / "case_study_library.csv"),
        "opportunity_analysis": _row_count(bd / "opportunity_analysis.csv"),
        "competitor_library": _row_count(bd / "competitor_library.csv"),
        "buyer_persona_library": 0,  # dedicated store not yet present
        "regulation_library": 0,
        "discovery_question_library": _row_count(bd / "discovery_question_library.csv"),
        "business_signal_library": _row_count(bd / "business_signal_library.csv"),
    }


def _active_sources(repo: Path) -> int:
    reg = repo / "metadata/source_registry.csv"
    if not reg.exists():
        return 0
    n = 0
    with reg.open(encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            if str(r.get("Status") or "").lower() == "active" and str(
                r.get("Allowed") or ""
            ).lower() == "true":
                n += 1
    return n


def _deps_met(item: dict[str, Any], counts: dict[str, int]) -> bool:
    for dep in item.get("hard_deps") or []:
        # baselines
        if dep == "industry_library" and counts.get(dep, 0) < item.get("min_baseline", 0) and item["dataset"] != "industry_library":
            # for non-industry, require industry baseline 50 if listed
            if counts.get("industry_library", 0) < 50:
                return False
        elif dep == "company_profile" and counts.get(dep, 0) < 25:
            return False
        elif dep == "pain_point_library" and counts.get(dep, 0) < 1:
            return False
        elif dep == "solution_library" and counts.get(dep, 0) < 1:
            return False
        elif dep == "product_catalog" and counts.get(dep, 0) < 1:
            return False
        elif counts.get(dep, 0) < 1 and dep not in ("industry_library",):
            return False
    if item["dataset"] != "industry_library" and counts.get("industry_library", 0) < 50:
        # global root gate
        if "industry_library" in (item.get("hard_deps") or []) or item["batch_id"] != "Batch-001":
            if counts.get("industry_library", 0) < 50 and item["batch_id"] not in (
                "Batch-001",
            ):
                pass  # industry continuous still allowed
    return True


@dataclass
class SelectedMission:
    batch_id: str
    dataset: str
    title: str
    instruction: str
    coverage_pct: float
    current_rows: int
    product_target: int
    product_priority: int
    score: float
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "batch_id": self.batch_id,
            "dataset": self.dataset,
            "title": self.title,
            "instruction": self.instruction,
            "coverage_pct": self.coverage_pct,
            "current_rows": self.current_rows,
            "product_target": self.product_target,
            "product_priority": self.product_priority,
            "score": self.score,
            "reason": self.reason,
        }


def select_next_mission(repo_root: Path | None = None) -> dict[str, Any]:
    """Select highest-value next mission. Pure function of repo state + targets."""
    repo = Path(repo_root) if repo_root else find_repo_root()
    targets = _load_targets(repo)
    counts = _counts(repo)
    sources = _active_sources(repo)
    source_factor = 1.0 if sources >= 6 else 0.7 if sources >= 3 else 0.4

    # capacity: prefer lower coverage; if all high, still pick lowest
    ranked: list[dict[str, Any]] = []
    for item in CATALOG:
        key = item["target_key"]
        cur = counts.get(key, 0)
        if item.get("service_type"):
            cur = counts.get("service_library", 0)
        tgt = int(targets.get(key, targets.get("_default", 100)))
        cov = min(100.0, (cur / tgt) * 100.0) if tgt else 0.0
        deps_ok = _deps_met(item, counts)
        if not deps_ok:
            continue
        # skip fully covered
        if cov >= 100.0:
            continue
        # score: lower coverage dominates, then product priority
        # Industry only wins if its score is best — not forced continuous
        gap_weight = (100.0 - cov) / 100.0
        score = (
            gap_weight * 1000.0
            + float(item["product_priority"]) * 2.0
            + (50.0 if cov == 0 else 0.0)  # empty official classes
        ) * source_factor
        # slight boost for official next empty Batch-009 when deps met
        if item["batch_id"] == "Batch-009" and cur == 0:
            score += 200.0
        ranked.append(
            {
                "item": item,
                "cur": cur,
                "tgt": tgt,
                "cov": round(cov, 1),
                "score": round(score, 2),
            }
        )

    ranked.sort(key=lambda x: (-x["score"], x["cov"], -x["item"]["product_priority"]))

    if not ranked:
        # fallback industry maintenance
        item = CATALOG[0]
        sel = SelectedMission(
            batch_id=item["batch_id"],
            dataset=item["dataset"],
            title=item["title"],
            instruction=item["instruction"],
            coverage_pct=100.0,
            current_rows=counts.get("industry_library", 0),
            product_target=int(targets.get("industry_library", 250)),
            product_priority=item["product_priority"],
            score=0.0,
            reason="all_targets_met_or_blocked_fallback_industry",
        )
        return {
            "ok": True,
            "selected": sel.to_dict(),
            "ranking": [],
            "counts": counts,
            "active_sources": sources,
        }

    top = ranked[0]
    item = top["item"]
    sel = SelectedMission(
        batch_id=item["batch_id"],
        dataset=item["dataset"],
        title=item["title"],
        instruction=item["instruction"],
        coverage_pct=top["cov"],
        current_rows=top["cur"],
        product_target=top["tgt"],
        product_priority=item["product_priority"],
        score=top["score"],
        reason=(
            f"lowest_coverage={top['cov']}% · priority={item['product_priority']} · "
            f"deps_met · sources={sources}"
        ),
    )
    return {
        "ok": True,
        "selected": sel.to_dict(),
        "ranking": [
            {
                "batch_id": r["item"]["batch_id"],
                "dataset": r["item"]["dataset"],
                "coverage_pct": r["cov"],
                "score": r["score"],
            }
            for r in ranked[:8]
        ],
        "counts": counts,
        "active_sources": sources,
    }


def is_default_or_empty_instruction(text: str | None) -> bool:
    t = (text or "").strip().lower()
    if not t:
        return True
    defaults = (
        "learn industry library knowledge",
        "continuous learning session",
        "learn industry library knowledge — continuous learning session",
        "produce industry dataset — factory learn cycle",
    )
    return any(d in t for d in defaults) or t in {
        "continuous",
        "auto",
        "scheduler",
        "default",
    }
