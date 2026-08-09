# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T08:14:45+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 354 | 1.57 | 70.9 | 554.8 |
| source_discovery | 354 | 4.55 | 186.3 | 1609.0 |
| connector | 354 | 89777.5 | 97806.1 | 31781236.4 |
| document_discovery | 354 | 89777.7 | 97806.2 | 31781304.7 |
| document_download | 354 | 231630.62 | 1509355.9 | 81997240.6 |
| extraction | 354 | 97.13 | 274.0 | 34382.7 |
| candidate_validation | 354 | 14.23 | 136.9 | 5038.1 |
| publish_queue | 354 | 14.3 | 136.9 | 5062.3 |
| append_dataset | 354 | 39.11 | 119.7 | 13844.2 |
| export | 354 | 0.35 | 2.1 | 123.0 |
| git_commit | 354 | 0.35 | 15.1 | 125.1 |
| push | 354 | 0.63 | 81.1 | 222.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10494 |
| Documents processed | 23656 |
| Process ratio | 225.4% (target ≥90.0%) |
| Rows published (traces) | 1699 |
| Sessions observed | 305 |
| Avg session duration (s) | 1065.682 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13709.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **225.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
