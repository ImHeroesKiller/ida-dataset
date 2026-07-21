# Pipeline Bottleneck Analysis

**Generated:** 2026-07-21T19:43:55+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 142 | 1.0 | 6.5 | 141.8 |
| source_discovery | 142 | 3.15 | 39.8 | 447.4 |
| connector | 142 | 83454.55 | 97806.1 | 11850546.5 |
| document_discovery | 142 | 83454.69 | 97806.2 | 11850566.4 |
| document_download | 142 | 254870.86 | 1509355.9 | 36191661.5 |
| extraction | 142 | 85.22 | 274.0 | 12100.7 |
| candidate_validation | 142 | 8.63 | 30.0 | 1225.3 |
| publish_queue | 142 | 8.79 | 34.7 | 1248.6 |
| append_dataset | 142 | 44.04 | 119.7 | 6253.2 |
| export | 142 | 0.35 | 1.9 | 49.3 |
| git_commit | 142 | 0.32 | 2.1 | 44.8 |
| push | 142 | 0.31 | 0.8 | 44.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3993 |
| Documents processed | 11568 |
| Process ratio | 289.7% (target ≥90.0%) |
| Rows published (traces) | 642 |
| Sessions observed | 170 |
| Avg session duration (s) | 884.006 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.748 |
| Avg connector latency (ms) | 13775.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **289.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
