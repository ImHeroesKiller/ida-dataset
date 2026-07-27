# Pipeline Bottleneck Analysis

**Generated:** 2026-07-27T00:20:43+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 200 | 0.99 | 6.5 | 198.0 |
| source_discovery | 200 | 3.07 | 39.8 | 614.0 |
| connector | 200 | 86515.97 | 97806.1 | 17303194.7 |
| document_discovery | 200 | 86516.12 | 97806.2 | 17303223.9 |
| document_download | 200 | 254326.56 | 1509355.9 | 50865312.9 |
| extraction | 200 | 89.3 | 274.0 | 17859.7 |
| candidate_validation | 200 | 10.19 | 37.2 | 2038.7 |
| publish_queue | 200 | 10.32 | 37.4 | 2063.3 |
| append_dataset | 200 | 42.63 | 119.7 | 8525.6 |
| export | 200 | 0.35 | 1.9 | 69.8 |
| git_commit | 200 | 0.31 | 2.1 | 62.4 |
| push | 200 | 0.32 | 0.8 | 63.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5771 |
| Documents processed | 15207 |
| Process ratio | 263.5% (target ≥90.0%) |
| Rows published (traces) | 932 |
| Sessions observed | 228 |
| Avg session duration (s) | 937.066 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.824 |
| Avg connector latency (ms) | 13708.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **263.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
