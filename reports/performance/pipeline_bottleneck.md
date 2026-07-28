# Pipeline Bottleneck Analysis

**Generated:** 2026-07-28T06:06:19+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 211 | 1.32 | 70.9 | 279.4 |
| source_discovery | 211 | 3.94 | 186.3 | 830.4 |
| connector | 211 | 86910.81 | 97806.1 | 18338181.7 |
| document_discovery | 211 | 86910.96 | 97806.2 | 18338212.3 |
| document_download | 211 | 251765.54 | 1509355.9 | 53122529.4 |
| extraction | 211 | 90.13 | 274.0 | 19016.6 |
| candidate_validation | 211 | 10.47 | 37.2 | 2210.1 |
| publish_queue | 211 | 10.59 | 37.4 | 2235.3 |
| append_dataset | 211 | 42.43 | 119.7 | 8952.6 |
| export | 211 | 0.35 | 1.9 | 73.4 |
| git_commit | 211 | 0.31 | 2.1 | 65.8 |
| push | 211 | 0.32 | 0.8 | 66.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6112 |
| Documents processed | 15878 |
| Process ratio | 259.8% (target ≥90.0%) |
| Rows published (traces) | 987 |
| Sessions observed | 239 |
| Avg session duration (s) | 941.9 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.833 |
| Avg connector latency (ms) | 13672.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **259.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
