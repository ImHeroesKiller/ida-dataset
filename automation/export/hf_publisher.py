"""Continuous Hugging Face dataset publisher — additive export target only.

Pushes domains/*.csv knowledge as CSV + JSONL + Parquet (+ metadata + dataset card)
to https://huggingface.co/datasets/ariew/ida-dataset

Never blocks manufacturing: all failures are captured and returned as ok=False.
Incremental: only uploads changed files based on content hashes.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from automation.lib.paths import find_repo_root

DEFAULT_REPO = "ariew/ida-dataset"
STATE_REL = "automation/learning/state/huggingface_publish_state.json"
REPORTS_REL = "reports/huggingface"


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8")) or {}
    except Exception:  # noqa: BLE001
        return {}


def _write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _git_head(repo_root: Path) -> str:
    try:
        import subprocess

        r = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=str(repo_root),
            capture_output=True,
            text=True,
            timeout=10,
        )
        return (r.stdout or "").strip() or "unknown"
    except Exception:  # noqa: BLE001
        return "unknown"


def list_domain_datasets(repo_root: Path) -> list[Path]:
    """Product dataset CSVs under domains/ (skip guidance)."""
    root = repo_root / "domains"
    out: list[Path] = []
    if not root.exists():
        return out
    skip = {"guidance.csv"}
    for p in sorted(root.rglob("*.csv")):
        if p.name in skip:
            continue
        if p.name.startswith("."):
            continue
        out.append(p)
    return out


def dataset_folder_name(csv_path: Path) -> str:
    """HF folder name from CSV stem (schema-stable)."""
    return csv_path.stem


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def rows_to_jsonl_bytes(rows: list[dict[str, str]]) -> bytes:
    lines = [json.dumps(r, ensure_ascii=False) for r in rows]
    return ("\n".join(lines) + ("\n" if lines else "")).encode("utf-8")


def rows_to_parquet_bytes(rows: list[dict[str, str]]) -> Optional[bytes]:
    """Optional parquet via pyarrow; None if unavailable."""
    if not rows:
        # empty table
        try:
            import pyarrow as pa
            import pyarrow.parquet as pq
            import io

            table = pa.table({})
            buf = io.BytesIO()
            pq.write_table(table, buf)
            return buf.getvalue()
        except Exception:  # noqa: BLE001
            return None
    try:
        import io
        import pyarrow as pa
        import pyarrow.parquet as pq

        # normalize to string columns for stability
        cols = list(rows[0].keys())
        arrays = {c: [str(r.get(c, "") or "") for r in rows] for c in cols}
        table = pa.table(arrays)
        buf = io.BytesIO()
        pq.write_table(table, buf)
        return buf.getvalue()
    except Exception:  # noqa: BLE001
        return None


def build_local_bundle(
    repo_root: Path,
    *,
    staging_dir: Path | None = None,
) -> dict[str, Any]:
    """Materialize per-dataset export tree for HF upload."""
    staging = staging_dir or (repo_root / "exports" / "huggingface" / "hub_staging")
    if staging.exists():
        # clean only hub_staging contents we own
        for p in staging.rglob("*"):
            if p.is_file():
                try:
                    p.unlink()
                except Exception:  # noqa: BLE001
                    pass
    staging.mkdir(parents=True, exist_ok=True)

    datasets_meta: list[dict[str, Any]] = []
    files: dict[str, Path] = {}  # relative path -> absolute path
    total_rows = 0

    for csv_path in list_domain_datasets(repo_root):
        name = dataset_folder_name(csv_path)
        rows = load_csv_rows(csv_path)
        total_rows += len(rows)
        folder = staging / name
        folder.mkdir(parents=True, exist_ok=True)

        # CSV copy
        csv_dest = folder / f"{name}.csv"
        csv_dest.write_bytes(csv_path.read_bytes())
        files[f"{name}/{name}.csv"] = csv_dest

        # JSONL
        jsonl_dest = folder / f"{name}.jsonl"
        jsonl_dest.write_bytes(rows_to_jsonl_bytes(rows))
        files[f"{name}/{name}.jsonl"] = jsonl_dest

        # Parquet (optional)
        pq_bytes = rows_to_parquet_bytes(rows)
        parquet_ok = False
        if pq_bytes is not None:
            pq_dest = folder / f"{name}.parquet"
            pq_dest.write_bytes(pq_bytes)
            files[f"{name}/{name}.parquet"] = pq_dest
            parquet_ok = True

        # Per-dataset README snippet
        snip = folder / "README.md"
        snip.write_text(
            f"# {name}\n\n"
            f"- Rows: **{len(rows)}**\n"
            f"- Formats: CSV, JSONL" + (", Parquet" if parquet_ok else "") + "\n"
            f"- Source: `{csv_path.relative_to(repo_root)}`\n"
            f"- Updated: {_utc_now()}\n",
            encoding="utf-8",
        )
        files[f"{name}/README.md"] = snip

        datasets_meta.append(
            {
                "name": name,
                "rows": len(rows),
                "source": str(csv_path.relative_to(repo_root)),
                "parquet": parquet_ok,
                "columns": list(rows[0].keys()) if rows else [],
            }
        )

    # Global metadata
    meta_dir = staging / "metadata"
    meta_dir.mkdir(parents=True, exist_ok=True)
    stats = {
        "generated_at": _utc_now(),
        "git_commit": _git_head(repo_root),
        "datasets": datasets_meta,
        "total_datasets": len(datasets_meta),
        "total_rows": total_rows,
    }
    stats_path = meta_dir / "statistics.json"
    _write_json(stats_path, stats)
    files["metadata/statistics.json"] = stats_path

    return {
        "staging": staging,
        "files": files,
        "stats": stats,
        "datasets": datasets_meta,
        "total_rows": total_rows,
    }


def load_state(repo_root: Path) -> dict[str, Any]:
    return _read_json(repo_root / STATE_REL)


def save_state(repo_root: Path, state: dict[str, Any]) -> None:
    _write_json(repo_root / STATE_REL, state)


def next_semver(prev: str | None, *, bump: str = "patch") -> str:
    """Bump semantic version for dataset releases (independent of repo VERSION)."""
    base = (prev or "2.0.0").strip().lstrip("v")
    m = re.match(r"^(\d+)\.(\d+)\.(\d+)", base)
    if not m:
        return "2.0.1"
    major, minor, patch = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if bump == "major":
        major, minor, patch = major + 1, 0, 0
    elif bump == "minor":
        minor, patch = minor + 1, 0
    else:
        patch += 1
    return f"{major}.{minor}.{patch}"


def compute_file_hashes(files: dict[str, Path]) -> dict[str, str]:
    return {rel: _sha256_file(path) for rel, path in files.items()}


def diff_files(
    new_hashes: dict[str, str],
    old_hashes: dict[str, str],
) -> dict[str, list[str]]:
    added = [k for k in new_hashes if k not in old_hashes]
    changed = [k for k in new_hashes if k in old_hashes and new_hashes[k] != old_hashes[k]]
    removed = [k for k in old_hashes if k not in new_hashes]
    unchanged = [k for k in new_hashes if k in old_hashes and new_hashes[k] == old_hashes[k]]
    return {
        "added": sorted(added),
        "changed": sorted(changed),
        "removed": sorted(removed),
        "unchanged": sorted(unchanged),
    }


def build_dataset_card(
    *,
    version: str,
    stats: dict[str, Any],
    change_summary: dict[str, Any],
    repo_root: Path,
) -> str:
    """Generate Hugging Face dataset README (dataset card)."""
    # Optional quality/learning signals
    daily = {}
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    daily = _read_json(repo_root / f"automation/learning/state/daily_{day}.json")
    acq = _read_json(repo_root / "automation/learning/state/acquisition_performance.json")
    ft = _read_json(repo_root / "automation/learning/state/fulltext_acquisition.json")
    manufacturing = _read_json(repo_root / "automation/learning/state/manufacturing_state.json")

    datasets = stats.get("datasets") or []
    ds_lines = "\n".join(
        f"| `{d.get('name')}` | {d.get('rows', 0)} | {d.get('source')} |"
        for d in datasets
    ) or "| — | 0 | — |"

    license_note = "See repository LICENSE. Public knowledge derived from trusted open sources."
    citation = (
        f"@dataset{{ida_dataset_{version.replace('.', '_')},\n"
        f"  title={{IDA Dataset Factory Knowledge Datasets}},\n"
        f"  author={{IDA Dataset Factory}},\n"
        f"  year={{{datetime.now(timezone.utc).year}}},\n"
        f"  url={{https://huggingface.co/datasets/ariew/ida-dataset}},\n"
        f"  note={{version {version}}}\n"
        f"}}"
    )

    mode = ((manufacturing.get("mode") or {}) if manufacturing else {})
    mode_s = mode.get("mode") if isinstance(mode, dict) else str(mode or "—")

    return f"""---
license: other
task_categories:
  - text-classification
  - feature-extraction
language:
  - en
  - id
tags:
  - ida
  - knowledge-factory
  - business-development
  - enterprise
  - indonesia
pretty_name: IDA Dataset Factory
size_categories:
  - 1K<n<10K
---

# IDA Dataset Factory

Continuous knowledge datasets produced by the **IDA Dataset Factory** for enterprise LLM fine-tuning and retrieval.

- **Hub:** [ariew/ida-dataset](https://huggingface.co/datasets/ariew/ida-dataset)
- **Version:** `{version}`
- **Generated:** {stats.get('generated_at')}
- **Git commit:** `{stats.get('git_commit')}`
- **Total datasets:** {stats.get('total_datasets')}
- **Total rows:** {stats.get('total_rows')}

## Datasets

| Dataset | Rows | Source |
|---------|-----:|--------|
{ds_lines}

## Formats

Each dataset folder contains:

- `{{name}}.csv` — canonical tabular export
- `{{name}}.jsonl` — row-oriented JSON Lines
- `{{name}}.parquet` — columnar (when available)
- `README.md` — dataset snippet

Global metadata lives under `metadata/`.

## Knowledge growth

| Signal | Value |
|--------|------:|
| Knowledge added (today state) | {daily.get('knowledge_added', '—')} |
| Manufacturing mode | {mode_s} |
| Last acquisition session | {(acq or {}).get('session_id', '—')} |
| Full-text enrichments (last) | {(ft or {}).get('enriched', '—')} |

## This release

| Field | Value |
|-------|------:|
| Files added | {len(change_summary.get('added') or [])} |
| Files changed | {len(change_summary.get('changed') or [])} |
| Files unchanged | {len(change_summary.get('unchanged') or [])} |
| Rows added (est.) | {change_summary.get('rows_added', '—')} |
| Datasets changed | {', '.join(change_summary.get('datasets_changed') or []) or '—'} |

## Quality notes

- Rows are append-oriented knowledge with provenance fields when available.
- Confidence / duplicate / source diversity metrics are computed in the factory reports under `reports/`.
- Acquisition and provider statistics are factory-local; this Hub mirror is the continuous public export.

## License

{license_note}

## Citation

```bibtex
{citation}
```

## Contact

Maintained by the IDA Dataset Factory pipeline. Automated publish after successful learning sessions.
"""


def _import_hf():
    try:
        from huggingface_hub import HfApi  # type: ignore

        return HfApi
    except Exception as exc:  # noqa: BLE001
        raise RuntimeError(
            "huggingface_hub is required. Install with: pip install huggingface_hub"
        ) from exc


def verify_hub(
    api: Any,
    repo_id: str,
    *,
    token: str,
    expected_files: list[str],
) -> dict[str, Any]:
    """Verify repo access and uploaded files."""
    out: dict[str, Any] = {
        "repo_id": repo_id,
        "auth_ok": False,
        "repo_exists": False,
        "files_checked": 0,
        "files_found": 0,
        "missing": [],
        "whoami": None,
        "errors": [],
    }
    try:
        who = api.whoami(token=token)
        out["auth_ok"] = True
        out["whoami"] = who.get("name") if isinstance(who, dict) else str(who)
    except Exception as exc:  # noqa: BLE001
        out["errors"].append(f"auth:{exc}")
        return out

    try:
        info = api.repo_info(repo_id=repo_id, repo_type="dataset", token=token)
        out["repo_exists"] = True
        out["repo_info"] = {
            "id": getattr(info, "id", repo_id),
            "sha": getattr(info, "sha", None),
            "lastModified": str(getattr(info, "lastModified", "") or ""),
        }
    except Exception as exc:  # noqa: BLE001
        out["errors"].append(f"repo_info:{exc}")
        return out

    try:
        siblings = api.list_repo_files(repo_id=repo_id, repo_type="dataset", token=token)
        remote = set(siblings or [])
        out["files_checked"] = len(expected_files)
        missing = [f for f in expected_files if f not in remote]
        out["missing"] = missing[:50]
        out["files_found"] = out["files_checked"] - len(missing)
        out["card_present"] = "README.md" in remote
        out["ok"] = out["auth_ok"] and out["repo_exists"] and not missing
    except Exception as exc:  # noqa: BLE001
        out["errors"].append(f"list_files:{exc}")
        out["ok"] = False
    return out


def upload_incremental(
    api: Any,
    *,
    repo_id: str,
    token: str,
    files: dict[str, Path],
    to_upload: list[str],
    commit_message: str,
) -> dict[str, Any]:
    """Upload only changed/new files."""
    uploaded: list[str] = []
    errors: list[str] = []
    for rel in to_upload:
        path = files.get(rel)
        if not path or not path.exists():
            errors.append(f"missing_local:{rel}")
            continue
        try:
            api.upload_file(
                path_or_fileobj=str(path),
                path_in_repo=rel,
                repo_id=repo_id,
                repo_type="dataset",
                token=token,
                commit_message=commit_message,
            )
            uploaded.append(rel)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{rel}:{exc}")
    return {"uploaded": uploaded, "errors": errors, "count": len(uploaded)}


def write_reports(
    repo_root: Path,
    summary: dict[str, Any],
) -> dict[str, str]:
    out_dir = repo_root / REPORTS_REL
    out_dir.mkdir(parents=True, exist_ok=True)
    written: dict[str, str] = {}

    def w(name: str, body: str) -> None:
        p = out_dir / name
        p.write_text(body.rstrip() + "\n", encoding="utf-8", newline="\n")
        written[name] = str(p.relative_to(repo_root))

    now = summary.get("finished_at") or _utc_now()
    ver = summary.get("version") or "—"
    ok = summary.get("ok")
    diff = summary.get("diff") or {}
    verify = summary.get("verification") or {}
    stats = summary.get("stats") or {}
    history = summary.get("version_history") or []

    w(
        "publish_report.md",
        f"""# Hugging Face Publish Report

**Generated:** {now}  
**Status:** `{"SUCCESS" if ok else "FAILED / SKIPPED"}`  
**Repo:** `{summary.get('repo_id')}`  
**Version:** `{ver}`  
**Git commit:** `{summary.get('git_commit')}`

| Metric | Value |
|--------|------:|
| Total datasets | {stats.get('total_datasets', 0)} |
| Total rows | {stats.get('total_rows', 0)} |
| Files uploaded | {summary.get('uploaded_count', 0)} |
| Files unchanged | {len(diff.get('unchanged') or [])} |
| Duration ms | {summary.get('elapsed_ms', 0)} |
| Attempts | {summary.get('attempts', 1)} |

## Message

{summary.get('message') or '—'}

## Errors

{chr(10).join(f"- {e}" for e in (summary.get('errors') or [])) or "- none"}
""",
    )

    w(
        "upload_summary.md",
        f"""# Upload Summary

**Generated:** {now}

| Field | Value |
|-------|------:|
| Uploaded | {summary.get('uploaded_count', 0)} |
| Added | {len(diff.get('added') or [])} |
| Changed | {len(diff.get('changed') or [])} |
| Unchanged | {len(diff.get('unchanged') or [])} |
| Removed (local) | {len(diff.get('removed') or [])} |

## Uploaded paths

{chr(10).join(f"- `{p}`" for p in (summary.get('uploaded_files') or [])[:100]) or "- (none)"}
""",
    )

    w(
        "sync_statistics.md",
        f"""# Sync Statistics

**Generated:** {now}

| Dataset | Rows | Parquet |
|---------|-----:|---------|
"""
        + "\n".join(
            f"| `{d.get('name')}` | {d.get('rows')} | {d.get('parquet')} |"
            for d in (stats.get("datasets") or [])
        )
        + f"""

## Incremental

| Class | Count |
|-------|------:|
| added | {len(diff.get('added') or [])} |
| changed | {len(diff.get('changed') or [])} |
| unchanged | {len(diff.get('unchanged') or [])} |
""",
    )

    hist_lines = "\n".join(
        f"| {h.get('version')} | {h.get('at')} | {h.get('rows')} | {h.get('uploaded')} | {h.get('git_commit')} |"
        for h in history[-20:]
    ) or "| — | — | — | — | — |"
    w(
        "version_history.md",
        f"""# Version History

**Generated:** {now}  
**Current:** `{ver}`

| Version | At | Rows | Uploaded | Git |
|---------|----|-----:|---------:|-----|
{hist_lines}
""",
    )

    # growth from history
    growth_rows = []
    for h in history:
        growth_rows.append(f"| {h.get('version')} | {h.get('rows')} | {h.get('at')} |")
    w(
        "dataset_growth.md",
        f"""# Dataset Growth

**Generated:** {now}

| Version | Total rows | Timestamp |
|---------|----------:|-----------|
{chr(10).join(growth_rows) or "| — | 0 | — |"}

Current total rows: **{stats.get('total_rows', 0)}**
""",
    )

    w(
        "verification.md",
        f"""# Verification

**Generated:** {now}

| Check | Value |
|-------|------:|
| Auth OK | {verify.get('auth_ok')} |
| Repo exists | {verify.get('repo_exists')} |
| Whoami | {verify.get('whoami')} |
| Files checked | {verify.get('files_checked')} |
| Files found | {verify.get('files_found')} |
| README present | {verify.get('card_present')} |
| Verify OK | {verify.get('ok')} |

## Missing files

{chr(10).join(f"- `{m}`" for m in (verify.get('missing') or [])) or "- none"}

## Errors

{chr(10).join(f"- {e}" for e in (verify.get('errors') or [])) or "- none"}
""",
    )

    return written


def publish_to_huggingface(
    *,
    repo_root: Path | None = None,
    repo_id: str | None = None,
    token: str | None = None,
    dry_run: bool = False,
    force_full: bool = False,
    retries: int = 3,
    create_if_missing: bool = True,
) -> dict[str, Any]:
    """Main entry: build bundle, incremental upload, verify, reports.

    Never raises for operational failures — returns structured result.
    """
    root = repo_root or find_repo_root()
    t0 = time.perf_counter()
    repo_id = (repo_id or os.environ.get("HF_DATASET_REPO") or DEFAULT_REPO).strip()
    token = (token or os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_TOKEN") or "").strip()
    git_commit = _git_head(root)

    summary: dict[str, Any] = {
        "ok": False,
        "repo_id": repo_id,
        "git_commit": git_commit,
        "started_at": _utc_now(),
        "errors": [],
        "attempts": 0,
        "dry_run": dry_run,
    }

    if not token and not dry_run:
        summary["message"] = "HF_TOKEN missing — skipped Hugging Face publish"
        summary["skipped"] = True
        summary["finished_at"] = _utc_now()
        summary["elapsed_ms"] = round((time.perf_counter() - t0) * 1000, 1)
        try:
            write_reports(root, summary)
        except Exception:  # noqa: BLE001
            pass
        return summary

    # Build local artifacts
    try:
        bundle = build_local_bundle(root)
    except Exception as exc:  # noqa: BLE001
        summary["errors"].append(f"bundle:{exc}")
        summary["message"] = "Failed to build export bundle"
        summary["finished_at"] = _utc_now()
        summary["elapsed_ms"] = round((time.perf_counter() - t0) * 1000, 1)
        write_reports(root, summary)
        return summary

    files: dict[str, Path] = dict(bundle["files"])
    stats = bundle["stats"]
    new_hashes = compute_file_hashes(files)
    state = load_state(root)
    old_hashes = dict(state.get("file_hashes") or {})
    if force_full:
        old_hashes = {}
    diff = diff_files(new_hashes, old_hashes)
    to_upload = sorted(set(diff["added"] + diff["changed"]))

    # Version bump only if something changed
    prev_ver = str(state.get("version") or "2.0.0")
    version = prev_ver
    rows_prev = int(state.get("total_rows") or 0)
    rows_now = int(stats.get("total_rows") or 0)
    rows_added = max(0, rows_now - rows_prev)
    datasets_changed = sorted(
        {
            p.split("/")[0]
            for p in to_upload
            if "/" in p and not p.startswith("metadata") and p != "README.md"
        }
    )
    change_summary = {
        **diff,
        "rows_added": rows_added,
        "datasets_changed": datasets_changed,
    }

    if to_upload or force_full or "README.md" not in old_hashes:
        version = next_semver(prev_ver, bump="patch")
        # Always refresh card when publishing changes
        card = build_dataset_card(
            version=version,
            stats=stats,
            change_summary=change_summary,
            repo_root=root,
        )
        card_path = Path(bundle["staging"]) / "README.md"
        card_path.write_text(card, encoding="utf-8")
        files["README.md"] = card_path
        new_hashes["README.md"] = _sha256_file(card_path)
        if "README.md" not in to_upload:
            if old_hashes.get("README.md") != new_hashes["README.md"]:
                to_upload.append("README.md")

        # Version metadata file
        ver_meta = {
            "version": version,
            "generated_at": _utc_now(),
            "git_commit": git_commit,
            "total_rows": rows_now,
            "total_datasets": stats.get("total_datasets"),
            "rows_added": rows_added,
            "datasets_changed": datasets_changed,
            "files_uploaded": to_upload,
        }
        ver_path = Path(bundle["staging"]) / "metadata" / "version.json"
        _write_json(ver_path, ver_meta)
        files["metadata/version.json"] = ver_path
        new_hashes["metadata/version.json"] = _sha256_file(ver_path)
        if "metadata/version.json" not in to_upload:
            to_upload.append("metadata/version.json")
        # statistics always if any change
        if "metadata/statistics.json" not in to_upload:
            to_upload.append("metadata/statistics.json")

    summary["version"] = version
    summary["stats"] = stats
    summary["diff"] = diff
    summary["change_summary"] = change_summary

    if dry_run:
        summary["ok"] = True
        summary["skipped"] = False
        summary["message"] = f"Dry-run: would upload {len(to_upload)} files as {version}"
        summary["uploaded_count"] = 0
        summary["uploaded_files"] = []
        summary["would_upload"] = to_upload
        summary["finished_at"] = _utc_now()
        summary["elapsed_ms"] = round((time.perf_counter() - t0) * 1000, 1)
        write_reports(root, summary)
        return summary

    if not to_upload:
        summary["ok"] = True
        summary["message"] = "No changes detected — Hugging Face already in sync"
        summary["uploaded_count"] = 0
        summary["uploaded_files"] = []
        summary["verification"] = {"ok": True, "note": "skipped_no_changes"}
        summary["finished_at"] = _utc_now()
        summary["elapsed_ms"] = round((time.perf_counter() - t0) * 1000, 1)
        # still refresh reports
        hist = list(state.get("version_history") or [])
        summary["version_history"] = hist
        write_reports(root, summary)
        return summary

    # Upload with retries
    last_err = ""
    upload_result: dict[str, Any] = {"uploaded": [], "errors": []}
    HfApi = None
    api = None
    for attempt in range(1, max(1, retries) + 1):
        summary["attempts"] = attempt
        try:
            HfApi = _import_hf()
            api = HfApi()
            if create_if_missing:
                try:
                    api.create_repo(
                        repo_id=repo_id,
                        repo_type="dataset",
                        token=token,
                        private=False,
                        exist_ok=True,
                    )
                except Exception as exc:  # noqa: BLE001
                    # exist_ok should prevent errors; record non-fatal
                    last_err = f"create_repo:{exc}"

            upload_result = upload_incremental(
                api,
                repo_id=repo_id,
                token=token,
                files=files,
                to_upload=to_upload,
                commit_message=f"chore(data): IDA factory publish {version} ({git_commit})",
            )
            if not upload_result.get("errors"):
                last_err = ""
                break
            last_err = "; ".join(upload_result.get("errors") or [])
        except Exception as exc:  # noqa: BLE001
            last_err = str(exc)
            upload_result = {"uploaded": [], "errors": [last_err]}
        # exponential backoff
        if attempt < retries:
            time.sleep(min(60, 2 ** attempt))

    summary["uploaded_files"] = upload_result.get("uploaded") or []
    summary["uploaded_count"] = len(summary["uploaded_files"])
    if upload_result.get("errors"):
        summary["errors"].extend(upload_result["errors"])

    # Verify
    verification: dict[str, Any] = {}
    if api is not None:
        try:
            verification = verify_hub(
                api,
                repo_id,
                token=token,
                expected_files=summary["uploaded_files"]
                + (["README.md"] if "README.md" in files else []),
            )
        except Exception as exc:  # noqa: BLE001
            verification = {"ok": False, "errors": [str(exc)]}
    else:
        verification = {"ok": False, "errors": ["hf_api_unavailable", last_err]}

    summary["verification"] = verification
    success = bool(summary["uploaded_count"] > 0 and not upload_result.get("errors"))
    # partial success if some uploaded
    if summary["uploaded_count"] > 0 and upload_result.get("errors"):
        success = True
        summary["message"] = "Partial upload completed with some errors"
    elif success and verification.get("ok"):
        summary["message"] = f"Published {version} to {repo_id}"
    elif success:
        summary["message"] = f"Uploaded {version}; verification incomplete"
    else:
        summary["message"] = f"Hugging Face publish failed: {last_err or 'unknown'}"
        if last_err:
            summary["errors"].append(last_err)

    summary["ok"] = success

    # Persist state only on success
    hist = list(state.get("version_history") or [])
    if success:
        # merge hashes for uploaded files; keep old for others if partial
        merged = dict(old_hashes)
        for rel in summary["uploaded_files"]:
            if rel in new_hashes:
                merged[rel] = new_hashes[rel]
        # if full success of to_upload list
        if not upload_result.get("errors"):
            merged = dict(new_hashes)
        hist.append(
            {
                "version": version,
                "at": _utc_now(),
                "rows": rows_now,
                "uploaded": summary["uploaded_count"],
                "git_commit": git_commit,
                "rows_added": rows_added,
            }
        )
        hist = hist[-50:]
        save_state(
            root,
            {
                "version": version,
                "total_rows": rows_now,
                "file_hashes": merged,
                "last_publish_at": _utc_now(),
                "last_repo": repo_id,
                "last_git_commit": git_commit,
                "version_history": hist,
            },
        )
    summary["version_history"] = hist

    summary["finished_at"] = _utc_now()
    summary["elapsed_ms"] = round((time.perf_counter() - t0) * 1000, 1)
    try:
        summary["reports"] = write_reports(root, summary)
    except Exception as exc:  # noqa: BLE001
        summary["errors"].append(f"reports:{exc}")

    return summary
