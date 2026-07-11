# Performance Projection

**Generated:** 2026-07-11  
**Sprint:** IDA Dataset Factory Simplification v2.0

## API cost

| Vector | Expected change |
|--------|-----------------|
| Paid search calls / session | Cap ≤ 10 Tavily (+ cache hits free) |
| Multi-provider fan-out | Eliminated by default |
| Secondary API spend | ~0 unless fallback enabled |
| Session length window | Hourly deeper runs vs 15-min thrash |
| GHA runs / day | ~96 → ~24 continuous ticks (plus daily deep at 06:00 UTC, still hourly-aligned) |

## Throughput

| Vector | Expected change |
|--------|-----------------|
| Knowledge rows / session | ↑ (deeper processing, less setup tax) |
| Rows / wall-clock day | Stable to ↑ if sessions complete fully |
| Duplicate discovery | ↓ (one primary engine + cache) |
| Startup / HTTP overhead | ↓ fewer provider probes |
| Content quality per URL | ↑ (`include_raw_content`) |

## Knowledge production

**Not reduced by design.** Policy shifts spend from repeated multi-API search into richer single-engine discovery + deeper extract/route within the hour.

## Runtime risk mitigated

Previous 15-min cadence stacked behind hung long sessions. Hourly + concurrency group reduces queue pressure while preserving continuous manufacturing.
