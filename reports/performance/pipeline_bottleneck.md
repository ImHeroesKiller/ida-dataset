# Pipeline Bottleneck Analysis

**Generated:** 2026-08-02T21:14:11+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 272 | 1.39 | 70.9 | 379.2 |
| source_discovery | 272 | 4.19 | 186.3 | 1139.1 |
| connector | 272 | 88501.47 | 97806.1 | 24072401.1 |
| document_discovery | 272 | 88501.69 | 97806.2 | 24072458.7 |
| document_download | 272 | 238971.24 | 1509355.9 | 65000178.0 |
| extraction | 272 | 93.19 | 274.0 | 25346.8 |
| candidate_validation | 272 | 12.27 | 102.5 | 3337.0 |
| publish_queue | 272 | 12.35 | 102.7 | 3359.2 |
| append_dataset | 272 | 40.87 | 119.7 | 11117.5 |
| export | 272 | 0.35 | 2.1 | 95.2 |
| git_commit | 272 | 0.37 | 15.1 | 99.5 |
| push | 272 | 0.61 | 81.1 | 166.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7982 |
| Documents processed | 19290 |
| Process ratio | 241.7% (target ≥90.0%) |
| Rows published (traces) | 1289 |
| Sessions observed | 300 |
| Avg session duration (s) | 958.98 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.86 |
| Avg connector latency (ms) | 13807.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **241.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
