"""Connector event stream for telemetry / ECC console."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

from .types import ConnectorEvent, utc_now_iso


class ConnectorEventLog:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def emit(
        self,
        event: str,
        connector_id: str,
        detail: str,
        *,
        level: str = "info",
        document_id: str | None = None,
    ) -> ConnectorEvent:
        row = ConnectorEvent(
            ts=utc_now_iso(),
            event=event,
            connector_id=connector_id,
            detail=detail,
            level=level,
            document_id=document_id,
        )
        with self.path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(json.dumps(row.to_dict(), ensure_ascii=False) + "\n")
        return row

    def recent(self, limit: int = 100) -> list[dict[str, Any]]:
        if not self.path.exists():
            return []
        lines = self.path.read_text(encoding="utf-8").splitlines()
        out: list[dict[str, Any]] = []
        for line in lines[-limit:]:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                continue
        return out
