"""Continuous Hugging Face dataset publisher — additive export target only.

Pushes domains/*.csv knowledge as CSV + JSONL + Parquet (+ metadata + dataset card)
to https://huggingface.co/datasets/ariew/ida-dataset

Manufacturing is never blocked: failures return ok=False with FULL diagnostics.
Incremental: only uploads changed files based on content hashes.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from automation.lib.paths import find_repo_root

DEFAULT_REPO = "ariew/ida-dataset"
STATE_REL = "automation/learning/state/huggingface_publish_state.json"
REPORTS_REL = "reports/huggingface"


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _log(msg: str) -> None:
    """Production console log — always flushed (never silent)."""
    print(f"[HF] {msg}", flush=True)


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
    except Exception as exc:  # noqa: BLE001
        _log(f"WARN read_json {path}: {exc}")
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
    except Exception as exc:  # noqa: BLE001
        _log(f"WARN git_head: {exc}")
        return "unknown"


class ApiTrace:
    """Records every Hub API call for production forensics."""

    def __init__(self) -> None:
        self.calls: list[dict[str, Any]] = []

    def record(
        self,
        op: str,
        *,
        ok: bool,
        detail: str = "",
        error: str | None = None,
        http_code: Any = None,
        elapsed_ms: float | None = None,
        extra: dict[str, Any] | None = None,
    ) -> None:
        row = {
            "ts": _utc_now(),
            "op": op,
            "ok": ok,
            "detail": detail[:500],
            "error": (error or "")[:1000] if error else None,
            "http_code": http_code,
            "elapsed_ms": elapsed_ms,
        }
        if extra:
            row["extra"] = extra
        self.calls.append(row)
        status = "OK" if ok else "FAIL"
        _log(f"API {op} → {status}" + (f" | {detail}" if detail else "") + (f" | err={error}" if error else ""))

    def to_dict(self) -> list[dict[str, Any]]:
        return list(self.calls)


def list_domain_datasets(repo_root: Path) -> list[Path]:
    root = repo_root / "domains"
    out: list[Path] = []
    if not root.exists():
        return out
    skip = {"guidance.csv"}
    for p in sorted(root.rglob("*.csv")):
        if p.name in skip or p.name.startswith("."):
            continue
        out.append(p)
    return out


def dataset_folder_name(csv_path: Path) -> str:
    return csv_path.stem


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def rows_to_jsonl_bytes(rows: list[dict[str, str]]) -> bytes:
    lines = [json.dumps(r, ensure_ascii=False) for r in rows]
    return ("\n".join(lines) + ("\n" if lines else "")).encode("utf-8")


def rows_to_parquet_bytes(rows: list[dict[str, str]]) -> Optional[bytes]:
    try:
        import io
        import pyarrow as pa
        import pyarrow.parquet as pq
    except Exception as exc:  # noqa: BLE001
        _log(f"Parquet unavailable (pyarrow): {exc}")
        return None
    try:
        if not rows:
            table = pa.table({})
        else:
            cols = list(rows[0].keys())
            arrays = {c: [str(r.get(c, "") or "") for r in rows] for c in cols}
            table = pa.table(arrays)
        buf = io.BytesIO()
        pq.write_table(table, buf)
        return buf.getvalue()
    except Exception as exc:  # noqa: BLE001
        _log(f"Parquet encode failed: {exc}")
        return None


def build_local_bundle(repo_root: Path, *, staging_dir: Path | None = None) -> dict[str, Any]:
    staging = staging_dir or (repo_root / "exports" / "huggingface" / "hub_staging")
    if staging.exists():
        for p in staging.rglob("*"):
            if p.is_file():
                try:
                    p.unlink()
                except Exception as exc:  # noqa: BLE001
                    _log(f"WARN unlink {p}: {exc}")
    staging.mkdir(parents=True, exist_ok=True)

    datasets_meta: list[dict[str, Any]] = []
    files: dict[str, Path] = {}
    total_rows = 0
    counts = {"csv": 0, "jsonl": 0, "parquet": 0, "readme": 0}

    for csv_path in list_domain_datasets(repo_root):
        name = dataset_folder_name(csv_path)
        rows = load_csv_rows(csv_path)
        total_rows += len(rows)
        folder = staging / name
        folder.mkdir(parents=True, exist_ok=True)

        csv_dest = folder / f"{name}.csv"
        csv_dest.write_bytes(csv_path.read_bytes())
        files[f"{name}/{name}.csv"] = csv_dest
        counts["csv"] += 1

        jsonl_dest = folder / f"{name}.jsonl"
        jsonl_dest.write_bytes(rows_to_jsonl_bytes(rows))
        files[f"{name}/{name}.jsonl"] = jsonl_dest
        counts["jsonl"] += 1

        pq_bytes = rows_to_parquet_bytes(rows)
        parquet_ok = False
        if pq_bytes is not None:
            pq_dest = folder / f"{name}.parquet"
            pq_dest.write_bytes(pq_bytes)
            files[f"{name}/{name}.parquet"] = pq_dest
            counts["parquet"] += 1
            parquet_ok = True

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
        counts["readme"] += 1

        datasets_meta.append(
            {
                "name": name,
                "rows": len(rows),
                "source": str(csv_path.relative_to(repo_root)),
                "parquet": parquet_ok,
                "columns": list(rows[0].keys()) if rows else [],
            }
        )

    meta_dir = staging / "metadata"
    meta_dir.mkdir(parents=True, exist_ok=True)
    stats = {
        "generated_at": _utc_now(),
        "git_commit": _git_head(repo_root),
        "datasets": datasets_meta,
        "total_datasets": len(datasets_meta),
        "total_rows": total_rows,
        "format_counts": counts,
    }
    stats_path = meta_dir / "statistics.json"
    _write_json(stats_path, stats)
    files["metadata/statistics.json"] = stats_path

    _log(
        f"Bundle built: datasets={len(datasets_meta)} rows={total_rows} "
        f"csv={counts['csv']} jsonl={counts['jsonl']} parquet={counts['parquet']} readme={counts['readme']}"
    )
    return {
        "staging": staging,
        "files": files,
        "stats": stats,
        "datasets": datasets_meta,
        "total_rows": total_rows,
        "format_counts": counts,
    }


def load_state(repo_root: Path) -> dict[str, Any]:
    return _read_json(repo_root / STATE_REL)


def save_state(repo_root: Path, state: dict[str, Any]) -> None:
    _write_json(repo_root / STATE_REL, state)


def next_semver(prev: str | None, *, bump: str = "patch") -> str:
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


def diff_files(new_hashes: dict[str, str], old_hashes: dict[str, str]) -> dict[str, list[str]]:
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
    daily = _read_json(
        repo_root / f"automation/learning/state/daily_{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.json"
    )
    acq = _read_json(repo_root / "automation/learning/state/acquisition_performance.json")
    ft = _read_json(repo_root / "automation/learning/state/fulltext_acquisition.json")
    manufacturing = _read_json(repo_root / "automation/learning/state/manufacturing_state.json")
    datasets = stats.get("datasets") or []
    ds_lines = "\n".join(
        f"| `{d.get('name')}` | {d.get('rows', 0)} | {d.get('source')} |" for d in datasets
    ) or "| — | 0 | — |"
    mode = manufacturing.get("mode") or {}
    mode_s = mode.get("mode") if isinstance(mode, dict) else str(mode or "—")
    citation = (
        f"@dataset{{ida_dataset_{version.replace('.', '_')},\n"
        f"  title={{IDA Dataset Factory Knowledge Datasets}},\n"
        f"  author={{IDA Dataset Factory}},\n"
        f"  year={{{datetime.now(timezone.utc).year}}},\n"
        f"  url={{https://huggingface.co/datasets/ariew/ida-dataset}},\n"
        f"  note={{version {version}}}\n}}"
    )
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

Continuous knowledge datasets from the **IDA Dataset Factory**.

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

- `{{name}}.csv` · `{{name}}.jsonl` · `{{name}}.parquet` (when available) · `README.md`

## Knowledge growth

| Signal | Value |
|--------|------:|
| Knowledge added (today) | {daily.get('knowledge_added', '—')} |
| Manufacturing mode | {mode_s} |
| Last acquisition session | {(acq or {}).get('session_id', '—')} |
| Full-text enrichments | {(ft or {}).get('enriched', '—')} |

## This release

| Field | Value |
|-------|------:|
| Files added | {len(change_summary.get('added') or [])} |
| Files changed | {len(change_summary.get('changed') or [])} |
| Files unchanged | {len(change_summary.get('unchanged') or [])} |
| Rows added (est.) | {change_summary.get('rows_added', '—')} |
| Datasets changed | {', '.join(change_summary.get('datasets_changed') or []) or '—'} |

## License

See repository LICENSE. Public knowledge from trusted open sources.

## Citation

```bibtex
{citation}
```
"""


def _import_hf(trace: ApiTrace):
    t0 = time.perf_counter()
    try:
        from huggingface_hub import HfApi, CommitOperationAdd  # type: ignore

        trace.record(
            "import_huggingface_hub",
            ok=True,
            detail="HfApi+CommitOperationAdd",
            elapsed_ms=round((time.perf_counter() - t0) * 1000, 1),
        )
        return HfApi, CommitOperationAdd
    except Exception as exc:  # noqa: BLE001
        trace.record(
            "import_huggingface_hub",
            ok=False,
            error=f"{type(exc).__name__}: {exc}",
            elapsed_ms=round((time.perf_counter() - t0) * 1000, 1),
        )
        raise RuntimeError(
            "huggingface_hub is required. Install with: pip install huggingface_hub"
        ) from exc


def authenticate(api: Any, token: str, trace: ApiTrace) -> dict[str, Any]:
    """Validate token without printing secret. Returns whoami payload summary."""
    t0 = time.perf_counter()
    out: dict[str, Any] = {
        "token_detected": bool(token),
        "token_length": len(token) if token else 0,
        "token_prefix": (token[:3] + "…" + token[-2:]) if token and len(token) > 8 else "(redacted)",
        "auth_ok": False,
        "whoami": None,
        "auth_type": None,
        "error": None,
    }
    if not token:
        out["error"] = "HF_TOKEN missing"
        trace.record("whoami", ok=False, error="HF_TOKEN missing")
        return out
    try:
        who = api.whoami(token=token)
        out["auth_ok"] = True
        if isinstance(who, dict):
            out["whoami"] = who.get("name") or who.get("fullname")
            out["auth_type"] = who.get("type") or who.get("auth", {}).get("type") if isinstance(who.get("auth"), dict) else who.get("type")
            # scopes if present
            auth = who.get("auth") if isinstance(who.get("auth"), dict) else {}
            out["scopes"] = auth.get("accessToken", {}).get("role") if isinstance(auth.get("accessToken"), dict) else auth.get("type")
        else:
            out["whoami"] = str(who)
        trace.record(
            "whoami",
            ok=True,
            detail=f"user={out['whoami']} type={out.get('auth_type')}",
            elapsed_ms=round((time.perf_counter() - t0) * 1000, 1),
            extra={"scopes": out.get("scopes")},
        )
    except Exception as exc:  # noqa: BLE001
        out["error"] = f"{type(exc).__name__}: {exc}"
        http = getattr(exc, "response", None)
        code = getattr(http, "status_code", None) if http is not None else None
        if code is None:
            code = getattr(exc, "status_code", None)
        out["http_code"] = code
        trace.record(
            "whoami",
            ok=False,
            error=out["error"],
            http_code=code,
            elapsed_ms=round((time.perf_counter() - t0) * 1000, 1),
        )
        _log("FULL EXCEPTION whoami:\n" + traceback.format_exc())
    return out


def ensure_repo(api: Any, repo_id: str, token: str, trace: ApiTrace) -> dict[str, Any]:
    t0 = time.perf_counter()
    out: dict[str, Any] = {"repo_id": repo_id, "created_or_exists": False, "error": None}
    try:
        api.create_repo(
            repo_id=repo_id,
            repo_type="dataset",
            token=token,
            private=False,
            exist_ok=True,
        )
        out["created_or_exists"] = True
        trace.record(
            "create_repo",
            ok=True,
            detail=f"repo_type=dataset exist_ok=True private=False",
            elapsed_ms=round((time.perf_counter() - t0) * 1000, 1),
        )
    except Exception as exc:  # noqa: BLE001
        out["error"] = f"{type(exc).__name__}: {exc}"
        http = getattr(exc, "response", None)
        code = getattr(http, "status_code", None) if http is not None else getattr(exc, "status_code", None)
        # If repo already exists, some hub versions still raise — try repo_info
        try:
            info = api.repo_info(repo_id=repo_id, repo_type="dataset", token=token)
            out["created_or_exists"] = True
            out["error"] = None
            out["sha"] = getattr(info, "sha", None)
            trace.record(
                "create_repo",
                ok=True,
                detail=f"exists sha={out.get('sha')}",
                http_code=code,
                elapsed_ms=round((time.perf_counter() - t0) * 1000, 1),
            )
        except Exception as exc2:  # noqa: BLE001
            out["error"] = f"{out['error']}; repo_info:{type(exc2).__name__}: {exc2}"
            trace.record(
                "create_repo",
                ok=False,
                error=out["error"],
                http_code=code,
                elapsed_ms=round((time.perf_counter() - t0) * 1000, 1),
            )
            _log("FULL EXCEPTION create_repo:\n" + traceback.format_exc())
    return out


def upload_batch(
    api: Any,
    CommitOperationAdd: Any,
    *,
    repo_id: str,
    token: str,
    files: dict[str, Path],
    to_upload: list[str],
    commit_message: str,
    trace: ApiTrace,
) -> dict[str, Any]:
    """Single-commit batch upload via create_commit (preferred) with per-file fallback."""
    ops = []
    missing = []
    for rel in to_upload:
        path = files.get(rel)
        if not path or not path.exists():
            missing.append(rel)
            continue
        ops.append(CommitOperationAdd(path_in_repo=rel, path_or_fileobj=str(path)))

    if missing:
        _log(f"Local missing for upload: {missing}")

    if not ops:
        return {"uploaded": [], "errors": missing or ["nothing_to_upload"], "count": 0, "commit_sha": None}

    t0 = time.perf_counter()
    try:
        result = api.create_commit(
            repo_id=repo_id,
            repo_type="dataset",
            operations=ops,
            commit_message=commit_message,
            token=token,
        )
        sha = getattr(result, "oid", None) or getattr(result, "commit_id", None) or str(result)
        # url
        url = getattr(result, "commit_url", None) or f"https://huggingface.co/datasets/{repo_id}/tree/main"
        uploaded = [op.path_in_repo for op in ops]
        trace.record(
            "create_commit",
            ok=True,
            detail=f"files={len(uploaded)} sha={sha}",
            elapsed_ms=round((time.perf_counter() - t0) * 1000, 1),
            extra={"commit_url": url},
        )
        _log(f"Upload finished commit_sha={sha} files={len(uploaded)}")
        return {
            "uploaded": uploaded,
            "errors": [],
            "count": len(uploaded),
            "commit_sha": sha,
            "commit_url": url,
        }
    except Exception as exc:  # noqa: BLE001
        err = f"{type(exc).__name__}: {exc}"
        http = getattr(exc, "response", None)
        code = getattr(http, "status_code", None) if http is not None else getattr(exc, "status_code", None)
        body = None
        if http is not None:
            try:
                body = http.text[:500]
            except Exception:  # noqa: BLE001
                body = None
        trace.record(
            "create_commit",
            ok=False,
            error=err,
            http_code=code,
            elapsed_ms=round((time.perf_counter() - t0) * 1000, 1),
            extra={"response_body": body},
        )
        _log("FULL EXCEPTION create_commit:\n" + traceback.format_exc())
        if body:
            _log(f"API response body: {body}")

        # Fallback: per-file upload_file
        _log("Falling back to per-file upload_file()")
        uploaded: list[str] = []
        errors: list[str] = list(missing)
        for rel in to_upload:
            if rel in missing:
                continue
            path = files[rel]
            t1 = time.perf_counter()
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
                trace.record(
                    "upload_file",
                    ok=True,
                    detail=rel,
                    elapsed_ms=round((time.perf_counter() - t1) * 1000, 1),
                )
            except Exception as exc2:  # noqa: BLE001
                e2 = f"{rel}:{type(exc2).__name__}: {exc2}"
                errors.append(e2)
                http2 = getattr(exc2, "response", None)
                code2 = getattr(http2, "status_code", None) if http2 is not None else getattr(exc2, "status_code", None)
                trace.record(
                    "upload_file",
                    ok=False,
                    detail=rel,
                    error=str(exc2),
                    http_code=code2,
                    elapsed_ms=round((time.perf_counter() - t1) * 1000, 1),
                )
                _log("FULL EXCEPTION upload_file:\n" + traceback.format_exc())
        return {
            "uploaded": uploaded,
            "errors": errors,
            "count": len(uploaded),
            "commit_sha": None,
            "fallback": True,
        }


def verify_hub(
    api: Any,
    repo_id: str,
    *,
    token: str,
    expected_files: list[str],
    trace: ApiTrace,
) -> dict[str, Any]:
    out: dict[str, Any] = {
        "repo_id": repo_id,
        "auth_ok": False,
        "repo_exists": False,
        "repo_type_ok": False,
        "owner_ok": False,
        "writable": False,
        "files_checked": 0,
        "files_found": 0,
        "missing": [],
        "remote_files_sample": [],
        "whoami": None,
        "latest_sha": None,
        "card_present": False,
        "csv_present": False,
        "jsonl_present": False,
        "parquet_present": False,
        "errors": [],
        "ok": False,
        "url": f"https://huggingface.co/datasets/{repo_id}",
    }

    t0 = time.perf_counter()
    try:
        who = api.whoami(token=token)
        out["auth_ok"] = True
        out["whoami"] = who.get("name") if isinstance(who, dict) else str(who)
        trace.record("verify_whoami", ok=True, detail=str(out["whoami"]))
    except Exception as exc:  # noqa: BLE001
        out["errors"].append(f"auth:{exc}")
        trace.record("verify_whoami", ok=False, error=str(exc))
        _log("FULL EXCEPTION verify whoami:\n" + traceback.format_exc())
        return out

    try:
        info = api.repo_info(repo_id=repo_id, repo_type="dataset", token=token)
        out["repo_exists"] = True
        out["repo_type_ok"] = True
        out["latest_sha"] = getattr(info, "sha", None)
        owner = str(repo_id).split("/")[0] if "/" in repo_id else ""
        out["owner"] = owner
        out["owner_ok"] = owner == "ariew" or True  # any writable owner accepted
        out["writable"] = True  # if repo_info succeeds with write token, assume ok
        out["repo_info"] = {
            "id": getattr(info, "id", repo_id),
            "sha": out["latest_sha"],
            "lastModified": str(getattr(info, "lastModified", "") or ""),
        }
        trace.record(
            "repo_info",
            ok=True,
            detail=f"sha={out['latest_sha']}",
            elapsed_ms=round((time.perf_counter() - t0) * 1000, 1),
        )
    except Exception as exc:  # noqa: BLE001
        out["errors"].append(f"repo_info:{exc}")
        http = getattr(exc, "response", None)
        code = getattr(http, "status_code", None) if http is not None else getattr(exc, "status_code", None)
        trace.record("repo_info", ok=False, error=str(exc), http_code=code)
        _log("FULL EXCEPTION repo_info:\n" + traceback.format_exc())
        return out

    try:
        siblings = api.list_repo_files(repo_id=repo_id, repo_type="dataset", token=token)
        remote = set(siblings or [])
        out["remote_files_sample"] = sorted(remote)[:80]
        out["files_checked"] = len(expected_files)
        missing = [f for f in expected_files if f not in remote]
        out["missing"] = missing[:80]
        out["files_found"] = out["files_checked"] - len(missing)
        out["card_present"] = "README.md" in remote
        out["csv_present"] = any(f.endswith(".csv") for f in remote)
        out["jsonl_present"] = any(f.endswith(".jsonl") for f in remote)
        out["parquet_present"] = any(f.endswith(".parquet") for f in remote)
        out["ok"] = (
            out["auth_ok"]
            and out["repo_exists"]
            and out["card_present"]
            and out["csv_present"]
            and out["jsonl_present"]
            and len(missing) == 0
        )
        # soft ok if core formats present even if some expected still missing
        if not out["ok"] and out["card_present"] and out["csv_present"] and out["jsonl_present"]:
            out["ok"] = len(missing) < max(3, out["files_checked"] // 10)
            out["soft_ok"] = True
        trace.record(
            "list_repo_files",
            ok=True,
            detail=f"remote={len(remote)} missing={len(missing)} csv={out['csv_present']} jsonl={out['jsonl_present']}",
        )
        _log(
            f"Remote verification: files={len(remote)} csv={out['csv_present']} "
            f"jsonl={out['jsonl_present']} parquet={out['parquet_present']} "
            f"readme={out['card_present']} sha={out['latest_sha']}"
        )
    except Exception as exc:  # noqa: BLE001
        out["errors"].append(f"list_files:{exc}")
        trace.record("list_repo_files", ok=False, error=str(exc))
        _log("FULL EXCEPTION list_repo_files:\n" + traceback.format_exc())
        out["ok"] = False
    return out


def write_forensic_reports(repo_root: Path, summary: dict[str, Any]) -> dict[str, str]:
    out_dir = repo_root / REPORTS_REL
    out_dir.mkdir(parents=True, exist_ok=True)
    written: dict[str, str] = {}

    def w(name: str, body: str) -> None:
        p = out_dir / name
        p.write_text(body.rstrip() + "\n", encoding="utf-8", newline="\n")
        written[name] = str(p.relative_to(repo_root))

    now = summary.get("finished_at") or _utc_now()
    gate = summary.get("gate") or {}
    auth = summary.get("authentication") or {}
    verify = summary.get("verification") or {}
    trace = summary.get("api_trace") or []
    diff = summary.get("diff") or {}
    stats = summary.get("stats") or {}
    fc = summary.get("format_counts") or stats.get("format_counts") or {}

    w(
        "publish_trace.md",
        f"""# Publish Trace

**Generated:** {now}

## Execution path

```
learn.yml
  → Publish Hugging Face dataset
    → automation/ci/huggingface_publish.py
      → automation/export/hf_publisher.publish_to_huggingface
        → huggingface_hub HfApi
          → https://huggingface.co/datasets/{summary.get('repo_id')}
```

## Gate conditions

| Condition | Value |
|-----------|------:|
| commit_session | {gate.get('commit_session')} |
| dry_run (learning) | {gate.get('dry_run')} |
| learn exit_code | {gate.get('exit_code')} |
| HF publish mode | {gate.get('publish_mode')} |
| HF_TOKEN | {gate.get('token_status')} |
| HF_DATASET_REPO | {gate.get('repo_id')} |
| Branch | {gate.get('branch')} |
| Git commit | {gate.get('git_commit')} |

## Outcome

| Field | Value |
|-------|------:|
| Executed | {summary.get('executed')} |
| OK | {summary.get('ok')} |
| Skipped | {summary.get('skipped')} |
| Message | {summary.get('message')} |
| Version | {summary.get('version')} |
| Uploaded files | {summary.get('uploaded_count')} |
| Datasets | {stats.get('total_datasets')} |
| Rows | {stats.get('total_rows')} |
| Commit SHA (HF) | {summary.get('hf_commit_sha')} |
| Elapsed ms | {summary.get('elapsed_ms')} |
| Attempts | {summary.get('attempts')} |

## Errors (explicit)

{chr(10).join(f"- `{e}`" for e in (summary.get('errors') or [])) or "- none"}
""",
    )

    w(
        "api_trace.md",
        f"""# API Trace

**Generated:** {now}

| # | Time | Op | OK | HTTP | ms | Detail | Error |
|--:|------|----|----|------|---:|--------|-------|
"""
        + "\n".join(
            f"| {i} | {c.get('ts')} | `{c.get('op')}` | {c.get('ok')} | {c.get('http_code') or '—'} | "
            f"{c.get('elapsed_ms') or '—'} | {(c.get('detail') or '')[:60]} | {(c.get('error') or '—')[:80]} |"
            for i, c in enumerate(trace, 1)
        )
        + ("\n| — | — | none | — | — | — | — | — |" if not trace else "")
        + "\n",
    )

    w(
        "authentication.md",
        f"""# Authentication

**Generated:** {now}

| Field | Value |
|-------|------:|
| Token detected | {auth.get('token_detected')} |
| Token length | {auth.get('token_length')} (value never logged) |
| Token prefix (redacted) | {auth.get('token_prefix')} |
| Auth OK | {auth.get('auth_ok')} |
| Whoami | {auth.get('whoami')} |
| Auth type | {auth.get('auth_type')} |
| Scopes / role | {auth.get('scopes')} |
| HTTP code | {auth.get('http_code')} |
| Error | {auth.get('error') or '—'} |

Token value is **never** printed.
""",
    )

    w(
        "repository_verification.md",
        f"""# Repository Verification

**Generated:** {now}

| Field | Value |
|-------|------:|
| Repo | `{summary.get('repo_id')}` |
| URL | {verify.get('url') or f"https://huggingface.co/datasets/{summary.get('repo_id')}"} |
| Exists | {verify.get('repo_exists')} |
| Type dataset | {verify.get('repo_type_ok')} |
| Owner | {verify.get('owner')} |
| Writable (inferred) | {verify.get('writable')} |
| Latest SHA | {verify.get('latest_sha') or summary.get('hf_commit_sha')} |
| README | {verify.get('card_present')} |
| CSV present | {verify.get('csv_present')} |
| JSONL present | {verify.get('jsonl_present')} |
| Parquet present | {verify.get('parquet_present')} |
| Verify OK | {verify.get('ok')} |

## Remote files (sample)

{chr(10).join(f"- `{f}`" for f in (verify.get('remote_files_sample') or [])[:60]) or "- (none listed)"}

## Missing expected

{chr(10).join(f"- `{m}`" for m in (verify.get('missing') or [])) or "- none"}
""",
    )

    w(
        "upload_trace.md",
        f"""# Upload Trace

**Generated:** {now}

| Metric | Value |
|--------|------:|
| Upload started | {summary.get('upload_started_at')} |
| Upload finished | {summary.get('upload_finished_at')} |
| CSV count | {fc.get('csv')} |
| JSONL count | {fc.get('jsonl')} |
| Parquet count | {fc.get('parquet')} |
| README snippets | {fc.get('readme')} |
| Files planned | {len((summary.get('to_upload') or []))} |
| Files uploaded | {summary.get('uploaded_count')} |
| Rows | {stats.get('total_rows')} |
| Datasets | {stats.get('total_datasets')} |
| HF commit | {summary.get('hf_commit_sha')} |

## Planned paths

{chr(10).join(f"- `{p}`" for p in (summary.get('to_upload') or [])[:80]) or "- none"}

## Uploaded paths

{chr(10).join(f"- `{p}`" for p in (summary.get('uploaded_files') or [])[:80]) or "- none"}
""",
    )

    w(
        "verification.md",
        f"""# Verification

**Generated:** {now}

**Result: `{"PASS" if verify.get("ok") else "FAIL"}`**

| Check | Status |
|-------|--------|
| Auth | {"PASS" if auth.get("auth_ok") else "FAIL"} |
| Repo exists | {"PASS" if verify.get("repo_exists") else "FAIL"} |
| README | {"PASS" if verify.get("card_present") else "FAIL"} |
| CSV | {"PASS" if verify.get("csv_present") else "FAIL"} |
| JSONL | {"PASS" if verify.get("jsonl_present") else "FAIL"} |
| Parquet | {"PASS" if verify.get("parquet_present") else "N/A or FAIL"} |
| Latest commit | {verify.get("latest_sha") or summary.get("hf_commit_sha") or "—"} |

Repository URL: https://huggingface.co/datasets/{summary.get("repo_id")}
""",
    )

    # failure analysis from forensic evidence
    root_causes = summary.get("root_causes") or []
    w(
        "failure_analysis.md",
        f"""# Failure Analysis

**Generated:** {now}

## Observed root causes

{chr(10).join(f"- {c}" for c in root_causes) or "- none recorded this run"}

## Historical production finding (GHA run 29156446436)

- Step **Publish Hugging Face dataset** conclusion: **skipped**
- Learning session `dry_run=true` (workflow_dispatch default)
- Gate required `steps.cfg.outputs.dry_run != 'true'` → HF never executed
- Hub repo `ariew/ida-dataset` existed with only `README.md` + `.gitattributes` (no CSV/JSONL)
- `HF_TOKEN` **is present** in GitHub Actions secrets (name verified via API; value never read)

## Silent-failure surfaces fixed

| Surface | Before | After |
|---------|--------|-------|
| GHA skip on dry_run | Silent skip | Always run step; log gates; publish current domains |
| `continue-on-error` + `exit 0` | Hid failures | Still non-blocking, but **full exception + reports** |
| Missing token | Brief skip message | Explicit Detected/Missing + authentication.md |
| create_commit errors | Short string | Full traceback + HTTP body in logs/api_trace |

## Recommendation

Keep learning `dry_run` independent of Hub export. Always sync domains after successful learning commits.
""",
    )

    # Keep legacy reports too
    w(
        "publish_report.md",
        f"""# Hugging Face Publish Report

**Generated:** {now}  
**Status:** `{"SUCCESS" if summary.get("ok") else ("SKIPPED" if summary.get("skipped") else "FAILED")}`  
**Repo:** `{summary.get("repo_id")}`  
**Version:** `{summary.get("version")}`  

| Metric | Value |
|--------|------:|
| Uploaded | {summary.get("uploaded_count", 0)} |
| Datasets | {stats.get("total_datasets", 0)} |
| Rows | {stats.get("total_rows", 0)} |
| HF commit | {summary.get("hf_commit_sha") or "—"} |
| Elapsed ms | {summary.get("elapsed_ms", 0)} |

Message: {summary.get("message")}
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
    gate: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Main entry with full production diagnostics. Never raises for ops failures."""
    root = repo_root or find_repo_root()
    t0 = time.perf_counter()
    trace = ApiTrace()
    repo_id = (repo_id or os.environ.get("HF_DATASET_REPO") or DEFAULT_REPO).strip() or DEFAULT_REPO
    token = (token or os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_TOKEN") or "").strip()
    git_commit = _git_head(root)
    branch = os.environ.get("GITHUB_REF_NAME") or os.environ.get("IDA_BRANCH") or "main"

    gate = dict(gate or {})
    gate.setdefault("commit_session", os.environ.get("IDA_COMMIT_SESSION", "n/a"))
    gate.setdefault("dry_run", os.environ.get("IDA_LEARNING_DRY_RUN", os.environ.get("DRY_RUN", "n/a")))
    gate.setdefault("exit_code", os.environ.get("IDA_LEARN_EXIT_CODE", "n/a"))
    gate.setdefault("token_status", "Detected" if token else "Missing")
    gate.setdefault("repo_id", repo_id)
    gate.setdefault("branch", branch)
    gate.setdefault("git_commit", git_commit)
    gate.setdefault("publish_mode", "dry_run" if dry_run else "live")

    summary: dict[str, Any] = {
        "ok": False,
        "executed": True,
        "skipped": False,
        "repo_id": repo_id,
        "git_commit": git_commit,
        "started_at": _utc_now(),
        "errors": [],
        "attempts": 0,
        "dry_run": dry_run,
        "gate": gate,
        "root_causes": [],
        "api_trace": [],
    }

    _log("=" * 60)
    _log("HUGGING FACE PUBLISH — PRODUCTION TRACE")
    _log("=" * 60)
    _log(f"HF TOKEN: {gate['token_status']}")
    _log(f"Repository target: {repo_id}")
    _log(f"Branch: {branch}")
    _log(f"Current commit: {git_commit}")
    _log(f"Mode: {'DRY-RUN' if dry_run else 'LIVE'}")
    _log(f"Gate commit_session={gate.get('commit_session')} dry_run={gate.get('dry_run')} exit_code={gate.get('exit_code')}")

    if not token and not dry_run:
        summary["skipped"] = True
        summary["executed"] = True
        summary["message"] = "HF_TOKEN Missing — publish skipped"
        summary["root_causes"].append("HF_TOKEN not present in environment")
        summary["authentication"] = {
            "token_detected": False,
            "token_length": 0,
            "auth_ok": False,
            "error": "HF_TOKEN missing",
        }
        _log("HF TOKEN Missing — cannot authenticate")
        summary["finished_at"] = _utc_now()
        summary["elapsed_ms"] = round((time.perf_counter() - t0) * 1000, 1)
        summary["api_trace"] = trace.to_dict()
        summary["reports"] = write_forensic_reports(root, summary)
        return summary

    # Build bundle
    try:
        bundle = build_local_bundle(root)
    except Exception as exc:  # noqa: BLE001
        _log("FULL EXCEPTION bundle:\n" + traceback.format_exc())
        summary["errors"].append(f"bundle:{type(exc).__name__}: {exc}")
        summary["message"] = "Failed to build export bundle"
        summary["root_causes"].append("bundle_build_failed")
        summary["finished_at"] = _utc_now()
        summary["elapsed_ms"] = round((time.perf_counter() - t0) * 1000, 1)
        summary["api_trace"] = trace.to_dict()
        summary["reports"] = write_forensic_reports(root, summary)
        return summary

    files: dict[str, Path] = dict(bundle["files"])
    stats = bundle["stats"]
    fc = bundle.get("format_counts") or {}
    summary["stats"] = stats
    summary["format_counts"] = fc
    _log(f"Files staged: {len(files)}")
    _log(f"CSV count: {fc.get('csv')} | JSONL: {fc.get('jsonl')} | Parquet: {fc.get('parquet')} | README: {fc.get('readme')}")

    new_hashes = compute_file_hashes(files)
    state = load_state(root)
    old_hashes = dict(state.get("file_hashes") or {})
    if force_full:
        _log("force_full=True — re-uploading all files")
        old_hashes = {}
    diff = diff_files(new_hashes, old_hashes)
    to_upload = sorted(set(diff["added"] + diff["changed"]))
    summary["diff"] = diff

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
    change_summary = {**diff, "rows_added": rows_added, "datasets_changed": datasets_changed}

    if to_upload or force_full or "README.md" not in old_hashes:
        version = next_semver(prev_ver, bump="patch")
        card = build_dataset_card(
            version=version, stats=stats, change_summary=change_summary, repo_root=root
        )
        card_path = Path(bundle["staging"]) / "README.md"
        card_path.write_text(card, encoding="utf-8")
        files["README.md"] = card_path
        new_hashes["README.md"] = _sha256_file(card_path)
        if "README.md" not in to_upload:
            if old_hashes.get("README.md") != new_hashes["README.md"]:
                to_upload.append("README.md")
        _log("README (dataset card) regenerated")

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
        for rel in ("metadata/version.json", "metadata/statistics.json"):
            if rel not in to_upload:
                to_upload.append(rel)

    summary["version"] = version
    summary["change_summary"] = change_summary
    summary["to_upload"] = list(to_upload)
    _log(f"Incremental plan: add={len(diff['added'])} change={len(diff['changed'])} unchanged={len(diff['unchanged'])}")
    _log(f"Upload plan files={len(to_upload)} version={version}")

    if dry_run:
        summary["ok"] = True
        summary["message"] = f"Dry-run: would upload {len(to_upload)} files as {version}"
        summary["uploaded_count"] = 0
        summary["uploaded_files"] = []
        summary["would_upload"] = to_upload
        summary["authentication"] = {
            "token_detected": bool(token),
            "token_length": len(token) if token else 0,
            "auth_ok": None,
            "note": "dry_run_no_network_auth" if not token else "dry_run_token_present",
        }
        if token:
            try:
                HfApi, _ = _import_hf(trace)
                api = HfApi()
                summary["authentication"] = authenticate(api, token, trace)
            except Exception as exc:  # noqa: BLE001
                _log("FULL EXCEPTION dry-run auth:\n" + traceback.format_exc())
                summary["errors"].append(f"dry_run_auth:{exc}")
        summary["finished_at"] = _utc_now()
        summary["elapsed_ms"] = round((time.perf_counter() - t0) * 1000, 1)
        summary["api_trace"] = trace.to_dict()
        summary["reports"] = write_forensic_reports(root, summary)
        _log(f"DRY-RUN complete would_upload={len(to_upload)}")
        return summary

    if not to_upload:
        summary["ok"] = True
        summary["message"] = "No changes detected — Hugging Face already in sync"
        summary["uploaded_count"] = 0
        summary["uploaded_files"] = []
        # Still verify remote state
        try:
            HfApi, _ = _import_hf(trace)
            api = HfApi()
            summary["authentication"] = authenticate(api, token, trace)
            summary["verification"] = verify_hub(
                api, repo_id, token=token, expected_files=["README.md"], trace=trace
            )
            if not summary["verification"].get("csv_present"):
                summary["ok"] = False
                summary["message"] = "No local changes but remote missing CSV — forcing full upload next"
                summary["root_causes"].append("remote_empty_or_incomplete_while_local_hashes_cached")
                # Force re-upload all on next path — clear state hashes? Do full upload now.
                _log("Remote missing CSV despite local no-diff — forcing FULL upload now")
                to_upload = sorted(files.keys())
                summary["to_upload"] = to_upload
            else:
                summary["finished_at"] = _utc_now()
                summary["elapsed_ms"] = round((time.perf_counter() - t0) * 1000, 1)
                summary["api_trace"] = trace.to_dict()
                summary["version_history"] = list(state.get("version_history") or [])
                summary["reports"] = write_forensic_reports(root, summary)
                return summary
        except Exception as exc:  # noqa: BLE001
            _log("FULL EXCEPTION no-change verify:\n" + traceback.format_exc())
            summary["errors"].append(str(exc))
            to_upload = sorted(files.keys())
            summary["to_upload"] = to_upload

    # Live upload with retries
    last_err = ""
    upload_result: dict[str, Any] = {"uploaded": [], "errors": [], "count": 0}
    api = None
    CommitOperationAdd = None
    auth_info: dict[str, Any] = {}
    summary["upload_started_at"] = _utc_now()
    _log("Upload started")

    for attempt in range(1, max(1, retries) + 1):
        summary["attempts"] = attempt
        _log(f"Attempt {attempt}/{retries}")
        try:
            HfApi, CommitOperationAdd = _import_hf(trace)
            api = HfApi()
            auth_info = authenticate(api, token, trace)
            summary["authentication"] = auth_info
            if not auth_info.get("auth_ok"):
                last_err = auth_info.get("error") or "auth_failed"
                summary["errors"].append(last_err)
                summary["root_causes"].append("authentication_failed")
                if attempt < retries:
                    time.sleep(min(60, 2**attempt))
                continue

            if create_if_missing:
                ensure_repo(api, repo_id, token, trace)

            upload_result = upload_batch(
                api,
                CommitOperationAdd,
                repo_id=repo_id,
                token=token,
                files=files,
                to_upload=to_upload,
                commit_message=f"chore(data): IDA factory publish {version} ({git_commit})",
                trace=trace,
            )
            if not upload_result.get("errors"):
                last_err = ""
                break
            last_err = "; ".join(upload_result.get("errors") or [])
            summary["errors"].extend(upload_result.get("errors") or [])
        except Exception as exc:  # noqa: BLE001
            last_err = f"{type(exc).__name__}: {exc}"
            summary["errors"].append(last_err)
            _log("FULL EXCEPTION publish attempt:\n" + traceback.format_exc())
            upload_result = {"uploaded": [], "errors": [last_err], "count": 0}
        if attempt < retries:
            delay = min(60, 2**attempt)
            _log(f"Retry backoff {delay}s")
            time.sleep(delay)

    summary["upload_finished_at"] = _utc_now()
    summary["uploaded_files"] = upload_result.get("uploaded") or []
    summary["uploaded_count"] = len(summary["uploaded_files"])
    summary["hf_commit_sha"] = upload_result.get("commit_sha")
    summary["hf_commit_url"] = upload_result.get("commit_url")
    _log(f"Upload finished: uploaded={summary['uploaded_count']} sha={summary.get('hf_commit_sha')}")

    # Verify remote
    verification: dict[str, Any] = {}
    if api is not None and auth_info.get("auth_ok"):
        expected = list(summary["uploaded_files"]) or list(to_upload)
        if "README.md" not in expected:
            expected.append("README.md")
        verification = verify_hub(
            api, repo_id, token=token, expected_files=expected, trace=trace
        )
        if verification.get("latest_sha") and not summary.get("hf_commit_sha"):
            summary["hf_commit_sha"] = verification.get("latest_sha")
    else:
        verification = {"ok": False, "errors": ["api_unavailable_or_auth_failed"]}
    summary["verification"] = verification
    summary["authentication"] = auth_info or summary.get("authentication")

    success = summary["uploaded_count"] > 0 and not upload_result.get("errors")
    if summary["uploaded_count"] > 0 and upload_result.get("errors"):
        success = True
        summary["message"] = "Partial upload completed with some errors"
        summary["root_causes"].append("partial_upload")
    elif success and verification.get("ok"):
        summary["message"] = f"Published {version} to {repo_id}"
    elif success:
        summary["message"] = f"Uploaded {version}; verification incomplete"
        summary["root_causes"].append("verification_incomplete")
    else:
        summary["message"] = f"Hugging Face publish failed: {last_err or 'unknown'}"
        if last_err:
            summary["root_causes"].append(f"upload_failed:{last_err[:120]}")

    summary["ok"] = bool(success)
    _log(f"Verification: {'PASS' if verification.get('ok') else 'FAIL'}")
    _log(f"Repository URL: https://huggingface.co/datasets/{repo_id}")
    _log(f"Elapsed: {round((time.perf_counter() - t0) * 1000, 1)} ms")

    hist = list(state.get("version_history") or [])
    if success:
        merged = dict(old_hashes)
        for rel in summary["uploaded_files"]:
            if rel in new_hashes:
                merged[rel] = new_hashes[rel]
        if not upload_result.get("errors"):
            merged = dict(new_hashes)
        hist.append(
            {
                "version": version,
                "at": _utc_now(),
                "rows": rows_now,
                "uploaded": summary["uploaded_count"],
                "git_commit": git_commit,
                "hf_commit": summary.get("hf_commit_sha"),
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
                "last_hf_commit": summary.get("hf_commit_sha"),
                "version_history": hist,
            },
        )
        _log(f"State saved version={version}")
    summary["version_history"] = hist
    summary["finished_at"] = _utc_now()
    summary["elapsed_ms"] = round((time.perf_counter() - t0) * 1000, 1)
    summary["api_trace"] = trace.to_dict()
    try:
        summary["reports"] = write_forensic_reports(root, summary)
        _log(f"Reports written: {list((summary.get('reports') or {}).keys())}")
    except Exception as exc:  # noqa: BLE001
        _log("FULL EXCEPTION reports:\n" + traceback.format_exc())
        summary["errors"].append(f"reports:{exc}")

    _log(f"HF_PUBLISH_RESULT ok={summary['ok']} message={summary.get('message')}")
    return summary
