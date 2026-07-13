# Pipeline Bottleneck Analysis

**Generated:** 2026-07-13T20:36:46+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 48 | 1.09 | 6.5 | 52.5 |
| source_discovery | 48 | 2.72 | 3.3 | 130.5 |
| connector | 48 | 62797.28 | 97806.1 | 3014269.5 |
| document_discovery | 48 | 62797.42 | 97806.2 | 3014276.3 |
| document_download | 48 | 218774.86 | 1509355.9 | 10501193.3 |
| extraction | 48 | 70.46 | 109.5 | 3382.2 |
| candidate_validation | 48 | 5.7 | 8.7 | 273.4 |
| publish_queue | 48 | 5.75 | 8.8 | 276.1 |
| append_dataset | 48 | 46.38 | 119.7 | 2226.0 |
| export | 48 | 0.34 | 0.6 | 16.5 |
| git_commit | 48 | 0.34 | 2.1 | 16.1 |
| push | 48 | 0.33 | 0.8 | 15.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1139 |
| Documents processed | 4295 |
| Process ratio | 377.1% (target ≥90.0%) |
| Rows published (traces) | 172 |
| Sessions observed | 76 |
| Avg session duration (s) | 600.211 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.171 |
| Avg connector latency (ms) | 13750.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **377.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
