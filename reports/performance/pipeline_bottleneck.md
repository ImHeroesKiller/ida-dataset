# Pipeline Bottleneck Analysis

**Generated:** 2026-07-15T05:55:01+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 62 | 1.05 | 6.5 | 65.2 |
| source_discovery | 62 | 2.72 | 3.3 | 168.6 |
| connector | 62 | 69843.06 | 97806.1 | 4330269.6 |
| document_discovery | 62 | 69843.2 | 97806.2 | 4330278.4 |
| document_download | 62 | 253233.84 | 1509355.9 | 15700498.2 |
| extraction | 62 | 79.45 | 274.0 | 4925.8 |
| candidate_validation | 62 | 6.18 | 9.5 | 383.4 |
| publish_queue | 62 | 6.23 | 9.5 | 386.3 |
| append_dataset | 62 | 48.74 | 119.7 | 3021.7 |
| export | 62 | 0.34 | 0.6 | 20.9 |
| git_commit | 62 | 0.33 | 2.1 | 20.2 |
| push | 62 | 0.32 | 0.8 | 19.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1553 |
| Documents processed | 5970 |
| Process ratio | 384.4% (target ≥90.0%) |
| Rows published (traces) | 242 |
| Sessions observed | 90 |
| Avg session duration (s) | 697.011 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.382 |
| Avg connector latency (ms) | 13714.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **384.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
