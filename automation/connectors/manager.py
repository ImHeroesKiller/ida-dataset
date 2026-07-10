"""Connector Manager — only component that executes connectors.

Planner never calls connectors directly.
Manager validates policy/source trust, throttles, caches, retries, queues docs.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Optional

from .base_connector import BaseConnector
from .builtin import CONNECTOR_CLASSES
from .cache import JsonFileCache
from .connector_events import ConnectorEventLog
from .connector_metrics import ConnectorMetrics
from .document_queue import DocumentQueue
from .health import HealthMonitor
from .registry import ConnectorRegistry, load_connectors_config
from .retry import RetryEngine
from .throttle import RateLimiter
from .types import DocumentRef, SearchQuery, SearchResult, utc_now_iso


class ConnectorManager:
    def __init__(self, repo_root: Path | None = None, config: dict[str, Any] | None = None):
        self.config = config or load_connectors_config(repo_root)
        self.repo_root = Path(self.config["_repo_root"])
        self.registry = ConnectorRegistry(self.config)
        paths = self.config.get("paths") or {}
        defaults = self.config.get("defaults") or {}

        self.events = ConnectorEventLog(
            self.repo_root / paths.get("events", "automation/connectors/cache/events.jsonl")
        )
        self.metrics = ConnectorMetrics(
            self.repo_root / paths.get("metrics", "automation/connectors/cache/metrics.json")
        )
        self.cache = JsonFileCache(
            self.repo_root / paths.get("connector_cache", "automation/connectors/cache"),
            default_ttl=int(defaults.get("cache_ttl_seconds") or 86400),
        )
        self.queue = DocumentQueue(
            incoming=self.repo_root
            / paths.get("document_incoming", "automation/documents/incoming"),
            processing=self.repo_root
            / paths.get("document_processing", "automation/documents/processing"),
            processed=self.repo_root
            / paths.get("document_processed", "automation/documents/processed"),
            failed=self.repo_root
            / paths.get("document_failed", "automation/documents/failed"),
        )
        self.health = HealthMonitor(
            self.repo_root / "metadata/connectors/connector_health.csv"
        )
        self.limiter = RateLimiter()
        self.retry = RetryEngine(
            max_retries=int(defaults.get("retries") or 3),
            base_seconds=float(defaults.get("backoff_base_seconds") or 1.0),
            max_seconds=float(defaults.get("backoff_max_seconds") or 60.0),
            breaker_failures=int(defaults.get("circuit_breaker_failures") or 5),
            cooldown_seconds=float(defaults.get("circuit_breaker_cooldown_seconds") or 300),
        )
        self._instances: dict[str, BaseConnector] = {}

    def _build(self, cfg: dict[str, Any]) -> BaseConnector:
        class_key = str(cfg.get("class") or "")
        cls = CONNECTOR_CLASSES.get(class_key)
        if not cls:
            raise KeyError(f"unknown_connector_class:{class_key}")
        return cls(cfg)

    def get_connector(self, connector_id: str) -> BaseConnector:
        if connector_id in self._instances:
            return self._instances[connector_id]
        cfg = self.registry.get(connector_id)
        if not cfg:
            raise KeyError(f"unknown_connector:{connector_id}")
        inst = self._build(cfg)
        self._instances[connector_id] = inst
        return inst

    def list_connectors(self) -> list[dict[str, Any]]:
        out = []
        for cfg in self.registry.list_configs():
            cid = str(cfg["connector_id"])
            report = self.health.get(cid)
            out.append(
                {
                    **cfg,
                    "health": report.to_dict(),
                    "rate_remaining": self.limiter.remaining(
                        cid, int(cfg.get("rate_limit_per_minute") or 30)
                    ),
                }
            )
        return out

    def connect_all(self, *, enabled_only: bool = True) -> list[dict[str, Any]]:
        results = []
        for cfg in self.registry.list_configs(enabled_only=enabled_only):
            cid = str(cfg["connector_id"])
            try:
                conn = self.get_connector(cid)
                res = conn.connect()
                self.events.emit("connector_started", cid, f"{conn.name} started")
                self.health.probe(cid, conn.health)
                results.append({"connector_id": cid, "ok": True, "result": res})
            except Exception as exc:  # noqa: BLE001
                self.events.emit(
                    "failed", cid, str(exc), level="error"
                )
                self.metrics.bump(cid, errors=1)
                results.append({"connector_id": cid, "ok": False, "error": str(exc)})
        return results

    def search(
        self,
        query: SearchQuery,
        *,
        connector_ids: Optional[list[str]] = None,
    ) -> list[SearchResult]:
        if not self.config.get("enabled", True):
            raise RuntimeError("knowledge_network_disabled")

        approved_sources = self.registry.approved_source_ids()
        configs = self.registry.list_configs(enabled_only=True)
        if connector_ids:
            configs = [c for c in configs if c.get("connector_id") in connector_ids]

        cache_key = f"{query.query}|{query.limit}|{','.join(connector_ids or [])}"
        cached = self.cache.get("search", cache_key)
        if cached is not None:
            for cfg in configs[:1]:
                self.metrics.bump(str(cfg["connector_id"]), cached_hits=1)
                self.events.emit(
                    "cached",
                    str(cfg["connector_id"]),
                    f"search cache hit for '{query.query}'",
                )
            return [SearchResult(**row) for row in cached]

        workers = int((self.config.get("workers") or {}).get("max_parallel_connectors") or 8)
        results: list[SearchResult] = []

        def _run(cfg: dict[str, Any]) -> list[SearchResult]:
            cid = str(cfg["connector_id"])
            if not self.retry.is_available(cid):
                self.events.emit("failed", cid, "circuit_open", level="warn")
                return []
            if not self.limiter.allow(cid, int(cfg.get("rate_limit_per_minute") or 30)):
                self.metrics.bump(cid, rate_limited=1)
                self.events.emit("rate_limited", cid, "search throttled", level="warn")
                return []
            # Policy: source must be trusted/allowed when present in registry
            source_id = str(cfg.get("source_id") or "")
            if source_id and approved_sources and source_id not in approved_sources:
                # allow connector-specific source ids declared for phase1 placeholders
                if not str(source_id).startswith("SRC-CONN-") and source_id not in approved_sources:
                    self.events.emit(
                        "failed",
                        cid,
                        f"source_not_approved:{source_id}",
                        level="warn",
                    )
                    return []

            conn = self.get_connector(cid)
            self.events.emit("searching", cid, f"query='{query.query}'")
            q = SearchQuery(
                query=query.query,
                limit=query.limit,
                domains=query.domains,
                mission_id=query.mission_id,
                planner_request_id=query.planner_request_id,
                dry_run=bool(cfg.get("dry_run", True)) or query.dry_run,
                metadata=query.metadata,
            )

            def _search() -> list[SearchResult]:
                if not conn._connected:
                    conn.connect()
                return conn.search(q)

            try:
                found = self.retry.run(cid, _search, dry_run=q.dry_run)
                self.metrics.bump(cid, searches=1)
                self.events.emit(
                    "completed",
                    cid,
                    f"search returned {len(found)} result(s)",
                )
                return found
            except Exception as exc:  # noqa: BLE001
                self.metrics.bump(cid, errors=1)
                self.events.emit("failed", cid, str(exc), level="error")
                return []

        with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
            futures = [pool.submit(_run, cfg) for cfg in configs]
            for fut in as_completed(futures):
                results.extend(fut.result())

        # de-dupe by URL
        seen: set[str] = set()
        unique: list[SearchResult] = []
        for row in results:
            key = row.url.strip().lower()
            if not key or key in seen:
                continue
            seen.add(key)
            unique.append(row)

        unique = unique[: max(query.limit * max(len(configs), 1), query.limit)]
        self.cache.set("search", cache_key, [r.to_dict() for r in unique])
        return unique

    def acquire(
        self,
        result: SearchResult,
        *,
        mission_id: Optional[str] = None,
    ) -> DocumentRef:
        """Fetch/download placeholder metadata and enqueue document."""
        cid = result.connector_id
        conn = self.get_connector(cid)
        self.events.emit("downloading", cid, result.url)

        def _download() -> DocumentRef:
            doc = conn.download(result.url)
            doc.mission_id = mission_id or result.metadata.get("mission_id")
            doc.planner_request_id = result.metadata.get("planner_request_id")
            doc.source_id = result.source_id or conn.source_id
            doc.trust_score = result.trust_score or conn.trust_score()
            doc.title = result.title or doc.title
            doc.original_url = result.url
            meta = conn.extract_metadata(result.to_dict())
            doc.metadata = {**doc.metadata, **meta}
            return doc

        try:
            doc = self.retry.run(cid, _download, dry_run=True)
            path = self.queue.enqueue(doc)
            doc.local_path = str(path)
            self.metrics.bump(cid, downloads=1, documents_retrieved=1, queue_added=1)
            self.events.emit(
                "queue_added",
                cid,
                f"{doc.document_id} queued",
                document_id=doc.document_id,
            )
            self.events.emit("completed", cid, f"acquired {doc.document_id}")
            return doc
        except Exception as exc:  # noqa: BLE001
            self.metrics.bump(cid, errors=1)
            self.events.emit("failed", cid, str(exc), level="error")
            raise

    def health_check_all(self) -> list[dict[str, Any]]:
        reports = []
        for cfg in self.registry.list_configs():
            cid = str(cfg["connector_id"])
            try:
                conn = self.get_connector(cid)
                if cfg.get("enabled"):
                    report = self.health.probe(cid, conn.health)
                else:
                    from .types import HealthReport, ConnectorHealth

                    report = HealthReport(
                        connector_id=cid,
                        health=ConnectorHealth.DISABLED.value,
                        message="disabled by config",
                    )
                    self.health.update(report)
                self.events.emit(
                    "health_changed",
                    cid,
                    f"{report.health}: {report.message}",
                )
                reports.append(report.to_dict())
            except Exception as exc:  # noqa: BLE001
                self.events.emit("failed", cid, str(exc), level="error")
                reports.append(
                    {
                        "connector_id": cid,
                        "health": "error",
                        "message": str(exc),
                        "last_check": utc_now_iso(),
                    }
                )
        return reports

    def shutdown(self) -> None:
        for conn in self._instances.values():
            try:
                conn.shutdown()
            except Exception:  # noqa: BLE001
                pass
        self._instances.clear()

    def dashboard(self) -> dict[str, Any]:
        return {
            "updated_at": utc_now_iso(),
            "enabled": bool(self.config.get("enabled", True)),
            "connectors": self.list_connectors(),
            "queue": self.queue.snapshot(),
            "metrics": self.metrics.load(),
            "events": self.events.recent(50),
            "rules": self.config.get("rules") or {},
            "workers": self.config.get("workers") or {},
            "architecture": {
                "flow": [
                    "Scheduler",
                    "Planner",
                    "Policy",
                    "ConnectorManager",
                    "Connectors",
                    "DocumentQueue",
                    "Pipeline",
                    "Review",
                    "Publisher",
                    "Telemetry",
                ]
            },
        }
