"""Export packager for Dataset Factory outputs."""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from automation.lib.paths import find_repo_root


def export_dataset(
    dataset_rel: str = "domains/business_development/industry_library.csv",
    *,
    formats: list[str] | None = None,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """Export a domain CSV into factory export formats."""
    root = repo_root or find_repo_root()
    formats = formats or ["jsonl", "json"]
    src = root / dataset_rel
    if not src.exists():
        return {"ok": False, "error": f"missing {dataset_rel}"}

    rows: list[dict[str, str]] = []
    with src.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    stem = src.stem
    out: dict[str, Any] = {"ok": True, "rows": len(rows), "artifacts": []}

    if "jsonl" in formats:
        dest = root / "exports" / "jsonl" / f"{stem}_{stamp}.jsonl"
        dest.parent.mkdir(parents=True, exist_ok=True)
        with dest.open("w", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        out["artifacts"].append(str(dest.relative_to(root)))

    if "json" in formats:
        dest = root / "exports" / "jsonl" / f"{stem}_{stamp}.json"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(
            json.dumps({"dataset": dataset_rel, "rows": rows}, ensure_ascii=False, indent=2)
            + "\n",
            encoding="utf-8",
        )
        out["artifacts"].append(str(dest.relative_to(root)))

    if "openai" in formats:
        # Chat fine-tune style: system+user+assistant from industry rows
        dest = root / "exports" / "openai" / f"{stem}_ft_{stamp}.jsonl"
        dest.parent.mkdir(parents=True, exist_ok=True)
        with dest.open("w", encoding="utf-8") as f:
            for r in rows:
                name = r.get("Industry Name") or r.get("name") or "entity"
                desc = r.get("Industry Description") or json.dumps(r, ensure_ascii=False)[:800]
                rec = {
                    "messages": [
                        {
                            "role": "system",
                            "content": "You are a dataset-backed industry knowledge assistant.",
                        },
                        {
                            "role": "user",
                            "content": f"Describe the industry: {name}",
                        },
                        {"role": "assistant", "content": desc},
                    ]
                }
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        out["artifacts"].append(str(dest.relative_to(root)))

    if "huggingface" in formats:
        dest = root / "exports" / "huggingface" / f"{stem}_{stamp}.json"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(
            json.dumps(
                {
                    "dataset_name": stem,
                    "description": "IDA Dataset Factory export",
                    "data": rows,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        out["artifacts"].append(str(dest.relative_to(root)))

    return out


if __name__ == "__main__":
    print(json.dumps(export_dataset(formats=["jsonl", "openai", "huggingface"]), indent=2))
