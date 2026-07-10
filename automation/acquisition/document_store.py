"""Document queue store — automation/queue/documents/ (+ mirror of connector queue)."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Optional

from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root


class DocumentStore:
    """Persist acquired documents with required acquisition metadata."""

    STAGES = ("incoming", "processing", "processed", "failed")

    def __init__(self, repo_root: Path | None = None):
        self.repo_root = repo_root or find_repo_root()
        self.root = self.repo_root / "automation" / "queue" / "documents"
        for stage in self.STAGES:
            (self.root / stage).mkdir(parents=True, exist_ok=True)

    def _path(self, stage: str, document_id: str) -> Path:
        return self.root / stage / f"{document_id}.json"

    def _find(self, document_id: str) -> Optional[Path]:
        for stage in self.STAGES:
            p = self._path(stage, document_id)
            if p.exists():
                return p
        return None

    def enqueue(self, doc: dict[str, Any]) -> Path:
        """Store document record with required fields."""
        doc_id = str(doc.get("document_id") or "")
        if not doc_id:
            raise ValueError("document_id required")
        text = str(
            (doc.get("metadata") or {}).get("text_excerpt")
            or doc.get("text")
            or doc.get("snippet")
            or ""
        )
        content_hash = str(doc.get("hash") or doc.get("checksum") or "")
        if not content_hash and text:
            content_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        record = {
            "source_id": doc.get("source_id") or "",
            "url": doc.get("original_url") or doc.get("url") or "",
            "title": doc.get("title") or "",
            "retrieved_at": doc.get("retrieved_at") or utc_now_iso(),
            "published_at": (doc.get("metadata") or {}).get("published_at")
            or doc.get("published_at")
            or "",
            "hash": content_hash,
            "content_type": doc.get("content_type") or "text/plain",
            "mission_id": doc.get("mission_id") or "",
            "status": "incoming",
            "document_id": doc_id,
            "connector_id": doc.get("connector_id") or "",
            "trust_score": doc.get("trust_score"),
            "local_path": doc.get("local_path"),
            "metadata": doc.get("metadata") or {},
            "queued_at": utc_now_iso(),
        }
        path = self._path("incoming", doc_id)
        path.write_text(
            json.dumps(record, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        return path

    def move(self, document_id: str, stage: str) -> Optional[Path]:
        if stage not in self.STAGES:
            raise ValueError(f"invalid stage {stage}")
        src = self._find(document_id)
        if not src:
            return None
        data = json.loads(src.read_text(encoding="utf-8"))
        data["status"] = stage
        data["updated_at"] = utc_now_iso()
        dest = self._path(stage, document_id)
        dest.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        if src.resolve() != dest.resolve():
            src.unlink(missing_ok=True)
        return dest

    def load(self, document_id: str) -> Optional[dict[str, Any]]:
        p = self._find(document_id)
        if not p:
            return None
        return json.loads(p.read_text(encoding="utf-8"))

    def counts(self) -> dict[str, int]:
        return {
            stage: len(list((self.root / stage).glob("*.json")))
            for stage in self.STAGES
        }

    def list_stage(self, stage: str = "incoming") -> list[dict[str, Any]]:
        folder = self.root / stage
        rows: list[dict[str, Any]] = []
        for p in sorted(folder.glob("*.json")):
            try:
                rows.append(json.loads(p.read_text(encoding="utf-8")))
            except Exception:  # noqa: BLE001
                continue
        return rows
