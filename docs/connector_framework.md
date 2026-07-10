# Connector Framework

## Purpose

Plugin architecture for unlimited future connectors.

## Status: Active (Sprint 5)

## Modules

| Module | Role |
| --- | --- |
| `base_connector.py` | Mandatory interface |
| `manager.py` | Only execution entry |
| `registry.py` | Config + CSV registry |
| `throttle.py` | Rate limits |
| `retry.py` | Backoff + circuit breaker |
| `cache.py` | JSON file cache |
| `health.py` | Health monitor |
| `document_queue.py` | Incoming→failed queues |
| `scheduler_bridge.py` | Planner-safe bridge |
| `builtin/` | Phase 1 placeholders |

## Interface

Every connector implements: connect, health, search, fetch, download, extract_metadata, supported_formats, rate_limit, cache_policy, trust_score, shutdown.

## Phase 1 connectors

World Bank, BPS, OECD, SEC, Company AR, GitHub, RSS, Generic Search, Generic Website, Local Files, PDF Repository, Internal Dataset — all dry-run placeholders.
