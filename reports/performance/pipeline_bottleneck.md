# Pipeline Bottleneck Analysis

**Generated:** 2026-07-14T05:53:23+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 51 | 1.08 | 6.5 | 55.3 |
| source_discovery | 51 | 2.73 | 3.3 | 139.0 |
| connector | 51 | 64639.5 | 97806.1 | 3296614.6 |
| document_discovery | 51 | 64639.64 | 97806.2 | 3296621.8 |
| document_download | 51 | 224683.58 | 1509355.9 | 11458862.8 |
| extraction | 51 | 72.27 | 109.5 | 3685.8 |
| candidate_validation | 51 | 5.83 | 8.7 | 297.1 |
| publish_queue | 51 | 5.88 | 8.8 | 299.9 |
| append_dataset | 51 | 47.25 | 119.7 | 2409.7 |
| export | 51 | 0.35 | 0.6 | 17.6 |
| git_commit | 51 | 0.33 | 2.1 | 17.0 |
| push | 51 | 0.33 | 0.8 | 16.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1232 |
| Documents processed | 4642 |
| Process ratio | 376.8% (target ≥90.0%) |
| Rows published (traces) | 187 |
| Sessions observed | 79 |
| Avg session duration (s) | 622.481 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.227 |
| Avg connector latency (ms) | 13779.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **376.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
