"""Production Trace — end-to-end manufacturing-line observability.

Records real runtime events only. Never invents counters.
"""

from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Optional

from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root

STAGE_ORDER = [
    "mission",
    "source_discovery",
    "connector",
    "document_discovery",
    "document_download",
    "extraction",
    "candidate_validation",
    "publish_queue",
    "append_dataset",
    "export",
    "git_commit",
    "push",
]


@dataclass
class StageTrace:
    name: str
    start_time: str = ""
    finish_time: str = ""
    duration_ms: float = 0.0
    status: str = "pending"  # pending|running|completed|failed|skipped
    rows: int = 0
    documents: int = 0
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    meta: dict[str, Any] = field(default_factory=dict)
    _t0: float = field(default=0.0, repr=False)

    def start(self) -> None:
        self.start_time = utc_now_iso()
        self._t0 = time.perf_counter()
        self.status = "running"

    def finish(
        self,
        *,
        status: str = "completed",
        rows: int | None = None,
        documents: int | None = None,
        error: str | None = None,
        warning: str | None = None,
        **meta: Any,
    ) -> None:
        self.finish_time = utc_now_iso()
        if self._t0:
            self.duration_ms = round((time.perf_counter() - self._t0) * 1000, 1)
        self.status = status
        if rows is not None:
            self.rows = rows
        if documents is not None:
            self.documents = documents
        if error:
            self.errors.append(error)
        if warning:
            self.warnings.append(warning)
        if meta:
            self.meta.update(meta)

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d.pop("_t0", None)
        return d


class ProductionTrace:
    """Session-scoped manufacturing trace."""

    def __init__(
        self,
        *,
        mission: str = "",
        mission_id: str = "",
        session_id: str = "",
        dataset: str = "industry_library",
        repo_root: Path | None = None,
    ) -> None:
        self.repo_root = repo_root or find_repo_root()
        self.mission = mission
        self.mission_id = mission_id
        self.session_id = session_id
        self.dataset = dataset
        self.started_at = utc_now_iso()
        self.finished_at = ""
        self.stages: dict[str, StageTrace] = {
            name: StageTrace(name=name) for name in STAGE_ORDER
        }
        self.connectors: list[dict[str, Any]] = []
        self.documents: list[dict[str, Any]] = []
        self.candidates: list[dict[str, Any]] = []
        self.evidence_chains: list[dict[str, Any]] = []
        self.publish: dict[str, Any] = {
            "extracted": 0,
            "validated": 0,
            "rejected": 0,
            "queued": 0,
            "published": 0,
            "skipped": 0,
            "duplicate": 0,
            "by_dataset": {},
        }
        self.document_queue: dict[str, int] = {
            "queued": 0,
            "processing": 0,
            "completed": 0,
            "failed": 0,
            "duplicates": 0,
        }
        self.exports: dict[str, Any] = {
            "jsonl": False,
            "openai": False,
            "huggingface": False,
            "notes": [],
        }
        self.git: dict[str, Any] = {
            "commit": False,
            "push": False,
            "notes": [],
        }
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.current_stage = "mission"
        self.current_connector = ""
        self.current_document = ""
        self.last_connector = ""
        self.last_document = ""
        self.last_published_entity = ""

    def stage(self, name: str) -> StageTrace:
        if name not in self.stages:
            self.stages[name] = StageTrace(name=name)
        self.current_stage = name
        return self.stages[name]

    def start_stage(self, name: str) -> StageTrace:
        st = self.stage(name)
        st.start()
        self._write_live()
        return st

    def finish_stage(self, name: str, **kwargs: Any) -> StageTrace:
        st = self.stage(name)
        if st.status == "pending":
            st.start()
        st.finish(**kwargs)
        self._write_live()
        return st

    def add_connector(self, row: dict[str, Any]) -> None:
        self.connectors.append(row)
        self.last_connector = str(row.get("name") or row.get("connector_id") or "")
        self.current_connector = self.last_connector
        self._write_live()

    def add_document(self, row: dict[str, Any]) -> None:
        self.documents.append(row)
        did = str(row.get("document_id") or "")
        self.last_document = did
        self.current_document = did
        status = str(row.get("status") or "queued")
        if status in self.document_queue:
            self.document_queue[status] = self.document_queue.get(status, 0) + 1
        self._write_live()

    def add_candidate(self, row: dict[str, Any]) -> None:
        self.candidates.append(row)
        self._write_live()

    def add_evidence(
        self,
        *,
        dataset: str,
        entity: str,
        entity_id: str,
        candidate_id: str,
        document_id: str,
        document_title: str,
        connector_id: str,
        connector_name: str,
        source_id: str,
        source_name: str,
        url: str,
        confidence: float,
        evidence_snippet: str = "",
    ) -> None:
        chain = {
            "dataset": dataset,
            "entity": entity,
            "entity_id": entity_id,
            "candidate_id": candidate_id,
            "document_id": document_id,
            "document_title": document_title,
            "connector_id": connector_id,
            "connector_name": connector_name,
            "source_id": source_id,
            "source_name": source_name,
            "url": url,
            "confidence": confidence,
            "evidence_snippet": evidence_snippet[:400],
        }
        self.evidence_chains.append(chain)
        self.last_published_entity = entity
        self._write_live()

    def set_publish_counts(
        self,
        *,
        extracted: int,
        validated: int,
        rejected: int,
        queued: int,
        published: int,
        skipped: int = 0,
        duplicate: int = 0,
        by_dataset: Optional[dict[str, int]] = None,
    ) -> None:
        self.publish = {
            "extracted": extracted,
            "validated": validated,
            "rejected": rejected,
            "queued": queued,
            "published": published,
            "skipped": skipped,
            "duplicate": duplicate,
            "by_dataset": by_dataset or {},
            "balance_ok": (
                extracted == validated + rejected
                and published + duplicate + skipped <= validated
            ),
        }
        self._write_live()

    def finalize(self, *, ok: bool = True) -> dict[str, Any]:
        self.finished_at = utc_now_iso()
        # mark unfinished stages
        for st in self.stages.values():
            if st.status == "running":
                st.finish(status="completed" if ok else "failed")
            elif st.status == "pending" and st.name in {
                "export",
                "git_commit",
                "push",
            }:
                st.finish(
                    status="skipped",
                    warning="Not executed in this session (handled by CI/export jobs)",
                )
        payload = self.to_dict()
        self._persist(payload)
        self._write_live(payload)
        return payload

    def to_dict(self) -> dict[str, Any]:
        return {
            "version": "1.0",
            "mission": self.mission,
            "mission_id": self.mission_id,
            "session_id": self.session_id,
            "dataset": self.dataset,
            "started_at": self.started_at,
            "finished_at": self.finished_at or utc_now_iso(),
            "current_stage": self.current_stage,
            "current_connector": self.current_connector,
            "current_document": self.current_document,
            "last_connector": self.last_connector,
            "last_document": self.last_document,
            "last_published_entity": self.last_published_entity,
            "stages": [self.stages[n].to_dict() for n in STAGE_ORDER if n in self.stages],
            "connectors": self.connectors,
            "documents": self.documents,
            "candidates": self.candidates,
            "document_queue": self.document_queue,
            "publish": self.publish,
            "evidence_chains": self.evidence_chains,
            "exports": self.exports,
            "git": self.git,
            "errors": self.errors,
            "warnings": self.warnings,
            "summary": {
                "connectors_ok": sum(
                    1 for c in self.connectors if c.get("status") in {"ok", "success", "no_updates"}
                ),
                "connectors_failed": sum(
                    1 for c in self.connectors if c.get("status") in {"error", "failed"}
                ),
                "documents_discovered": sum(
                    int(c.get("documents_discovered") or 0) for c in self.connectors
                ),
                "documents_downloaded": len(
                    [d for d in self.documents if d.get("status") != "failed"]
                ),
                "documents_failed": len(
                    [d for d in self.documents if d.get("status") == "failed"]
                ),
                "documents_duplicates": int(self.document_queue.get("duplicates") or 0),
                "candidates_extracted": int(self.publish.get("extracted") or 0),
                "candidates_validated": int(self.publish.get("validated") or 0),
                "candidates_rejected": int(self.publish.get("rejected") or 0),
                "rows_published": int(self.publish.get("published") or 0),
                "rows_duplicate": int(self.publish.get("duplicate") or 0),
            },
        }

    def format_console(self) -> str:
        """Human-readable manufacturing console."""
        s = self.to_dict()
        lines: list[str] = []
        lines.append(f"Mission")
        lines.append(f"  {self.mission or self.mission_id or '—'}")
        lines.append("")
        lines.append("--------------------------------")
        lines.append("CONNECTORS")
        lines.append("")
        if not self.connectors:
            lines.append("  (none)")
        for c in self.connectors:
            mark = "✓" if c.get("status") in {"ok", "success", "no_updates"} else "✗"
            name = c.get("name") or c.get("connector_id")
            http = c.get("http_status")
            http_s = f"HTTP {http}" if http else (c.get("status") or "")
            disc = int(c.get("documents_discovered") or 0)
            down = int(c.get("documents_downloaded") or 0)
            if c.get("status") == "no_updates" or (disc == 0 and c.get("status") in {"ok", "success"}):
                lines.append(f"{mark} {name}")
                lines.append(f"  {http_s or 'OK'}")
                lines.append(f"  No updates" if disc == 0 else f"  {disc} documents · {down} downloaded")
            else:
                lines.append(f"{mark} {name}")
                lines.append(f"  {http_s}")
                lines.append(f"  {disc} documents")
                lines.append(f"  {down} downloaded")
            if c.get("error"):
                lines.append(f"  error: {c['error']}")
            lines.append("")
        lines.append("--------------------------------")
        lines.append("DOCUMENTS")
        lines.append("")
        lines.append(f"Discovered")
        lines.append(f"  {s['summary']['documents_discovered']}")
        lines.append("")
        lines.append(f"Downloaded")
        lines.append(f"  {s['summary']['documents_downloaded']}")
        lines.append("")
        lines.append(f"Duplicates")
        lines.append(f"  {s['summary']['documents_duplicates']}")
        lines.append("")
        lines.append("--------------------------------")
        lines.append("EXTRACTION")
        lines.append("")
        lines.append(f"Candidates")
        lines.append(f"  {self.publish.get('extracted', 0)}")
        lines.append("")
        lines.append(f"Accepted")
        lines.append(f"  {self.publish.get('validated', 0)}")
        lines.append("")
        lines.append(f"Rejected")
        lines.append(f"  {self.publish.get('rejected', 0)}")
        lines.append("")
        lines.append("--------------------------------")
        lines.append("PUBLISH")
        lines.append("")
        by_ds = self.publish.get("by_dataset") or {}
        if by_ds:
            for ds, n in by_ds.items():
                short = (
                    ds.replace("_library", "")
                    .replace("business_", "")
                    .replace("_", " ")
                    .title()
                )
                lines.append(f"{short}")
                lines.append(f"  +{n}")
                lines.append("")
        else:
            lines.append(f"Rows")
            lines.append(f"  +{self.publish.get('published', 0)}")
            lines.append("")
        if self.publish.get("duplicate"):
            lines.append(f"Duplicate")
            lines.append(f"  {self.publish.get('duplicate')}")
            lines.append("")
        lines.append("--------------------------------")
        lines.append("DATASET")
        lines.append("")
        lines.append(f"Rows appended")
        lines.append(f"  {self.publish.get('published', 0)}")
        lines.append("")
        lines.append("--------------------------------")
        lines.append("EXPORT")
        lines.append("")
        lines.append(
            "JSONL updated" if self.exports.get("jsonl") else "JSONL deferred to export job"
        )
        lines.append(
            "OpenAI updated" if self.exports.get("openai") else "OpenAI deferred to export job"
        )
        lines.append(
            "HF updated" if self.exports.get("huggingface") else "HF deferred to export job"
        )
        lines.append("")
        lines.append("--------------------------------")
        lines.append(
            "Git commit completed"
            if self.git.get("commit")
            else "Git commit deferred to CI"
        )
        lines.append(
            "Push completed" if self.git.get("push") else "Push deferred to CI"
        )
        lines.append("")
        # balance line
        p = self.publish
        lines.append(
            f"Balance: extracted={p.get('extracted')} "
            f"validated={p.get('validated')} rejected={p.get('rejected')} "
            f"queued={p.get('queued')} published={p.get('published')} "
            f"duplicate={p.get('duplicate')} skipped={p.get('skipped')}"
        )
        return "\n".join(lines)

    def _persist(self, payload: dict[str, Any] | None = None) -> Path:
        data = payload or self.to_dict()
        root = self.repo_root
        out_dir = root / "reports" / "production"
        out_dir.mkdir(parents=True, exist_ok=True)
        sid = self.session_id or "latest"
        path = out_dir / f"production_trace_{sid}.json"
        path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        # latest pointer for dashboard
        latest = root / "automation" / "learning" / "state" / "production_trace.json"
        latest.parent.mkdir(parents=True, exist_ok=True)
        latest.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        return path

    def _write_live(self, payload: dict[str, Any] | None = None) -> None:
        """Lightweight live snapshot for dashboard polling."""
        try:
            data = payload or {
                "updated_at": utc_now_iso(),
                "mission": self.mission,
                "mission_id": self.mission_id,
                "session_id": self.session_id,
                "current_stage": self.current_stage,
                "current_connector": self.current_connector,
                "current_document": self.current_document,
                "last_connector": self.last_connector,
                "last_document": self.last_document,
                "last_published_entity": self.last_published_entity,
                "publish": self.publish,
                "document_queue": self.document_queue,
                "connectors": self.connectors[-8:],
                "summary": {
                    "documents_downloaded": len(self.documents),
                    "candidates_extracted": len(self.candidates),
                    "rows_published": int(self.publish.get("published") or 0),
                },
            }
            path = (
                self.repo_root
                / "automation"
                / "learning"
                / "state"
                / "production_trace.json"
            )
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
                newline="\n",
            )
        except Exception:  # noqa: BLE001
            pass


def load_latest_trace(repo_root: Path | None = None) -> dict[str, Any]:
    root = repo_root or find_repo_root()
    path = root / "automation" / "learning" / "state" / "production_trace.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return {}
