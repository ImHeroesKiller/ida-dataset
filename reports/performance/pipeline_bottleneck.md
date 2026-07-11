# Pipeline Bottleneck Analysis

**Generated:** 2026-07-11T13:09:24+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 15 | 0.85 | 1.1 | 12.7 |
| source_discovery | 15 | 2.37 | 2.8 | 35.5 |
| connector | 15 | 17359.15 | 93987.7 | 260387.3 |
| document_discovery | 15 | 17359.33 | 93987.8 | 260390.0 |
| document_download | 15 | 29250.69 | 49397.5 | 438760.3 |
| extraction | 15 | 23.41 | 38.2 | 351.1 |
| candidate_validation | 15 | 4.27 | 6.9 | 64.1 |
| publish_queue | 15 | 4.28 | 6.9 | 64.2 |
| append_dataset | 15 | 7.33 | 25.6 | 109.9 |
| export | 15 | 0.32 | 0.6 | 4.8 |
| git_commit | 15 | 0.29 | 0.4 | 4.4 |
| push | 15 | 0.29 | 0.3 | 4.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 189 |
| Documents processed | 181 |
| Process ratio | 95.8% (target ≥90.0%) |
| Rows published (traces) | 41 |
| Sessions observed | 41 |
| Avg session duration (s) | 209.049 |
| Max session duration (s) | 1262.0 |
| Rows / session (productive) | 3.333 |
| Avg connector latency (ms) | 14367.5 |
| Worker utilization (est) | 0.084 |
| Idle fraction (est) | 0.916 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **95.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
