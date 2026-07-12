# Pipeline Bottleneck Analysis

**Generated:** 2026-07-12T21:10:46+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 37 | 1.11 | 6.5 | 41.0 |
| source_discovery | 37 | 2.66 | 3.3 | 98.4 |
| connector | 37 | 53531.92 | 97806.1 | 1980680.9 |
| document_discovery | 37 | 53532.06 | 97806.2 | 1980686.3 |
| document_download | 37 | 210695.39 | 1509355.9 | 7795729.4 |
| extraction | 37 | 62.44 | 109.5 | 2310.2 |
| candidate_validation | 37 | 5.14 | 8.7 | 190.0 |
| publish_queue | 37 | 5.2 | 8.8 | 192.4 |
| append_dataset | 37 | 39.76 | 119.7 | 1471.2 |
| export | 37 | 0.33 | 0.6 | 12.1 |
| git_commit | 37 | 0.35 | 2.1 | 12.8 |
| push | 37 | 0.31 | 0.6 | 11.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 818 |
| Documents processed | 2905 |
| Process ratio | 355.1% (target ≥90.0%) |
| Rows published (traces) | 121 |
| Sessions observed | 65 |
| Avg session duration (s) | 514.415 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.0 |
| Avg connector latency (ms) | 14099.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **355.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
