# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T21:58:08+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 368 | 1.54 | 70.9 | 567.2 |
| source_discovery | 368 | 4.47 | 186.3 | 1646.7 |
| connector | 368 | 89936.97 | 97806.1 | 33096804.6 |
| document_discovery | 368 | 89937.16 | 97806.2 | 33096875.2 |
| document_download | 368 | 234297.03 | 1509355.9 | 86221307.7 |
| extraction | 368 | 97.52 | 274.0 | 35887.7 |
| candidate_validation | 368 | 14.46 | 136.9 | 5320.4 |
| publish_queue | 368 | 14.52 | 136.9 | 5345.0 |
| append_dataset | 368 | 38.9 | 119.7 | 14313.6 |
| export | 368 | 0.35 | 2.1 | 127.1 |
| git_commit | 368 | 0.35 | 15.1 | 129.1 |
| push | 368 | 0.61 | 81.1 | 226.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10928 |
| Documents processed | 24469 |
| Process ratio | 223.9% (target ≥90.0%) |
| Rows published (traces) | 1769 |
| Sessions observed | 308 |
| Avg session duration (s) | 1063.724 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13723.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **223.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
