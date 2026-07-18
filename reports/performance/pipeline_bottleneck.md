# Pipeline Bottleneck Analysis

**Generated:** 2026-07-18T00:11:52+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 95 | 1.02 | 6.5 | 97.0 |
| source_discovery | 95 | 2.76 | 3.5 | 262.2 |
| connector | 95 | 78244.19 | 97806.1 | 7433197.9 |
| document_discovery | 95 | 78244.33 | 97806.2 | 7433211.7 |
| document_download | 95 | 270370.23 | 1509355.9 | 25685171.9 |
| extraction | 95 | 83.27 | 274.0 | 7910.7 |
| candidate_validation | 95 | 7.28 | 18.7 | 691.8 |
| publish_queue | 95 | 7.51 | 34.7 | 713.2 |
| append_dataset | 95 | 47.53 | 119.7 | 4515.3 |
| export | 95 | 0.34 | 0.6 | 32.0 |
| git_commit | 95 | 0.32 | 2.1 | 30.3 |
| push | 95 | 0.31 | 0.8 | 29.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2566 |
| Documents processed | 8616 |
| Process ratio | 335.8% (target ≥90.0%) |
| Rows published (traces) | 407 |
| Sessions observed | 123 |
| Avg session duration (s) | 816.797 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.614 |
| Avg connector latency (ms) | 13683.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **335.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
