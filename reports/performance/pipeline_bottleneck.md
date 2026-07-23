# Pipeline Bottleneck Analysis

**Generated:** 2026-07-23T08:56:06+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 158 | 0.99 | 6.5 | 156.4 |
| source_discovery | 158 | 3.12 | 39.8 | 493.2 |
| connector | 158 | 84529.17 | 97806.1 | 13355608.9 |
| document_discovery | 158 | 84529.32 | 97806.2 | 13355633.0 |
| document_download | 158 | 251894.81 | 1509355.9 | 39799379.2 |
| extraction | 158 | 86.39 | 274.0 | 13649.8 |
| candidate_validation | 158 | 9.04 | 30.0 | 1427.8 |
| publish_queue | 158 | 9.19 | 34.7 | 1451.6 |
| append_dataset | 158 | 43.81 | 119.7 | 6921.8 |
| export | 158 | 0.35 | 1.9 | 55.6 |
| git_commit | 158 | 0.31 | 2.1 | 49.7 |
| push | 158 | 0.31 | 0.8 | 49.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4479 |
| Documents processed | 12696 |
| Process ratio | 283.5% (target ≥90.0%) |
| Rows published (traces) | 722 |
| Sessions observed | 186 |
| Avg session duration (s) | 899.548 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.775 |
| Avg connector latency (ms) | 14086.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **283.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
