# Pipeline Bottleneck Analysis

**Generated:** 2026-07-28T14:27:11+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 214 | 1.32 | 70.9 | 282.7 |
| source_discovery | 214 | 3.92 | 186.3 | 839.8 |
| connector | 214 | 87010.15 | 97806.1 | 18620172.9 |
| document_discovery | 214 | 87010.3 | 97806.2 | 18620203.9 |
| document_download | 214 | 250377.16 | 1509355.9 | 53580711.5 |
| extraction | 214 | 90.27 | 274.0 | 19318.7 |
| candidate_validation | 214 | 10.5 | 37.2 | 2246.1 |
| publish_queue | 214 | 10.61 | 37.4 | 2271.5 |
| append_dataset | 214 | 42.33 | 119.7 | 9059.3 |
| export | 214 | 0.35 | 1.9 | 74.4 |
| git_commit | 214 | 0.31 | 2.1 | 66.7 |
| push | 214 | 0.32 | 0.8 | 67.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6195 |
| Documents processed | 16032 |
| Process ratio | 258.8% (target ≥90.0%) |
| Rows published (traces) | 999 |
| Sessions observed | 242 |
| Avg session duration (s) | 942.533 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.821 |
| Avg connector latency (ms) | 13910.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **258.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
