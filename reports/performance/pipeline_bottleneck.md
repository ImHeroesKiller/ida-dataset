# Pipeline Bottleneck Analysis

**Generated:** 2026-07-22T12:43:41+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 150 | 0.99 | 6.5 | 148.9 |
| source_discovery | 150 | 3.13 | 39.8 | 470.2 |
| connector | 150 | 84019.58 | 97806.1 | 12602936.8 |
| document_discovery | 150 | 84019.73 | 97806.2 | 12602959.8 |
| document_download | 150 | 252769.14 | 1509355.9 | 37915370.9 |
| extraction | 150 | 85.84 | 274.0 | 12876.3 |
| candidate_validation | 150 | 8.82 | 30.0 | 1323.7 |
| publish_queue | 150 | 8.98 | 34.7 | 1347.2 |
| append_dataset | 150 | 43.94 | 119.7 | 6591.1 |
| export | 150 | 0.35 | 1.9 | 52.0 |
| git_commit | 150 | 0.31 | 2.1 | 47.2 |
| push | 150 | 0.31 | 0.8 | 47.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4241 |
| Documents processed | 12160 |
| Process ratio | 286.7% (target ≥90.0%) |
| Rows published (traces) | 682 |
| Sessions observed | 178 |
| Avg session duration (s) | 891.77 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.762 |
| Avg connector latency (ms) | 13776.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **286.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
