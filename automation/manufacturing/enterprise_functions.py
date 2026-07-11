"""Enterprise Function generalization — knowledge expansion layer.

Freeze-compliant: no schema, path, queue, or engine redesign.
Classifies existing rows by function keywords, scores Function×Dataset gaps,
balances mission topics, and builds discovery queries with function context.

Domain CSVs remain under domains/business_development/ (frozen layout).
Business Development is one function among the full enterprise taxonomy.
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any, Optional

from automation.lib.paths import find_repo_root
from automation.lib.simple_yaml import load_simple_yaml

# Canonical product datasets (no new types)
CANONICAL_DATASETS = [
    "industry_library",
    "company_profile",
    "service_library",
    "product_catalog",
    "pain_point_library",
    "solution_library",
    "framework_library",
    "case_study_library",
    "buyer_persona_library",
    "decision_maker_library",
    "regulation_library",
    "risk_library",
    "trend_library",
    "opportunity_analysis",
    "competitor_library",
]

_DATASET_PATHS = {
    "industry_library": "domains/business_development/industry_library.csv",
    "company_profile": "domains/business_development/company_profile.csv",
    "service_library": "domains/business_development/product_catalog.csv",
    "product_catalog": "domains/business_development/product_catalog.csv",
    "pain_point_library": "domains/business_development/pain_point_library.csv",
    "solution_library": "domains/business_development/solution_library.csv",
    "framework_library": "domains/business_development/framework_library.csv",
    "case_study_library": "domains/business_development/case_study_library.csv",
    "buyer_persona_library": "domains/business_development/buyer_persona_library.csv",
    "decision_maker_library": "domains/business_development/decision_maker_library.csv",
    "regulation_library": "domains/business_development/regulation_library.csv",
    "risk_library": "domains/business_development/risk_library.csv",
    "trend_library": "domains/business_development/trend_library.csv",
    "opportunity_analysis": "domains/business_development/opportunity_analysis.csv",
    "competitor_library": "domains/business_development/competitor_library.csv",
}


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    data: Any
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(text)
    except ImportError:
        data = load_simple_yaml(text)
    if data is None:
        return {}
    return data if isinstance(data, dict) else {}


def load_taxonomy(repo_root: Path | None = None) -> dict[str, Any]:
    root = repo_root or find_repo_root()
    return _load_yaml(root / "automation/config/enterprise_functions.yaml")


def load_source_mapping(repo_root: Path | None = None) -> dict[str, Any]:
    root = repo_root or find_repo_root()
    return _load_yaml(root / "automation/config/enterprise_function_sources.yaml")


def list_functions(repo_root: Path | None = None) -> list[dict[str, Any]]:
    tax = load_taxonomy(repo_root)
    funcs = tax.get("functions") or []
    return [f for f in funcs if isinstance(f, dict) and f.get("id")]


def _row_blob(row: dict[str, str]) -> str:
    return " ".join(str(v or "") for v in row.values()).lower()


def classify_row(blob: str, functions: list[dict[str, Any]]) -> list[str]:
    """Return matching function ids for a text blob (multi-label).

    Uses word-boundary matching only. Short tokens (len < 3) are ignored
    to avoid false positives (e.g. 'ai' inside 'chain', 'pr' inside 'report').
    """
    hits: list[str] = []
    for fn in functions:
        kws = fn.get("keywords") or []
        for kw in kws:
            k = str(kw).lower().strip()
            if len(k) < 3:
                continue
            # Multi-word phrases: substring OK; single tokens: word boundary
            if " " in k:
                if k in blob:
                    hits.append(str(fn["id"]))
                    break
            elif re.search(rf"\b{re.escape(k)}\b", blob):
                hits.append(str(fn["id"]))
                break
    return hits


def _iter_dataset_rows(
    repo: Path, dataset: str
) -> list[dict[str, str]]:
    rel = _DATASET_PATHS.get(dataset)
    if not rel:
        return []
    path = repo / rel
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if dataset == "service_library":
        return [
            r
            for r in rows
            if "service" in (r.get("Product Type") or "").lower()
        ]
    if dataset == "product_catalog":
        return [
            r
            for r in rows
            if "service" not in (r.get("Product Type") or "").lower()
        ]
    return rows


def knowledge_by_function(
    repo_root: Path | None = None,
    *,
    datasets: list[str] | None = None,
) -> dict[str, Any]:
    """Count rows attributable to each enterprise function (keyword multi-label)."""
    root = repo_root or find_repo_root()
    functions = list_functions(root)
    ds_list = datasets or CANONICAL_DATASETS
    by_fn: dict[str, dict[str, Any]] = {
        str(f["id"]): {
            "id": f["id"],
            "name": f.get("name") or f["id"],
            "priority": int(f.get("priority") or 50),
            "rows": 0,
            "by_dataset": {d: 0 for d in ds_list},
        }
        for f in functions
    }
    unclassified = 0
    total_labeled = 0

    for ds in ds_list:
        for row in _iter_dataset_rows(root, ds):
            blob = _row_blob(row)
            hits = classify_row(blob, functions)
            if not hits:
                unclassified += 1
                # Default residual toward business_development only if empty taxonomy miss
                # Count once under _unclassified — do not force BD monopoly
                continue
            for hid in hits:
                if hid not in by_fn:
                    continue
                by_fn[hid]["rows"] += 1
                by_fn[hid]["by_dataset"][ds] = (
                    int(by_fn[hid]["by_dataset"].get(ds) or 0) + 1
                )
                total_labeled += 1

    ranked = sorted(by_fn.values(), key=lambda x: (-int(x["rows"]), -int(x["priority"])))
    return {
        "functions": ranked,
        "unclassified_rows": unclassified,
        "labeled_assignments": total_labeled,
        "function_count": len(functions),
        "dataset_count": len(ds_list),
    }


def function_dataset_gap_matrix(
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """Knowledge gap for Enterprise Function × Dataset cells."""
    root = repo_root or find_repo_root()
    tax = load_taxonomy(root)
    floor = int(tax.get("gap_floor_per_cell") or 2)
    kb = knowledge_by_function(root)
    cells: list[dict[str, Any]] = []
    for fn in kb["functions"]:
        fid = str(fn["id"])
        for ds in CANONICAL_DATASETS:
            cur = int((fn.get("by_dataset") or {}).get(ds) or 0)
            gap = max(0, floor - cur)
            # Higher gap + higher business priority = more manufacturing demand
            priority = int(fn.get("priority") or 50)
            score = gap * 10.0 + (0 if cur > 0 else 25.0) + (100 - min(priority, 100)) * 0.05
            # Invert priority into urgency for under-covered high-priority functions
            if cur == 0:
                score += priority * 0.15
            cells.append(
                {
                    "enterprise_function": fid,
                    "function_name": fn.get("name"),
                    "dataset": ds,
                    "current_rows": cur,
                    "gap_floor": floor,
                    "gap": gap,
                    "business_priority": priority,
                    "gap_score": round(score, 3),
                }
            )
    cells.sort(key=lambda c: (-float(c["gap_score"]), c["enterprise_function"], c["dataset"]))
    weakest = cells[0] if cells else {}
    by_function_cov = []
    for fn in kb["functions"]:
        total = sum(int(v or 0) for v in (fn.get("by_dataset") or {}).values())
        covered_ds = sum(
            1 for d in CANONICAL_DATASETS if int((fn.get("by_dataset") or {}).get(d) or 0) >= floor
        )
        by_function_cov.append(
            {
                "id": fn["id"],
                "name": fn.get("name"),
                "priority": fn.get("priority"),
                "rows": total,
                "datasets_at_floor": covered_ds,
                "datasets_total": len(CANONICAL_DATASETS),
                "coverage_pct": round(
                    100.0 * covered_ds / max(1, len(CANONICAL_DATASETS)), 2
                ),
            }
        )
    by_function_cov.sort(key=lambda x: (x["coverage_pct"], x["rows"]))
    return {
        "gap_floor_per_cell": floor,
        "cells": cells,
        "top_gaps": cells[:40],
        "weakest_cell": weakest,
        "coverage_by_function": by_function_cov,
        "weakest_function": by_function_cov[0] if by_function_cov else {},
        "strongest_function": by_function_cov[-1] if by_function_cov else {},
    }


def production_distribution(repo_root: Path | None = None) -> dict[str, Any]:
    kb = knowledge_by_function(repo_root)
    total = sum(int(f["rows"]) for f in kb["functions"]) or 1
    dist = [
        {
            "id": f["id"],
            "name": f.get("name"),
            "rows": int(f["rows"]),
            "share_pct": round(100.0 * int(f["rows"]) / total, 2),
            "priority": f.get("priority"),
        }
        for f in kb["functions"]
    ]
    dist.sort(key=lambda x: -x["rows"])
    top_growing = dist[0] if dist else {}
    # Weakest among non-zero priority: lowest rows
    weakest = min(dist, key=lambda x: (x["rows"], -int(x.get("priority") or 0))) if dist else {}
    return {
        "distribution": dist,
        "top_function": top_growing,
        "weakest_function": weakest,
        "total_labeled_rows": sum(int(f["rows"]) for f in kb["functions"]),
        "unclassified_rows": kb.get("unclassified_rows"),
        "function_count": kb.get("function_count"),
    }


def select_function_for_dataset(
    dataset: str,
    repo_root: Path | None = None,
    *,
    rotate_index: int = 0,
) -> dict[str, Any]:
    """Pick enterprise function with highest gap for this dataset (balance production)."""
    root = repo_root or find_repo_root()
    matrix = function_dataset_gap_matrix(root)
    cells = [c for c in matrix["cells"] if c["dataset"] == dataset]
    if not cells:
        funcs = list_functions(root)
        if not funcs:
            return {"id": "business_development", "name": "Business Development"}
        f = funcs[rotate_index % len(funcs)]
        return {"id": f["id"], "name": f.get("name"), "gap_score": 0}
    # Prefer zero coverage cells, then highest gap_score
    cells.sort(key=lambda c: (-float(c["gap_score"]), -int(c["business_priority"])))
    # Rotate among top-N to avoid always same function
    top_n = cells[: max(3, min(8, len(cells)))]
    pick = top_n[rotate_index % len(top_n)]
    return {
        "id": pick["enterprise_function"],
        "name": pick.get("function_name"),
        "gap_score": pick.get("gap_score"),
        "current_rows": pick.get("current_rows"),
        "dataset": dataset,
    }


def function_topic_hint(
    function_id: str,
    dataset: str,
    repo_root: Path | None = None,
) -> str:
    root = repo_root or find_repo_root()
    funcs = {str(f["id"]): f for f in list_functions(root)}
    fn = funcs.get(function_id) or {}
    name = str(fn.get("name") or function_id.replace("_", " ").title())
    focus = (load_taxonomy(root).get("dataset_function_focus") or {}).get(dataset) or {}
    emphasis = str(focus.get("emphasis") or "topic_hints")
    if emphasis == "persona_roles":
        roles = fn.get("persona_roles") or []
        if roles:
            role = roles[0]
            return f"{role} — {name} ({dataset.replace('_', ' ')})"
    terms = fn.get("discovery_terms") or fn.get("topic_hints") or [name]
    term = terms[0] if terms else name
    ds_label = dataset.replace("_library", "").replace("_", " ")
    return f"{term} — {ds_label} knowledge for {name}"


def build_discovery_queries(
    *,
    dataset: str,
    enterprise_function: str,
    base_query: str = "",
    limit: int = 5,
    repo_root: Path | None = None,
) -> list[str]:
    """Discovery queries with enterprise function context (site: trusted hosts)."""
    root = repo_root or find_repo_root()
    mapping = load_source_mapping(root)
    by_fn = (mapping.get("by_function") or {}).get(enterprise_function) or {}
    examples = list(by_fn.get("query_examples") or [])
    hosts = list(by_fn.get("site_hosts") or [])
    funcs = {str(f["id"]): f for f in list_functions(root)}
    fn = funcs.get(enterprise_function) or {}
    terms = list(fn.get("discovery_terms") or fn.get("topic_hints") or [])
    ds_term = dataset.replace("_library", "").replace("_", " ")
    out: list[str] = []
    if base_query:
        out.append(base_query.strip())
    for ex in examples[:limit]:
        if ex not in out:
            out.append(ex)
    for host in hosts[:limit]:
        term = terms[0] if terms else ds_term
        q = f"site:{host} {term} {ds_term}".strip()
        if q not in out:
            out.append(q)
    if not out:
        name = str(fn.get("name") or enterprise_function)
        out.append(f"{name} {ds_term} Indonesia")
    return out[: max(1, limit)]


def enrich_mission_instruction(
    dataset: str,
    base_instruction: str,
    repo_root: Path | None = None,
    *,
    current_rows: int = 0,
) -> dict[str, Any]:
    """Attach enterprise function context to a manufacturing mission (additive)."""
    root = repo_root or find_repo_root()
    fn = select_function_for_dataset(dataset, root, rotate_index=current_rows)
    topic = function_topic_hint(str(fn["id"]), dataset, root)
    queries = build_discovery_queries(
        dataset=dataset,
        enterprise_function=str(fn["id"]),
        base_query=topic,
        repo_root=root,
    )
    instruction = (
        f"{topic} — continuous knowledge manufacturing for {dataset} "
        f"across enterprise function {fn.get('name')} "
        f"(function_gap={fn.get('gap_score')}; not BD-only)"
    )
    if base_instruction and "enterprise function" not in base_instruction.lower():
        # Prefer function-aware instruction
        pass
    return {
        "enterprise_function": fn.get("id"),
        "enterprise_function_name": fn.get("name"),
        "title": topic,
        "instruction": instruction,
        "discovery_queries": queries,
        "function_gap_score": fn.get("gap_score"),
    }


def build_enterprise_state(repo_root: Path | None = None) -> dict[str, Any]:
    root = repo_root or find_repo_root()
    kb = knowledge_by_function(root)
    gaps = function_dataset_gap_matrix(root)
    dist = production_distribution(root)
    cov = gaps.get("coverage_by_function") or []
    # Top growing = highest rows; weakest = lowest coverage_pct
    top_growing = max(cov, key=lambda x: int(x.get("rows") or 0)) if cov else {}
    weakest = min(cov, key=lambda x: (float(x.get("coverage_pct") or 0), int(x.get("rows") or 0))) if cov else {}
    return {
        "version": "1.0",
        "scope": "enterprise_functions",
        "note": (
            "Business Development is one enterprise function. "
            "All product datasets expand across the full taxonomy."
        ),
        "function_count": kb.get("function_count"),
        "knowledge_by_function": [
            {
                "id": f["id"],
                "name": f.get("name"),
                "rows": f["rows"],
                "priority": f.get("priority"),
            }
            for f in (kb.get("functions") or [])[:20]
        ],
        "coverage_by_function": cov,
        "top_growing_function": top_growing,
        "weakest_function": weakest,
        "production_distribution": dist.get("distribution"),
        "top_gaps": gaps.get("top_gaps"),
        "weakest_cell": gaps.get("weakest_cell"),
        "unclassified_rows": kb.get("unclassified_rows"),
        "labeled_assignments": kb.get("labeled_assignments"),
    }


def write_enterprise_reports(
    state: dict[str, Any] | None = None,
    *,
    repo_root: Path | None = None,
) -> dict[str, str]:
    """Generate reports/enterprise/* markdown artifacts."""
    root = repo_root or find_repo_root()
    out_dir = root / "reports" / "enterprise"
    out_dir.mkdir(parents=True, exist_ok=True)
    st = state or build_enterprise_state(root)
    tax = load_taxonomy(root)
    src_map = load_source_mapping(root)
    funcs = list_functions(root)
    gaps = function_dataset_gap_matrix(root)
    kb = knowledge_by_function(root)
    dist = production_distribution(root)
    written: dict[str, str] = {}

    def w(name: str, body: str) -> None:
        p = out_dir / name
        p.write_text(body.rstrip() + "\n", encoding="utf-8", newline="\n")
        written[name] = str(p.relative_to(root))

    # 1 taxonomy
    lines = [
        "# Enterprise Function Taxonomy",
        "",
        "Canonical taxonomy for continuous knowledge manufacturing.",
        "Business Development is **one** of these functions — not the whole factory.",
        "",
        f"**Function count:** {len(funcs)}",
        "",
        "| ID | Name | Priority |",
        "|----|------|----------|",
    ]
    for f in sorted(funcs, key=lambda x: -int(x.get("priority") or 0)):
        lines.append(
            f"| `{f['id']}` | {f.get('name')} | {f.get('priority')} |"
        )
    lines += [
        "",
        "## Product datasets (unchanged)",
        "",
    ]
    for d in tax.get("datasets") or CANONICAL_DATASETS:
        lines.append(f"- `{d}`")
    lines += [
        "",
        "No new dataset types. Schema and domain folder layout are frozen.",
        "",
    ]
    w("enterprise_function_taxonomy.md", "\n".join(lines))

    # 2 mapping
    map_lines = [
        "# Enterprise Function Knowledge Mapping",
        "",
        "Every dataset supports every enterprise function.",
        "",
        "## Examples",
        "",
        "### Buyer Persona",
        "",
    ]
    for f in funcs[:12]:
        roles = f.get("persona_roles") or []
        role = roles[0] if roles else f.get("name")
        map_lines.append(f"- **{f.get('name')}** → {role}")
    map_lines += ["", "### Trend", ""]
    for f in funcs:
        if f["id"] in {
            "cyber_security",
            "treasury",
            "manufacturing",
            "recruitment",
            "esg",
            "ai",
            "information_technology",
        }:
            terms = f.get("discovery_terms") or []
            map_lines.append(f"- **{f.get('name')}** → {terms[0] if terms else f.get('name')}")
    map_lines += ["", "### Regulation", ""]
    for f in funcs:
        if f["id"] in {
            "human_resources",
            "tax",
            "procurement",
            "cyber_security",
            "health_safety_environment",
            "accounting",
            "finance",
        }:
            terms = f.get("discovery_terms") or []
            map_lines.append(f"- **{f.get('name')}** → {terms[0] if terms else f.get('name')}")
    map_lines += [
        "",
        "## Dataset × function focus",
        "",
    ]
    for ds, conf in (tax.get("dataset_function_focus") or {}).items():
        map_lines.append(f"- `{ds}`: emphasis=`{conf.get('emphasis')}`")
    w("enterprise_function_mapping.md", "\n".join(map_lines))

    # 3 matrix
    mx = [
        "# Dataset × Enterprise Function Matrix",
        "",
        f"Gap floor per cell: **{gaps.get('gap_floor_per_cell')}** (progress signal, not a stop).",
        "",
        "| Function | Dataset | Rows | Gap | Score |",
        "|----------|---------|------|-----|-------|",
    ]
    for c in (gaps.get("top_gaps") or [])[:80]:
        mx.append(
            f"| {c.get('function_name')} | `{c.get('dataset')}` | {c.get('current_rows')} | "
            f"{c.get('gap')} | {c.get('gap_score')} |"
        )
    w("dataset_function_matrix.md", "\n".join(mx))

    # 4 source matrix
    sm = [
        "# Source × Enterprise Function Matrix",
        "",
        "Trusted sources only (configuration mapping).",
        "",
        "| Function | Sources | Example discovery |",
        "|----------|---------|-------------------|",
    ]
    by_fn = src_map.get("by_function") or {}
    for fid, conf in sorted(by_fn.items()):
        srcs = ", ".join(f"`{s}`" for s in (conf.get("sources") or [])[:6])
        ex = (conf.get("query_examples") or ["—"])[0]
        sm.append(f"| `{fid}` | {srcs} | `{ex}` |")
    sm += [
        "",
        "## Global sources",
        "",
    ]
    for s in src_map.get("global_sources") or []:
        sm.append(f"- `{s}`")
    w("source_function_matrix.md", "\n".join(sm))

    # 5 coverage
    cov_lines = [
        "# Coverage by Enterprise Function",
        "",
        "| Function | Rows | Datasets at floor | Coverage % | Priority |",
        "|----------|------|-------------------|------------|----------|",
    ]
    for c in gaps.get("coverage_by_function") or []:
        cov_lines.append(
            f"| {c.get('name')} | {c.get('rows')} | {c.get('datasets_at_floor')}/"
            f"{c.get('datasets_total')} | {c.get('coverage_pct')}% | {c.get('priority')} |"
        )
    w("coverage_by_function.md", "\n".join(cov_lines))

    # 6 knowledge gap
    kg = [
        "# Knowledge Gap by Enterprise Function × Dataset",
        "",
        f"Weakest cell: **{(gaps.get('weakest_cell') or {}).get('function_name')}** × "
        f"`{(gaps.get('weakest_cell') or {}).get('dataset')}` "
        f"(score={(gaps.get('weakest_cell') or {}).get('gap_score')})",
        "",
        "| Rank | Function | Dataset | Rows | Gap | Score |",
        "|------|----------|---------|------|-----|-------|",
    ]
    for i, c in enumerate((gaps.get("top_gaps") or [])[:50], 1):
        kg.append(
            f"| {i} | {c.get('function_name')} | `{c.get('dataset')}` | "
            f"{c.get('current_rows')} | {c.get('gap')} | {c.get('gap_score')} |"
        )
    w("knowledge_gap_by_function.md", "\n".join(kg))

    # 7 production distribution
    pd = [
        "# Production Distribution by Enterprise Function",
        "",
        f"Top function (volume): **{(dist.get('top_function') or {}).get('name')}** "
        f"({(dist.get('top_function') or {}).get('rows')} labeled rows)",
        "",
        f"Weakest function (volume): **{(dist.get('weakest_function') or {}).get('name')}** "
        f"({(dist.get('weakest_function') or {}).get('rows')} labeled rows)",
        "",
        f"Unclassified rows (no keyword hit): **{dist.get('unclassified_rows')}**",
        "",
        "| Function | Rows | Share % | Priority |",
        "|----------|------|---------|----------|",
    ]
    for d in dist.get("distribution") or []:
        pd.append(
            f"| {d.get('name')} | {d.get('rows')} | {d.get('share_pct')}% | {d.get('priority')} |"
        )
    pd += [
        "",
        "## Manufacturing policy",
        "",
        "- Balance production across **all** enterprise functions.",
        "- Never stay focused on Business Development alone.",
        "- Priority drivers: coverage gap, knowledge gap, freshness, business value.",
        "",
    ]
    w("production_distribution.md", "\n".join(pd))

    # JSON snapshot for dashboard readers
    snap = out_dir / "enterprise_state.json"
    snap.write_text(
        json.dumps(st, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    written["enterprise_state.json"] = str(snap.relative_to(root))
    return written


def run_enterprise_generalization(repo_root: Path | None = None) -> dict[str, Any]:
    root = repo_root or find_repo_root()
    state = build_enterprise_state(root)
    paths = write_enterprise_reports(state, repo_root=root)
    state["reports"] = paths
    # Persist beside manufacturing state
    path = root / "automation/learning/state/enterprise_function_state.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(state, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return state


if __name__ == "__main__":
    result = run_enterprise_generalization()
    print(
        json.dumps(
            {
                "ok": True,
                "functions": result.get("function_count"),
                "weakest": result.get("weakest_function"),
                "top_growing": result.get("top_growing_function"),
                "reports": result.get("reports"),
            },
            indent=2,
        )
    )
