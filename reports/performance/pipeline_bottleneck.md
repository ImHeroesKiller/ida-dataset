# Pipeline Bottleneck Analysis

**Generated:** 2026-08-02T23:19:49+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 274 | 1.39 | 70.9 | 381.2 |
| source_discovery | 274 | 4.18 | 186.3 | 1144.5 |
| connector | 274 | 88541.71 | 97806.1 | 24260427.7 |
| document_discovery | 274 | 88541.92 | 97806.2 | 24260485.6 |
| document_download | 274 | 238183.36 | 1509355.9 | 65262239.6 |
| extraction | 274 | 93.28 | 274.0 | 25557.9 |
| candidate_validation | 274 | 12.3 | 102.5 | 3370.5 |
| publish_queue | 274 | 12.38 | 102.7 | 3392.8 |
| append_dataset | 274 | 40.82 | 119.7 | 11184.6 |
| export | 274 | 0.35 | 2.1 | 95.8 |
| git_commit | 274 | 0.36 | 15.1 | 100.0 |
| push | 274 | 0.61 | 81.1 | 166.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8044 |
| Documents processed | 19406 |
| Process ratio | 241.2% (target ≥90.0%) |
| Rows published (traces) | 1299 |
| Sessions observed | 302 |
| Avg session duration (s) | 959.152 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.861 |
| Avg connector latency (ms) | 13748.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **241.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
