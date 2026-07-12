# Pipeline Bottleneck Analysis

**Generated:** 2026-07-12T23:08:43+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 39 | 1.11 | 6.5 | 43.3 |
| source_discovery | 39 | 2.68 | 3.3 | 104.4 |
| connector | 39 | 55604.35 | 97806.1 | 2168569.8 |
| document_discovery | 39 | 55604.5 | 97806.2 | 2168575.5 |
| document_download | 39 | 210660.51 | 1509355.9 | 8215760.0 |
| extraction | 39 | 64.13 | 109.5 | 2501.1 |
| candidate_validation | 39 | 5.29 | 8.7 | 206.4 |
| publish_queue | 39 | 5.36 | 8.8 | 208.9 |
| append_dataset | 39 | 41.45 | 119.7 | 1616.4 |
| export | 39 | 0.33 | 0.6 | 12.9 |
| git_commit | 39 | 0.34 | 2.1 | 13.4 |
| push | 39 | 0.31 | 0.6 | 12.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 870 |
| Documents processed | 3169 |
| Process ratio | 364.3% (target ≥90.0%) |
| Rows published (traces) | 131 |
| Sessions observed | 67 |
| Avg session duration (s) | 531.313 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.062 |
| Avg connector latency (ms) | 14044.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **364.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
