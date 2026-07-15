# Pipeline Bottleneck Analysis

**Generated:** 2026-07-15T03:00:46+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 61 | 1.06 | 6.5 | 64.7 |
| source_discovery | 61 | 2.73 | 3.3 | 166.6 |
| connector | 61 | 69450.82 | 97806.1 | 4236499.8 |
| document_discovery | 61 | 69450.96 | 97806.2 | 4236508.5 |
| document_download | 61 | 247504.49 | 1509355.9 | 15097774.0 |
| extraction | 61 | 79.38 | 274.0 | 4842.4 |
| candidate_validation | 61 | 6.2 | 9.5 | 378.2 |
| publish_queue | 61 | 6.25 | 9.5 | 381.0 |
| append_dataset | 61 | 48.81 | 119.7 | 2977.7 |
| export | 61 | 0.34 | 0.6 | 20.7 |
| git_commit | 61 | 0.33 | 2.1 | 20.0 |
| push | 61 | 0.32 | 0.8 | 19.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1522 |
| Documents processed | 5820 |
| Process ratio | 382.4% (target ≥90.0%) |
| Rows published (traces) | 237 |
| Sessions observed | 89 |
| Avg session duration (s) | 688.371 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.37 |
| Avg connector latency (ms) | 13826.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **382.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
