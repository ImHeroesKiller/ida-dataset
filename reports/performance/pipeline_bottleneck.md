# Pipeline Bottleneck Analysis

**Generated:** 2026-07-11T12:21:16+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 14 | 0.84 | 1.1 | 11.8 |
| source_discovery | 14 | 2.34 | 2.8 | 32.7 |
| connector | 14 | 18155.76 | 93987.7 | 254180.7 |
| document_discovery | 14 | 18155.94 | 93987.8 | 254183.2 |
| document_download | 14 | 28528.18 | 49397.5 | 399394.5 |
| extraction | 14 | 22.58 | 38.2 | 316.1 |
| candidate_validation | 14 | 4.48 | 6.9 | 62.7 |
| publish_queue | 14 | 4.49 | 6.9 | 62.8 |
| append_dataset | 14 | 6.02 | 14.9 | 84.3 |
| export | 14 | 0.32 | 0.6 | 4.5 |
| git_commit | 14 | 0.29 | 0.4 | 4.1 |
| push | 14 | 0.29 | 0.3 | 4.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 168 |
| Documents processed | 120 |
| Process ratio | 71.4% (target ≥90.0%) |
| Rows published (traces) | 41 |
| Sessions observed | 40 |
| Avg session duration (s) | 200.25 |
| Max session duration (s) | 1262.0 |
| Rows / session (productive) | 3.333 |
| Avg connector latency (ms) | 2413.9 |
| Worker utilization (est) | 0.107 |
| Idle fraction (est) | 0.893 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **71.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
