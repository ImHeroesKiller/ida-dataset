"""Production integrity guard — reject rows that would increase integrity debt.

Observe append-only publish path. Does not rewrite history or datasets.
"""

from __future__ import annotations

from typing import Any, Optional


def _to_float(v: Any) -> Optional[float]:
    if v is None or v == "":
        return None
    try:
        x = float(v)
        if x > 1:
            return x / 100.0 if x > 1 else x
        return x
    except (TypeError, ValueError):
        return None


def validate_row(
    row: dict[str, Any],
    *,
    dataset_stem: str = "",
    schema: Optional[dict[str, Any]] = None,
) -> tuple[bool, str]:
    """Return (ok, reason). ok=False blocks publish."""
    if not isinstance(row, dict):
        return False, "row_not_dict"

    conf = None
    for k in ("confidence", "Confidence", "score", "quality_score"):
        if k in row and row[k] not in (None, ""):
            conf = _to_float(row[k])
            break

    # Soft bootstrap floor for free DuckDuckGo multi-table fill
    if conf is not None and conf < 0.45:
        return False, f"confidence_below_threshold:{conf}"

    # Required provenance-ish fields when present in payload
    for key in ("entity_id", "Entity ID", "source_url", "source_id"):
        if key in row and (row[key] is None or str(row[key]).strip() == ""):
            return False, f"empty_required:{key}"

    return True, "ok"
