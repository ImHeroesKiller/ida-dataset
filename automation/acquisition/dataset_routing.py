"""Dataset routing from mission instruction → target library.

Architecture-compatible: no redesign; pure resolve helpers used by
live_runtime, multi_stage_extract, and mission tooling.
"""

from __future__ import annotations

import re
from typing import Optional

# Canonical product datasets the factory manufactures
DATASET_ALIASES: dict[str, tuple[str, ...]] = {
    "industry_library": ("industry", "industri"),
    "company_profile": ("company", "companies", "perusahaan"),
    "product_catalog": ("product catalog", "product dataset", "products"),
    "service_library": ("service dataset", "services"),
    "pain_point_library": ("pain point", "pain points"),
    "solution_library": ("solution", "solutions"),
    "framework_library": ("framework", "frameworks"),
    "case_study_library": ("case study", "case studies"),
    "buyer_persona_library": ("buyer persona", "persona", "personas", "icp"),
    "decision_maker_library": ("decision maker", "decision-maker", "decision makers"),
    "regulation_library": ("regulation", "regulations", "regulatory", "law ", "undang"),
    "risk_library": ("risk library", "risk dataset", "risks", "risiko"),
    "trend_library": ("trend library", "trend dataset", "trends", "tren"),
    "competitor_library": ("competitor", "competitors", "kompetitor"),
    "opportunity_analysis": ("opportunity", "opportunities"),
    "business_signal_library": ("business signal", "signals"),
    "discovery_question_library": ("discovery question", "discovery questions"),
}

# Preferred query terms per dataset for connector search
DATASET_QUERY_HINTS: dict[str, str] = {
    "buyer_persona_library": "buyer persona industry workforce Indonesia employment skills",
    "decision_maker_library": "decision maker organization structure director executive Indonesia",
    "regulation_library": "regulation law policy Indonesia labor finance banking compliance",
    "risk_library": "risk assessment Indonesia economic operational regulatory risk",
    "trend_library": "industry trend Indonesia digital economy labour market outlook",
    "competitor_library": "company competitor market share Indonesia industry competition",
    "industry_library": "industry sector Indonesia",
    "company_profile": "company profile Indonesia annual report",
}


def resolve_dataset_from_instruction(
    instruction: str,
    *,
    default: str = "industry_library",
    explicit: Optional[str] = None,
) -> str:
    """Map mission text / explicit key to a canonical dataset stem.

    Instruction text wins when it names a library (mission selector path).
    Explicit is used when instruction does not name a dataset.
    """
    text = (instruction or "").lower()
    # Prefer longer / more specific matches first
    scored: list[tuple[int, str]] = []
    for dataset, aliases in DATASET_ALIASES.items():
        for alias in aliases:
            if alias in text:
                scored.append((len(alias), dataset))
                break
    if scored:
        scored.sort(key=lambda x: -x[0])
        return scored[0][1]

    # manufacturing controller phrasing: "for buyer_persona_library"
    m = re.search(
        r"for\s+([a-z0-9_]+_library|[a-z0-9_]+_profile|[a-z0-9_]+_catalog|[a-z0-9_]+_analysis)",
        text,
    )
    if m and m.group(1) in DATASET_ALIASES:
        return m.group(1)

    if explicit:
        key = explicit.strip().lower().replace(" ", "_")
        if key.endswith(".csv"):
            key = key[:-4]
        if key in DATASET_ALIASES:
            return key

    return default


def search_query_for_dataset(dataset: str, instruction: str = "") -> str:
    """Build a grounded search query preferring dataset-specific trusted topics."""
    hint = DATASET_QUERY_HINTS.get(dataset) or dataset.replace("_", " ")
    instr = (instruction or "").strip()
    if instr and len(instr) < 160 and dataset.replace("_", " ").split()[0] in instr.lower():
        q = instr
    else:
        q = hint
    if "indonesia" not in q.lower():
        q = f"{q} Indonesia"
    return q
