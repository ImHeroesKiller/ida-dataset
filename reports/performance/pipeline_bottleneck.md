# Pipeline Bottleneck Analysis

**Generated:** 2026-07-18T02:54:23+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 96 | 1.02 | 6.5 | 98.1 |
| source_discovery | 96 | 2.76 | 3.5 | 265.1 |
| connector | 96 | 78409.12 | 97806.1 | 7527275.1 |
| document_discovery | 96 | 78409.26 | 97806.2 | 7527289.0 |
| document_download | 96 | 269526.13 | 1509355.9 | 25874508.4 |
| extraction | 96 | 83.28 | 274.0 | 7994.5 |
| candidate_validation | 96 | 7.32 | 18.7 | 702.5 |
| publish_queue | 96 | 7.54 | 34.7 | 723.9 |
| append_dataset | 96 | 47.39 | 119.7 | 4549.6 |
| export | 96 | 0.34 | 0.6 | 32.4 |
| git_commit | 96 | 0.32 | 2.1 | 30.6 |
| push | 96 | 0.31 | 0.8 | 30.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2597 |
| Documents processed | 8667 |
| Process ratio | 333.7% (target ≥90.0%) |
| Rows published (traces) | 412 |
| Sessions observed | 124 |
| Avg session duration (s) | 818.444 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.618 |
| Avg connector latency (ms) | 13683.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **333.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
