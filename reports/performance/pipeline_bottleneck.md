# Pipeline Bottleneck Analysis

**Generated:** 2026-07-26T08:51:00+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 191 | 0.99 | 6.5 | 189.5 |
| source_discovery | 191 | 3.08 | 39.8 | 588.3 |
| connector | 191 | 86161.15 | 97806.1 | 16456779.6 |
| document_discovery | 191 | 86161.3 | 97806.2 | 16456807.7 |
| document_download | 191 | 255057.76 | 1509355.9 | 48716032.4 |
| extraction | 191 | 88.63 | 274.0 | 16928.5 |
| candidate_validation | 191 | 9.85 | 30.0 | 1881.6 |
| publish_queue | 191 | 9.98 | 34.7 | 1905.8 |
| append_dataset | 191 | 42.97 | 119.7 | 8207.8 |
| export | 191 | 0.35 | 1.9 | 67.0 |
| git_commit | 191 | 0.31 | 2.1 | 59.6 |
| push | 191 | 0.32 | 0.8 | 60.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5502 |
| Documents processed | 14714 |
| Process ratio | 267.4% (target ≥90.0%) |
| Rows published (traces) | 887 |
| Sessions observed | 219 |
| Avg session duration (s) | 931.306 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.815 |
| Avg connector latency (ms) | 13763.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **267.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
