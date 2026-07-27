# Pipeline Bottleneck Analysis

**Generated:** 2026-07-27T08:48:26+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 202 | 0.99 | 6.5 | 200.0 |
| source_discovery | 202 | 3.07 | 39.8 | 620.1 |
| connector | 202 | 86589.47 | 97806.1 | 17491073.8 |
| document_discovery | 202 | 86589.62 | 97806.2 | 17491103.3 |
| document_download | 202 | 255527.69 | 1509355.9 | 51616592.5 |
| extraction | 202 | 89.45 | 274.0 | 18069.5 |
| candidate_validation | 202 | 10.25 | 37.2 | 2069.9 |
| publish_queue | 202 | 10.37 | 37.4 | 2094.6 |
| append_dataset | 202 | 42.59 | 119.7 | 8603.7 |
| export | 202 | 0.35 | 1.9 | 70.4 |
| git_commit | 202 | 0.31 | 2.1 | 63.1 |
| push | 202 | 0.32 | 0.8 | 63.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5833 |
| Documents processed | 15331 |
| Process ratio | 262.8% (target ≥90.0%) |
| Rows published (traces) | 942 |
| Sessions observed | 230 |
| Avg session duration (s) | 939.526 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.826 |
| Avg connector latency (ms) | 13803.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **262.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
