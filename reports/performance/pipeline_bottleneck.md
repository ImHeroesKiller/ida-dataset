# Pipeline Bottleneck Analysis

**Generated:** 2026-07-15T12:38:29+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 65 | 1.05 | 6.5 | 68.3 |
| source_discovery | 65 | 2.73 | 3.3 | 177.2 |
| connector | 65 | 70957.16 | 97806.1 | 4612215.4 |
| document_discovery | 65 | 70957.3 | 97806.2 | 4612224.5 |
| document_download | 65 | 262443.74 | 1509355.9 | 17058842.8 |
| extraction | 65 | 80.33 | 274.0 | 5221.4 |
| candidate_validation | 65 | 6.3 | 9.5 | 409.2 |
| publish_queue | 65 | 6.34 | 9.5 | 412.2 |
| append_dataset | 65 | 49.55 | 119.7 | 3220.6 |
| export | 65 | 0.34 | 0.6 | 21.9 |
| git_commit | 65 | 0.33 | 2.1 | 21.2 |
| push | 65 | 0.32 | 0.8 | 20.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1646 |
| Documents processed | 6333 |
| Process ratio | 384.8% (target ≥90.0%) |
| Rows published (traces) | 257 |
| Sessions observed | 93 |
| Avg session duration (s) | 717.161 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.414 |
| Avg connector latency (ms) | 14172.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **384.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
