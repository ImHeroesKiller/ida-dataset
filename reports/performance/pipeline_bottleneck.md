# Pipeline Bottleneck Analysis

**Generated:** 2026-08-10T09:40:06+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 375 | 1.53 | 70.9 | 573.9 |
| source_discovery | 375 | 4.44 | 186.3 | 1666.2 |
| connector | 375 | 90012.04 | 97806.1 | 33754514.0 |
| document_discovery | 375 | 90012.23 | 97806.2 | 33754585.3 |
| document_download | 375 | 238048.97 | 1509355.9 | 89268363.4 |
| extraction | 375 | 97.85 | 274.0 | 36692.9 |
| candidate_validation | 375 | 14.95 | 149.0 | 5607.1 |
| publish_queue | 375 | 15.02 | 149.1 | 5632.2 |
| append_dataset | 375 | 38.83 | 119.7 | 14562.9 |
| export | 375 | 0.35 | 2.1 | 130.1 |
| git_commit | 375 | 0.35 | 15.1 | 131.7 |
| push | 375 | 0.61 | 81.1 | 228.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11145 |
| Documents processed | 24870 |
| Process ratio | 223.1% (target ≥90.0%) |
| Rows published (traces) | 1804 |
| Sessions observed | 305 |
| Avg session duration (s) | 1061.056 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 14340.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **223.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
