# Pipeline Bottleneck Analysis

**Generated:** 2026-08-01T12:22:06+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 256 | 1.27 | 70.9 | 323.9 |
| source_discovery | 256 | 3.74 | 186.3 | 958.7 |
| connector | 256 | 88158.42 | 97806.1 | 22568554.3 |
| document_discovery | 256 | 88158.63 | 97806.2 | 22568609.6 |
| document_download | 256 | 239086.58 | 1509355.9 | 61206164.6 |
| extraction | 256 | 92.8 | 274.0 | 23755.9 |
| candidate_validation | 256 | 11.98 | 102.5 | 3065.8 |
| publish_queue | 256 | 12.06 | 102.7 | 3087.8 |
| append_dataset | 256 | 41.32 | 119.7 | 10579.0 |
| export | 256 | 0.35 | 2.1 | 90.2 |
| git_commit | 256 | 0.37 | 15.1 | 94.4 |
| push | 256 | 0.63 | 81.1 | 161.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7486 |
| Documents processed | 18404 |
| Process ratio | 245.8% (target ≥90.0%) |
| Rows published (traces) | 1209 |
| Sessions observed | 284 |
| Avg session duration (s) | 954.018 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.851 |
| Avg connector latency (ms) | 13828.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **245.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
