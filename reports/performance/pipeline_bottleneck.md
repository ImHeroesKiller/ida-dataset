# Pipeline Bottleneck Analysis

**Generated:** 2026-07-22T19:41:01+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 153 | 0.99 | 6.5 | 151.6 |
| source_discovery | 153 | 3.13 | 39.8 | 478.8 |
| connector | 153 | 84219.02 | 97806.1 | 12885509.7 |
| document_discovery | 153 | 84219.17 | 97806.2 | 12885533.1 |
| document_download | 153 | 252991.17 | 1509355.9 | 38707649.4 |
| extraction | 153 | 86.11 | 274.0 | 13175.4 |
| candidate_validation | 153 | 8.91 | 30.0 | 1362.8 |
| publish_queue | 153 | 9.06 | 34.7 | 1386.4 |
| append_dataset | 153 | 43.88 | 119.7 | 6713.5 |
| export | 153 | 0.35 | 1.9 | 53.0 |
| git_commit | 153 | 0.32 | 2.1 | 48.2 |
| push | 153 | 0.32 | 0.8 | 48.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4334 |
| Documents processed | 12359 |
| Process ratio | 285.2% (target ≥90.0%) |
| Rows published (traces) | 697 |
| Sessions observed | 181 |
| Avg session duration (s) | 895.315 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.767 |
| Avg connector latency (ms) | 14153.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **285.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
