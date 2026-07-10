"""IO helpers for queues, reports, and CSV append-only publishing."""

from __future__ import annotations

import csv
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Iterator, Mapping, Sequence

from .models import CandidateRecord


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_jsonl(path: Path, records: Iterable[Mapping[str, Any]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
            count += 1
    return count


def append_jsonl(path: Path, record: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def iter_candidate_files(directory: Path) -> Iterator[Path]:
    if not directory.exists():
        return iter(())
    return iter(sorted(directory.glob("*.json")))


def save_candidate(directory: Path, candidate: CandidateRecord) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{candidate.candidate_id}.json"
    write_json(path, candidate.to_dict())
    return path


def load_candidate(path: Path) -> CandidateRecord:
    return CandidateRecord.from_dict(read_json(path))


def load_candidates(directory: Path) -> list[CandidateRecord]:
    return [load_candidate(path) for path in iter_candidate_files(directory)]


def move_candidate(src: Path, dest_dir: Path) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / src.name
    src.replace(dest)
    return dest


def read_csv_headers(path: Path) -> list[str]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        try:
            return next(reader)
        except StopIteration:
            return []


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def append_csv_rows(
    path: Path,
    rows: Sequence[Mapping[str, Any]],
    *,
    fieldnames: Sequence[str] | None = None,
) -> int:
    """Append rows to a CSV without overwriting existing data.

    If the file does not exist, write a header from fieldnames or row keys.
    Existing headers are preserved; new columns are not silently dropped —
    values for unknown columns are ignored; missing columns become empty.
    """
    if not rows:
        return 0

    path.parent.mkdir(parents=True, exist_ok=True)
    existing_headers = read_csv_headers(path)
    if existing_headers:
        headers = existing_headers
        write_header = False
    else:
        headers = list(fieldnames) if fieldnames else list(rows[0].keys())
        write_header = True

    with path.open("a", encoding="utf-8", newline="\n") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=headers,
            extrasaction="ignore",
            lineterminator="\n",
        )
        if write_header:
            writer.writeheader()
        for row in rows:
            writer.writerow({h: row.get(h, "") for h in headers})
    return len(rows)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = content.replace("\r\n", "\n").replace("\r", "\n")
    if not content.endswith("\n"):
        content += "\n"
    path.write_text(content, encoding="utf-8", newline="\n")


def git_diff_stat(repo_root: Path) -> str:
    """Return git diff --stat for reproducibility reports. Empty if git unavailable."""
    try:
        result = subprocess.run(
            ["git", "diff", "--stat"],
            cwd=str(repo_root),
            capture_output=True,
            text=True,
            check=False,
        )
        return (result.stdout or "").strip()
    except OSError:
        return ""


def git_status_porcelain(repo_root: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=str(repo_root),
            capture_output=True,
            text=True,
            check=False,
        )
        return (result.stdout or "").strip()
    except OSError:
        return ""
