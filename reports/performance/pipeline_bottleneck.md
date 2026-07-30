# Pipeline Bottleneck Analysis

**Generated:** 2026-07-30T18:35:06+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 238 | 1.29 | 70.9 | 306.6 |
| source_discovery | 238 | 3.81 | 186.3 | 907.3 |
| connector | 238 | 87715.68 | 97806.1 | 20876332.4 |
| document_discovery | 238 | 87715.83 | 97806.2 | 20876367.8 |
| document_download | 238 | 244347.56 | 1509355.9 | 58154718.5 |
| extraction | 238 | 92.13 | 274.0 | 21927.9 |
| candidate_validation | 238 | 11.16 | 37.2 | 2655.7 |
| publish_queue | 238 | 11.25 | 37.4 | 2676.6 |
| append_dataset | 238 | 41.84 | 119.7 | 9958.4 |
| export | 238 | 0.35 | 1.9 | 82.5 |
| git_commit | 238 | 0.31 | 2.1 | 74.4 |
| push | 238 | 0.31 | 0.8 | 74.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6939 |
| Documents processed | 17397 |
| Process ratio | 250.7% (target ≥90.0%) |
| Rows published (traces) | 1119 |
| Sessions observed | 266 |
| Avg session duration (s) | 950.846 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.84 |
| Avg connector latency (ms) | 13817.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **250.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
