# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T20:57:45+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 367 | 1.54 | 70.9 | 566.2 |
| source_discovery | 367 | 4.48 | 186.3 | 1643.8 |
| connector | 367 | 89926.2 | 97806.1 | 33002917.1 |
| document_discovery | 367 | 89926.4 | 97806.2 | 33002987.6 |
| document_download | 367 | 233447.33 | 1509355.9 | 85675169.2 |
| extraction | 367 | 97.5 | 274.0 | 35784.1 |
| candidate_validation | 367 | 14.44 | 136.9 | 5298.1 |
| publish_queue | 367 | 14.5 | 136.9 | 5322.7 |
| append_dataset | 367 | 38.9 | 119.7 | 14274.6 |
| export | 367 | 0.35 | 2.1 | 126.8 |
| git_commit | 367 | 0.35 | 15.1 | 128.7 |
| push | 367 | 0.62 | 81.1 | 225.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10897 |
| Documents processed | 24407 |
| Process ratio | 224.0% (target ≥90.0%) |
| Rows published (traces) | 1764 |
| Sessions observed | 307 |
| Avg session duration (s) | 1062.7 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13702.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **224.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
