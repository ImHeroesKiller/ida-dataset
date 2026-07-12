# Pipeline Bottleneck Analysis

**Generated:** 2026-07-12T22:11:45+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 38 | 1.11 | 6.5 | 42.1 |
| source_discovery | 38 | 2.67 | 3.3 | 101.3 |
| connector | 38 | 54597.07 | 97806.1 | 2074688.7 |
| document_discovery | 38 | 54597.22 | 97806.2 | 2074694.3 |
| document_download | 38 | 210962.88 | 1509355.9 | 8016589.4 |
| extraction | 38 | 63.08 | 109.5 | 2396.9 |
| candidate_validation | 38 | 5.21 | 8.7 | 197.9 |
| publish_queue | 38 | 5.27 | 8.8 | 200.3 |
| append_dataset | 38 | 40.63 | 119.7 | 1543.9 |
| export | 38 | 0.33 | 0.6 | 12.5 |
| git_commit | 38 | 0.34 | 2.1 | 13.1 |
| push | 38 | 0.31 | 0.6 | 11.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 839 |
| Documents processed | 3038 |
| Process ratio | 362.1% (target ≥90.0%) |
| Rows published (traces) | 126 |
| Sessions observed | 66 |
| Avg session duration (s) | 523.182 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.032 |
| Avg connector latency (ms) | 13799.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **362.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
