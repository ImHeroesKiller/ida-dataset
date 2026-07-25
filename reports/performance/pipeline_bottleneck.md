# Pipeline Bottleneck Analysis

**Generated:** 2026-07-25T13:54:12+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 182 | 0.99 | 6.5 | 180.0 |
| source_discovery | 182 | 3.09 | 39.8 | 561.8 |
| connector | 182 | 85777.48 | 97806.1 | 15611501.5 |
| document_discovery | 182 | 85777.63 | 97806.2 | 15611528.6 |
| document_download | 182 | 254426.26 | 1509355.9 | 46305578.5 |
| extraction | 182 | 87.84 | 274.0 | 15986.4 |
| candidate_validation | 182 | 9.62 | 30.0 | 1751.0 |
| publish_queue | 182 | 9.75 | 34.7 | 1775.2 |
| append_dataset | 182 | 43.1 | 119.7 | 7845.1 |
| export | 182 | 0.35 | 1.9 | 64.0 |
| git_commit | 182 | 0.31 | 2.1 | 56.8 |
| push | 182 | 0.32 | 0.8 | 57.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5223 |
| Documents processed | 14156 |
| Process ratio | 271.0% (target ≥90.0%) |
| Rows published (traces) | 842 |
| Sessions observed | 210 |
| Avg session duration (s) | 923.738 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.806 |
| Avg connector latency (ms) | 13855.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **271.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
