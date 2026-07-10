"""Rate limiting for connectors."""

from __future__ import annotations

import time
from collections import defaultdict, deque
from typing import Deque, Dict


class RateLimiter:
    def __init__(self) -> None:
        self._hits: Dict[str, Deque[float]] = defaultdict(deque)

    def allow(self, key: str, per_minute: int) -> bool:
        if per_minute <= 0:
            return False
        now = time.time()
        window = self._hits[key]
        while window and now - window[0] > 60.0:
            window.popleft()
        if len(window) >= per_minute:
            return False
        window.append(now)
        return True

    def remaining(self, key: str, per_minute: int) -> int:
        now = time.time()
        window = self._hits[key]
        while window and now - window[0] > 60.0:
            window.popleft()
        return max(0, per_minute - len(window))
