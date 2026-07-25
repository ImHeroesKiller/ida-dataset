# Pipeline Bottleneck Analysis

**Generated:** 2026-07-25T04:29:29+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 177 | 0.99 | 6.5 | 174.9 |
| source_discovery | 177 | 3.09 | 39.8 | 547.6 |
| connector | 177 | 85544.92 | 97806.1 | 15141450.4 |
| document_discovery | 177 | 85545.07 | 97806.2 | 15141476.9 |
| document_download | 177 | 253955.14 | 1509355.9 | 44950059.8 |
| extraction | 177 | 87.43 | 274.0 | 15474.5 |
| candidate_validation | 177 | 9.5 | 30.0 | 1681.0 |
| publish_queue | 177 | 9.63 | 34.7 | 1705.0 |
| append_dataset | 177 | 43.22 | 119.7 | 7650.3 |
| export | 177 | 0.35 | 1.9 | 62.2 |
| git_commit | 177 | 0.31 | 2.1 | 55.3 |
| push | 177 | 0.31 | 0.8 | 55.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5068 |
| Documents processed | 13857 |
| Process ratio | 273.4% (target ≥90.0%) |
| Rows published (traces) | 817 |
| Sessions observed | 205 |
| Avg session duration (s) | 919.117 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.8 |
| Avg connector latency (ms) | 13836.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **273.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
