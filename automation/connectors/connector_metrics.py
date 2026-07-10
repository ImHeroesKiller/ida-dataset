"""Connector metrics persistence."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .types import utc_now_iso


class ConnectorMetrics:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def load(self) -> dict[str, Any]:
        empty = {
            "updated_at": None,
            "connectors": {},
            "totals": {
                "searches": 0,
                "fetches": 0,
                "downloads": 0,
                "cached_hits": 0,
                "errors": 0,
                "rate_limited": 0,
                "queue_added": 0,
            },
        }
        if not self.path.exists():
            return empty
        try:
            text = self.path.read_text(encoding="utf-8").strip()
            if not text:
                return empty
            return json.loads(text)
        except (OSError, json.JSONDecodeError):
            return empty


    def save(self, data: dict[str, Any]) -> None:
        data["updated_at"] = utc_now_iso()
        self.path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )

    def bump(self, connector_id: str, **counters: int) -> dict[str, Any]:
        data = self.load()
        totals = data.setdefault("totals", {})
        conn = data.setdefault("connectors", {}).setdefault(
            connector_id,
            {
                "searches": 0,
                "fetches": 0,
                "downloads": 0,
                "cached_hits": 0,
                "errors": 0,
                "rate_limited": 0,
                "documents_retrieved": 0,
            },
        )
        for key, value in counters.items():
            conn[key] = int(conn.get(key, 0)) + int(value)
            totals[key] = int(totals.get(key, 0)) + int(value)
        self.save(data)
        return data
