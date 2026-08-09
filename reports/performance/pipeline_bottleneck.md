# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T23:56:12+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 370 | 1.54 | 70.9 | 569.4 |
| source_discovery | 370 | 4.47 | 186.3 | 1652.4 |
| connector | 370 | 89957.95 | 97806.1 | 33284440.6 |
| document_discovery | 370 | 89958.14 | 97806.2 | 33284511.4 |
| document_download | 370 | 235338.54 | 1509355.9 | 87075259.0 |
| extraction | 370 | 97.56 | 274.0 | 36098.5 |
| candidate_validation | 370 | 14.5 | 136.9 | 5365.6 |
| publish_queue | 370 | 14.57 | 136.9 | 5390.4 |
| append_dataset | 370 | 38.88 | 119.7 | 14387.4 |
| export | 370 | 0.35 | 2.1 | 127.8 |
| git_commit | 370 | 0.35 | 15.1 | 130.0 |
| push | 370 | 0.61 | 81.1 | 226.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10990 |
| Documents processed | 24582 |
| Process ratio | 223.7% (target ≥90.0%) |
| Rows published (traces) | 1779 |
| Sessions observed | 310 |
| Avg session duration (s) | 1065.003 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13672.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **223.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
