# Pipeline Bottleneck Analysis

**Generated:** 2026-08-07T12:03:34+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 316 | 1.64 | 70.9 | 517.7 |
| source_discovery | 316 | 4.75 | 186.3 | 1501.7 |
| connector | 316 | 89269.32 | 97806.1 | 28209106.1 |
| document_discovery | 316 | 89269.52 | 97806.2 | 28209169.1 |
| document_download | 316 | 232446.58 | 1509355.9 | 73453120.3 |
| extraction | 316 | 95.69 | 274.0 | 30239.2 |
| candidate_validation | 316 | 13.53 | 136.9 | 4274.4 |
| publish_queue | 316 | 13.6 | 136.9 | 4297.3 |
| append_dataset | 316 | 39.83 | 119.7 | 12585.9 |
| export | 316 | 0.35 | 2.1 | 109.2 |
| git_commit | 316 | 0.36 | 15.1 | 112.8 |
| push | 316 | 0.67 | 81.1 | 211.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9336 |
| Documents processed | 21581 |
| Process ratio | 231.2% (target ≥90.0%) |
| Rows published (traces) | 1509 |
| Sessions observed | 312 |
| Avg session duration (s) | 1056.577 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.931 |
| Avg connector latency (ms) | 13708.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **231.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
