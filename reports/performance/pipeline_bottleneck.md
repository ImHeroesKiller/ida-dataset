# Pipeline Bottleneck Analysis

**Generated:** 2026-07-14T08:29:02+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 52 | 1.08 | 6.5 | 56.4 |
| source_discovery | 52 | 2.73 | 3.3 | 142.0 |
| connector | 52 | 65200.96 | 97806.1 | 3390449.9 |
| document_discovery | 52 | 65201.1 | 97806.2 | 3390457.2 |
| document_download | 52 | 225322.64 | 1509355.9 | 11716777.1 |
| extraction | 52 | 72.77 | 109.5 | 3783.8 |
| candidate_validation | 52 | 5.88 | 8.7 | 305.6 |
| publish_queue | 52 | 5.93 | 8.8 | 308.4 |
| append_dataset | 52 | 47.34 | 119.7 | 2461.8 |
| export | 52 | 0.35 | 0.6 | 18.0 |
| git_commit | 52 | 0.33 | 2.1 | 17.4 |
| push | 52 | 0.33 | 0.8 | 17.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1263 |
| Documents processed | 4731 |
| Process ratio | 374.6% (target ≥90.0%) |
| Rows published (traces) | 192 |
| Sessions observed | 80 |
| Avg session duration (s) | 629.875 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.244 |
| Avg connector latency (ms) | 13814.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **374.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
