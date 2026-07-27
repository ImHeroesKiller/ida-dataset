# Pipeline Bottleneck Analysis

**Generated:** 2026-07-27T18:01:03+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 206 | 0.99 | 6.5 | 204.4 |
| source_discovery | 206 | 3.07 | 39.8 | 632.3 |
| connector | 206 | 86734.94 | 97806.1 | 17867398.0 |
| document_discovery | 206 | 86735.09 | 97806.2 | 17867427.9 |
| document_download | 206 | 253557.93 | 1509355.9 | 52232934.2 |
| extraction | 206 | 89.78 | 274.0 | 18495.5 |
| candidate_validation | 206 | 10.35 | 37.2 | 2131.2 |
| publish_queue | 206 | 10.47 | 37.4 | 2156.1 |
| append_dataset | 206 | 42.57 | 119.7 | 8768.8 |
| export | 206 | 0.35 | 1.9 | 71.7 |
| git_commit | 206 | 0.31 | 2.1 | 64.3 |
| push | 206 | 0.32 | 0.8 | 65.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5957 |
| Documents processed | 15579 |
| Process ratio | 261.5% (target ≥90.0%) |
| Rows published (traces) | 962 |
| Sessions observed | 234 |
| Avg session duration (s) | 940.269 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.829 |
| Avg connector latency (ms) | 13845.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **261.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
