# Pipeline Bottleneck Analysis

**Generated:** 2026-08-05T19:53:03+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 302 | 1.53 | 70.9 | 462.4 |
| source_discovery | 302 | 4.3 | 186.3 | 1299.4 |
| connector | 302 | 89048.7 | 97806.1 | 26892705.9 |
| document_discovery | 302 | 89048.9 | 97806.2 | 26892767.3 |
| document_download | 302 | 234413.48 | 1509355.9 | 70792871.4 |
| extraction | 302 | 94.89 | 274.0 | 28655.9 |
| candidate_validation | 302 | 12.86 | 102.5 | 3882.6 |
| publish_queue | 302 | 12.93 | 102.7 | 3905.1 |
| append_dataset | 302 | 40.07 | 119.7 | 12102.1 |
| export | 302 | 0.35 | 2.1 | 104.8 |
| git_commit | 302 | 0.36 | 15.1 | 108.6 |
| push | 302 | 0.69 | 81.1 | 206.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8902 |
| Documents processed | 20811 |
| Process ratio | 233.8% (target ≥90.0%) |
| Rows published (traces) | 1439 |
| Sessions observed | 330 |
| Avg session duration (s) | 964.064 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.875 |
| Avg connector latency (ms) | 13807.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **233.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
