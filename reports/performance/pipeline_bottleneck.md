# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T10:53:16+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 357 | 1.56 | 70.9 | 557.9 |
| source_discovery | 357 | 4.53 | 186.3 | 1617.7 |
| connector | 357 | 89813.45 | 97806.1 | 32063400.9 |
| document_discovery | 357 | 89813.64 | 97806.2 | 32063469.5 |
| document_download | 357 | 231928.33 | 1509355.9 | 82798414.4 |
| extraction | 357 | 97.29 | 274.0 | 34731.8 |
| candidate_validation | 357 | 14.3 | 136.9 | 5106.1 |
| publish_queue | 357 | 14.37 | 136.9 | 5130.3 |
| append_dataset | 357 | 39.09 | 119.7 | 13954.8 |
| export | 357 | 0.35 | 2.1 | 123.9 |
| git_commit | 357 | 0.35 | 15.1 | 126.0 |
| push | 357 | 0.62 | 81.1 | 223.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10587 |
| Documents processed | 23831 |
| Process ratio | 225.1% (target ≥90.0%) |
| Rows published (traces) | 1714 |
| Sessions observed | 308 |
| Avg session duration (s) | 1066.042 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13708.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **225.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
