# Pipeline Bottleneck Analysis

**Generated:** 2026-08-10T05:58:21+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 373 | 1.53 | 70.9 | 572.1 |
| source_discovery | 373 | 4.45 | 186.3 | 1661.0 |
| connector | 373 | 89990.1 | 97806.1 | 33566307.7 |
| document_discovery | 373 | 89990.29 | 97806.2 | 33566378.7 |
| document_download | 373 | 237157.87 | 1509355.9 | 88459884.5 |
| extraction | 373 | 97.67 | 274.0 | 36430.1 |
| candidate_validation | 373 | 14.57 | 136.9 | 5435.2 |
| publish_queue | 373 | 14.64 | 136.9 | 5460.1 |
| append_dataset | 373 | 38.89 | 119.7 | 14506.6 |
| export | 373 | 0.35 | 2.1 | 129.5 |
| git_commit | 373 | 0.35 | 15.1 | 131.2 |
| push | 373 | 0.61 | 81.1 | 227.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11083 |
| Documents processed | 24768 |
| Process ratio | 223.5% (target ≥90.0%) |
| Rows published (traces) | 1794 |
| Sessions observed | 303 |
| Avg session duration (s) | 1059.835 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13769.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **223.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
