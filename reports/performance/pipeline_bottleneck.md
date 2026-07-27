# Pipeline Bottleneck Analysis

**Generated:** 2026-07-27T12:42:45+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 204 | 0.99 | 6.5 | 202.3 |
| source_discovery | 204 | 3.07 | 39.8 | 625.9 |
| connector | 204 | 86663.95 | 97806.1 | 17679445.8 |
| document_discovery | 204 | 86664.1 | 97806.2 | 17679475.5 |
| document_download | 204 | 254362.23 | 1509355.9 | 51889894.9 |
| extraction | 204 | 89.61 | 274.0 | 18280.1 |
| candidate_validation | 204 | 10.3 | 37.2 | 2100.3 |
| publish_queue | 204 | 10.42 | 37.4 | 2125.0 |
| append_dataset | 204 | 42.57 | 119.7 | 8683.6 |
| export | 204 | 0.35 | 1.9 | 71.0 |
| git_commit | 204 | 0.31 | 2.1 | 63.7 |
| push | 204 | 0.32 | 0.8 | 64.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5895 |
| Documents processed | 15455 |
| Process ratio | 262.2% (target ≥90.0%) |
| Rows published (traces) | 952 |
| Sessions observed | 232 |
| Avg session duration (s) | 939.78 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.827 |
| Avg connector latency (ms) | 14155.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **262.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
