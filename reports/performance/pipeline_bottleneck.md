# Pipeline Bottleneck Analysis

**Generated:** 2026-08-07T07:33:11+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 313 | 1.51 | 70.9 | 473.4 |
| source_discovery | 313 | 4.25 | 186.3 | 1331.2 |
| connector | 313 | 89224.22 | 97806.1 | 27927179.5 |
| document_discovery | 313 | 89224.42 | 97806.2 | 27927242.2 |
| document_download | 313 | 233364.84 | 1509355.9 | 73043195.2 |
| extraction | 313 | 95.37 | 274.0 | 29849.9 |
| candidate_validation | 313 | 13.1 | 102.5 | 4101.6 |
| publish_queue | 313 | 13.18 | 102.7 | 4124.5 |
| append_dataset | 313 | 39.93 | 119.7 | 12496.7 |
| export | 313 | 0.35 | 2.1 | 108.4 |
| git_commit | 313 | 0.36 | 15.1 | 112.1 |
| push | 313 | 0.67 | 81.1 | 210.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9243 |
| Documents processed | 21418 |
| Process ratio | 231.7% (target ≥90.0%) |
| Rows published (traces) | 1494 |
| Sessions observed | 309 |
| Avg session duration (s) | 1057.647 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.93 |
| Avg connector latency (ms) | 13719.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **231.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
