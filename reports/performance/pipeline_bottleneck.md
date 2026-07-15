# Pipeline Bottleneck Analysis

**Generated:** 2026-07-15T08:37:16+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 63 | 1.05 | 6.5 | 66.2 |
| source_discovery | 63 | 2.72 | 3.3 | 171.4 |
| connector | 63 | 70229.1 | 97806.1 | 4424433.0 |
| document_discovery | 63 | 70229.24 | 97806.2 | 4424441.9 |
| document_download | 63 | 255170.45 | 1509355.9 | 16075738.5 |
| extraction | 63 | 79.77 | 274.0 | 5025.6 |
| candidate_validation | 63 | 6.23 | 9.5 | 392.2 |
| publish_queue | 63 | 6.27 | 9.5 | 395.1 |
| append_dataset | 63 | 49.08 | 119.7 | 3092.0 |
| export | 63 | 0.34 | 0.6 | 21.3 |
| git_commit | 63 | 0.33 | 2.1 | 20.5 |
| push | 63 | 0.32 | 0.8 | 20.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1584 |
| Documents processed | 6097 |
| Process ratio | 384.9% (target ≥90.0%) |
| Rows published (traces) | 247 |
| Sessions observed | 91 |
| Avg session duration (s) | 702.978 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.393 |
| Avg connector latency (ms) | 15116.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **384.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
