# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T09:59:23+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 335 | 1.6 | 70.9 | 535.8 |
| source_discovery | 335 | 4.64 | 186.3 | 1555.0 |
| connector | 335 | 89535.04 | 97806.1 | 29994239.9 |
| document_discovery | 335 | 89535.24 | 97806.2 | 29994305.4 |
| document_download | 335 | 232659.91 | 1509355.9 | 77941069.7 |
| extraction | 335 | 96.49 | 274.0 | 32323.2 |
| candidate_validation | 335 | 13.89 | 136.9 | 4651.5 |
| publish_queue | 335 | 13.96 | 136.9 | 4675.1 |
| append_dataset | 335 | 39.49 | 119.7 | 13229.0 |
| export | 335 | 0.34 | 2.1 | 115.4 |
| git_commit | 335 | 0.36 | 15.1 | 119.1 |
| push | 335 | 0.65 | 81.1 | 216.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9915 |
| Documents processed | 22652 |
| Process ratio | 228.5% (target ≥90.0%) |
| Rows published (traces) | 1604 |
| Sessions observed | 310 |
| Avg session duration (s) | 1067.135 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.964 |
| Avg connector latency (ms) | 14022.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **228.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
