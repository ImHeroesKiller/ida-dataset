# Pipeline Bottleneck Analysis

**Generated:** 2026-07-21T17:40:41+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 141 | 1.0 | 6.5 | 140.9 |
| source_discovery | 141 | 3.15 | 39.8 | 444.5 |
| connector | 141 | 83381.59 | 97806.1 | 11756803.5 |
| document_discovery | 141 | 83381.72 | 97806.2 | 11756823.2 |
| document_download | 141 | 254973.38 | 1509355.9 | 35951246.5 |
| extraction | 141 | 85.15 | 274.0 | 12006.0 |
| candidate_validation | 141 | 8.6 | 30.0 | 1212.7 |
| publish_queue | 141 | 8.77 | 34.7 | 1236.0 |
| append_dataset | 141 | 44.11 | 119.7 | 6219.4 |
| export | 141 | 0.35 | 1.9 | 49.0 |
| git_commit | 141 | 0.32 | 2.1 | 44.5 |
| push | 141 | 0.31 | 0.8 | 44.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3962 |
| Documents processed | 11517 |
| Process ratio | 290.7% (target ≥90.0%) |
| Rows published (traces) | 637 |
| Sessions observed | 169 |
| Avg session duration (s) | 882.852 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.746 |
| Avg connector latency (ms) | 13726.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **290.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
