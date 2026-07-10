# Connector Lifecycle

## Purpose

Describe runtime lifecycle for a connector instance.

## Status: Active (Sprint 5)

```text
register → enable (config) → connect → health
→ search/fetch/download (throttled, cached, retried)
→ document queue → shutdown
```

## States

unknown · idle · healthy · degraded · rate_limited · error · disabled

## Circuit breaker

After N consecutive failures, connector opens for cooldown, then half-open probe.
