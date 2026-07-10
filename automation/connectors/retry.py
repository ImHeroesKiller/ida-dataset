"""Retry engine with exponential backoff and circuit breaker."""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Callable, Dict, Optional, TypeVar

T = TypeVar("T")


@dataclass
class CircuitState:
    failures: int = 0
    opened_at: Optional[float] = None
    state: str = "closed"  # closed | open | half_open


class RetryEngine:
    def __init__(
        self,
        *,
        max_retries: int = 3,
        base_seconds: float = 1.0,
        max_seconds: float = 60.0,
        breaker_failures: int = 5,
        cooldown_seconds: float = 300.0,
    ) -> None:
        self.max_retries = max_retries
        self.base_seconds = base_seconds
        self.max_seconds = max_seconds
        self.breaker_failures = breaker_failures
        self.cooldown_seconds = cooldown_seconds
        self._circuits: Dict[str, CircuitState] = {}

    def circuit(self, key: str) -> CircuitState:
        if key not in self._circuits:
            self._circuits[key] = CircuitState()
        return self._circuits[key]

    def is_available(self, key: str) -> bool:
        c = self.circuit(key)
        if c.state != "open":
            return True
        if c.opened_at is None:
            return True
        if time.time() - c.opened_at >= self.cooldown_seconds:
            c.state = "half_open"
            return True
        return False

    def record_success(self, key: str) -> None:
        c = self.circuit(key)
        c.failures = 0
        c.state = "closed"
        c.opened_at = None

    def record_failure(self, key: str) -> None:
        c = self.circuit(key)
        c.failures += 1
        if c.failures >= self.breaker_failures:
            c.state = "open"
            c.opened_at = time.time()

    def run(self, key: str, fn: Callable[[], T], *, dry_run: bool = True) -> T:
        if not self.is_available(key):
            raise RuntimeError(f"circuit_open:{key}")
        last_err: Optional[Exception] = None
        attempts = self.max_retries + 1
        for attempt in range(attempts):
            try:
                result = fn()
                self.record_success(key)
                return result
            except Exception as exc:  # noqa: BLE001 — connector boundary
                last_err = exc
                self.record_failure(key)
                if attempt >= self.max_retries:
                    break
                delay = min(self.max_seconds, self.base_seconds * (2**attempt))
                if not dry_run:
                    time.sleep(delay)
        assert last_err is not None
        raise last_err
