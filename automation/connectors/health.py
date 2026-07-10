"""Connector health monitor."""

from __future__ import annotations

import csv
import time
from pathlib import Path
from typing import Any, Callable, Optional

from .types import ConnectorHealth, HealthReport, utc_now_iso


class HealthMonitor:
    def __init__(self, health_csv: Path) -> None:
        self.health_csv = health_csv
        self._runtime: dict[str, HealthReport] = {}

    def update(self, report: HealthReport) -> None:
        self._runtime[report.connector_id] = report
        self._persist()

    def get(self, connector_id: str) -> HealthReport:
        if connector_id in self._runtime:
            return self._runtime[connector_id]
        return HealthReport(
            connector_id=connector_id,
            health=ConnectorHealth.UNKNOWN.value,
            message="Waiting for first execution",
        )

    def all(self) -> list[HealthReport]:
        return list(self._runtime.values())

    def probe(
        self,
        connector_id: str,
        health_fn: Callable[[], Any],
        *,
        documents_retrieved: int = 0,
        errors: int = 0,
        success_rate: Optional[float] = None,
    ) -> HealthReport:
        started = time.time()
        try:
            result = health_fn()
            latency = (time.time() - started) * 1000.0
            ok = bool(result.get("ok", True)) if isinstance(result, dict) else bool(result)
            report = HealthReport(
                connector_id=connector_id,
                health=ConnectorHealth.HEALTHY.value if ok else ConnectorHealth.DEGRADED.value,
                latency_ms=round(latency, 2),
                success_rate=success_rate if success_rate is not None else (1.0 if ok else 0.0),
                documents_retrieved=documents_retrieved,
                errors=errors,
                message=str(result.get("message", "ok") if isinstance(result, dict) else "ok"),
                last_check=utc_now_iso(),
            )
        except Exception as exc:  # noqa: BLE001
            report = HealthReport(
                connector_id=connector_id,
                health=ConnectorHealth.ERROR.value,
                latency_ms=round((time.time() - started) * 1000.0, 2),
                success_rate=0.0,
                documents_retrieved=documents_retrieved,
                errors=errors + 1,
                message=str(exc),
                last_check=utc_now_iso(),
            )
        self.update(report)
        return report

    def _persist(self) -> None:
        self.health_csv.parent.mkdir(parents=True, exist_ok=True)
        headers = [
            "Connector ID",
            "Health",
            "Latency Ms",
            "Success Rate",
            "Documents Retrieved",
            "Errors",
            "Last Check",
            "Message",
        ]
        rows = [self.get(cid) for cid in sorted(self._runtime.keys())]
        # merge with existing ids if file present
        existing_ids: set[str] = set()
        if self.health_csv.exists():
            with self.health_csv.open("r", encoding="utf-8-sig", newline="") as handle:
                for row in csv.DictReader(handle):
                    existing_ids.add(row.get("Connector ID", ""))
        with self.health_csv.open("w", encoding="utf-8", newline="\n") as handle:
            writer = csv.DictWriter(handle, fieldnames=headers, lineterminator="\n")
            writer.writeheader()
            written = set()
            for report in rows:
                writer.writerow(
                    {
                        "Connector ID": report.connector_id,
                        "Health": report.health,
                        "Latency Ms": report.latency_ms if report.latency_ms is not None else "",
                        "Success Rate": report.success_rate if report.success_rate is not None else "",
                        "Documents Retrieved": report.documents_retrieved,
                        "Errors": report.errors,
                        "Last Check": report.last_check,
                        "Message": report.message,
                    }
                )
                written.add(report.connector_id)
