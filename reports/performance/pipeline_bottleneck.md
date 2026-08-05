# Pipeline Bottleneck Analysis

**Generated:** 2026-08-05T17:59:19+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 301 | 1.53 | 70.9 | 461.1 |
| source_discovery | 301 | 4.31 | 186.3 | 1296.4 |
| connector | 301 | 89032.94 | 97806.1 | 26798915.4 |
| document_discovery | 301 | 89033.15 | 97806.2 | 26798976.7 |
| document_download | 301 | 234356.56 | 1509355.9 | 70541325.9 |
| extraction | 301 | 94.84 | 274.0 | 28547.7 |
| candidate_validation | 301 | 12.83 | 102.5 | 3863.2 |
| publish_queue | 301 | 12.91 | 102.7 | 3885.8 |
| append_dataset | 301 | 40.12 | 119.7 | 12075.3 |
| export | 301 | 0.35 | 2.1 | 104.4 |
| git_commit | 301 | 0.36 | 15.1 | 108.3 |
| push | 301 | 0.69 | 81.1 | 206.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8871 |
| Documents processed | 20780 |
| Process ratio | 234.2% (target ≥90.0%) |
| Rows published (traces) | 1434 |
| Sessions observed | 329 |
| Avg session duration (s) | 963.587 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.874 |
| Avg connector latency (ms) | 13749.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **234.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
