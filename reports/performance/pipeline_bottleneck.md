# Pipeline Bottleneck Analysis

**Generated:** 2026-08-12T08:03:45+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 406 | 1.49 | 70.9 | 605.1 |
| source_discovery | 406 | 4.32 | 186.3 | 1755.9 |
| connector | 406 | 90317.64 | 97806.1 | 36668960.7 |
| document_discovery | 406 | 90317.82 | 97806.2 | 36669036.0 |
| document_download | 406 | 236338.8 | 1509355.9 | 95953553.9 |
| extraction | 406 | 99.24 | 274.0 | 40292.8 |
| candidate_validation | 406 | 15.6 | 149.0 | 6334.9 |
| publish_queue | 406 | 15.67 | 149.1 | 6361.2 |
| append_dataset | 406 | 38.7 | 119.7 | 15711.6 |
| export | 406 | 0.35 | 2.7 | 142.3 |
| git_commit | 406 | 0.35 | 15.1 | 142.0 |
| push | 406 | 0.59 | 81.1 | 237.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 12086 |
| Documents processed | 26680 |
| Process ratio | 220.8% (target ≥90.0%) |
| Rows published (traces) | 1959 |
| Sessions observed | 311 |
| Avg session duration (s) | 1058.772 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 14370.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **220.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
