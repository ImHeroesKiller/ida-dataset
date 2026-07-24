# Pipeline Bottleneck Analysis

**Generated:** 2026-07-24T22:22:31+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 175 | 0.99 | 6.5 | 173.0 |
| source_discovery | 175 | 3.1 | 39.8 | 541.9 |
| connector | 175 | 85448.27 | 97806.1 | 14953446.8 |
| document_discovery | 175 | 85448.42 | 97806.2 | 14953473.0 |
| document_download | 175 | 253651.13 | 1509355.9 | 44388947.1 |
| extraction | 175 | 87.33 | 274.0 | 15282.3 |
| candidate_validation | 175 | 9.45 | 30.0 | 1653.2 |
| publish_queue | 175 | 9.58 | 34.7 | 1677.1 |
| append_dataset | 175 | 43.29 | 119.7 | 7575.2 |
| export | 175 | 0.35 | 1.9 | 61.6 |
| git_commit | 175 | 0.31 | 2.1 | 54.7 |
| push | 175 | 0.31 | 0.8 | 55.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5006 |
| Documents processed | 13744 |
| Process ratio | 274.6% (target ≥90.0%) |
| Rows published (traces) | 807 |
| Sessions observed | 203 |
| Avg session duration (s) | 917.192 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.798 |
| Avg connector latency (ms) | 13720.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **274.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
