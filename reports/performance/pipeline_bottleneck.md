# Pipeline Bottleneck Analysis

**Generated:** 2026-07-11T10:22:55+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 12 | 0.82 | 1.1 | 9.8 |
| source_discovery | 12 | 2.27 | 2.8 | 27.2 |
| connector | 12 | 5518.68 | 7301.3 | 66224.1 |
| document_discovery | 12 | 5518.87 | 7301.7 | 66226.4 |
| document_download | 12 | 29757.15 | 49397.5 | 357085.8 |
| extraction | 12 | 19.98 | 31.4 | 239.8 |
| candidate_validation | 12 | 4.08 | 6.7 | 49.0 |
| publish_queue | 12 | 4.09 | 6.7 | 49.1 |
| append_dataset | 12 | 4.61 | 7.7 | 55.3 |
| export | 12 | 0.3 | 0.4 | 3.6 |
| git_commit | 12 | 0.29 | 0.4 | 3.5 |
| push | 12 | 0.28 | 0.3 | 3.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 106 |
| Documents processed | 68 |
| Process ratio | 64.2% (target ≥90.0%) |
| Rows published (traces) | 31 |
| Sessions observed | 38 |
| Avg session duration (s) | 144.421 |
| Max session duration (s) | 604.0 |
| Rows / session (productive) | 3.0 |
| Avg connector latency (ms) | 13804.1 |
| Worker utilization (est) | 0.054 |
| Idle fraction (est) | 0.946 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **64.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
