# Pipeline Bottleneck Analysis

**Generated:** 2026-07-15T15:14:10+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 66 | 1.05 | 6.5 | 69.1 |
| source_discovery | 66 | 2.73 | 3.3 | 180.0 |
| connector | 66 | 71309.81 | 97806.1 | 4706447.5 |
| document_discovery | 66 | 71309.95 | 97806.2 | 4706456.7 |
| document_download | 66 | 264756.26 | 1509355.9 | 17473913.1 |
| extraction | 66 | 80.55 | 274.0 | 5316.6 |
| candidate_validation | 66 | 6.34 | 9.5 | 418.2 |
| publish_queue | 66 | 6.38 | 9.5 | 421.2 |
| append_dataset | 66 | 49.73 | 119.7 | 3282.4 |
| export | 66 | 0.34 | 0.6 | 22.2 |
| git_commit | 66 | 0.33 | 2.1 | 21.6 |
| push | 66 | 0.32 | 0.8 | 21.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1677 |
| Documents processed | 6446 |
| Process ratio | 384.4% (target ≥90.0%) |
| Rows published (traces) | 262 |
| Sessions observed | 94 |
| Avg session duration (s) | 723.074 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.424 |
| Avg connector latency (ms) | 13651.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **384.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
