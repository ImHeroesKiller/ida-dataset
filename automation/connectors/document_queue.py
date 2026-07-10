"""Document queue — all acquired docs land here, never in domain datasets."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Optional

from .types import DocumentRef, DocumentStatus, utc_now_iso


class DocumentQueue:
    def __init__(
        self,
        *,
        incoming: Path,
        processing: Path,
        processed: Path,
        failed: Path,
    ) -> None:
        self.incoming = incoming
        self.processing = processing
        self.processed = processed
        self.failed = failed
        for path in (incoming, processing, processed, failed):
            path.mkdir(parents=True, exist_ok=True)

    def _path_for(self, status: str, document_id: str) -> Path:
        folder = {
            DocumentStatus.INCOMING.value: self.incoming,
            DocumentStatus.PROCESSING.value: self.processing,
            DocumentStatus.PROCESSED.value: self.processed,
            DocumentStatus.FAILED.value: self.failed,
        }.get(status, self.incoming)
        return folder / f"{document_id}.json"

    def enqueue(self, doc: DocumentRef) -> Path:
        doc.status = DocumentStatus.INCOMING.value
        if not doc.checksum:
            raw = f"{doc.original_url}|{doc.connector_id}|{doc.retrieved_at}"
            doc.checksum = hashlib.sha256(raw.encode("utf-8")).hexdigest()
        path = self._path_for(doc.status, doc.document_id)
        path.write_text(
            json.dumps(doc.to_dict(), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        return path

    def load(self, document_id: str) -> Optional[DocumentRef]:
        for status in (
            DocumentStatus.INCOMING.value,
            DocumentStatus.PROCESSING.value,
            DocumentStatus.PROCESSED.value,
            DocumentStatus.FAILED.value,
        ):
            path = self._path_for(status, document_id)
            if path.exists():
                data = json.loads(path.read_text(encoding="utf-8"))
                return DocumentRef(**{k: data.get(k) for k in DocumentRef.__dataclass_fields__})
        return None

    def move(self, document_id: str, new_status: str) -> Optional[Path]:
        doc = self.load(document_id)
        if not doc:
            return None
        old = self._path_for(doc.status, document_id)
        doc.status = new_status
        new_path = self._path_for(new_status, document_id)
        new_path.write_text(
            json.dumps(doc.to_dict(), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        if old.exists() and old != new_path:
            old.unlink(missing_ok=True)
        return new_path

    def list_status(self, status: str) -> list[dict[str, Any]]:
        folder = {
            DocumentStatus.INCOMING.value: self.incoming,
            DocumentStatus.PROCESSING.value: self.processing,
            DocumentStatus.PROCESSED.value: self.processed,
            DocumentStatus.FAILED.value: self.failed,
        }.get(status, self.incoming)
        rows: list[dict[str, Any]] = []
        for path in sorted(folder.glob("DOC-*.json")):
            try:
                rows.append(json.loads(path.read_text(encoding="utf-8")))
            except (OSError, json.JSONDecodeError):
                continue
        return rows

    def counts(self) -> dict[str, int]:
        return {
            "incoming": len(list(self.incoming.glob("DOC-*.json"))),
            "processing": len(list(self.processing.glob("DOC-*.json"))),
            "processed": len(list(self.processed.glob("DOC-*.json"))),
            "failed": len(list(self.failed.glob("DOC-*.json"))),
        }

    def snapshot(self) -> dict[str, Any]:
        counts = self.counts()
        return {
            "updated_at": utc_now_iso(),
            "counts": counts,
            "queue_length": sum(counts.values()),
            "incoming": self.list_status("incoming")[:50],
            "processing": self.list_status("processing")[:20],
            "failed": self.list_status("failed")[:20],
        }
