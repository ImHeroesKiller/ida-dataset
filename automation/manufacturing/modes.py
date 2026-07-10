"""Automatic production modes — BOOTSTRAP / EXPANSION / CONTINUOUS / MAINTENANCE."""

from __future__ import annotations

from typing import Any


def detect_mode(evaluations: list[dict[str, Any]]) -> dict[str, Any]:
    """Choose factory manufacturing mode from dataset evaluations."""
    if not evaluations:
        return {
            "mode": "CONTINUOUS",
            "reason": "no_evaluations_default_continuous",
        }

    empty = [e for e in evaluations if int(e.get("current_rows") or 0) == 0]
    below_min = [e for e in evaluations if e.get("below_minimum")]
    high_fresh_gap = [e for e in evaluations if float(e.get("freshness_gap") or 0) > 0.5]
    high_conf_gap = [e for e in evaluations if float(e.get("confidence_gap") or 0) > 0.25]
    high_rel = [e for e in evaluations if float(e.get("relationship_gap") or 0) > 0.5]

    # BOOTSTRAP: any official empty dataset or majority below minimum
    if empty or len(below_min) >= max(1, len(evaluations) // 3):
        return {
            "mode": "BOOTSTRAP",
            "reason": "empty_or_below_minimum_datasets",
            "empty_datasets": [e["dataset"] for e in empty],
            "below_minimum": [e["dataset"] for e in below_min],
        }

    # MAINTENANCE: weak freshness / confidence / relationships dominate
    if (len(high_fresh_gap) + len(high_conf_gap) + len(high_rel)) >= max(
        2, len(evaluations) // 2
    ):
        return {
            "mode": "MAINTENANCE",
            "reason": "freshness_confidence_or_relationship_repair",
            "freshness_focus": [e["dataset"] for e in high_fresh_gap[:5]],
            "confidence_focus": [e["dataset"] for e in high_conf_gap[:5]],
        }

    # EXPANSION: still large stretch/universe gaps
    top = evaluations[0]
    if float(top.get("coverage_stretch_pct") or 0) < 80 or int(top.get("universe_gap") or 0) > 100:
        return {
            "mode": "EXPANSION",
            "reason": "significant_universe_or_stretch_gap",
            "focus_dataset": top.get("dataset"),
        }

    # CONTINUOUS: collect newly published knowledge forever
    return {
        "mode": "CONTINUOUS",
        "reason": "minimum_met_continue_new_publications",
        "focus_dataset": top.get("dataset"),
    }


def mode_mission_prefix(mode: str) -> str:
    return {
        "BOOTSTRAP": "Bootstrap",
        "EXPANSION": "Expand",
        "CONTINUOUS": "Collect New",
        "MAINTENANCE": "Refresh",
    }.get(mode, "Expand")
