# Pipeline Bottleneck Analysis

**Generated:** 2026-07-20T03:20:23+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 123 | 1.0 | 6.5 | 123.4 |
| source_discovery | 123 | 3.07 | 39.8 | 378.0 |
| connector | 123 | 81829.71 | 97806.1 | 10065054.4 |
| document_discovery | 123 | 81829.85 | 97806.2 | 10065071.3 |
| document_download | 123 | 265352.85 | 1509355.9 | 32638400.0 |
| extraction | 123 | 82.56 | 274.0 | 10155.1 |
| candidate_validation | 123 | 8.1 | 30.0 | 995.9 |
| publish_queue | 123 | 8.28 | 34.7 | 1017.9 |
| append_dataset | 123 | 45.01 | 119.7 | 5536.7 |
| export | 123 | 0.34 | 0.7 | 41.7 |
| git_commit | 123 | 0.32 | 2.1 | 38.8 |
| push | 123 | 0.31 | 0.8 | 38.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3414 |
| Documents processed | 10379 |
| Process ratio | 304.0% (target ≥90.0%) |
| Rows published (traces) | 547 |
| Sessions observed | 151 |
| Avg session duration (s) | 866.152 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.707 |
| Avg connector latency (ms) | 13779.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **304.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
