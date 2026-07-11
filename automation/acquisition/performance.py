"""Acquisition performance metrics + reports/performance/*."""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Optional

from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root


class PerformanceCollector:
    def __init__(self, repo_root: Path | None = None):
        self.repo_root = repo_root or find_repo_root()
        self.t0 = time.perf_counter()
        self.data: dict[str, Any] = {
            "started_at": utc_now_iso(),
            "connectors": [],
            "downloads": {},
            "cache": {},
            "fingerprints": {},
            "extraction": {},
            "publish": {},
            "ranking": [],
            "throughput": {},
        }

    def set_connectors(self, rows: list[dict[str, Any]]) -> None:
        self.data["connectors"] = rows

    def set_downloads(self, snap: dict[str, Any]) -> None:
        self.data["downloads"] = snap

    def set_cache(self, snap: dict[str, Any]) -> None:
        self.data["cache"] = snap

    def set_fingerprints(self, snap: dict[str, Any]) -> None:
        self.data["fingerprints"] = snap

    def set_extraction(self, snap: dict[str, Any]) -> None:
        self.data["extraction"] = snap

    def set_publish(self, snap: dict[str, Any]) -> None:
        self.data["publish"] = snap

    def set_ranking(self, rows: list[dict[str, Any]]) -> None:
        self.data["ranking"] = [
            {
                "id": r.get("id"),
                "name": r.get("name"),
                "score": r.get("_rank_score"),
                "breakdown": r.get("_rank_breakdown"),
            }
            for r in rows[:30]
        ]

    def finalize(
        self,
        *,
        documents: int = 0,
        rows: int = 0,
        mission_id: str = "",
        session_id: str = "",
    ) -> dict[str, Any]:
        elapsed_s = max(0.001, time.perf_counter() - self.t0)
        elapsed_h = elapsed_s / 3600.0
        self.data["finished_at"] = utc_now_iso()
        self.data["mission_id"] = mission_id
        self.data["session_id"] = session_id
        self.data["elapsed_seconds"] = round(elapsed_s, 3)
        self.data["throughput"] = {
            "documents": documents,
            "rows": rows,
            "documents_per_hour": round(documents / elapsed_h, 2),
            "rows_per_hour": round(rows / elapsed_h, 2),
            "documents_per_second": round(documents / elapsed_s, 3),
            "rows_per_second": round(rows / elapsed_s, 3),
        }
        # persist latest
        state = (
            self.repo_root
            / "automation"
            / "learning"
            / "state"
            / "acquisition_performance.json"
        )
        state.parent.mkdir(parents=True, exist_ok=True)
        state.write_text(
            json.dumps(self.data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        write_performance_reports(self.data, repo_root=self.repo_root)
        return self.data


def write_performance_reports(
    data: dict[str, Any],
    *,
    repo_root: Path | None = None,
) -> dict[str, str]:
    root = repo_root or find_repo_root()
    out = root / "reports" / "performance"
    out.mkdir(parents=True, exist_ok=True)
    written: dict[str, str] = {}

    def w(name: str, body: str) -> None:
        p = out / name
        p.write_text(body.rstrip() + "\n", encoding="utf-8", newline="\n")
        written[name] = str(p.relative_to(root))

    thr = data.get("throughput") or {}
    cons = data.get("connectors") or []
    dl = data.get("downloads") or {}
    cache = data.get("cache") or {}
    fp = data.get("fingerprints") or {}
    ext = data.get("extraction") or {}
    ranking = data.get("ranking") or []

    w(
        "throughput.md",
        "\n".join(
            [
                "# Throughput",
                "",
                f"**Session:** `{data.get('session_id')}`",
                f"**Mission:** `{data.get('mission_id')}`",
                f"**Elapsed (s):** {data.get('elapsed_seconds')}",
                "",
                f"| Metric | Value |",
                f"|--------|------:|",
                f"| Documents | {thr.get('documents', 0)} |",
                f"| Rows | {thr.get('rows', 0)} |",
                f"| Documents/hour | {thr.get('documents_per_hour', 0)} |",
                f"| Rows/hour | {thr.get('rows_per_hour', 0)} |",
                f"| Documents/second | {thr.get('documents_per_second', 0)} |",
                f"| Rows/second | {thr.get('rows_per_second', 0)} |",
                "",
            ]
        ),
    )

    lines = [
        "# Connector Performance",
        "",
        f"**Session:** `{data.get('session_id')}`",
        "",
        "| Connector | Status | HTTP | ms | Discovered | Downloaded | Error |",
        "|-----------|--------|------|---:|-----------:|-----------:|-------|",
    ]
    for c in cons:
        lines.append(
            f"| {c.get('name') or c.get('connector_id')} | {c.get('status')} | "
            f"{c.get('http_status') or '—'} | {c.get('elapsed_ms', 0)} | "
            f"{c.get('documents_discovered', 0)} | {c.get('documents_downloaded', 0)} | "
            f"{(c.get('error') or '—')[:40]} |"
        )
    w("connector_performance.md", "\n".join(lines))

    w(
        "download_statistics.md",
        "\n".join(
            [
                "# Download Statistics",
                "",
                "```json",
                json.dumps(dl, indent=2, ensure_ascii=False),
                "```",
                "",
            ]
        ),
    )
    w(
        "cache_statistics.md",
        "\n".join(
            [
                "# HTTP Cache Statistics",
                "",
                "```json",
                json.dumps(cache, indent=2, ensure_ascii=False),
                "```",
                "",
            ]
        ),
    )
    w(
        "crawler_statistics.md",
        "\n".join(
            [
                "# Crawler / Fingerprint Statistics",
                "",
                "```json",
                json.dumps(
                    {"fingerprints": fp, "downloads": dl, "extraction": ext},
                    indent=2,
                    ensure_ascii=False,
                ),
                "```",
                "",
            ]
        ),
    )
    w(
        "api_statistics.md",
        "\n".join(
            [
                "# API Statistics",
                "",
                f"Connectors contacted: **{len(cons)}**",
                f"OK: **{sum(1 for c in cons if c.get('status') in {'ok','success','no_updates'})}**",
                f"Errors: **{sum(1 for c in cons if c.get('status') in {'error','failed'})}**",
                "",
                "| Connector | Elapsed ms | Status |",
                "|-----------|-----------:|--------|",
                *[
                    f"| {c.get('name')} | {c.get('elapsed_ms', 0)} | {c.get('status')} |"
                    for c in cons
                ],
                "",
            ]
        ),
    )
    rank_lines = [
        "# Source Ranking",
        "",
        "Adaptive scores used for mission source selection.",
        "",
        "| Rank | Source | Score |",
        "|-----:|--------|------:|",
    ]
    for i, r in enumerate(ranking, 1):
        rank_lines.append(
            f"| {i} | {r.get('name') or r.get('id')} | {r.get('score')} |"
        )
    if not ranking:
        rank_lines.append("| — | — | 0 |")
    rank_lines.append("")
    w("source_ranking.md", "\n".join(rank_lines))

    # Extraction path observability
    w(
        "extraction_statistics.md",
        "\n".join(
            [
                "# Extraction Statistics",
                "",
                "```json",
                json.dumps(ext, indent=2, ensure_ascii=False),
                "```",
                "",
                f"| Metric | Value |",
                f"|--------|------:|",
                f"| Fast path candidates | {ext.get('fast', 0)} |",
                f"| Medium path candidates | {ext.get('medium', 0)} |",
                f"| Deep path candidates | {ext.get('deep', 0)} |",
                f"| LLM used | {ext.get('llm_used', ext.get('llm', 0))} |",
                f"| LLM skipped | {ext.get('skipped_llm', ext.get('llm_skipped', 0))} |",
                f"| Avg extraction ms | {ext.get('avg_ms', ext.get('average_extraction_ms', 0))} |",
                "",
            ]
        ),
    )

    # Stage timings if present
    stages = data.get("stage_timings") or {}
    stage_rows = stages.get("stages") if isinstance(stages, dict) else {}
    if stage_rows:
        sl = [
            "# Stage Timings",
            "",
            "| Stage | Count | Avg ms | Max ms |",
            "|-------|------:|-------:|-------:|",
        ]
        for name, st in stage_rows.items():
            if not isinstance(st, dict):
                continue
            sl.append(
                f"| {name} | {st.get('count', 1)} | {st.get('avg_ms', 0)} | {st.get('max_ms', 0)} |"
            )
        sl.append("")
        w("stage_timings.md", "\n".join(sl))

    # Auto-publish ratio
    ap = data.get("auto_publish") or {}
    if ap:
        w(
            "auto_publish.md",
            "\n".join(
                [
                    "# Auto-Publish Gate",
                    "",
                    f"| Metric | Value |",
                    f"|--------|------:|",
                    f"| Threshold | {ap.get('threshold', 0.92)} |",
                    f"| Auto-publish count | {ap.get('auto_publish_count', 0)} |",
                    f"| Manual review count | {ap.get('manual_review_count', 0)} |",
                    f"| Auto-publish ratio | {ap.get('auto_publish_ratio', 0)} |",
                    f"| Manual review ratio | {ap.get('manual_review_ratio', 0)} |",
                    "",
                ]
            ),
        )

    # Always refresh aggregate throughput pack from real production
    try:
        from automation.acquisition.throughput_ops import write_throughput_reports

        thr_pack = write_throughput_reports(
            session_perf={
                "stage_timings": (stage_rows or {}),
                "workers": data.get("workers"),
                "extraction": ext,
                "auto_publish": ap,
                "process_ratio": (data.get("throughput_detail") or {}).get(
                    "final_process_ratio_pct"
                ),
            },
            repo_root=root,
        )
        written.update(thr_pack)
    except Exception:  # noqa: BLE001
        pass

    return written
