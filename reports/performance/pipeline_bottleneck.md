# Pipeline Bottleneck Analysis

**Generated:** 2026-08-02T13:41:30+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 268 | 1.4 | 70.9 | 375.5 |
| source_discovery | 268 | 4.12 | 186.3 | 1103.6 |
| connector | 268 | 88418.85 | 97806.1 | 23696253.0 |
| document_discovery | 268 | 88419.07 | 97806.2 | 23696310.0 |
| document_download | 268 | 237709.06 | 1509355.9 | 63706028.3 |
| extraction | 268 | 93.08 | 274.0 | 24946.5 |
| candidate_validation | 268 | 12.19 | 102.5 | 3267.2 |
| publish_queue | 268 | 12.27 | 102.7 | 3289.3 |
| append_dataset | 268 | 40.97 | 119.7 | 10981.1 |
| export | 268 | 0.35 | 2.1 | 93.8 |
| git_commit | 268 | 0.37 | 15.1 | 98.4 |
| push | 268 | 0.62 | 81.1 | 165.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7858 |
| Documents processed | 19073 |
| Process ratio | 242.7% (target ≥90.0%) |
| Rows published (traces) | 1269 |
| Sessions observed | 296 |
| Avg session duration (s) | 956.341 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.858 |
| Avg connector latency (ms) | 13702.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **242.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
