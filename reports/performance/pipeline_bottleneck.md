# Pipeline Bottleneck Analysis

**Generated:** 2026-07-11T17:09:33+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 18 | 0.89 | 1.3 | 16.0 |
| source_discovery | 18 | 2.45 | 2.9 | 44.1 |
| connector | 18 | 20384.52 | 94176.1 | 366921.3 |
| document_discovery | 18 | 20384.69 | 94176.2 | 366924.4 |
| document_download | 18 | 106835.2 | 1263152.2 | 1923033.6 |
| extraction | 18 | 30.19 | 67.7 | 543.4 |
| candidate_validation | 18 | 4.01 | 6.9 | 72.2 |
| publish_queue | 18 | 4.02 | 6.9 | 72.3 |
| append_dataset | 18 | 17.62 | 119.7 | 317.1 |
| export | 18 | 0.33 | 0.6 | 5.9 |
| git_commit | 18 | 0.3 | 0.4 | 5.4 |
| push | 18 | 0.29 | 0.3 | 5.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 262 |
| Documents processed | 626 |
| Process ratio | 238.9% (target ≥90.0%) |
| Rows published (traces) | 43 |
| Sessions observed | 46 |
| Avg session duration (s) | 260.283 |
| Max session duration (s) | 2163.0 |
| Rows / session (productive) | 3.231 |
| Avg connector latency (ms) | 14258.0 |
| Worker utilization (est) | 0.266 |
| Idle fraction (est) | 0.734 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **238.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
