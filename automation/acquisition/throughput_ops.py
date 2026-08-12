"""Production throughput optimization helpers.

Architecture-compatible: does not redesign queues, missions, or schemas.
Optimizes prioritization, worker scaling, process ratio, auto-publish gates,
queue rebalance signals, and performance report generation from real state only.
"""

from __future__ import annotations

import json
import math
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root

# Process ratio target: discovered → processed
TARGET_PROCESS_RATIO = 0.90

# Auto-publish confidence — lowered so free DDG multi-table fill can land rows
# (still requires provenance + validation; quality gate remains in integrity)
AUTO_PUBLISH_CONFIDENCE = 0.55
MANUAL_REVIEW_CONFIDENCE = 0.40

# Adaptive download workers based on observed connector latency
WORKER_LADDER = (2, 4, 8, 16)


def adaptive_workers(avg_latency_ms: float, *, max_workers: int = 16) -> int:
    """Scale download workers from latency: slow connectors → fewer workers."""
    lat = max(0.0, float(avg_latency_ms or 0))
    if lat <= 400:
        n = 16
    elif lat <= 1200:
        n = 8
    elif lat <= 3000:
        n = 4
    else:
        n = 2
    allowed = [w for w in WORKER_LADDER if w <= max_workers]
    chosen = allowed[0] if allowed else 2
    for w in allowed:
        if w <= n:
            chosen = w
    return chosen
