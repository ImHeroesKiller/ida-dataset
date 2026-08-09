# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T13:11:42+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 359 | 1.56 | 70.9 | 559.8 |
| source_discovery | 359 | 4.52 | 186.3 | 1623.7 |
| connector | 359 | 89836.71 | 97806.1 | 32251377.3 |
| document_discovery | 359 | 89836.9 | 97806.2 | 32251446.2 |
| document_download | 359 | 231379.07 | 1509355.9 | 83065087.6 |
| extraction | 359 | 97.38 | 274.0 | 34960.6 |
| candidate_validation | 359 | 14.35 | 136.9 | 5150.4 |
| publish_queue | 359 | 14.41 | 136.9 | 5174.7 |
| append_dataset | 359 | 39.08 | 119.7 | 14028.6 |
| export | 359 | 0.35 | 2.1 | 124.5 |
| git_commit | 359 | 0.35 | 15.1 | 126.6 |
| push | 359 | 0.62 | 81.1 | 223.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10649 |
| Documents processed | 23944 |
| Process ratio | 224.8% (target ≥90.0%) |
| Rows published (traces) | 1724 |
| Sessions observed | 310 |
| Avg session duration (s) | 1065.416 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13678.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **224.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
