# Pipeline Bottleneck Analysis

**Generated:** 2026-08-05T21:28:03+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 303 | 1.53 | 70.9 | 463.5 |
| source_discovery | 303 | 4.3 | 186.3 | 1302.6 |
| connector | 303 | 89064.68 | 97806.1 | 26986597.4 |
| document_discovery | 303 | 89064.88 | 97806.2 | 26986658.9 |
| document_download | 303 | 234452.94 | 1509355.9 | 71039241.2 |
| extraction | 303 | 94.93 | 274.0 | 28763.3 |
| candidate_validation | 303 | 12.88 | 102.5 | 3903.1 |
| publish_queue | 303 | 12.96 | 102.7 | 3925.7 |
| append_dataset | 303 | 40.04 | 119.7 | 12131.2 |
| export | 303 | 0.35 | 2.1 | 105.2 |
| git_commit | 303 | 0.36 | 15.1 | 108.9 |
| push | 303 | 0.68 | 81.1 | 207.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8933 |
| Documents processed | 20845 |
| Process ratio | 233.3% (target ≥90.0%) |
| Rows published (traces) | 1444 |
| Sessions observed | 331 |
| Avg session duration (s) | 963.885 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.875 |
| Avg connector latency (ms) | 13685.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **233.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
