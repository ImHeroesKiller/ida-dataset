# Pipeline Bottleneck Analysis

**Generated:** 2026-07-12T11:30:03+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 31 | 1.15 | 6.5 | 35.6 |
| source_discovery | 31 | 2.65 | 3.3 | 82.3 |
| connector | 31 | 45707.78 | 97806.1 | 1416941.3 |
| document_discovery | 31 | 45707.93 | 97806.2 | 1416945.8 |
| document_download | 31 | 203612.58 | 1509355.9 | 6311989.9 |
| extraction | 31 | 56.82 | 109.5 | 1761.4 |
| candidate_validation | 31 | 4.84 | 7.8 | 150.0 |
| publish_queue | 31 | 4.91 | 8.8 | 152.3 |
| append_dataset | 31 | 35.86 | 119.7 | 1111.8 |
| export | 31 | 0.32 | 0.6 | 10.0 |
| git_commit | 31 | 0.3 | 0.4 | 9.2 |
| push | 31 | 0.31 | 0.5 | 9.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 632 |
| Documents processed | 2171 |
| Process ratio | 343.5% (target ≥90.0%) |
| Rows published (traces) | 95 |
| Sessions observed | 59 |
| Avg session duration (s) | 454.288 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 3.917 |
| Avg connector latency (ms) | 13719.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **343.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
