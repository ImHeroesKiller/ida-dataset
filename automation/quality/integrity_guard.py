"""Production integrity guard — reject rows that would increase integrity debt.

Observe append-only: never rewrites existing datasets. Filters candidate rows
before append. Used by live runtime and pipeline publisher.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path
from typing import Any, Mapping, Sequence

from automation.lib.paths import find_repo_root

# Primary ID column by dataset stem
ID_FIELDS: dict[str, str] = {
    "industry_library": "Industry ID",
    "company_profile": "Company ID",
    "product_catalog": "Product ID",
    "pain_point_library": "Pain ID",
    "solution_library": "Solution ID",
    "framework_library": "Framework ID",
    "case_study_library": "Case ID",
    "opportunity_analysis": "Opportunity ID",
    "competitor_library": "Competitor ID",
    "business_signal_library": "Signal ID",
    "discovery_question_library": "Question ID",
    "buyer_persona_library": "Persona ID",
    "decision_maker_library": "Decision Maker ID",
    "regulation_library": "Regulation ID",
    "risk_library": "Risk ID",
    "trend_library": "Trend ID",
}

ID_PATTERNS: dict[str, re.Pattern[str]] = {
    "industry_library": re.compile(r"^IND-", re.I),
    "company_profile": re.compile(r"^COMP-", re.I),
    "product_catalog": re.compile(r"^PROD-", re.I),
    "pain_point_library": re.compile(r"^PAIN-", re.I),
    "solution_library": re.compile(r"^SOL-", re.I),
    "framework_library": re.compile(r"^FW-", re.I),
    "case_study_library": re.compile(r"^CASE-", re.I),
    "opportunity_analysis": re.compile(r"^(OPP|OP)-", re.I),
    "competitor_library": re.compile(r"^CMP-", re.I),
    "buyer_persona_library": re.compile(r"^PER-", re.I),
    "decision_maker_library": re.compile(r"^DM-", re.I),
    "regulation_library": re.compile(r"^REG-", re.I),
    "risk_library": re.compile(r"^RISK-", re.I),
    "trend_library": re.compile(r"^TRD-", re.I),
}


def _stem(path: Path) -> str:
    return path.stem


def _load_index(path: Path, id_field: str) -> set[str]:
    if not path.exists():
        return set()
    out: set[str] = set()
    with path.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            v = (row.get(id_field) or "").strip()
            if v:
                out.add(v)
    return out


def _industry_ids(repo: Path) -> set[str]:
    p = repo / "domains/business_development/industry_library.csv"
    return _load_index(p, "Industry ID")


def _company_ids(repo: Path) -> set[str]:
    p = repo / "domains/business_development/company_profile.csv"
    return _load_index(p, "Company ID")


def _pain_ids(repo: Path) -> set[str]:
    p = repo / "domains/business_development/pain_point_library.csv"
    return _load_index(p, "Pain ID")


def _conf(row: Mapping[str, Any]) -> float | None:
    blob = " ".join(
        str(row.get(k) or "")
        for k in ("Notes", "Data Sources", "Data Source", "References", "confidence")
    )
    m = re.search(r"confidence[=:\s]+([0-9]*\.?[0-9]+)", blob, re.I)
    if m:
        v = float(m.group(1))
        return v / 100.0 if v > 1 else v
    # structured field
    raw = row.get("confidence")
    if raw is not None and str(raw).strip() != "":
        try:
            v = float(raw)
            return v / 100.0 if v > 1 else v
        except ValueError:
            return None
    return None


def validate_row(
    dataset_path: Path,
    row: Mapping[str, Any],
    *,
    repo_root: Path | None = None,
    existing_ids: set[str] | None = None,
) -> tuple[bool, str]:
    """Return (ok, reason). ok=False → reject row (do not append)."""
    root = repo_root or find_repo_root()
    stem = _stem(dataset_path)
    id_field = ID_FIELDS.get(stem)
    if not id_field:
        # unknown dataset — allow but require non-empty first column-ish
        return True, "ok_unindexed_dataset"

    eid = str(row.get(id_field) or "").strip()
    if not eid:
        return False, "missing_primary_id"

    pat = ID_PATTERNS.get(stem)
    if pat and not pat.match(eid):
        return False, f"invalid_id_pattern:{eid}"

    ids = existing_ids if existing_ids is not None else _load_index(dataset_path, id_field)
    if eid in ids:
        return False, f"duplicate_id:{eid}"

    conf = _conf(row)
    if conf is not None and conf < 0.80:
        return False, f"confidence_below_threshold:{conf}"

    # Foreign keys by dataset
    if stem == "company_profile":
        iid = str(row.get("Industry ID") or "").strip()
        if iid and iid not in _industry_ids(root):
            # name-only soft link not enough for new production rows
            return False, f"broken_industry_fk:{iid}"
        if not iid and not str(row.get("Industry") or "").strip():
            return False, "missing_industry_link"

    if stem == "pain_point_library":
        iid = str(row.get("Industry ID") or "").strip()
        if not iid:
            return False, "missing_industry_fk"
        if iid not in _industry_ids(root):
            return False, f"broken_industry_fk:{iid}"

    if stem == "solution_library":
        pid = str(row.get("Related Pain ID") or "").strip()
        if not pid:
            return False, "missing_pain_fk"
        if pid not in _pain_ids(root):
            return False, f"broken_pain_fk:{pid}"

    if stem == "case_study_library":
        cid = str(row.get("Company ID") or "").strip()
        if not cid:
            return False, "missing_company_fk"
        if cid not in _company_ids(root):
            return False, f"broken_company_fk:{cid}"

    if stem == "opportunity_analysis":
        cid = str(row.get("Company ID") or "").strip()
        if cid and cid not in _company_ids(root):
            return False, f"broken_company_fk:{cid}"

    # Provenance soft-required for production knowledge rows
    blob = " ".join(
        str(row.get(k) or "")
        for k in ("Notes", "Data Sources", "Data Source", "References")
    )
    if stem in {
        "industry_library",
        "company_profile",
        "product_catalog",
        "pain_point_library",
        "solution_library",
        "buyer_persona_library",
        "decision_maker_library",
        "regulation_library",
        "risk_library",
        "trend_library",
        "competitor_library",
    }:
        if "SRC-" not in blob and "source" not in blob.lower() and not str(
            row.get("Data Sources") or row.get("Data Source") or row.get("Information Source") or ""
        ).strip():
            # allow if confidence present from structured provenance path
            if conf is None:
                return False, "missing_provenance"

    return True, "ok"


def filter_append_rows(
    dataset_path: Path,
    rows: Sequence[Mapping[str, Any]],
    *,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """Filter rows for append. Accepted may be appended; rejected must not."""
    path = Path(dataset_path)
    root = repo_root or find_repo_root()
    stem = _stem(path)
    id_field = ID_FIELDS.get(stem)
    existing = _load_index(path, id_field) if id_field else set()
    accepted: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    batch_ids: set[str] = set()

    for row in rows:
        r = dict(row)
        if id_field:
            eid = str(r.get(id_field) or "").strip()
            if eid and eid in batch_ids:
                rejected.append({"row": r, "reason": f"duplicate_id_in_batch:{eid}"})
                continue
        ok, reason = validate_row(
            path, r, repo_root=root, existing_ids=existing | batch_ids
        )
        if not ok:
            rejected.append({"row": r, "reason": reason})
            continue
        if id_field:
            eid = str(r.get(id_field) or "").strip()
            if eid:
                batch_ids.add(eid)
        accepted.append(r)

    return {
        "ok": True,
        "dataset": stem,
        "accepted": accepted,
        "rejected": rejected,
        "accepted_count": len(accepted),
        "rejected_count": len(rejected),
    }
