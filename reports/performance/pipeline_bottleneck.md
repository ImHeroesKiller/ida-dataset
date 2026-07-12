# Pipeline Bottleneck Analysis

**Generated:** 2026-07-12T18:23:01+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 35 | 1.13 | 6.5 | 39.5 |
| source_discovery | 35 | 2.68 | 3.3 | 93.9 |
| connector | 35 | 51212.4 | 97806.1 | 1792433.9 |
| document_discovery | 35 | 51212.54 | 97806.2 | 1792438.9 |
| document_download | 35 | 203854.26 | 1509355.9 | 7134899.2 |
| extraction | 35 | 61.69 | 109.5 | 2159.3 |
| candidate_validation | 35 | 5.15 | 8.7 | 180.2 |
| publish_queue | 35 | 5.21 | 8.8 | 182.5 |
| append_dataset | 35 | 39.42 | 119.7 | 1379.7 |
| export | 35 | 0.33 | 0.6 | 11.4 |
| git_commit | 35 | 0.3 | 0.4 | 10.4 |
| push | 35 | 0.31 | 0.6 | 11.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 756 |
| Documents processed | 2676 |
| Process ratio | 354.0% (target ≥90.0%) |
| Rows published (traces) | 115 |
| Sessions observed | 63 |
| Avg session duration (s) | 492.952 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.071 |
| Avg connector latency (ms) | 13792.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **354.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
