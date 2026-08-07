# Pipeline Bottleneck Analysis

**Generated:** 2026-08-07T11:11:22+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 315 | 1.64 | 70.9 | 516.6 |
| source_discovery | 315 | 4.76 | 186.3 | 1498.7 |
| connector | 315 | 89254.93 | 97806.1 | 28115303.8 |
| document_discovery | 315 | 89255.13 | 97806.2 | 28115366.7 |
| document_download | 315 | 232643.36 | 1509355.9 | 73282659.2 |
| extraction | 315 | 95.64 | 274.0 | 30126.8 |
| candidate_validation | 315 | 13.51 | 136.9 | 4254.1 |
| publish_queue | 315 | 13.58 | 136.9 | 4277.0 |
| append_dataset | 315 | 39.83 | 119.7 | 12545.8 |
| export | 315 | 0.35 | 2.1 | 108.9 |
| git_commit | 315 | 0.36 | 15.1 | 112.5 |
| push | 315 | 0.67 | 81.1 | 210.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9305 |
| Documents processed | 21519 |
| Process ratio | 231.3% (target ≥90.0%) |
| Rows published (traces) | 1504 |
| Sessions observed | 311 |
| Avg session duration (s) | 1056.727 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.93 |
| Avg connector latency (ms) | 13750.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **231.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
