# Pipeline Bottleneck Analysis

**Generated:** 2026-07-11T08:14:59+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 10 | 0.79 | 1.1 | 7.9 |
| source_discovery | 10 | 2.17 | 2.8 | 21.7 |
| connector | 10 | 5379.23 | 7301.3 | 53792.3 |
| document_discovery | 10 | 5379.44 | 7301.7 | 53794.4 |
| document_download | 10 | 28831.35 | 49397.5 | 288313.5 |
| extraction | 10 | 17.77 | 20.6 | 177.7 |
| candidate_validation | 10 | 3.62 | 6.6 | 36.2 |
| publish_queue | 10 | 3.63 | 6.5 | 36.3 |
| append_dataset | 10 | 4.02 | 6.3 | 40.2 |
| export | 10 | 0.3 | 0.4 | 3.0 |
| git_commit | 10 | 0.28 | 0.3 | 2.8 |
| push | 10 | 0.28 | 0.3 | 2.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 84 |
| Documents processed | 46 |
| Process ratio | 54.8% (target ≥90.0%) |
| Rows published (traces) | 21 |
| Sessions observed | 36 |
| Avg session duration (s) | 119.806 |
| Max session duration (s) | 604.0 |
| Rows / session (productive) | 2.5 |
| Avg connector latency (ms) | 2670.4 |
| Worker utilization (est) | 0.039 |
| Idle fraction (est) | 0.961 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **54.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
