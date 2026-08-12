# Pipeline Bottleneck Analysis

**Generated:** 2026-08-12T02:22:33+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 403 | 1.49 | 70.9 | 601.7 |
| source_discovery | 403 | 4.33 | 186.3 | 1746.4 |
| connector | 403 | 90289.24 | 97806.1 | 36386564.2 |
| document_discovery | 403 | 90289.43 | 97806.2 | 36386639.1 |
| document_download | 403 | 235926.2 | 1509355.9 | 95078259.4 |
| extraction | 403 | 99.11 | 274.0 | 39941.1 |
| candidate_validation | 403 | 15.53 | 149.0 | 6260.0 |
| publish_queue | 403 | 15.6 | 149.1 | 6286.3 |
| append_dataset | 403 | 38.7 | 119.7 | 15596.4 |
| export | 403 | 0.35 | 2.7 | 141.4 |
| git_commit | 403 | 0.35 | 15.1 | 141.0 |
| push | 403 | 0.59 | 81.1 | 236.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11993 |
| Documents processed | 26505 |
| Process ratio | 221.0% (target ≥90.0%) |
| Rows published (traces) | 1944 |
| Sessions observed | 308 |
| Avg session duration (s) | 1057.932 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13798.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **221.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
