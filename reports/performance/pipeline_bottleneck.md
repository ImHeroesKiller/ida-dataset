# Pipeline Bottleneck Analysis

**Generated:** 2026-08-12T21:04:12+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 415 | 1.48 | 70.9 | 614.4 |
| source_discovery | 415 | 4.29 | 186.3 | 1780.8 |
| connector | 415 | 90397.0 | 97806.1 | 37514753.8 |
| document_discovery | 415 | 90397.18 | 97806.2 | 37514830.0 |
| document_download | 415 | 235636.9 | 1509355.9 | 97789311.7 |
| extraction | 415 | 99.42 | 274.0 | 41260.6 |
| candidate_validation | 415 | 15.8 | 149.0 | 6557.1 |
| publish_queue | 415 | 15.86 | 149.1 | 6583.9 |
| append_dataset | 415 | 38.6 | 119.7 | 16017.4 |
| export | 415 | 0.35 | 2.7 | 145.1 |
| git_commit | 415 | 0.35 | 15.1 | 144.8 |
| push | 415 | 0.63 | 81.1 | 263.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 12355 |
| Documents processed | 27184 |
| Process ratio | 220.0% (target ≥90.0%) |
| Rows published (traces) | 2004 |
| Sessions observed | 306 |
| Avg session duration (s) | 1057.016 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13848.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **220.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
