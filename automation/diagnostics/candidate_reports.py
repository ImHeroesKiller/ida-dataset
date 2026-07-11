"""Write candidate lifecycle diagnostic reports (observe-only)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional

from automation.diagnostics.candidate_lifecycle import run_candidate_lifecycle_diagnostics
from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root


def _w(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body.rstrip() + "\n", encoding="utf-8", newline="\n")


def _table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for r in rows:
        cells = [str(c if c is not None else "—").replace("|", "\\|")[:140] for c in r]
        lines.append("| " + " | ".join(cells) + " |")
    if len(lines) == 2:
        lines.append("| " + " | ".join(["—"] * len(headers)) + " |")
    return "\n".join(lines)


def write_candidate_lifecycle_reports(
    *,
    repo_root: Path | None = None,
    session: Optional[dict[str, Any]] = None,
) -> dict[str, str]:
    root = repo_root or find_repo_root()
    out = root / "reports" / "diagnostics"
    out.mkdir(parents=True, exist_ok=True)
    bundle = run_candidate_lifecycle_diagnostics(root, session=session)
    gen = utc_now_iso()
    written: dict[str, str] = {}
    cands = bundle.get("candidates") or []
    stats = bundle.get("statistics") or {}
    rca = bundle.get("root_cause") or {}

    # Persist machine-readable
    try:
        state = root / "automation" / "learning" / "state" / "candidate_lifecycle_last.json"
        state.parent.mkdir(parents=True, exist_ok=True)
        slim = {
            "generated_at": gen,
            "session_id": bundle.get("session_id"),
            "dry_run": bundle.get("dry_run"),
            "root_cause": rca,
            "statistics": stats,
            "dataset_summary": bundle.get("dataset_summary"),
            "candidates": [
                {
                    k: c.get(k)
                    for k in (
                        "candidate_id",
                        "document_id",
                        "dataset",
                        "confidence",
                        "integrity_ok",
                        "integrity_reason",
                        "primary_block_reason",
                        "failed_rules",
                        "publish_decision",
                        "publish_reason",
                        "potential_false_negative",
                        "false_negative_rule",
                    )
                }
                for c in cands
            ],
        }
        state.write_text(
            json.dumps(slim, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    except Exception:  # noqa: BLE001
        pass

    # 1 candidate_lifecycle.md
    rows = []
    for c in cands:
        rows.append(
            [
                c.get("candidate_id"),
                c.get("document_id"),
                c.get("mission_id"),
                c.get("session_id"),
                c.get("dataset"),
                c.get("entity"),
                c.get("confidence"),
                c.get("integrity_ok"),
                c.get("primary_block_reason"),
                c.get("publish_decision"),
            ]
        )
    body = "\n".join(
        [
            "# Candidate Lifecycle",
            "",
            f"**Generated:** {gen}",
            f"**Session:** `{bundle.get('session_id')}`",
            f"**Mission:** `{bundle.get('mission_id')}`",
            f"**dry_run:** `{bundle.get('dry_run')}`",
            "",
            "Lifecycle: Document → Extraction → Candidate → Validation → Integrity Guard → Publisher → Dataset",
            "",
            _table(
                [
                    "candidate_id",
                    "document_id",
                    "mission_id",
                    "session_id",
                    "dataset",
                    "entity",
                    "confidence",
                    "integrity_ok",
                    "block_reason",
                    "publish",
                ],
                rows,
            ),
            "",
            f"Total candidates: **{len(cands)}**",
            "",
        ]
    )
    p = out / "candidate_lifecycle.md"
    _w(p, body)
    written[p.name] = str(p.relative_to(root))

    # 2 validation_trace.md — every rule every candidate
    parts = [
        "# Validation Trace",
        "",
        f"**Generated:** {gen}",
        "",
        "Every Integrity Guard rule evaluated (observe-only mirror).",
        "",
    ]
    for c in cands:
        parts.append(f"## {c.get('candidate_id')} · {c.get('entity')}")
        parts.append("")
        parts.append(
            f"dataset=`{c.get('dataset')}` · confidence=`{c.get('confidence')}` · "
            f"threshold=`{c.get('confidence_threshold')}` · document=`{c.get('document_id')}`"
        )
        parts.append("")
        rrows = []
        for r in c.get("rules") or []:
            rrows.append(
                [
                    r.get("rule"),
                    r.get("status"),
                    r.get("input"),
                    r.get("expected"),
                    r.get("actual"),
                    r.get("evidence"),
                ]
            )
        parts.append(
            _table(
                ["Rule Name", "PASS/FAIL", "Input", "Expected", "Actual", "Evidence"],
                rrows,
            )
        )
        parts.append("")
        parts.append(
            f"**Integrity final:** `{c.get('integrity_ok')}` · reason=`{c.get('integrity_reason')}`"
        )
        parts.append("")
    p = out / "validation_trace.md"
    _w(p, "\n".join(parts))
    written[p.name] = str(p.relative_to(root))

    # 3 integrity_trace.md — decision chain per candidate
    parts = [
        "# Integrity Guard Trace",
        "",
        f"**Generated:** {gen}",
        "",
        "Per-candidate decision chain (evidence only).",
        "",
    ]
    for c in cands:
        parts.append(f"## Candidate `{c.get('candidate_id')}`")
        parts.append("")
        parts.append("```text")
        parts.append(f"Candidate {c.get('candidate_id')}")
        for r in c.get("rules") or []:
            if r.get("status") == "N/A":
                continue
            line = f"  ↓\n{r.get('rule')}\n  {r.get('status')}"
            if r.get("rule") == "confidence_threshold":
                line += f"\n  actual={r.get('actual')} threshold={c.get('confidence_threshold')}"
            elif r.get("actual") is not None:
                line += f"\n  actual={r.get('actual')}"
            if r.get("evidence"):
                line += f"\n  evidence={r.get('evidence')}"
            parts.append(line)
        parts.append("  ↓")
        parts.append(f"Publisher decision: {c.get('publish_decision')}")
        parts.append(f"  reason={c.get('publish_reason')}")
        parts.append("```")
        parts.append("")
    p = out / "integrity_trace.md"
    _w(p, "\n".join(parts))
    written[p.name] = str(p.relative_to(root))

    # 4 publisher_trace.md
    prows = []
    for c in cands:
        prows.append(
            [
                c.get("candidate_id"),
                "YES" if c.get("publish_attempted") else "NO",
                c.get("publish_decision"),
                c.get("publish_reason"),
                c.get("integrity_ok"),
                c.get("dry_run"),
                c.get("trace_publish_status"),
            ]
        )
    body = "\n".join(
        [
            "# Publisher Trace",
            "",
            f"**Generated:** {gen}",
            "",
            _table(
                [
                    "candidate_id",
                    "Publish attempted?",
                    "Decision",
                    "Reason",
                    "Integrity ok",
                    "dry_run",
                    "trace_status",
                ],
                prows,
            ),
            "",
            "Decisions: Published | Rejected | Queued | Manual Review | Skipped",
            "",
        ]
    )
    p = out / "publisher_trace.md"
    _w(p, body)
    written[p.name] = str(p.relative_to(root))

    # 5 validation_statistics.md
    freq = stats.get("frequency") or []
    frows = [[f.get("rule_family"), f.get("count"), f"{f.get('pct')}%"] for f in freq]
    body = "\n".join(
        [
            "# Validation Statistics",
            "",
            f"**Generated:** {gen}",
            f"**Total candidates:** {stats.get('total_candidates')}",
            f"**Integrity blocked:** {stats.get('blocked')}",
            f"**Integrity passed:** {stats.get('passed_integrity')}",
            "",
            "Rule family frequency (descending):",
            "",
            _table(["Rule family", "Count", "Percentage"], frows),
            "",
        ]
    )
    p = out / "validation_statistics.md"
    _w(p, body)
    written[p.name] = str(p.relative_to(root))

    # 6 rule_impact.md
    irows = []
    for r in stats.get("rule_impact") or []:
        irows.append(
            [
                r.get("rule"),
                r.get("candidates_affected"),
                r.get("rows_blocked"),
                f"{r.get('pct_blocked')}%",
                r.get("average_confidence"),
            ]
        )
    body = "\n".join(
        [
            "# Rule Impact",
            "",
            f"**Generated:** {gen}",
            "",
            _table(
                [
                    "Rule",
                    "Candidates affected",
                    "Rows blocked",
                    "% blocked",
                    "Avg confidence",
                ],
                irows,
            ),
            "",
            "Business impact (evidence): each blocked candidate is one prevented append to the target dataset CSV.",
            "",
        ]
    )
    p = out / "rule_impact.md"
    _w(p, body)
    written[p.name] = str(p.relative_to(root))

    # 7 false_negative_analysis.md
    fns = bundle.get("false_negatives") or []
    frows = []
    for c in fns:
        frows.append(
            [
                c.get("candidate_id"),
                c.get("confidence"),
                c.get("false_negative_rule"),
                c.get("primary_block_reason"),
                "YES",
            ]
        )
    body = "\n".join(
        [
            "# False Negative Analysis",
            "",
            f"**Generated:** {gen}",
            "",
            "Candidates blocked by **exactly one** integrity rule family (potential false negative).",
            "Do **not** publish. Report only.",
            "",
            _table(
                [
                    "candidate_id",
                    "confidence",
                    "single_block_rule",
                    "integrity_reason",
                    "Potential FN",
                ],
                frows,
            ),
            "",
            f"Count: **{len(fns)}**",
            "",
        ]
    )
    p = out / "false_negative_analysis.md"
    _w(p, body)
    written[p.name] = str(p.relative_to(root))

    # 8 dataset_validation_summary.md
    drows = []
    for d in bundle.get("dataset_summary") or []:
        drows.append(
            [
                d.get("dataset"),
                d.get("candidates"),
                d.get("published"),
                d.get("rejected"),
                d.get("top_rejection_rule"),
                d.get("average_confidence"),
            ]
        )
    body = "\n".join(
        [
            "# Dataset Validation Summary",
            "",
            f"**Generated:** {gen}",
            "",
            _table(
                [
                    "Dataset",
                    "Candidates",
                    "Published",
                    "Rejected",
                    "Top rejection rule",
                    "Avg confidence",
                ],
                drows,
            ),
            "",
        ]
    )
    p = out / "dataset_validation_summary.md"
    _w(p, body)
    written[p.name] = str(p.relative_to(root))

    # 9 candidate_root_cause.md
    body = "\n".join(
        [
            "# Candidate Root Cause",
            "",
            f"**Generated:** {gen}",
            f"**Session:** `{bundle.get('session_id')}`",
            "",
            "> Diagnostics only. No recommendations. Evidence only.",
            "",
            "## Exactly which rule blocked production?",
            "",
            f"**Primary integrity block reason:** `{rca.get('primary_integrity_block_reason')}`",
            "",
            f"**dry_run publisher gate:** `{rca.get('dry_run_blocked_publish')}`",
            "",
            "## How many candidates?",
            "",
            f"- Total analyzed: **{rca.get('total_candidates')}**",
            f"- Integrity blocked: **{rca.get('integrity_blocked')}**",
            f"- Blocked by primary reason: **{rca.get('candidates_blocked_by_primary')}**",
            "",
            "## What evidence proves it?",
            "",
            *[f"- `{e}`" for e in (rca.get("evidence") or ["—"])],
            "",
            "## Per-candidate integrity reasons",
            "",
            _table(
                ["candidate_id", "dataset", "confidence", "integrity_ok", "reason", "publish"],
                [
                    [
                        c.get("candidate_id"),
                        c.get("dataset"),
                        c.get("confidence"),
                        c.get("integrity_ok"),
                        c.get("integrity_reason"),
                        c.get("publish_decision"),
                    ]
                    for c in cands
                ],
            ),
            "",
            "## Could production continue if that rule were satisfied?",
            "",
            str(rca.get("could_continue_if_satisfied") or "—"),
            "",
            "No recommendation is made. Statement is conditional evidence only.",
            "",
        ]
    )
    p = out / "candidate_root_cause.md"
    _w(p, body)
    written[p.name] = str(p.relative_to(root))

    return written
