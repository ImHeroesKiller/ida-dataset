# Pipeline Bottleneck Analysis

**Generated:** 2026-08-04T16:30:56+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 290 | 1.37 | 70.9 | 397.2 |
| source_discovery | 290 | 4.37 | 186.3 | 1266.1 |
| connector | 290 | 88845.09 | 97806.1 | 25765077.5 |
| document_discovery | 290 | 88845.3 | 97806.2 | 25765137.5 |
| document_download | 290 | 235048.78 | 1509355.9 | 68164146.9 |
| extraction | 290 | 94.03 | 274.0 | 27267.3 |
| candidate_validation | 290 | 12.63 | 102.5 | 3662.8 |
| publish_queue | 290 | 12.71 | 102.7 | 3685.1 |
| append_dataset | 290 | 40.38 | 119.7 | 11709.3 |
| export | 290 | 0.35 | 2.1 | 101.1 |
| git_commit | 290 | 0.36 | 15.1 | 105.1 |
| push | 290 | 0.7 | 81.1 | 203.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8540 |
| Documents processed | 20191 |
| Process ratio | 236.4% (target ≥90.0%) |
| Rows published (traces) | 1379 |
| Sessions observed | 318 |
| Avg session duration (s) | 960.151 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.869 |
| Avg connector latency (ms) | 13718.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **236.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
