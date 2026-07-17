# Pipeline Bottleneck Analysis

**Generated:** 2026-07-17T04:26:33+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 84 | 1.03 | 6.5 | 86.6 |
| source_discovery | 84 | 2.75 | 3.3 | 230.7 |
| connector | 84 | 76171.9 | 97806.1 | 6398439.2 |
| document_discovery | 84 | 76172.05 | 97806.2 | 6398451.9 |
| document_download | 84 | 265463.48 | 1509355.9 | 22298932.2 |
| extraction | 84 | 82.76 | 274.0 | 6951.5 |
| candidate_validation | 84 | 7.01 | 18.7 | 589.2 |
| publish_queue | 84 | 7.25 | 34.7 | 608.8 |
| append_dataset | 84 | 49.05 | 119.7 | 4120.3 |
| export | 84 | 0.34 | 0.6 | 28.2 |
| git_commit | 84 | 0.32 | 2.1 | 27.2 |
| push | 84 | 0.32 | 0.8 | 26.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2235 |
| Documents processed | 7929 |
| Process ratio | 354.8% (target ≥90.0%) |
| Rows published (traces) | 352 |
| Sessions observed | 112 |
| Avg session duration (s) | 784.732 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.558 |
| Avg connector latency (ms) | 13808.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **354.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
