"""Select connectors for a planned query using registry + trust."""

from __future__ import annotations

from typing import Any, Optional


class SourceSelector:
    def select(
        self,
        connectors: list[dict[str, Any]],
        *,
        preferred_types: Optional[list[str]] = None,
        limit: int = 8,
    ) -> list[str]:
        enabled = [c for c in connectors if c.get("enabled")]
        if preferred_types:
            preferred = {
                c["connector_id"]
                for c in enabled
                if c.get("type") in preferred_types
            }
            ordered = [c for c in enabled if c["connector_id"] in preferred]
            ordered += [c for c in enabled if c["connector_id"] not in preferred]
        else:
            ordered = enabled
        ordered.sort(key=lambda c: int(c.get("priority") or 0), reverse=True)
        return [str(c["connector_id"]) for c in ordered[:limit]]
