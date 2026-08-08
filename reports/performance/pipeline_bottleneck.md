# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T18:59:17+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 344 | 1.58 | 70.9 | 544.8 |
| source_discovery | 344 | 4.59 | 186.3 | 1580.4 |
| connector | 344 | 89653.83 | 97806.1 | 30840917.6 |
| document_discovery | 344 | 89654.02 | 97806.2 | 30840984.2 |
| document_download | 344 | 231563.99 | 1509355.9 | 79658011.8 |
| extraction | 344 | 96.78 | 274.0 | 33291.4 |
| candidate_validation | 344 | 14.05 | 136.9 | 4834.1 |
| publish_queue | 344 | 14.12 | 136.9 | 4857.8 |
| append_dataset | 344 | 39.27 | 119.7 | 13507.9 |
| export | 344 | 0.35 | 2.1 | 119.5 |
| git_commit | 344 | 0.35 | 15.1 | 121.9 |
| push | 344 | 0.64 | 81.1 | 219.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10184 |
| Documents processed | 23094 |
| Process ratio | 226.8% (target ≥90.0%) |
| Rows published (traces) | 1649 |
| Sessions observed | 304 |
| Avg session duration (s) | 1066.664 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.977 |
| Avg connector latency (ms) | 13824.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **226.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
