# Pipeline Bottleneck Analysis

**Generated:** 2026-07-13T03:48:14+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 41 | 1.11 | 6.5 | 45.4 |
| source_discovery | 41 | 2.69 | 3.3 | 110.2 |
| connector | 41 | 57472.46 | 97806.1 | 2356370.9 |
| document_discovery | 41 | 57472.6 | 97806.2 | 2356376.8 |
| document_download | 41 | 214679.5 | 1509355.9 | 8801859.6 |
| extraction | 41 | 65.44 | 109.5 | 2682.9 |
| candidate_validation | 41 | 5.42 | 8.7 | 222.1 |
| publish_queue | 41 | 5.48 | 8.8 | 224.6 |
| append_dataset | 41 | 42.75 | 119.7 | 1752.7 |
| export | 41 | 0.34 | 0.6 | 13.8 |
| git_commit | 41 | 0.34 | 2.1 | 14.0 |
| push | 41 | 0.32 | 0.8 | 13.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 922 |
| Documents processed | 3424 |
| Process ratio | 371.4% (target ≥90.0%) |
| Rows published (traces) | 141 |
| Sessions observed | 69 |
| Avg session duration (s) | 549.406 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.118 |
| Avg connector latency (ms) | 13735.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **371.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
