# Pipeline Bottleneck Analysis

**Generated:** 2026-07-31T21:22:58+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 250 | 1.27 | 70.9 | 318.1 |
| source_discovery | 250 | 3.76 | 186.3 | 941.2 |
| connector | 250 | 88019.71 | 97806.1 | 22004928.0 |
| document_discovery | 250 | 88019.93 | 97806.2 | 22004982.5 |
| document_download | 250 | 240001.13 | 1509355.9 | 60000282.2 |
| extraction | 250 | 92.56 | 274.0 | 23139.6 |
| candidate_validation | 250 | 11.84 | 102.5 | 2960.2 |
| publish_queue | 250 | 11.93 | 102.7 | 2981.9 |
| append_dataset | 250 | 41.46 | 119.7 | 10364.4 |
| export | 250 | 0.35 | 2.1 | 88.0 |
| git_commit | 250 | 0.37 | 15.1 | 92.6 |
| push | 250 | 0.64 | 81.1 | 159.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7311 |
| Documents processed | 18070 |
| Process ratio | 247.2% (target ≥90.0%) |
| Rows published (traces) | 1179 |
| Sessions observed | 278 |
| Avg session duration (s) | 952.996 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.848 |
| Avg connector latency (ms) | 13729.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **247.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
