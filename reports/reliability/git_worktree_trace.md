# Git Working Tree Trace

Snapshots after each production stage. Dirty files after commit indicate post-commit writers.

## reliability_sprint_local

- **time:** 2026-07-10T19:03:17Z
- **dirty_count:** 25
- **modified:** 21
- **deleted:** 0
- **untracked:** 4
- **staged:** 0

```
 M .github/workflows/learn.yml
 M automation/ci/learning_session.py
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/source_performance.json
 M automation/lib/git_safe.py
 M reports/performance/api_statistics.md
 M reports/performance/cache_statistics.md
 M reports/performance/connector_performance.md
 M reports/performance/crawler_statistics.md
 M reports/performance/download_statistics.md
 M reports/performance/source_ranking.md
 M reports/performance/throughput.md
 M reports/production/candidate_pipeline.md
 M reports/production/connector_summary.md
 M reports/production/document_pipeline.md
 M reports/production/evidence_trace.md
 M reports/production/production_trace.md
 M reports/production/publish_pipeline.md
 M reports/production/runtime_statistics.md
 M scripts/git_safe_sync_push.sh
?? automation/ci/worktree_trace.py
?? reports/production/production_trace_SES-DISC-E2E.json
?? reports/production/sessions/SES-DISC-E2E/
?? scripts/test_git_recovery.sh
```
## recovery_test_start

- **time:** 2026-07-10T19:03:17Z
- **dirty_count:** 25
- **modified:** 21
- **deleted:** 0
- **untracked:** 4
- **staged:** 0

```
 M .github/workflows/learn.yml
 M automation/ci/learning_session.py
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/source_performance.json
 M automation/lib/git_safe.py
 M reports/performance/api_statistics.md
 M reports/performance/cache_statistics.md
 M reports/performance/connector_performance.md
 M reports/performance/crawler_statistics.md
 M reports/performance/download_statistics.md
 M reports/performance/source_ranking.md
 M reports/performance/throughput.md
 M reports/production/candidate_pipeline.md
 M reports/production/connector_summary.md
 M reports/production/document_pipeline.md
 M reports/production/evidence_trace.md
 M reports/production/production_trace.md
 M reports/production/publish_pipeline.md
 M reports/production/runtime_statistics.md
 M scripts/git_safe_sync_push.sh
?? automation/ci/worktree_trace.py
?? reports/production/production_trace_SES-DISC-E2E.json
?? reports/production/sessions/SES-DISC-E2E/
?? scripts/test_git_recovery.sh
```
## recovery_dirty

- **time:** 2026-07-10T19:03:18Z
- **dirty_count:** 25
- **modified:** 21
- **deleted:** 0
- **untracked:** 4
- **staged:** 0

```
 M .github/workflows/learn.yml
 M automation/ci/learning_session.py
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/source_performance.json
 M automation/lib/git_safe.py
 M reports/performance/api_statistics.md
 M reports/performance/cache_statistics.md
 M reports/performance/connector_performance.md
 M reports/performance/crawler_statistics.md
 M reports/performance/download_statistics.md
 M reports/performance/source_ranking.md
 M reports/performance/throughput.md
 M reports/production/candidate_pipeline.md
 M reports/production/connector_summary.md
 M reports/production/document_pipeline.md
 M reports/production/evidence_trace.md
 M reports/production/production_trace.md
 M reports/production/publish_pipeline.md
 M reports/production/runtime_statistics.md
 M scripts/git_safe_sync_push.sh
?? automation/ci/worktree_trace.py
?? reports/production/production_trace_SES-DISC-E2E.json
?? reports/production/sessions/SES-DISC-E2E/
?? scripts/test_git_recovery.sh
```
## pre_acquire

- **time:** 2026-07-10T19:17:53Z
- **dirty_count:** 0

### status --porcelain=v1

```
(empty)
```

### diff --name-only

```
(empty)
```

### diff --stat

```
(empty)
```

## post_session_pre_commit

- **time:** 2026-07-10T19:27:55Z
- **dirty_count:** 37

### status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-10.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M reports/discovery/provider_health.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/query_statistics.md
 M reports/discovery/trusted_source_usage.md
 M reports/performance/api_statistics.md
 M reports/performance/cache_statistics.md
 M reports/performance/connector_performance.md
 M reports/performance/crawler_statistics.md
 M reports/performance/download_statistics.md
 M reports/performance/source_ranking.md
 M reports/performance/throughput.md
 M reports/production/candidate_pipeline.md
 M reports/production/connector_summary.md
 M reports/production/document_pipeline.md
 M reports/production/evidence_trace.md
 M reports/production/production_trace.md
 M reports/production/publish_pipeline.md
 M reports/production/runtime_statistics.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260710-88FC2E.jsonl
?? automation/queue/publish/CAND-94B9A207CDEE.json
?? automation/queue/publish/CAND-95C824E2F514.json
?? automation/queue/publish/CAND-AB5E38F39855.json
?? automation/sessions/2026-07-10/SESSION-20260710-005543.json
?? reports/production/production_trace_SES-20260710-88FC2E.json
?? reports/production/sessions/SES-20260710-88FC2E/
```

### diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-10.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
reports/discovery/provider_health.md
reports/discovery/provider_statistics.md
reports/discovery/query_statistics.md
reports/discovery/trusted_source_usage.md
reports/performance/api_statistics.md
reports/performance/cache_statistics.md
reports/performance/connector_performance.md
reports/performance/crawler_statistics.md
reports/performance/download_statistics.md
reports/performance/source_ranking.md
reports/performance/throughput.md
reports/production/candidate_pipeline.md
reports/production/connector_summary.md
reports/production/document_pipeline.md
reports/production/evidence_trace.md
reports/production/production_trace.md
reports/production/publish_pipeline.md
reports/production/runtime_statistics.md
reports/reliability/git_worktree_trace.md
reports/reliability/writer_finalize.json
```

### diff --stat

```
 .../learning/state/acquisition_performance.json    | 199 +++++----
 automation/learning/state/current_snapshot.json    |   6 +-
 automation/learning/state/discovery_analytics.json |  96 +++--
 automation/learning/state/learning_journal.jsonl   |  63 +++
 automation/learning/state/live_activity.json       |  10 +-
 automation/learning/state/production_trace.json    | 474 +++++++++++----------
 automation/learning/state/snapshot_2026-07-10.json |   6 +-
 automation/learning/state/source_health.json       |  50 +--
 automation/learning/state/source_performance.json  |  62 +--
 automation/sessions/index.json                     |  30 +-
 reports/discovery/provider_health.md               |   2 +-
 reports/discovery/provider_statistics.md           |  12 +-
 reports/discovery/query_statistics.md              |  46 +-
 reports/discovery/trusted_source_usage.md          |   6 +-
 reports/performance/api_statistics.md              |  14 +-
 reports/performance/cache_statistics.md            |   4 +-
 reports/performance/connector_performance.md       |  16 +-
 reports/performance/crawler_statistics.md          |  26 +-
 reports/performance/download_statistics.md         |  18 +-
 reports/performance/source_ranking.md              |  12 +-
 reports/performance/throughput.md                  |  18 +-
 reports/production/candidate_pipeline.md           |   9 +-
 reports/production/connector_summary.md            |  64 +--
 reports/production/document_pipeline.md            |  13 +-
 reports/production/evidence_trace.md               |  22 +-
 reports/production/production_trace.md             |  42 +-
 reports/production/publish_pipeline.md             |  20 +-
 reports/production/runtime_statistics.md           |  60 ++-
 reports/reliability/git_worktree_trace.md          |  23 +
 reports/reliability/writer_finalize.json           |   2 +-
 30 files changed, 780 insertions(+), 645 deletions(-)
```

## pre_acquire

- **time:** 2026-07-10T20:18:49Z
- **dirty_count:** 0

### status --porcelain=v1

```
(empty)
```

### diff --name-only

```
(empty)
```

### diff --stat

```
(empty)
```

## post_session_pre_commit

- **time:** 2026-07-10T20:28:42Z
- **dirty_count:** 41

### status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/daily_2026-07-10.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-10.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M domains/business_development/industry_library.csv
 M reports/discovery/provider_health.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/query_statistics.md
 M reports/discovery/reputation_scores.md
 M reports/manufacturing/factory_economics.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/production_capacity.md
 M reports/performance/api_statistics.md
 M reports/performance/cache_statistics.md
 M reports/performance/connector_performance.md
 M reports/performance/crawler_statistics.md
 M reports/performance/download_statistics.md
 M reports/performance/source_ranking.md
 M reports/performance/throughput.md
 M reports/production/candidate_pipeline.md
 M reports/production/connector_summary.md
 M reports/production/document_pipeline.md
 M reports/production/evidence_trace.md
 M reports/production/production_trace.md
 M reports/production/publish_pipeline.md
 M reports/production/runtime_statistics.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260710-D190E7.jsonl
?? automation/sessions/2026-07-10/SESSION-20260710-9F5887.json
?? reports/production/production_trace_SES-20260710-D190E7.json
?? reports/production/sessions/SES-20260710-D190E7/
```

### diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/daily_2026-07-10.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-10.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
domains/business_development/industry_library.csv
reports/discovery/provider_health.md
reports/discovery/provider_statistics.md
reports/discovery/query_statistics.md
reports/discovery/reputation_scores.md
reports/manufacturing/factory_economics.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/production_capacity.md
reports/performance/api_statistics.md
reports/performance/cache_statistics.md
reports/performance/connector_performance.md
reports/performance/crawler_statistics.md
reports/performance/download_statistics.md
reports/performance/source_ranking.md
reports/performance/throughput.md
reports/production/candidate_pipeline.md
reports/production/connector_summary.md
reports/production/document_pipeline.md
reports/production/evidence_trace.md
reports/production/production_trace.md
reports/production/publish_pipeline.md
reports/production/runtime_statistics.md
reports/reliability/git_worktree_trace.md
reports/reliability/writer_finalize.json
```

### diff --stat

```
 .../learning/state/acquisition_performance.json    | 164 ++++----
 automation/learning/state/current_snapshot.json    |   6 +-
 automation/learning/state/daily_2026-07-10.json    |   4 +-
 automation/learning/state/discovery_analytics.json |  88 ++---
 automation/learning/state/learning_journal.jsonl   |  69 ++++
 automation/learning/state/live_activity.json       |  10 +-
 automation/learning/state/manufacturing_state.json | 229 ++++++------
 automation/learning/state/production_trace.json    | 412 ++++++++++-----------
 automation/learning/state/snapshot_2026-07-10.json |   6 +-
 automation/learning/state/source_health.json       |  56 +--
 automation/learning/state/source_performance.json  |  62 ++--
 automation/sessions/index.json                     |  30 +-
 domains/business_development/industry_library.csv  |   1 +
 reports/discovery/provider_health.md               |   2 +-
 reports/discovery/provider_statistics.md           |  10 +-
 reports/discovery/query_statistics.md              |  46 +--
 reports/discovery/reputation_scores.md             |  14 +-
 reports/manufacturing/factory_economics.md         |  22 +-
 reports/manufacturing/growth_velocity.md           |  36 +-
 reports/manufacturing/knowledge_gap.md             |   2 +-
 reports/manufacturing/production_capacity.md       |  14 +-
 reports/performance/api_statistics.md              |  14 +-
 reports/performance/cache_statistics.md            |   4 +-
 reports/performance/connector_performance.md       |  16 +-
 reports/performance/crawler_statistics.md          |  36 +-
 reports/performance/download_statistics.md         |  20 +-
 reports/performance/source_ranking.md              |  14 +-
 reports/performance/throughput.md                  |  14 +-
 reports/production/candidate_pipeline.md           |  12 +-
 reports/production/connector_summary.md            |  52 +--
 reports/production/document_pipeline.md            |  14 +-
 reports/production/evidence_trace.md               |  14 +-
 reports/production/production_trace.md             |  38 +-
 reports/production/publish_pipeline.md             |  20 +-
 reports/production/runtime_statistics.md           |  54 +--
 reports/reliability/git_worktree_trace.md          |  23 ++
 reports/reliability/writer_finalize.json           |   2 +-
 37 files changed, 871 insertions(+), 759 deletions(-)
```

