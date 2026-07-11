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

## pre_acquire

- **time:** 2026-07-10T21:57:00Z
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

- **time:** 2026-07-10T22:06:50Z
- **dirty_count:** 43

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
 M domains/business_development/business_signal_library.csv
 M reports/discovery/provider_health.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/query_statistics.md
 M reports/discovery/reputation_scores.md
 M reports/discovery/trusted_source_usage.md
 M reports/manufacturing/factory_economics.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/knowledge_universe.md
 M reports/manufacturing/production_capacity.md
 M reports/manufacturing/scheduler_decisions.md
 M reports/performance/api_statistics.md
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
?? automation/learning/state/sessions/SES-20260710-31EBC7.jsonl
?? automation/sessions/2026-07-10/SESSION-20260710-D5E25C.json
?? reports/production/production_trace_SES-20260710-31EBC7.json
?? reports/production/sessions/SES-20260710-31EBC7/
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
domains/business_development/business_signal_library.csv
reports/discovery/provider_health.md
reports/discovery/provider_statistics.md
reports/discovery/query_statistics.md
reports/discovery/reputation_scores.md
reports/discovery/trusted_source_usage.md
reports/manufacturing/factory_economics.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/knowledge_universe.md
reports/manufacturing/production_capacity.md
reports/manufacturing/scheduler_decisions.md
reports/performance/api_statistics.md
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
 .../learning/state/acquisition_performance.json    | 190 ++++++-------
 automation/learning/state/current_snapshot.json    |   6 +-
 automation/learning/state/daily_2026-07-10.json    |   4 +-
 automation/learning/state/discovery_analytics.json | 140 +++++-----
 automation/learning/state/learning_journal.jsonl   |  73 +++++
 automation/learning/state/live_activity.json       |  10 +-
 automation/learning/state/manufacturing_state.json | 282 ++++++++++---------
 automation/learning/state/production_trace.json    | 304 +++++++++++++--------
 automation/learning/state/snapshot_2026-07-10.json |   6 +-
 automation/learning/state/source_health.json       |  30 +-
 automation/learning/state/source_performance.json  |  64 ++---
 automation/sessions/index.json                     |  30 +-
 .../business_signal_library.csv                    |   3 +
 reports/discovery/provider_health.md               |   2 +-
 reports/discovery/provider_statistics.md           |  10 +-
 reports/discovery/query_statistics.md              |  20 +-
 reports/discovery/reputation_scores.md             |  14 +-
 reports/discovery/trusted_source_usage.md          |   6 +-
 reports/manufacturing/factory_economics.md         |  18 +-
 reports/manufacturing/growth_velocity.md           |  44 +--
 reports/manufacturing/knowledge_gap.md             |   4 +-
 reports/manufacturing/knowledge_universe.md        |   2 +-
 reports/manufacturing/production_capacity.md       |  20 +-
 reports/manufacturing/scheduler_decisions.md       |   2 +-
 reports/performance/api_statistics.md              |  14 +-
 reports/performance/connector_performance.md       |  16 +-
 reports/performance/crawler_statistics.md          |   6 +-
 reports/performance/download_statistics.md         |   2 +-
 reports/performance/source_ranking.md              |  14 +-
 reports/performance/throughput.md                  |  14 +-
 reports/production/candidate_pipeline.md           |  12 +-
 reports/production/connector_summary.md            |  32 +--
 reports/production/document_pipeline.md            |   2 +-
 reports/production/evidence_trace.md               |  32 ++-
 reports/production/production_trace.md             |  34 +--
 reports/production/publish_pipeline.md             |  12 +-
 reports/production/runtime_statistics.md           |  38 +--
 reports/reliability/git_worktree_trace.md          |  23 ++
 reports/reliability/writer_finalize.json           |   2 +-
 39 files changed, 869 insertions(+), 668 deletions(-)
```

## pre_acquire

- **time:** 2026-07-10T22:59:19Z
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

- **time:** 2026-07-10T23:09:08Z
- **dirty_count:** 42

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
 M domains/business_development/business_signal_library.csv
 M reports/discovery/provider_health.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/query_statistics.md
 M reports/discovery/reputation_scores.md
 M reports/manufacturing/factory_economics.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/knowledge_universe.md
 M reports/manufacturing/production_capacity.md
 M reports/manufacturing/scheduler_decisions.md
 M reports/performance/api_statistics.md
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
?? automation/learning/state/sessions/SES-20260710-725C07.jsonl
?? automation/sessions/2026-07-10/SESSION-20260710-E077DD.json
?? reports/production/production_trace_SES-20260710-725C07.json
?? reports/production/sessions/SES-20260710-725C07/
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
domains/business_development/business_signal_library.csv
reports/discovery/provider_health.md
reports/discovery/provider_statistics.md
reports/discovery/query_statistics.md
reports/discovery/reputation_scores.md
reports/manufacturing/factory_economics.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/knowledge_universe.md
reports/manufacturing/production_capacity.md
reports/manufacturing/scheduler_decisions.md
reports/performance/api_statistics.md
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
 .../learning/state/acquisition_performance.json    |  60 ++--
 automation/learning/state/current_snapshot.json    |   6 +-
 automation/learning/state/daily_2026-07-10.json    |   4 +-
 automation/learning/state/discovery_analytics.json |  36 +--
 automation/learning/state/learning_journal.jsonl   |  73 +++++
 automation/learning/state/live_activity.json       |   6 +-
 automation/learning/state/manufacturing_state.json | 302 ++++++++++-----------
 automation/learning/state/production_trace.json    | 174 ++++++------
 automation/learning/state/snapshot_2026-07-10.json |   6 +-
 automation/learning/state/source_health.json       |  30 +-
 automation/learning/state/source_performance.json  |  64 ++---
 automation/sessions/index.json                     |  30 +-
 .../business_signal_library.csv                    |   3 +
 reports/discovery/provider_health.md               |   2 +-
 reports/discovery/provider_statistics.md           |  10 +-
 reports/discovery/query_statistics.md              |   8 +-
 reports/discovery/reputation_scores.md             |   8 +-
 reports/manufacturing/factory_economics.md         |  18 +-
 reports/manufacturing/growth_velocity.md           |  46 ++--
 reports/manufacturing/knowledge_gap.md             |   4 +-
 reports/manufacturing/knowledge_universe.md        |   2 +-
 reports/manufacturing/production_capacity.md       |  20 +-
 reports/manufacturing/scheduler_decisions.md       |   2 +-
 reports/performance/api_statistics.md              |  14 +-
 reports/performance/connector_performance.md       |  16 +-
 reports/performance/crawler_statistics.md          |   2 +-
 reports/performance/download_statistics.md         |   2 +-
 reports/performance/source_ranking.md              |   8 +-
 reports/performance/throughput.md                  |  12 +-
 reports/production/candidate_pipeline.md           |   8 +-
 reports/production/connector_summary.md            |  34 +--
 reports/production/document_pipeline.md            |   2 +-
 reports/production/evidence_trace.md               |  14 +-
 reports/production/production_trace.md             |  34 +--
 reports/production/publish_pipeline.md             |   2 +-
 reports/production/runtime_statistics.md           |  28 +-
 reports/reliability/git_worktree_trace.md          |  23 ++
 reports/reliability/writer_finalize.json           |   2 +-
 38 files changed, 621 insertions(+), 494 deletions(-)
```

## pre_acquire

- **time:** 2026-07-11T00:04:30Z
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

- **time:** 2026-07-11T00:14:21Z
- **dirty_count:** 42

### status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/daily_2026-07-11.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-11.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M domains/business_development/business_signal_library.csv
 M reports/discovery/provider_health.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/query_statistics.md
 M reports/discovery/reputation_scores.md
 M reports/manufacturing/factory_economics.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/knowledge_universe.md
 M reports/manufacturing/production_capacity.md
 M reports/manufacturing/scheduler_decisions.md
 M reports/performance/api_statistics.md
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
?? automation/learning/state/sessions/SES-20260711-D98C8B.jsonl
?? automation/sessions/2026-07-11/
?? reports/production/production_trace_SES-20260711-D98C8B.json
?? reports/production/sessions/SES-20260711-D98C8B/
```

### diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/daily_2026-07-11.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-11.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
domains/business_development/business_signal_library.csv
reports/discovery/provider_health.md
reports/discovery/provider_statistics.md
reports/discovery/query_statistics.md
reports/discovery/reputation_scores.md
reports/manufacturing/factory_economics.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/knowledge_universe.md
reports/manufacturing/production_capacity.md
reports/manufacturing/scheduler_decisions.md
reports/performance/api_statistics.md
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
 .../learning/state/acquisition_performance.json    |  60 +++---
 automation/learning/state/current_snapshot.json    |   8 +-
 automation/learning/state/daily_2026-07-11.json    |   4 +-
 automation/learning/state/discovery_analytics.json |  36 ++--
 automation/learning/state/learning_journal.jsonl   |  73 +++++++
 automation/learning/state/live_activity.json       |   6 +-
 automation/learning/state/manufacturing_state.json | 230 ++++++++++-----------
 automation/learning/state/production_trace.json    | 148 ++++++-------
 automation/learning/state/snapshot_2026-07-11.json |   8 +-
 automation/learning/state/source_health.json       |  30 +--
 automation/learning/state/source_performance.json  |  64 +++---
 automation/sessions/index.json                     |  30 ++-
 .../business_signal_library.csv                    |   3 +
 reports/discovery/provider_health.md               |   2 +-
 reports/discovery/provider_statistics.md           |  10 +-
 reports/discovery/query_statistics.md              |   8 +-
 reports/discovery/reputation_scores.md             |   8 +-
 reports/manufacturing/factory_economics.md         |  10 +-
 reports/manufacturing/growth_velocity.md           |  40 ++--
 reports/manufacturing/knowledge_gap.md             |   4 +-
 reports/manufacturing/knowledge_universe.md        |   2 +-
 reports/manufacturing/production_capacity.md       |  20 +-
 reports/manufacturing/scheduler_decisions.md       |   2 +-
 reports/performance/api_statistics.md              |  14 +-
 reports/performance/connector_performance.md       |  16 +-
 reports/performance/crawler_statistics.md          |   2 +-
 reports/performance/download_statistics.md         |   2 +-
 reports/performance/source_ranking.md              |   8 +-
 reports/performance/throughput.md                  |  12 +-
 reports/production/candidate_pipeline.md           |   8 +-
 reports/production/connector_summary.md            |  20 +-
 reports/production/document_pipeline.md            |   2 +-
 reports/production/evidence_trace.md               |  14 +-
 reports/production/production_trace.md             |  34 +--
 reports/production/publish_pipeline.md             |   2 +-
 reports/production/runtime_statistics.md           |  28 +--
 reports/reliability/git_worktree_trace.md          |  23 +++
 reports/reliability/writer_finalize.json           |   2 +-
 38 files changed, 560 insertions(+), 433 deletions(-)
```

## pre_acquire

- **time:** 2026-07-11T04:09:22Z
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

- **time:** 2026-07-11T04:19:12Z
- **dirty_count:** 42

### status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/daily_2026-07-11.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-11.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M domains/business_development/business_signal_library.csv
 M reports/discovery/provider_health.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/query_statistics.md
 M reports/discovery/reputation_scores.md
 M reports/manufacturing/factory_economics.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/knowledge_universe.md
 M reports/manufacturing/production_capacity.md
 M reports/manufacturing/scheduler_decisions.md
 M reports/performance/api_statistics.md
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
?? automation/learning/state/sessions/SES-20260711-D71612.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-14E554.json
?? reports/production/production_trace_SES-20260711-D71612.json
?? reports/production/sessions/SES-20260711-D71612/
```

### diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/daily_2026-07-11.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-11.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
domains/business_development/business_signal_library.csv
reports/discovery/provider_health.md
reports/discovery/provider_statistics.md
reports/discovery/query_statistics.md
reports/discovery/reputation_scores.md
reports/manufacturing/factory_economics.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/knowledge_universe.md
reports/manufacturing/production_capacity.md
reports/manufacturing/scheduler_decisions.md
reports/performance/api_statistics.md
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
 .../learning/state/acquisition_performance.json    |  58 +++---
 automation/learning/state/current_snapshot.json    |   6 +-
 automation/learning/state/daily_2026-07-11.json    |   4 +-
 automation/learning/state/discovery_analytics.json |  36 ++--
 automation/learning/state/learning_journal.jsonl   |  73 +++++++
 automation/learning/state/live_activity.json       |   6 +-
 automation/learning/state/manufacturing_state.json | 230 ++++++++++-----------
 automation/learning/state/production_trace.json    | 156 +++++++-------
 automation/learning/state/snapshot_2026-07-11.json |   6 +-
 automation/learning/state/source_health.json       |  30 +--
 automation/learning/state/source_performance.json  |  64 +++---
 automation/sessions/index.json                     |  30 ++-
 .../business_signal_library.csv                    |   3 +
 reports/discovery/provider_health.md               |   2 +-
 reports/discovery/provider_statistics.md           |  10 +-
 reports/discovery/query_statistics.md              |   8 +-
 reports/discovery/reputation_scores.md             |   8 +-
 reports/manufacturing/factory_economics.md         |  10 +-
 reports/manufacturing/growth_velocity.md           |  44 ++--
 reports/manufacturing/knowledge_gap.md             |   4 +-
 reports/manufacturing/knowledge_universe.md        |   2 +-
 reports/manufacturing/production_capacity.md       |  20 +-
 reports/manufacturing/scheduler_decisions.md       |   2 +-
 reports/performance/api_statistics.md              |  14 +-
 reports/performance/connector_performance.md       |  16 +-
 reports/performance/crawler_statistics.md          |   2 +-
 reports/performance/download_statistics.md         |   2 +-
 reports/performance/source_ranking.md              |   8 +-
 reports/performance/throughput.md                  |  10 +-
 reports/production/candidate_pipeline.md           |   8 +-
 reports/production/connector_summary.md            |  32 +--
 reports/production/document_pipeline.md            |   2 +-
 reports/production/evidence_trace.md               |  14 +-
 reports/production/production_trace.md             |  26 +--
 reports/production/publish_pipeline.md             |   2 +-
 reports/production/runtime_statistics.md           |  20 +-
 reports/reliability/git_worktree_trace.md          |  23 +++
 reports/reliability/writer_finalize.json           |   2 +-
 38 files changed, 560 insertions(+), 433 deletions(-)
```

## pre_acquire

- **time:** 2026-07-11T04:39:40Z
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

- **time:** 2026-07-11T04:49:45Z
- **dirty_count:** 37

### status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-11.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M reports/discovery/provider_health.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/query_statistics.md
 M reports/discovery/reputation_scores.md
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
?? automation/learning/state/sessions/SES-20260711-784A5F.jsonl
?? automation/queue/publish/CAND-7528E4183942.json
?? automation/queue/publish/CAND-D03DE2F0A439.json
?? automation/queue/publish/CAND-F04B1DEAECD0.json
?? automation/sessions/2026-07-11/SESSION-20260711-6BC023.json
?? reports/production/production_trace_SES-20260711-784A5F.json
?? reports/production/sessions/SES-20260711-784A5F/
```

### diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-11.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
reports/discovery/provider_health.md
reports/discovery/provider_statistics.md
reports/discovery/query_statistics.md
reports/discovery/reputation_scores.md
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
 .../learning/state/acquisition_performance.json    | 132 +++----
 automation/learning/state/current_snapshot.json    |   2 +-
 automation/learning/state/discovery_analytics.json |  76 ++--
 automation/learning/state/learning_journal.jsonl   |  63 ++++
 automation/learning/state/live_activity.json       |  10 +-
 automation/learning/state/production_trace.json    | 404 +++++++++------------
 automation/learning/state/snapshot_2026-07-11.json |   2 +-
 automation/learning/state/source_health.json       |   2 +-
 automation/learning/state/source_performance.json  |  62 ++--
 automation/sessions/index.json                     |  30 +-
 reports/discovery/provider_health.md               |   2 +-
 reports/discovery/provider_statistics.md           |  10 +-
 reports/discovery/query_statistics.md              |  46 +--
 reports/discovery/reputation_scores.md             |   8 +-
 reports/performance/api_statistics.md              |  14 +-
 reports/performance/cache_statistics.md            |   4 +-
 reports/performance/connector_performance.md       |  16 +-
 reports/performance/crawler_statistics.md          |  32 +-
 reports/performance/download_statistics.md         |  20 +-
 reports/performance/source_ranking.md              |   8 +-
 reports/performance/throughput.md                  |  14 +-
 reports/production/candidate_pipeline.md           |  10 +-
 reports/production/connector_summary.md            |  50 +--
 reports/production/document_pipeline.md            |  14 +-
 reports/production/evidence_trace.md               |  32 +-
 reports/production/production_trace.md             |  34 +-
 reports/production/publish_pipeline.md             |  14 +-
 reports/production/runtime_statistics.md           |  44 ++-
 reports/reliability/git_worktree_trace.md          |  23 ++
 reports/reliability/writer_finalize.json           |   2 +-
 30 files changed, 612 insertions(+), 568 deletions(-)
```

## pre_acquire

- **time:** 2026-07-11T08:05:10Z
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

- **time:** 2026-07-11T08:14:59Z
- **dirty_count:** 57

### status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/daily_2026-07-11.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-11.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M domains/business_development/business_signal_library.csv
 M reports/discovery/provider_health.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/query_statistics.md
 M reports/discovery/reputation_scores.md
 M reports/discovery/trusted_source_usage.md
 M reports/manufacturing/continuous_production.md
 M reports/manufacturing/factory_economics.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/knowledge_universe.md
 M reports/manufacturing/production_capacity.md
 M reports/manufacturing/scheduler_decisions.md
 M reports/performance/api_statistics.md
 M reports/performance/cache_statistics.md
 M reports/performance/connector_performance.md
 M reports/performance/connector_ranking.md
 M reports/performance/crawler_statistics.md
 M reports/performance/download_statistics.md
 M reports/performance/factory_capacity.md
 M reports/performance/pipeline_bottleneck.md
 M reports/performance/production_capacity.md
 M reports/performance/queue_efficiency.md
 M reports/performance/session_efficiency.md
 M reports/performance/source_efficiency.md
 M reports/performance/source_ranking.md
 M reports/performance/throughput.md
 M reports/performance/throughput_report.md
 M reports/performance/worker_utilization.md
 M reports/production/candidate_pipeline.md
 M reports/production/connector_summary.md
 M reports/production/document_pipeline.md
 M reports/production/evidence_trace.md
 M reports/production/production_trace.md
 M reports/production/publish_pipeline.md
 M reports/production/runtime_statistics.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-D73A0C.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-F61AC8.json
?? reports/performance/auto_publish.md
?? reports/performance/extraction_statistics.md
?? reports/performance/stage_timings.md
?? reports/production/production_trace_SES-20260711-D73A0C.json
?? reports/production/sessions/SES-20260711-D73A0C/
```

### diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/daily_2026-07-11.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-11.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
domains/business_development/business_signal_library.csv
reports/discovery/provider_health.md
reports/discovery/provider_statistics.md
reports/discovery/query_statistics.md
reports/discovery/reputation_scores.md
reports/discovery/trusted_source_usage.md
reports/manufacturing/continuous_production.md
reports/manufacturing/factory_economics.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/knowledge_universe.md
reports/manufacturing/production_capacity.md
reports/manufacturing/scheduler_decisions.md
reports/performance/api_statistics.md
reports/performance/cache_statistics.md
reports/performance/connector_performance.md
reports/performance/connector_ranking.md
reports/performance/crawler_statistics.md
reports/performance/download_statistics.md
reports/performance/factory_capacity.md
reports/performance/pipeline_bottleneck.md
reports/performance/production_capacity.md
reports/performance/queue_efficiency.md
reports/performance/session_efficiency.md
reports/performance/source_efficiency.md
reports/performance/source_ranking.md
reports/performance/throughput.md
reports/performance/throughput_report.md
reports/performance/worker_utilization.md
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
 .../learning/state/acquisition_performance.json    | 429 ++++++++---
 automation/learning/state/current_snapshot.json    |  53 +-
 automation/learning/state/daily_2026-07-11.json    |   4 +-
 automation/learning/state/discovery_analytics.json | 136 ++--
 automation/learning/state/learning_journal.jsonl   |  95 +++
 automation/learning/state/live_activity.json       |  10 +-
 automation/learning/state/manufacturing_state.json | 801 ++++++++++++---------
 automation/learning/state/production_trace.json    | 628 ++++++++++------
 automation/learning/state/snapshot_2026-07-11.json |  53 +-
 automation/learning/state/source_health.json       |  30 +-
 automation/learning/state/source_performance.json  |  64 +-
 automation/sessions/index.json                     |  30 +-
 .../business_signal_library.csv                    |   5 +
 reports/discovery/provider_health.md               |   2 +-
 reports/discovery/provider_statistics.md           |  14 +-
 reports/discovery/query_statistics.md              |  45 +-
 reports/discovery/reputation_scores.md             |  13 +-
 reports/discovery/trusted_source_usage.md          |  10 +-
 reports/manufacturing/continuous_production.md     |   2 +-
 reports/manufacturing/factory_economics.md         |  26 +-
 reports/manufacturing/growth_velocity.md           |  26 +-
 reports/manufacturing/knowledge_gap.md             |  16 +-
 reports/manufacturing/knowledge_universe.md        |  14 +-
 reports/manufacturing/production_capacity.md       |  12 +-
 reports/manufacturing/scheduler_decisions.md       |   8 +-
 reports/performance/api_statistics.md              |  14 +-
 reports/performance/cache_statistics.md            |   4 +-
 reports/performance/connector_performance.md       |  16 +-
 reports/performance/connector_ranking.md           |  16 +-
 reports/performance/crawler_statistics.md          |  56 +-
 reports/performance/download_statistics.md         |  25 +-
 reports/performance/factory_capacity.md            |  26 +-
 reports/performance/pipeline_bottleneck.md         |  52 +-
 reports/performance/production_capacity.md         |  16 +-
 reports/performance/queue_efficiency.md            |  23 +-
 reports/performance/session_efficiency.md          |  16 +-
 reports/performance/source_efficiency.md           |  16 +-
 reports/performance/source_ranking.md              |  13 +-
 reports/performance/throughput.md                  |  18 +-
 reports/performance/throughput_report.md           |  20 +-
 reports/performance/worker_utilization.md          |  14 +-
 reports/production/candidate_pipeline.md           |  12 +-
 reports/production/connector_summary.md            |  52 +-
 reports/production/document_pipeline.md            |  22 +-
 reports/production/evidence_trace.md               |  52 +-
 reports/production/production_trace.md             |  40 +-
 reports/production/publish_pipeline.md             |  20 +-
 reports/production/runtime_statistics.md           |  58 +-
 reports/reliability/git_worktree_trace.md          |  23 +
 reports/reliability/writer_finalize.json           |   4 +-
 50 files changed, 2005 insertions(+), 1149 deletions(-)
```

## pre_acquire

- **time:** 2026-07-11T08:22:27Z
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

- **time:** 2026-07-11T08:32:14Z
- **dirty_count:** 53

### status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/daily_2026-07-11.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-11.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M domains/business_development/business_signal_library.csv
 M reports/discovery/provider_health.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/query_statistics.md
 M reports/discovery/reputation_scores.md
 M reports/manufacturing/factory_economics.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/knowledge_universe.md
 M reports/manufacturing/production_capacity.md
 M reports/manufacturing/scheduler_decisions.md
 M reports/performance/api_statistics.md
 M reports/performance/connector_performance.md
 M reports/performance/connector_ranking.md
 M reports/performance/crawler_statistics.md
 M reports/performance/download_statistics.md
 M reports/performance/extraction_statistics.md
 M reports/performance/factory_capacity.md
 M reports/performance/pipeline_bottleneck.md
 M reports/performance/production_capacity.md
 M reports/performance/queue_efficiency.md
 M reports/performance/session_efficiency.md
 M reports/performance/source_efficiency.md
 M reports/performance/source_ranking.md
 M reports/performance/stage_timings.md
 M reports/performance/throughput.md
 M reports/performance/throughput_report.md
 M reports/performance/worker_utilization.md
 M reports/production/candidate_pipeline.md
 M reports/production/connector_summary.md
 M reports/production/document_pipeline.md
 M reports/production/evidence_trace.md
 M reports/production/production_trace.md
 M reports/production/publish_pipeline.md
 M reports/production/runtime_statistics.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-C77248.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-642972.json
?? reports/production/production_trace_SES-20260711-C77248.json
?? reports/production/sessions/SES-20260711-C77248/
```

### diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/daily_2026-07-11.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-11.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
domains/business_development/business_signal_library.csv
reports/discovery/provider_health.md
reports/discovery/provider_statistics.md
reports/discovery/query_statistics.md
reports/discovery/reputation_scores.md
reports/manufacturing/factory_economics.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/knowledge_universe.md
reports/manufacturing/production_capacity.md
reports/manufacturing/scheduler_decisions.md
reports/performance/api_statistics.md
reports/performance/connector_performance.md
reports/performance/connector_ranking.md
reports/performance/crawler_statistics.md
reports/performance/download_statistics.md
reports/performance/extraction_statistics.md
reports/performance/factory_capacity.md
reports/performance/pipeline_bottleneck.md
reports/performance/production_capacity.md
reports/performance/queue_efficiency.md
reports/performance/session_efficiency.md
reports/performance/source_efficiency.md
reports/performance/source_ranking.md
reports/performance/stage_timings.md
reports/performance/throughput.md
reports/performance/throughput_report.md
reports/performance/worker_utilization.md
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
 .../learning/state/acquisition_performance.json    | 138 ++++-----
 automation/learning/state/current_snapshot.json    |   6 +-
 automation/learning/state/daily_2026-07-11.json    |   4 +-
 automation/learning/state/discovery_analytics.json |  36 +--
 automation/learning/state/learning_journal.jsonl   |  95 ++++++
 automation/learning/state/live_activity.json       |   6 +-
 automation/learning/state/manufacturing_state.json | 332 ++++++++++-----------
 automation/learning/state/production_trace.json    | 252 ++++++++--------
 automation/learning/state/snapshot_2026-07-11.json |   6 +-
 automation/learning/state/source_health.json       |  30 +-
 automation/learning/state/source_performance.json  |  64 ++--
 automation/sessions/index.json                     |  30 +-
 .../business_signal_library.csv                    |   5 +
 reports/discovery/provider_health.md               |   2 +-
 reports/discovery/provider_statistics.md           |  10 +-
 reports/discovery/query_statistics.md              |   8 +-
 reports/discovery/reputation_scores.md             |   8 +-
 reports/manufacturing/factory_economics.md         |  24 +-
 reports/manufacturing/growth_velocity.md           |  50 ++--
 reports/manufacturing/knowledge_gap.md             |   4 +-
 reports/manufacturing/knowledge_universe.md        |   2 +-
 reports/manufacturing/production_capacity.md       |  20 +-
 reports/manufacturing/scheduler_decisions.md       |   2 +-
 reports/performance/api_statistics.md              |  14 +-
 reports/performance/connector_performance.md       |  16 +-
 reports/performance/connector_ranking.md           |  16 +-
 reports/performance/crawler_statistics.md          |  16 +-
 reports/performance/download_statistics.md         |   2 +-
 reports/performance/extraction_statistics.md       |  16 +-
 reports/performance/factory_capacity.md            |  16 +-
 reports/performance/pipeline_bottleneck.md         |  48 +--
 reports/performance/production_capacity.md         |  16 +-
 reports/performance/queue_efficiency.md            |   2 +-
 reports/performance/session_efficiency.md          |  12 +-
 reports/performance/source_efficiency.md           |  16 +-
 reports/performance/source_ranking.md              |   8 +-
 reports/performance/stage_timings.md               |  12 +-
 reports/performance/throughput.md                  |  10 +-
 reports/performance/throughput_report.md           |  12 +-
 reports/performance/worker_utilization.md          |  10 +-
 reports/production/candidate_pipeline.md           |  12 +-
 reports/production/connector_summary.md            |  42 +--
 reports/production/document_pipeline.md            |   2 +-
 reports/production/evidence_trace.md               |  22 +-
 reports/production/production_trace.md             |  30 +-
 reports/production/publish_pipeline.md             |   2 +-
 reports/production/runtime_statistics.md           |  24 +-
 reports/reliability/git_worktree_trace.md          |  23 ++
 reports/reliability/writer_finalize.json           |   2 +-
 49 files changed, 840 insertions(+), 695 deletions(-)
```

## pre_acquire

- **time:** 2026-07-11T10:01:19Z
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

- **time:** 2026-07-11T10:24:16Z
- **dirty_count:** 72

### status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/daily_2026-07-11.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-11.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M domains/business_development/business_signal_library.csv
 M reports/diagnostics/candidate_lifecycle.md
 M reports/diagnostics/candidate_root_cause.md
 M reports/diagnostics/dataset_validation_summary.md
 M reports/diagnostics/document_trace.md
 M reports/diagnostics/extraction_trace.md
 M reports/diagnostics/false_negative_analysis.md
 M reports/diagnostics/integrity_trace.md
 M reports/diagnostics/knowledge_gap_trace.md
 M reports/diagnostics/mission_trace.md
 M reports/diagnostics/publish_trace.md
 M reports/diagnostics/publisher_trace.md
 M reports/diagnostics/root_cause_analysis.md
 M reports/diagnostics/rule_impact.md
 M reports/diagnostics/scheduler_trace.md
 M reports/diagnostics/session_trace.md
 M reports/diagnostics/source_trace.md
 M reports/diagnostics/validation_statistics.md
 M reports/diagnostics/validation_trace.md
 M reports/discovery/provider_health.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/query_statistics.md
 M reports/discovery/reputation_scores.md
 M reports/manufacturing/factory_economics.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/knowledge_universe.md
 M reports/manufacturing/production_capacity.md
 M reports/manufacturing/scheduler_decisions.md
 M reports/performance/api_statistics.md
 M reports/performance/cache_statistics.md
 M reports/performance/connector_performance.md
 M reports/performance/connector_ranking.md
 M reports/performance/crawler_statistics.md
 M reports/performance/download_statistics.md
 M reports/performance/extraction_statistics.md
 M reports/performance/factory_capacity.md
 M reports/performance/pipeline_bottleneck.md
 M reports/performance/production_capacity.md
 M reports/performance/queue_efficiency.md
 M reports/performance/session_efficiency.md
 M reports/performance/source_efficiency.md
 M reports/performance/source_ranking.md
 M reports/performance/stage_timings.md
 M reports/performance/throughput.md
 M reports/performance/throughput_report.md
 M reports/performance/worker_utilization.md
 M reports/production/candidate_pipeline.md
 M reports/production/connector_summary.md
 M reports/production/document_pipeline.md
 M reports/production/evidence_trace.md
 M reports/production/production_trace.md
 M reports/production/publish_pipeline.md
 M reports/production/runtime_statistics.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-5BAD14.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-C6CDF9.json
?? reports/production/production_trace_SES-20260711-5BAD14.json
?? reports/production/sessions/SES-20260711-5BAD14/
```

### diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/daily_2026-07-11.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-11.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
domains/business_development/business_signal_library.csv
reports/diagnostics/candidate_lifecycle.md
reports/diagnostics/candidate_root_cause.md
reports/diagnostics/dataset_validation_summary.md
reports/diagnostics/document_trace.md
reports/diagnostics/extraction_trace.md
reports/diagnostics/false_negative_analysis.md
reports/diagnostics/integrity_trace.md
reports/diagnostics/knowledge_gap_trace.md
reports/diagnostics/mission_trace.md
reports/diagnostics/publish_trace.md
reports/diagnostics/publisher_trace.md
reports/diagnostics/root_cause_analysis.md
reports/diagnostics/rule_impact.md
reports/diagnostics/scheduler_trace.md
reports/diagnostics/session_trace.md
reports/diagnostics/source_trace.md
reports/diagnostics/validation_statistics.md
reports/diagnostics/validation_trace.md
reports/discovery/provider_health.md
reports/discovery/provider_statistics.md
reports/discovery/query_statistics.md
reports/discovery/reputation_scores.md
reports/manufacturing/factory_economics.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/knowledge_universe.md
reports/manufacturing/production_capacity.md
reports/manufacturing/scheduler_decisions.md
reports/performance/api_statistics.md
reports/performance/cache_statistics.md
reports/performance/connector_performance.md
reports/performance/connector_ranking.md
reports/performance/crawler_statistics.md
reports/performance/download_statistics.md
reports/performance/extraction_statistics.md
reports/performance/factory_capacity.md
reports/performance/pipeline_bottleneck.md
reports/performance/production_capacity.md
reports/performance/queue_efficiency.md
reports/performance/session_efficiency.md
reports/performance/source_efficiency.md
reports/performance/source_ranking.md
reports/performance/stage_timings.md
reports/performance/throughput.md
reports/performance/throughput_report.md
reports/performance/worker_utilization.md
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
 .../learning/state/acquisition_performance.json    | 348 +++++---
 automation/learning/state/current_snapshot.json    |   6 +-
 automation/learning/state/daily_2026-07-11.json    |   4 +-
 automation/learning/state/discovery_analytics.json | 167 +++-
 automation/learning/state/learning_journal.jsonl   | 147 ++++
 automation/learning/state/live_activity.json       |  10 +-
 automation/learning/state/manufacturing_state.json | 333 ++++----
 automation/learning/state/production_trace.json    | 906 ++++++++++++++-------
 automation/learning/state/snapshot_2026-07-11.json |   6 +-
 automation/learning/state/source_health.json       |  44 +-
 automation/learning/state/source_performance.json  |  68 +-
 automation/sessions/index.json                     |  30 +-
 .../business_signal_library.csv                    |   5 +
 reports/diagnostics/candidate_lifecycle.md         |  18 +-
 reports/diagnostics/candidate_root_cause.md        |  46 +-
 reports/diagnostics/dataset_validation_summary.md  |   4 +-
 reports/diagnostics/document_trace.md              |  42 +-
 reports/diagnostics/extraction_trace.md            |  10 +-
 reports/diagnostics/false_negative_analysis.md     |  12 +-
 reports/diagnostics/integrity_trace.md             | 194 ++++-
 reports/diagnostics/knowledge_gap_trace.md         |  16 +-
 reports/diagnostics/mission_trace.md               |  36 +-
 reports/diagnostics/publish_trace.md               |  18 +-
 reports/diagnostics/publisher_trace.md             |  10 +-
 reports/diagnostics/root_cause_analysis.md         |  50 +-
 reports/diagnostics/rule_impact.md                 |   6 +-
 reports/diagnostics/scheduler_trace.md             |  50 +-
 reports/diagnostics/session_trace.md               |  56 +-
 reports/diagnostics/source_trace.md                |  30 +-
 reports/diagnostics/validation_statistics.md       |   8 +-
 reports/diagnostics/validation_trace.md            | 118 ++-
 reports/discovery/provider_health.md               |   2 +-
 reports/discovery/provider_statistics.md           |  14 +-
 reports/discovery/query_statistics.md              |  46 +-
 reports/discovery/reputation_scores.md             |  17 +-
 reports/manufacturing/factory_economics.md         |  28 +-
 reports/manufacturing/growth_velocity.md           |  48 +-
 reports/manufacturing/knowledge_gap.md             |   4 +-
 reports/manufacturing/knowledge_universe.md        |   2 +-
 reports/manufacturing/production_capacity.md       |  20 +-
 reports/manufacturing/scheduler_decisions.md       |   2 +-
 reports/performance/api_statistics.md              |  14 +-
 reports/performance/cache_statistics.md            |   4 +-
 reports/performance/connector_performance.md       |  16 +-
 reports/performance/connector_ranking.md           |  16 +-
 reports/performance/crawler_statistics.md          |  60 +-
 reports/performance/download_statistics.md         |  28 +-
 reports/performance/extraction_statistics.md       |  28 +-
 reports/performance/factory_capacity.md            |  18 +-
 reports/performance/pipeline_bottleneck.md         |  48 +-
 reports/performance/production_capacity.md         |  16 +-
 reports/performance/queue_efficiency.md            |   4 +-
 reports/performance/session_efficiency.md          |  12 +-
 reports/performance/source_efficiency.md           |  16 +-
 reports/performance/source_ranking.md              |  12 +-
 reports/performance/stage_timings.md               |  12 +-
 reports/performance/throughput.md                  |  16 +-
 reports/performance/throughput_report.md           |  18 +-
 reports/performance/worker_utilization.md          |  14 +-
 reports/production/candidate_pipeline.md           |  12 +-
 reports/production/connector_summary.md            |  76 +-
 reports/production/document_pipeline.md            |  44 +-
 reports/production/evidence_trace.md               |  62 +-
 reports/production/production_trace.md             |  38 +-
 reports/production/publish_pipeline.md             |   2 +-
 reports/production/runtime_statistics.md           |  38 +-
 reports/reliability/git_worktree_trace.md          |  23 +
 reports/reliability/writer_finalize.json           |   4 +-
 68 files changed, 2282 insertions(+), 1350 deletions(-)
```

## pre_acquire

- **time:** 2026-07-11T11:26:39Z
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

- **time:** 2026-07-11T11:49:34Z
- **dirty_count:** 72

### status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/daily_2026-07-11.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-11.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M domains/business_development/business_signal_library.csv
 M reports/diagnostics/candidate_lifecycle.md
 M reports/diagnostics/candidate_root_cause.md
 M reports/diagnostics/dataset_validation_summary.md
 M reports/diagnostics/document_trace.md
 M reports/diagnostics/extraction_trace.md
 M reports/diagnostics/false_negative_analysis.md
 M reports/diagnostics/integrity_trace.md
 M reports/diagnostics/knowledge_gap_trace.md
 M reports/diagnostics/mission_trace.md
 M reports/diagnostics/publish_trace.md
 M reports/diagnostics/publisher_trace.md
 M reports/diagnostics/root_cause_analysis.md
 M reports/diagnostics/rule_impact.md
 M reports/diagnostics/scheduler_trace.md
 M reports/diagnostics/session_trace.md
 M reports/diagnostics/source_trace.md
 M reports/diagnostics/validation_statistics.md
 M reports/diagnostics/validation_trace.md
 M reports/discovery/provider_health.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/query_statistics.md
 M reports/discovery/reputation_scores.md
 M reports/manufacturing/factory_economics.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/knowledge_universe.md
 M reports/manufacturing/production_capacity.md
 M reports/manufacturing/scheduler_decisions.md
 M reports/performance/api_statistics.md
 M reports/performance/cache_statistics.md
 M reports/performance/connector_performance.md
 M reports/performance/connector_ranking.md
 M reports/performance/crawler_statistics.md
 M reports/performance/download_statistics.md
 M reports/performance/extraction_statistics.md
 M reports/performance/factory_capacity.md
 M reports/performance/pipeline_bottleneck.md
 M reports/performance/production_capacity.md
 M reports/performance/queue_efficiency.md
 M reports/performance/session_efficiency.md
 M reports/performance/source_efficiency.md
 M reports/performance/source_ranking.md
 M reports/performance/stage_timings.md
 M reports/performance/throughput.md
 M reports/performance/throughput_report.md
 M reports/performance/worker_utilization.md
 M reports/production/candidate_pipeline.md
 M reports/production/connector_summary.md
 M reports/production/document_pipeline.md
 M reports/production/evidence_trace.md
 M reports/production/production_trace.md
 M reports/production/publish_pipeline.md
 M reports/production/runtime_statistics.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-DE29FE.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-FB328B.json
?? reports/production/production_trace_SES-20260711-DE29FE.json
?? reports/production/sessions/SES-20260711-DE29FE/
```

### diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/daily_2026-07-11.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-11.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
domains/business_development/business_signal_library.csv
reports/diagnostics/candidate_lifecycle.md
reports/diagnostics/candidate_root_cause.md
reports/diagnostics/dataset_validation_summary.md
reports/diagnostics/document_trace.md
reports/diagnostics/extraction_trace.md
reports/diagnostics/false_negative_analysis.md
reports/diagnostics/integrity_trace.md
reports/diagnostics/knowledge_gap_trace.md
reports/diagnostics/mission_trace.md
reports/diagnostics/publish_trace.md
reports/diagnostics/publisher_trace.md
reports/diagnostics/root_cause_analysis.md
reports/diagnostics/rule_impact.md
reports/diagnostics/scheduler_trace.md
reports/diagnostics/session_trace.md
reports/diagnostics/source_trace.md
reports/diagnostics/validation_statistics.md
reports/diagnostics/validation_trace.md
reports/discovery/provider_health.md
reports/discovery/provider_statistics.md
reports/discovery/query_statistics.md
reports/discovery/reputation_scores.md
reports/manufacturing/factory_economics.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/knowledge_universe.md
reports/manufacturing/production_capacity.md
reports/manufacturing/scheduler_decisions.md
reports/performance/api_statistics.md
reports/performance/cache_statistics.md
reports/performance/connector_performance.md
reports/performance/connector_ranking.md
reports/performance/crawler_statistics.md
reports/performance/download_statistics.md
reports/performance/extraction_statistics.md
reports/performance/factory_capacity.md
reports/performance/pipeline_bottleneck.md
reports/performance/production_capacity.md
reports/performance/queue_efficiency.md
reports/performance/session_efficiency.md
reports/performance/source_efficiency.md
reports/performance/source_ranking.md
reports/performance/stage_timings.md
reports/performance/throughput.md
reports/performance/throughput_report.md
reports/performance/worker_utilization.md
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
 .../learning/state/acquisition_performance.json    | 270 ++++++------
 automation/learning/state/current_snapshot.json    |   6 +-
 automation/learning/state/daily_2026-07-11.json    |   4 +-
 automation/learning/state/discovery_analytics.json |  78 ++--
 automation/learning/state/learning_journal.jsonl   | 145 +++++++
 automation/learning/state/live_activity.json       |   8 +-
 automation/learning/state/manufacturing_state.json | 464 ++++++++++-----------
 automation/learning/state/production_trace.json    | 424 +++++++++----------
 automation/learning/state/snapshot_2026-07-11.json |   6 +-
 automation/learning/state/source_health.json       |  44 +-
 automation/learning/state/source_performance.json  |  82 ++--
 automation/sessions/index.json                     |  30 +-
 .../business_signal_library.csv                    |   5 +
 reports/diagnostics/candidate_lifecycle.md         |  16 +-
 reports/diagnostics/candidate_root_cause.md        |  32 +-
 reports/diagnostics/dataset_validation_summary.md  |   4 +-
 reports/diagnostics/document_trace.md              |  14 +-
 reports/diagnostics/extraction_trace.md            |  12 +-
 reports/diagnostics/false_negative_analysis.md     |  12 +-
 reports/diagnostics/integrity_trace.md             | 104 ++---
 reports/diagnostics/knowledge_gap_trace.md         |  18 +-
 reports/diagnostics/mission_trace.md               |  14 +-
 reports/diagnostics/publish_trace.md               |  12 +-
 reports/diagnostics/publisher_trace.md             |  12 +-
 reports/diagnostics/root_cause_analysis.md         |  14 +-
 reports/diagnostics/rule_impact.md                 |   2 +-
 reports/diagnostics/scheduler_trace.md             |  18 +-
 reports/diagnostics/session_trace.md               |  28 +-
 reports/diagnostics/source_trace.md                |  30 +-
 reports/diagnostics/validation_statistics.md       |   2 +-
 reports/diagnostics/validation_trace.md            | 116 +++---
 reports/discovery/provider_health.md               |   2 +-
 reports/discovery/provider_statistics.md           |  10 +-
 reports/discovery/query_statistics.md              |  14 +-
 reports/discovery/reputation_scores.md             |   8 +-
 reports/manufacturing/factory_economics.md         |  28 +-
 reports/manufacturing/growth_velocity.md           |  42 +-
 reports/manufacturing/knowledge_gap.md             |  18 +-
 reports/manufacturing/knowledge_universe.md        |  16 +-
 reports/manufacturing/production_capacity.md       |  20 +-
 reports/manufacturing/scheduler_decisions.md       |  10 +-
 reports/performance/api_statistics.md              |  14 +-
 reports/performance/cache_statistics.md            |   4 +-
 reports/performance/connector_performance.md       |  16 +-
 reports/performance/connector_ranking.md           |  16 +-
 reports/performance/crawler_statistics.md          |  40 +-
 reports/performance/download_statistics.md         |  16 +-
 reports/performance/extraction_statistics.md       |  26 +-
 reports/performance/factory_capacity.md            |  18 +-
 reports/performance/pipeline_bottleneck.md         |  50 +--
 reports/performance/production_capacity.md         |  16 +-
 reports/performance/queue_efficiency.md            |   4 +-
 reports/performance/session_efficiency.md          |  14 +-
 reports/performance/source_efficiency.md           |  16 +-
 reports/performance/source_ranking.md              |   8 +-
 reports/performance/stage_timings.md               |  12 +-
 reports/performance/throughput.md                  |  14 +-
 reports/performance/throughput_report.md           |  18 +-
 reports/performance/worker_utilization.md          |  10 +-
 reports/production/candidate_pipeline.md           |  12 +-
 reports/production/connector_summary.md            |  44 +-
 reports/production/document_pipeline.md            |  14 +-
 reports/production/evidence_trace.md               |  24 +-
 reports/production/production_trace.md             |  32 +-
 reports/production/publish_pipeline.md             |   2 +-
 reports/production/runtime_statistics.md           |  32 +-
 reports/reliability/git_worktree_trace.md          |  23 +
 reports/reliability/writer_finalize.json           |   2 +-
 68 files changed, 1426 insertions(+), 1265 deletions(-)
```

## pre_acquire

- **time:** 2026-07-11T12:11:55Z
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

- **time:** 2026-07-11T12:22:38Z
- **dirty_count:** 83

### status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-11.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M reports/diagnostics/candidate_lifecycle.md
 M reports/diagnostics/candidate_root_cause.md
 M reports/diagnostics/dataset_validation_summary.md
 M reports/diagnostics/document_trace.md
 M reports/diagnostics/extraction_trace.md
 M reports/diagnostics/false_negative_analysis.md
 M reports/diagnostics/integrity_trace.md
 M reports/diagnostics/knowledge_gap_trace.md
 M reports/diagnostics/mission_trace.md
 M reports/diagnostics/publish_trace.md
 M reports/diagnostics/publisher_trace.md
 M reports/diagnostics/root_cause_analysis.md
 M reports/diagnostics/rule_impact.md
 M reports/diagnostics/scheduler_trace.md
 M reports/diagnostics/session_trace.md
 M reports/diagnostics/source_trace.md
 M reports/diagnostics/validation_statistics.md
 M reports/diagnostics/validation_trace.md
 M reports/discovery/accepted_urls.md
 M reports/discovery/adaptive_budget.md
 M reports/discovery/discovery_capacity.md
 M reports/discovery/environment_audit.md
 M reports/discovery/hard_limit_audit.md
 M reports/discovery/provider_audit.md
 M reports/discovery/provider_exhaustion.md
 M reports/discovery/provider_health.md
 M reports/discovery/provider_ranking.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/provider_yield.md
 M reports/discovery/query_statistics.md
 M reports/discovery/rejected_urls.md
 M reports/discovery/reputation_scores.md
 M reports/discovery/throughput_analysis.md
 M reports/discovery/trusted_source_usage.md
 M reports/manufacturing/factory_economics.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/knowledge_universe.md
 M reports/manufacturing/production_capacity.md
 M reports/manufacturing/scheduler_decisions.md
 M reports/performance/api_statistics.md
 M reports/performance/auto_publish.md
 M reports/performance/cache_statistics.md
 M reports/performance/connector_performance.md
 M reports/performance/connector_ranking.md
 M reports/performance/crawler_statistics.md
 M reports/performance/download_statistics.md
 M reports/performance/extraction_statistics.md
 M reports/performance/factory_capacity.md
 M reports/performance/pipeline_bottleneck.md
 M reports/performance/production_capacity.md
 M reports/performance/queue_efficiency.md
 M reports/performance/session_efficiency.md
 M reports/performance/source_efficiency.md
 M reports/performance/source_ranking.md
 M reports/performance/stage_timings.md
 M reports/performance/throughput.md
 M reports/performance/throughput_report.md
 M reports/performance/worker_utilization.md
 M reports/production/candidate_pipeline.md
 M reports/production/connector_summary.md
 M reports/production/document_pipeline.md
 M reports/production/evidence_trace.md
 M reports/production/production_trace.md
 M reports/production/publish_pipeline.md
 M reports/production/runtime_statistics.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-D7A3F9.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-B8F6DE.json
?? reports/production/production_trace_SES-20260711-D7A3F9.json
?? reports/production/sessions/SES-20260711-D7A3F9/
```

### diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-11.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
reports/diagnostics/candidate_lifecycle.md
reports/diagnostics/candidate_root_cause.md
reports/diagnostics/dataset_validation_summary.md
reports/diagnostics/document_trace.md
reports/diagnostics/extraction_trace.md
reports/diagnostics/false_negative_analysis.md
reports/diagnostics/integrity_trace.md
reports/diagnostics/knowledge_gap_trace.md
reports/diagnostics/mission_trace.md
reports/diagnostics/publish_trace.md
reports/diagnostics/publisher_trace.md
reports/diagnostics/root_cause_analysis.md
reports/diagnostics/rule_impact.md
reports/diagnostics/scheduler_trace.md
reports/diagnostics/session_trace.md
reports/diagnostics/source_trace.md
reports/diagnostics/validation_statistics.md
reports/diagnostics/validation_trace.md
reports/discovery/accepted_urls.md
reports/discovery/adaptive_budget.md
reports/discovery/discovery_capacity.md
reports/discovery/environment_audit.md
reports/discovery/hard_limit_audit.md
reports/discovery/provider_audit.md
reports/discovery/provider_exhaustion.md
reports/discovery/provider_health.md
reports/discovery/provider_ranking.md
reports/discovery/provider_statistics.md
reports/discovery/provider_yield.md
reports/discovery/query_statistics.md
reports/discovery/rejected_urls.md
reports/discovery/reputation_scores.md
reports/discovery/throughput_analysis.md
reports/discovery/trusted_source_usage.md
reports/manufacturing/factory_economics.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/knowledge_universe.md
reports/manufacturing/production_capacity.md
reports/manufacturing/scheduler_decisions.md
reports/performance/api_statistics.md
reports/performance/auto_publish.md
reports/performance/cache_statistics.md
reports/performance/connector_performance.md
reports/performance/connector_ranking.md
reports/performance/crawler_statistics.md
reports/performance/download_statistics.md
reports/performance/extraction_statistics.md
reports/performance/factory_capacity.md
reports/performance/pipeline_bottleneck.md
reports/performance/production_capacity.md
reports/performance/queue_efficiency.md
reports/performance/session_efficiency.md
reports/performance/source_efficiency.md
reports/performance/source_ranking.md
reports/performance/stage_timings.md
reports/performance/throughput.md
reports/performance/throughput_report.md
reports/performance/worker_utilization.md
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
 .../learning/state/acquisition_performance.json    |  586 ++--
 automation/learning/state/current_snapshot.json    |    2 +-
 automation/learning/state/discovery_analytics.json | 2912 +++++++++-----------
 automation/learning/state/learning_journal.jsonl   |  344 +++
 automation/learning/state/live_activity.json       |   10 +-
 automation/learning/state/manufacturing_state.json |  408 ++-
 automation/learning/state/production_trace.json    | 1699 ++++++++----
 automation/learning/state/snapshot_2026-07-11.json |    2 +-
 automation/learning/state/source_health.json       |    2 +-
 automation/learning/state/source_performance.json  |   66 +-
 automation/sessions/index.json                     |   30 +-
 reports/diagnostics/candidate_lifecycle.md         |   17 +-
 reports/diagnostics/candidate_root_cause.md        |   42 +-
 reports/diagnostics/dataset_validation_summary.md  |    4 +-
 reports/diagnostics/document_trace.md              |   96 +-
 reports/diagnostics/extraction_trace.md            |    9 +-
 reports/diagnostics/false_negative_analysis.md     |   10 +-
 reports/diagnostics/integrity_trace.md             |  277 +-
 reports/diagnostics/knowledge_gap_trace.md         |   16 +-
 reports/diagnostics/mission_trace.md               |   14 +-
 reports/diagnostics/publish_trace.md               |   17 +-
 reports/diagnostics/publisher_trace.md             |    9 +-
 reports/diagnostics/root_cause_analysis.md         |   46 +-
 reports/diagnostics/rule_impact.md                 |    5 +-
 reports/diagnostics/scheduler_trace.md             |   18 +-
 reports/diagnostics/session_trace.md               |   54 +-
 reports/diagnostics/source_trace.md                |   30 +-
 reports/diagnostics/validation_statistics.md       |   10 +-
 reports/diagnostics/validation_trace.md            |  140 +-
 reports/discovery/accepted_urls.md                 |  370 +--
 reports/discovery/adaptive_budget.md               |   30 +-
 reports/discovery/discovery_capacity.md            |   14 +-
 reports/discovery/environment_audit.md             |   10 +-
 reports/discovery/hard_limit_audit.md              |  131 +-
 reports/discovery/provider_audit.md                |   24 +-
 reports/discovery/provider_exhaustion.md           |   16 +-
 reports/discovery/provider_health.md               |    4 +-
 reports/discovery/provider_ranking.md              |   26 +-
 reports/discovery/provider_statistics.md           |   30 +-
 reports/discovery/provider_yield.md                |   26 +-
 reports/discovery/query_statistics.md              |  162 +-
 reports/discovery/rejected_urls.md                 |  110 +-
 reports/discovery/reputation_scores.md             |   10 +-
 reports/discovery/throughput_analysis.md           |   18 +-
 reports/discovery/trusted_source_usage.md          |   30 +-
 reports/manufacturing/factory_economics.md         |   22 +-
 reports/manufacturing/growth_velocity.md           |   36 +-
 reports/manufacturing/knowledge_gap.md             |   16 +-
 reports/manufacturing/knowledge_universe.md        |   14 +-
 reports/manufacturing/production_capacity.md       |   14 +-
 reports/manufacturing/scheduler_decisions.md       |    8 +-
 reports/performance/api_statistics.md              |   14 +-
 reports/performance/auto_publish.md                |    8 +-
 reports/performance/cache_statistics.md            |    4 +-
 reports/performance/connector_performance.md       |   16 +-
 reports/performance/connector_ranking.md           |   16 +-
 reports/performance/crawler_statistics.md          |   65 +-
 reports/performance/download_statistics.md         |   30 +-
 reports/performance/extraction_statistics.md       |   35 +-
 reports/performance/factory_capacity.md            |   24 +-
 reports/performance/pipeline_bottleneck.md         |   48 +-
 reports/performance/production_capacity.md         |   16 +-
 reports/performance/queue_efficiency.md            |   14 +-
 reports/performance/session_efficiency.md          |   12 +-
 reports/performance/source_efficiency.md           |   16 +-
 reports/performance/source_ranking.md              |   28 +-
 reports/performance/stage_timings.md               |   12 +-
 reports/performance/throughput.md                  |   18 +-
 reports/performance/throughput_report.md           |   20 +-
 reports/performance/worker_utilization.md          |   14 +-
 reports/production/candidate_pipeline.md           |   19 +-
 reports/production/connector_summary.md            |   70 +-
 reports/production/document_pipeline.md            |   92 +-
 reports/production/evidence_trace.md               |   52 +-
 reports/production/production_trace.md             |   40 +-
 reports/production/publish_pipeline.md             |   20 +-
 reports/production/runtime_statistics.md           |   58 +-
 reports/reliability/git_worktree_trace.md          |   23 +
 reports/reliability/writer_finalize.json           |    4 +-
 79 files changed, 4623 insertions(+), 4161 deletions(-)
```

## pre_acquire

- **time:** 2026-07-11T12:32:46Z
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

- **time:** 2026-07-11T13:10:45Z
- **dirty_count:** 88

### status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/daily_2026-07-11.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-11.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M domains/business_development/industry_library.csv
 M reports/diagnostics/candidate_lifecycle.md
 M reports/diagnostics/candidate_root_cause.md
 M reports/diagnostics/dataset_validation_summary.md
 M reports/diagnostics/document_trace.md
 M reports/diagnostics/extraction_trace.md
 M reports/diagnostics/false_negative_analysis.md
 M reports/diagnostics/integrity_trace.md
 M reports/diagnostics/knowledge_gap_trace.md
 M reports/diagnostics/mission_trace.md
 M reports/diagnostics/publish_trace.md
 M reports/diagnostics/publisher_trace.md
 M reports/diagnostics/root_cause_analysis.md
 M reports/diagnostics/rule_impact.md
 M reports/diagnostics/scheduler_trace.md
 M reports/diagnostics/session_trace.md
 M reports/diagnostics/source_trace.md
 M reports/diagnostics/validation_statistics.md
 M reports/diagnostics/validation_trace.md
 M reports/discovery/accepted_urls.md
 M reports/discovery/adaptive_budget.md
 M reports/discovery/discovery_capacity.md
 M reports/discovery/environment_audit.md
 M reports/discovery/hard_limit_audit.md
 M reports/discovery/provider_audit.md
 M reports/discovery/provider_exhaustion.md
 M reports/discovery/provider_health.md
 M reports/discovery/provider_ranking.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/provider_yield.md
 M reports/discovery/query_statistics.md
 M reports/discovery/rejected_urls.md
 M reports/discovery/reputation_scores.md
 M reports/discovery/throughput_analysis.md
 M reports/discovery/trusted_source_usage.md
 M reports/enterprise/coverage_by_function.md
 M reports/enterprise/enterprise_state.json
 M reports/enterprise/production_distribution.md
 M reports/manufacturing/factory_economics.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/knowledge_universe.md
 M reports/manufacturing/production_capacity.md
 M reports/manufacturing/scheduler_decisions.md
 M reports/performance/api_statistics.md
 M reports/performance/auto_publish.md
 M reports/performance/cache_statistics.md
 M reports/performance/connector_performance.md
 M reports/performance/connector_ranking.md
 M reports/performance/crawler_statistics.md
 M reports/performance/download_statistics.md
 M reports/performance/extraction_statistics.md
 M reports/performance/factory_capacity.md
 M reports/performance/pipeline_bottleneck.md
 M reports/performance/production_capacity.md
 M reports/performance/queue_efficiency.md
 M reports/performance/session_efficiency.md
 M reports/performance/source_efficiency.md
 M reports/performance/source_ranking.md
 M reports/performance/stage_timings.md
 M reports/performance/throughput.md
 M reports/performance/throughput_report.md
 M reports/performance/worker_utilization.md
 M reports/production/candidate_pipeline.md
 M reports/production/connector_summary.md
 M reports/production/document_pipeline.md
 M reports/production/evidence_trace.md
 M reports/production/production_trace.md
 M reports/production/publish_pipeline.md
 M reports/production/runtime_statistics.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-607B7A.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-CF5FA7.json
?? reports/production/production_trace_SES-20260711-607B7A.json
?? reports/production/sessions/SES-20260711-607B7A/
```

### diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/daily_2026-07-11.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-11.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
domains/business_development/industry_library.csv
reports/diagnostics/candidate_lifecycle.md
reports/diagnostics/candidate_root_cause.md
reports/diagnostics/dataset_validation_summary.md
reports/diagnostics/document_trace.md
reports/diagnostics/extraction_trace.md
reports/diagnostics/false_negative_analysis.md
reports/diagnostics/integrity_trace.md
reports/diagnostics/knowledge_gap_trace.md
reports/diagnostics/mission_trace.md
reports/diagnostics/publish_trace.md
reports/diagnostics/publisher_trace.md
reports/diagnostics/root_cause_analysis.md
reports/diagnostics/rule_impact.md
reports/diagnostics/scheduler_trace.md
reports/diagnostics/session_trace.md
reports/diagnostics/source_trace.md
reports/diagnostics/validation_statistics.md
reports/diagnostics/validation_trace.md
reports/discovery/accepted_urls.md
reports/discovery/adaptive_budget.md
reports/discovery/discovery_capacity.md
reports/discovery/environment_audit.md
reports/discovery/hard_limit_audit.md
reports/discovery/provider_audit.md
reports/discovery/provider_exhaustion.md
reports/discovery/provider_health.md
reports/discovery/provider_ranking.md
reports/discovery/provider_statistics.md
reports/discovery/provider_yield.md
reports/discovery/query_statistics.md
reports/discovery/rejected_urls.md
reports/discovery/reputation_scores.md
reports/discovery/throughput_analysis.md
reports/discovery/trusted_source_usage.md
reports/enterprise/coverage_by_function.md
reports/enterprise/enterprise_state.json
reports/enterprise/production_distribution.md
reports/manufacturing/factory_economics.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/knowledge_universe.md
reports/manufacturing/production_capacity.md
reports/manufacturing/scheduler_decisions.md
reports/performance/api_statistics.md
reports/performance/auto_publish.md
reports/performance/cache_statistics.md
reports/performance/connector_performance.md
reports/performance/connector_ranking.md
reports/performance/crawler_statistics.md
reports/performance/download_statistics.md
reports/performance/extraction_statistics.md
reports/performance/factory_capacity.md
reports/performance/pipeline_bottleneck.md
reports/performance/production_capacity.md
reports/performance/queue_efficiency.md
reports/performance/session_efficiency.md
reports/performance/source_efficiency.md
reports/performance/source_ranking.md
reports/performance/stage_timings.md
reports/performance/throughput.md
reports/performance/throughput_report.md
reports/performance/worker_utilization.md
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
 .../learning/state/acquisition_performance.json    |  388 +-
 automation/learning/state/current_snapshot.json    |    6 +-
 automation/learning/state/daily_2026-07-11.json    |    4 +-
 automation/learning/state/discovery_analytics.json | 2690 ++++++----
 automation/learning/state/learning_journal.jsonl   | 1304 +++++
 automation/learning/state/live_activity.json       |   10 +-
 automation/learning/state/manufacturing_state.json |  460 +-
 automation/learning/state/production_trace.json    | 5452 +++++++++++++++++---
 automation/learning/state/snapshot_2026-07-11.json |    6 +-
 automation/learning/state/source_health.json       |  352 +-
 automation/learning/state/source_performance.json  |   72 +-
 automation/sessions/index.json                     |   30 +-
 domains/business_development/industry_library.csv  |    2 +
 reports/diagnostics/candidate_lifecycle.md         |   12 +-
 reports/diagnostics/candidate_root_cause.md        |   32 +-
 reports/diagnostics/dataset_validation_summary.md  |    4 +-
 reports/diagnostics/document_trace.md              |  348 +-
 reports/diagnostics/extraction_trace.md            |    6 +-
 reports/diagnostics/false_negative_analysis.md     |    7 +-
 reports/diagnostics/integrity_trace.md             |   72 +-
 reports/diagnostics/knowledge_gap_trace.md         |   16 +-
 reports/diagnostics/mission_trace.md               |   14 +-
 reports/diagnostics/publish_trace.md               |   14 +-
 reports/diagnostics/publisher_trace.md             |    6 +-
 reports/diagnostics/root_cause_analysis.md         |   44 +-
 reports/diagnostics/rule_impact.md                 |    5 +-
 reports/diagnostics/scheduler_trace.md             |   20 +-
 reports/diagnostics/session_trace.md               |   48 +-
 reports/diagnostics/source_trace.md                |   30 +-
 reports/diagnostics/validation_statistics.md       |    8 +-
 reports/diagnostics/validation_trace.md            |   46 +-
 reports/discovery/accepted_urls.md                 |  366 +-
 reports/discovery/adaptive_budget.md               |   28 +-
 reports/discovery/discovery_capacity.md            |   12 +-
 reports/discovery/environment_audit.md             |    2 +-
 reports/discovery/hard_limit_audit.md              |    4 +-
 reports/discovery/provider_audit.md                |   12 +-
 reports/discovery/provider_exhaustion.md           |   10 +-
 reports/discovery/provider_health.md               |    4 +-
 reports/discovery/provider_ranking.md              |   10 +-
 reports/discovery/provider_statistics.md           |   26 +-
 reports/discovery/provider_yield.md                |   10 +-
 reports/discovery/query_statistics.md              |  162 +-
 reports/discovery/rejected_urls.md                 |  110 +-
 reports/discovery/reputation_scores.md             |   35 +-
 reports/discovery/throughput_analysis.md           |   14 +-
 reports/discovery/trusted_source_usage.md          |   26 +-
 reports/enterprise/coverage_by_function.md         |    2 +-
 reports/enterprise/enterprise_state.json           |   26 +-
 reports/enterprise/production_distribution.md      |   18 +-
 reports/manufacturing/factory_economics.md         |   28 +-
 reports/manufacturing/growth_velocity.md           |   48 +-
 reports/manufacturing/knowledge_gap.md             |   16 +-
 reports/manufacturing/knowledge_universe.md        |   14 +-
 reports/manufacturing/production_capacity.md       |   20 +-
 reports/manufacturing/scheduler_decisions.md       |    8 +-
 reports/performance/api_statistics.md              |   14 +-
 reports/performance/auto_publish.md                |    8 +-
 reports/performance/cache_statistics.md            |    4 +-
 reports/performance/connector_performance.md       |   16 +-
 reports/performance/connector_ranking.md           |   16 +-
 reports/performance/crawler_statistics.md          |   64 +-
 reports/performance/download_statistics.md         |   30 +-
 reports/performance/extraction_statistics.md       |   34 +-
 reports/performance/factory_capacity.md            |   20 +-
 reports/performance/pipeline_bottleneck.md         |   44 +-
 reports/performance/production_capacity.md         |   12 +-
 reports/performance/queue_efficiency.md            |   14 +-
 reports/performance/session_efficiency.md          |    6 +-
 reports/performance/source_efficiency.md           |   16 +-
 reports/performance/source_ranking.md              |   35 +-
 reports/performance/stage_timings.md               |   12 +-
 reports/performance/throughput.md                  |   18 +-
 reports/performance/throughput_report.md           |   18 +-
 reports/performance/worker_utilization.md          |   14 +-
 reports/production/candidate_pipeline.md           |   16 +-
 reports/production/connector_summary.md            |   70 +-
 reports/production/document_pipeline.md            |  344 +-
 reports/production/evidence_trace.md               |   26 +-
 reports/production/production_trace.md             |   40 +-
 reports/production/publish_pipeline.md             |   14 +-
 reports/production/runtime_statistics.md           |   52 +-
 reports/reliability/git_worktree_trace.md          |   23 +
 reports/reliability/writer_finalize.json           |    2 +-
 84 files changed, 10037 insertions(+), 3464 deletions(-)
```

## pre_acquire

- **time:** 2026-07-11T14:06:41Z
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

- **time:** 2026-07-11T14:18:19Z
- **dirty_count:** 91

### status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-11.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M reports/diagnostics/candidate_lifecycle.md
 M reports/diagnostics/candidate_root_cause.md
 M reports/diagnostics/dataset_validation_summary.md
 M reports/diagnostics/document_trace.md
 M reports/diagnostics/extraction_trace.md
 M reports/diagnostics/false_negative_analysis.md
 M reports/diagnostics/integrity_trace.md
 M reports/diagnostics/knowledge_gap_trace.md
 M reports/diagnostics/mission_trace.md
 M reports/diagnostics/publish_trace.md
 M reports/diagnostics/publisher_trace.md
 M reports/diagnostics/root_cause_analysis.md
 M reports/diagnostics/rule_impact.md
 M reports/diagnostics/scheduler_trace.md
 M reports/diagnostics/session_trace.md
 M reports/diagnostics/source_trace.md
 M reports/diagnostics/validation_statistics.md
 M reports/diagnostics/validation_trace.md
 M reports/discovery/accepted_urls.md
 M reports/discovery/adaptive_budget.md
 M reports/discovery/discovery_capacity.md
 M reports/discovery/environment_audit.md
 M reports/discovery/hard_limit_audit.md
 M reports/discovery/provider_audit.md
 M reports/discovery/provider_exhaustion.md
 M reports/discovery/provider_health.md
 M reports/discovery/provider_ranking.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/provider_yield.md
 M reports/discovery/query_statistics.md
 M reports/discovery/rejected_urls.md
 M reports/discovery/reputation_scores.md
 M reports/discovery/throughput_analysis.md
 M reports/discovery/trusted_source_usage.md
 M reports/fulltext/acquisition_success.md
 M reports/fulltext/content_richness.md
 M reports/fulltext/doi_resolution.md
 M reports/fulltext/fallback_chain.md
 M reports/fulltext/fulltext_statistics.md
 M reports/fulltext/knowledge_gain_projection.md
 M reports/fulltext/publisher_resolution.md
 M reports/fulltext/repository_statistics.md
 M reports/fulltext/representation_quality.md
 M reports/fulltext/validation_before_after.md
 M reports/manufacturing/factory_economics.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/production_capacity.md
 M reports/performance/api_statistics.md
 M reports/performance/auto_publish.md
 M reports/performance/cache_statistics.md
 M reports/performance/connector_performance.md
 M reports/performance/connector_ranking.md
 M reports/performance/crawler_statistics.md
 M reports/performance/download_statistics.md
 M reports/performance/extraction_statistics.md
 M reports/performance/factory_capacity.md
 M reports/performance/pipeline_bottleneck.md
 M reports/performance/production_capacity.md
 M reports/performance/queue_efficiency.md
 M reports/performance/session_efficiency.md
 M reports/performance/source_efficiency.md
 M reports/performance/source_ranking.md
 M reports/performance/stage_timings.md
 M reports/performance/throughput.md
 M reports/performance/throughput_report.md
 M reports/performance/worker_utilization.md
 M reports/production/candidate_pipeline.md
 M reports/production/connector_summary.md
 M reports/production/document_pipeline.md
 M reports/production/evidence_trace.md
 M reports/production/production_trace.md
 M reports/production/publish_pipeline.md
 M reports/production/runtime_statistics.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-AE4E77.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-610B3E.json
?? reports/production/production_trace_SES-20260711-AE4E77.json
?? reports/production/sessions/SES-20260711-AE4E77/
```

### diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-11.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
reports/diagnostics/candidate_lifecycle.md
reports/diagnostics/candidate_root_cause.md
reports/diagnostics/dataset_validation_summary.md
reports/diagnostics/document_trace.md
reports/diagnostics/extraction_trace.md
reports/diagnostics/false_negative_analysis.md
reports/diagnostics/integrity_trace.md
reports/diagnostics/knowledge_gap_trace.md
reports/diagnostics/mission_trace.md
reports/diagnostics/publish_trace.md
reports/diagnostics/publisher_trace.md
reports/diagnostics/root_cause_analysis.md
reports/diagnostics/rule_impact.md
reports/diagnostics/scheduler_trace.md
reports/diagnostics/session_trace.md
reports/diagnostics/source_trace.md
reports/diagnostics/validation_statistics.md
reports/diagnostics/validation_trace.md
reports/discovery/accepted_urls.md
reports/discovery/adaptive_budget.md
reports/discovery/discovery_capacity.md
reports/discovery/environment_audit.md
reports/discovery/hard_limit_audit.md
reports/discovery/provider_audit.md
reports/discovery/provider_exhaustion.md
reports/discovery/provider_health.md
reports/discovery/provider_ranking.md
reports/discovery/provider_statistics.md
reports/discovery/provider_yield.md
reports/discovery/query_statistics.md
reports/discovery/rejected_urls.md
reports/discovery/reputation_scores.md
reports/discovery/throughput_analysis.md
reports/discovery/trusted_source_usage.md
reports/fulltext/acquisition_success.md
reports/fulltext/content_richness.md
reports/fulltext/doi_resolution.md
reports/fulltext/fallback_chain.md
reports/fulltext/fulltext_statistics.md
reports/fulltext/knowledge_gain_projection.md
reports/fulltext/publisher_resolution.md
reports/fulltext/repository_statistics.md
reports/fulltext/representation_quality.md
reports/fulltext/validation_before_after.md
reports/manufacturing/factory_economics.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/production_capacity.md
reports/performance/api_statistics.md
reports/performance/auto_publish.md
reports/performance/cache_statistics.md
reports/performance/connector_performance.md
reports/performance/connector_ranking.md
reports/performance/crawler_statistics.md
reports/performance/download_statistics.md
reports/performance/extraction_statistics.md
reports/performance/factory_capacity.md
reports/performance/pipeline_bottleneck.md
reports/performance/production_capacity.md
reports/performance/queue_efficiency.md
reports/performance/session_efficiency.md
reports/performance/source_efficiency.md
reports/performance/source_ranking.md
reports/performance/stage_timings.md
reports/performance/throughput.md
reports/performance/throughput_report.md
reports/performance/worker_utilization.md
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
 .../learning/state/acquisition_performance.json    |  649 +--
 automation/learning/state/current_snapshot.json    |    2 +-
 automation/learning/state/discovery_analytics.json | 2501 ++++-----
 automation/learning/state/learning_journal.jsonl   |  435 ++
 automation/learning/state/live_activity.json       |   10 +-
 automation/learning/state/manufacturing_state.json |  278 +-
 automation/learning/state/production_trace.json    | 5533 ++++----------------
 automation/learning/state/snapshot_2026-07-11.json |    2 +-
 automation/learning/state/source_health.json       |    2 +-
 automation/learning/state/source_performance.json  |   70 +-
 automation/sessions/index.json                     |   30 +-
 reports/diagnostics/candidate_lifecycle.md         |   15 +-
 reports/diagnostics/candidate_root_cause.md        |   37 +-
 reports/diagnostics/dataset_validation_summary.md  |    4 +-
 reports/diagnostics/document_trace.md              |  353 +-
 reports/diagnostics/extraction_trace.md            |    7 +-
 reports/diagnostics/false_negative_analysis.md     |    7 +-
 reports/diagnostics/integrity_trace.md             |  155 +-
 reports/diagnostics/knowledge_gap_trace.md         |    2 +-
 reports/diagnostics/mission_trace.md               |    2 +-
 reports/diagnostics/publish_trace.md               |   15 +-
 reports/diagnostics/publisher_trace.md             |    7 +-
 reports/diagnostics/root_cause_analysis.md         |   46 +-
 reports/diagnostics/rule_impact.md                 |    5 +-
 reports/diagnostics/scheduler_trace.md             |    8 +-
 reports/diagnostics/session_trace.md               |   54 +-
 reports/diagnostics/source_trace.md                |   30 +-
 reports/diagnostics/validation_statistics.md       |   10 +-
 reports/diagnostics/validation_trace.md            |   78 +-
 reports/discovery/accepted_urls.md                 |  334 +-
 reports/discovery/adaptive_budget.md               |   28 +-
 reports/discovery/discovery_capacity.md            |   12 +-
 reports/discovery/environment_audit.md             |    2 +-
 reports/discovery/hard_limit_audit.md              |   56 +-
 reports/discovery/provider_audit.md                |   12 +-
 reports/discovery/provider_exhaustion.md           |   10 +-
 reports/discovery/provider_health.md               |    4 +-
 reports/discovery/provider_ranking.md              |   12 +-
 reports/discovery/provider_statistics.md           |   26 +-
 reports/discovery/provider_yield.md                |   10 +-
 reports/discovery/query_statistics.md              |  162 +-
 reports/discovery/rejected_urls.md                 |  128 +-
 reports/discovery/reputation_scores.md             |   35 +-
 reports/discovery/throughput_analysis.md           |   14 +-
 reports/discovery/trusted_source_usage.md          |   22 +-
 reports/fulltext/acquisition_success.md            |   57 +-
 reports/fulltext/content_richness.md               |   10 +-
 reports/fulltext/doi_resolution.md                 |   14 +-
 reports/fulltext/fallback_chain.md                 |    2 +-
 reports/fulltext/fulltext_statistics.md            |   16 +-
 reports/fulltext/knowledge_gain_projection.md      |   16 +-
 reports/fulltext/publisher_resolution.md           |    8 +-
 reports/fulltext/repository_statistics.md          |    6 +-
 reports/fulltext/representation_quality.md         |   10 +-
 reports/fulltext/validation_before_after.md        |   14 +-
 reports/manufacturing/factory_economics.md         |   24 +-
 reports/manufacturing/growth_velocity.md           |   38 +-
 reports/manufacturing/knowledge_gap.md             |    2 +-
 reports/manufacturing/production_capacity.md       |   14 +-
 reports/performance/api_statistics.md              |   14 +-
 reports/performance/auto_publish.md                |    8 +-
 reports/performance/cache_statistics.md            |    4 +-
 reports/performance/connector_performance.md       |   16 +-
 reports/performance/connector_ranking.md           |   16 +-
 reports/performance/crawler_statistics.md          |   68 +-
 reports/performance/download_statistics.md         |   30 +-
 reports/performance/extraction_statistics.md       |   40 +-
 reports/performance/factory_capacity.md            |   24 +-
 reports/performance/pipeline_bottleneck.md         |   50 +-
 reports/performance/production_capacity.md         |   16 +-
 reports/performance/queue_efficiency.md            |   14 +-
 reports/performance/session_efficiency.md          |   14 +-
 reports/performance/source_efficiency.md           |   16 +-
 reports/performance/source_ranking.md              |   35 +-
 reports/performance/stage_timings.md               |   12 +-
 reports/performance/throughput.md                  |   18 +-
 reports/performance/throughput_report.md           |   20 +-
 reports/performance/worker_utilization.md          |   14 +-
 reports/production/candidate_pipeline.md           |   21 +-
 reports/production/connector_summary.md            |   74 +-
 reports/production/document_pipeline.md            |  349 +-
 reports/production/evidence_trace.md               |   26 +-
 reports/production/production_trace.md             |   44 +-
 reports/production/publish_pipeline.md             |   20 +-
 reports/production/runtime_statistics.md           |   62 +-
 reports/reliability/git_worktree_trace.md          |   23 +
 reports/reliability/writer_finalize.json           |    4 +-
 87 files changed, 4682 insertions(+), 7815 deletions(-)
```

## pre_acquire

- **time:** 2026-07-11T14:34:05Z
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

- **time:** 2026-07-11T14:35:46Z
- **dirty_count:** 9

### status --porcelain=v1

```
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M reports/manufacturing/knowledge_gap.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-C22382.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-F6132B.json
```

### diff --name-only

```
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
reports/manufacturing/knowledge_gap.md
reports/reliability/git_worktree_trace.md
reports/reliability/writer_finalize.json
```

### diff --stat

```
 automation/learning/state/learning_journal.jsonl   |   22 +
 automation/learning/state/live_activity.json       |   45 +-
 automation/learning/state/manufacturing_state.json |    4 +-
 automation/learning/state/production_trace.json    | 2083 +-------------------
 reports/manufacturing/knowledge_gap.md             |    2 +-
 reports/reliability/git_worktree_trace.md          |   23 +
 reports/reliability/writer_finalize.json           |    4 +-
 7 files changed, 110 insertions(+), 2073 deletions(-)
```

## pre_acquire

- **time:** 2026-07-11T14:37:31Z
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

- **time:** 2026-07-11T14:49:16Z
- **dirty_count:** 90

### status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-11.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M reports/diagnostics/candidate_lifecycle.md
 M reports/diagnostics/candidate_root_cause.md
 M reports/diagnostics/dataset_validation_summary.md
 M reports/diagnostics/document_trace.md
 M reports/diagnostics/extraction_trace.md
 M reports/diagnostics/false_negative_analysis.md
 M reports/diagnostics/integrity_trace.md
 M reports/diagnostics/knowledge_gap_trace.md
 M reports/diagnostics/mission_trace.md
 M reports/diagnostics/publish_trace.md
 M reports/diagnostics/publisher_trace.md
 M reports/diagnostics/root_cause_analysis.md
 M reports/diagnostics/rule_impact.md
 M reports/diagnostics/scheduler_trace.md
 M reports/diagnostics/session_trace.md
 M reports/diagnostics/source_trace.md
 M reports/diagnostics/validation_statistics.md
 M reports/diagnostics/validation_trace.md
 M reports/discovery/accepted_urls.md
 M reports/discovery/adaptive_budget.md
 M reports/discovery/discovery_capacity.md
 M reports/discovery/environment_audit.md
 M reports/discovery/hard_limit_audit.md
 M reports/discovery/provider_audit.md
 M reports/discovery/provider_exhaustion.md
 M reports/discovery/provider_health.md
 M reports/discovery/provider_ranking.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/provider_yield.md
 M reports/discovery/query_statistics.md
 M reports/discovery/rejected_urls.md
 M reports/discovery/reputation_scores.md
 M reports/discovery/throughput_analysis.md
 M reports/discovery/trusted_source_usage.md
 M reports/fulltext/acquisition_success.md
 M reports/fulltext/content_richness.md
 M reports/fulltext/doi_resolution.md
 M reports/fulltext/fallback_chain.md
 M reports/fulltext/fulltext_statistics.md
 M reports/fulltext/knowledge_gain_projection.md
 M reports/fulltext/publisher_resolution.md
 M reports/fulltext/repository_statistics.md
 M reports/fulltext/representation_quality.md
 M reports/fulltext/validation_before_after.md
 M reports/manufacturing/factory_economics.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/production_capacity.md
 M reports/performance/api_statistics.md
 M reports/performance/cache_statistics.md
 M reports/performance/connector_performance.md
 M reports/performance/connector_ranking.md
 M reports/performance/crawler_statistics.md
 M reports/performance/download_statistics.md
 M reports/performance/extraction_statistics.md
 M reports/performance/factory_capacity.md
 M reports/performance/pipeline_bottleneck.md
 M reports/performance/production_capacity.md
 M reports/performance/queue_efficiency.md
 M reports/performance/session_efficiency.md
 M reports/performance/source_efficiency.md
 M reports/performance/source_ranking.md
 M reports/performance/stage_timings.md
 M reports/performance/throughput.md
 M reports/performance/throughput_report.md
 M reports/performance/worker_utilization.md
 M reports/production/candidate_pipeline.md
 M reports/production/connector_summary.md
 M reports/production/document_pipeline.md
 M reports/production/evidence_trace.md
 M reports/production/production_trace.md
 M reports/production/publish_pipeline.md
 M reports/production/runtime_statistics.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-BAFFD0.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-CA5D36.json
?? reports/production/production_trace_SES-20260711-BAFFD0.json
?? reports/production/sessions/SES-20260711-BAFFD0/
```

### diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-11.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
reports/diagnostics/candidate_lifecycle.md
reports/diagnostics/candidate_root_cause.md
reports/diagnostics/dataset_validation_summary.md
reports/diagnostics/document_trace.md
reports/diagnostics/extraction_trace.md
reports/diagnostics/false_negative_analysis.md
reports/diagnostics/integrity_trace.md
reports/diagnostics/knowledge_gap_trace.md
reports/diagnostics/mission_trace.md
reports/diagnostics/publish_trace.md
reports/diagnostics/publisher_trace.md
reports/diagnostics/root_cause_analysis.md
reports/diagnostics/rule_impact.md
reports/diagnostics/scheduler_trace.md
reports/diagnostics/session_trace.md
reports/diagnostics/source_trace.md
reports/diagnostics/validation_statistics.md
reports/diagnostics/validation_trace.md
reports/discovery/accepted_urls.md
reports/discovery/adaptive_budget.md
reports/discovery/discovery_capacity.md
reports/discovery/environment_audit.md
reports/discovery/hard_limit_audit.md
reports/discovery/provider_audit.md
reports/discovery/provider_exhaustion.md
reports/discovery/provider_health.md
reports/discovery/provider_ranking.md
reports/discovery/provider_statistics.md
reports/discovery/provider_yield.md
reports/discovery/query_statistics.md
reports/discovery/rejected_urls.md
reports/discovery/reputation_scores.md
reports/discovery/throughput_analysis.md
reports/discovery/trusted_source_usage.md
reports/fulltext/acquisition_success.md
reports/fulltext/content_richness.md
reports/fulltext/doi_resolution.md
reports/fulltext/fallback_chain.md
reports/fulltext/fulltext_statistics.md
reports/fulltext/knowledge_gain_projection.md
reports/fulltext/publisher_resolution.md
reports/fulltext/repository_statistics.md
reports/fulltext/representation_quality.md
reports/fulltext/validation_before_after.md
reports/manufacturing/factory_economics.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/production_capacity.md
reports/performance/api_statistics.md
reports/performance/cache_statistics.md
reports/performance/connector_performance.md
reports/performance/connector_ranking.md
reports/performance/crawler_statistics.md
reports/performance/download_statistics.md
reports/performance/extraction_statistics.md
reports/performance/factory_capacity.md
reports/performance/pipeline_bottleneck.md
reports/performance/production_capacity.md
reports/performance/queue_efficiency.md
reports/performance/session_efficiency.md
reports/performance/source_efficiency.md
reports/performance/source_ranking.md
reports/performance/stage_timings.md
reports/performance/throughput.md
reports/performance/throughput_report.md
reports/performance/worker_utilization.md
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
 .../learning/state/acquisition_performance.json    |  226 +--
 automation/learning/state/current_snapshot.json    |    2 +-
 automation/learning/state/discovery_analytics.json | 2071 +++++++-------------
 automation/learning/state/learning_journal.jsonl   |  433 ++++
 automation/learning/state/live_activity.json       |   45 +-
 automation/learning/state/manufacturing_state.json |  162 +-
 automation/learning/state/production_trace.json    | 2011 ++++++++++++++++++-
 automation/learning/state/snapshot_2026-07-11.json |    2 +-
 automation/learning/state/source_health.json       |    2 +-
 automation/learning/state/source_performance.json  |   74 +-
 automation/sessions/index.json                     |   58 +-
 reports/diagnostics/candidate_lifecycle.md         |   12 +-
 reports/diagnostics/candidate_root_cause.md        |   12 +-
 reports/diagnostics/dataset_validation_summary.md  |    2 +-
 reports/diagnostics/document_trace.md              |   62 +-
 reports/diagnostics/extraction_trace.md            |    8 +-
 reports/diagnostics/false_negative_analysis.md     |    2 +-
 reports/diagnostics/integrity_trace.md             |   26 +-
 reports/diagnostics/knowledge_gap_trace.md         |    2 +-
 reports/diagnostics/mission_trace.md               |    2 +-
 reports/diagnostics/publish_trace.md               |    8 +-
 reports/diagnostics/publisher_trace.md             |    8 +-
 reports/diagnostics/root_cause_analysis.md         |   16 +-
 reports/diagnostics/rule_impact.md                 |    2 +-
 reports/diagnostics/scheduler_trace.md             |    8 +-
 reports/diagnostics/session_trace.md               |   28 +-
 reports/diagnostics/source_trace.md                |   30 +-
 reports/diagnostics/validation_statistics.md       |    2 +-
 reports/diagnostics/validation_trace.md            |   24 +-
 reports/discovery/accepted_urls.md                 |  212 +-
 reports/discovery/adaptive_budget.md               |    2 +-
 reports/discovery/discovery_capacity.md            |    2 +-
 reports/discovery/environment_audit.md             |    2 +-
 reports/discovery/hard_limit_audit.md              |    4 +-
 reports/discovery/provider_audit.md                |   10 +-
 reports/discovery/provider_exhaustion.md           |    6 +-
 reports/discovery/provider_health.md               |    6 +-
 reports/discovery/provider_ranking.md              |   12 +-
 reports/discovery/provider_statistics.md           |   26 +-
 reports/discovery/provider_yield.md                |    8 +-
 reports/discovery/query_statistics.md              |   72 +-
 reports/discovery/rejected_urls.md                 |  116 +-
 reports/discovery/reputation_scores.md             |    8 +-
 reports/discovery/throughput_analysis.md           |   12 +-
 reports/discovery/trusted_source_usage.md          |   19 +-
 reports/fulltext/acquisition_success.md            |   54 +-
 reports/fulltext/content_richness.md               |   10 +-
 reports/fulltext/doi_resolution.md                 |    4 +-
 reports/fulltext/fallback_chain.md                 |    2 +-
 reports/fulltext/fulltext_statistics.md            |   14 +-
 reports/fulltext/knowledge_gain_projection.md      |   12 +-
 reports/fulltext/publisher_resolution.md           |    4 +-
 reports/fulltext/repository_statistics.md          |    2 +-
 reports/fulltext/representation_quality.md         |    8 +-
 reports/fulltext/validation_before_after.md        |   12 +-
 reports/manufacturing/factory_economics.md         |   26 +-
 reports/manufacturing/growth_velocity.md           |   20 +-
 reports/manufacturing/knowledge_gap.md             |    2 +-
 reports/manufacturing/production_capacity.md       |    6 +-
 reports/performance/api_statistics.md              |   14 +-
 reports/performance/cache_statistics.md            |    4 +-
 reports/performance/connector_performance.md       |   16 +-
 reports/performance/connector_ranking.md           |   16 +-
 reports/performance/crawler_statistics.md          |   50 +-
 reports/performance/download_statistics.md         |   24 +-
 reports/performance/extraction_statistics.md       |   22 +-
 reports/performance/factory_capacity.md            |   12 +-
 reports/performance/pipeline_bottleneck.md         |   44 +-
 reports/performance/production_capacity.md         |    8 +-
 reports/performance/queue_efficiency.md            |    4 +-
 reports/performance/session_efficiency.md          |    6 +-
 reports/performance/source_efficiency.md           |   16 +-
 reports/performance/source_ranking.md              |    8 +-
 reports/performance/stage_timings.md               |   12 +-
 reports/performance/throughput.md                  |   12 +-
 reports/performance/throughput_report.md           |   14 +-
 reports/performance/worker_utilization.md          |   10 +-
 reports/production/candidate_pipeline.md           |   14 +-
 reports/production/connector_summary.md            |   38 +-
 reports/production/document_pipeline.md            |   60 +-
 reports/production/evidence_trace.md               |    2 +-
 reports/production/production_trace.md             |   30 +-
 reports/production/publish_pipeline.md             |    2 +-
 reports/production/runtime_statistics.md           |   30 +-
 reports/reliability/git_worktree_trace.md          |   23 +
 reports/reliability/writer_finalize.json           |    4 +-
 86 files changed, 4097 insertions(+), 2431 deletions(-)
```

## pre_acquire

- **time:** 2026-07-11T15:03:46Z
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

- **time:** 2026-07-11T15:34:43Z
- **dirty_count:** 29

### status --porcelain=v1

```
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/source_performance.json
 M reports/discovery/accepted_urls.md
 M reports/discovery/adaptive_budget.md
 M reports/discovery/discovery_capacity.md
 M reports/discovery/environment_audit.md
 M reports/discovery/hard_limit_audit.md
 M reports/discovery/provider_audit.md
 M reports/discovery/provider_exhaustion.md
 M reports/discovery/provider_health.md
 M reports/discovery/provider_ranking.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/provider_yield.md
 M reports/discovery/query_statistics.md
 M reports/discovery/rejected_urls.md
 M reports/discovery/reputation_scores.md
 M reports/discovery/throughput_analysis.md
 M reports/discovery/trusted_source_usage.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/production_capacity.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-C15C23.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-211F6B.json
```

### diff --name-only

```
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/source_performance.json
reports/discovery/accepted_urls.md
reports/discovery/adaptive_budget.md
reports/discovery/discovery_capacity.md
reports/discovery/environment_audit.md
reports/discovery/hard_limit_audit.md
reports/discovery/provider_audit.md
reports/discovery/provider_exhaustion.md
reports/discovery/provider_health.md
reports/discovery/provider_ranking.md
reports/discovery/provider_statistics.md
reports/discovery/provider_yield.md
reports/discovery/query_statistics.md
reports/discovery/rejected_urls.md
reports/discovery/reputation_scores.md
reports/discovery/throughput_analysis.md
reports/discovery/trusted_source_usage.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/production_capacity.md
reports/reliability/git_worktree_trace.md
reports/reliability/writer_finalize.json
```

### diff --stat

```
 automation/learning/state/discovery_analytics.json | 2826 ++++++++++++--------
 automation/learning/state/learning_journal.jsonl   |  398 +++
 automation/learning/state/live_activity.json       |   45 +-
 automation/learning/state/manufacturing_state.json |    8 +-
 automation/learning/state/production_trace.json    | 2032 +-------------
 automation/learning/state/source_performance.json  |   66 +-
 reports/discovery/accepted_urls.md                 |  396 +--
 reports/discovery/adaptive_budget.md               |   28 +-
 reports/discovery/discovery_capacity.md            |   12 +-
 reports/discovery/environment_audit.md             |    2 +-
 reports/discovery/hard_limit_audit.md              |    5 +-
 reports/discovery/provider_audit.md                |   12 +-
 reports/discovery/provider_exhaustion.md           |   10 +-
 reports/discovery/provider_health.md               |    6 +-
 reports/discovery/provider_ranking.md              |   12 +-
 reports/discovery/provider_statistics.md           |   26 +-
 reports/discovery/provider_yield.md                |   10 +-
 reports/discovery/query_statistics.md              |  162 +-
 reports/discovery/rejected_urls.md                 |  126 +-
 reports/discovery/reputation_scores.md             |   35 +-
 reports/discovery/throughput_analysis.md           |   14 +-
 reports/discovery/trusted_source_usage.md          |   27 +-
 reports/manufacturing/growth_velocity.md           |    4 +-
 reports/manufacturing/knowledge_gap.md             |    2 +-
 reports/manufacturing/production_capacity.md       |    2 +-
 reports/reliability/git_worktree_trace.md          |   23 +
 reports/reliability/writer_finalize.json           |    4 +-
 27 files changed, 2820 insertions(+), 3473 deletions(-)
```

## pre_acquire

- **time:** 2026-07-11T16:30:20Z
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

- **time:** 2026-07-11T17:10:54Z
- **dirty_count:** 95

### status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/daily_2026-07-11.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-11.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M domains/business_development/business_signal_library.csv
 M reports/diagnostics/candidate_lifecycle.md
 M reports/diagnostics/candidate_root_cause.md
 M reports/diagnostics/dataset_validation_summary.md
 M reports/diagnostics/document_trace.md
 M reports/diagnostics/extraction_trace.md
 M reports/diagnostics/false_negative_analysis.md
 M reports/diagnostics/integrity_trace.md
 M reports/diagnostics/knowledge_gap_trace.md
 M reports/diagnostics/mission_trace.md
 M reports/diagnostics/publish_trace.md
 M reports/diagnostics/publisher_trace.md
 M reports/diagnostics/root_cause_analysis.md
 M reports/diagnostics/rule_impact.md
 M reports/diagnostics/scheduler_trace.md
 M reports/diagnostics/session_trace.md
 M reports/diagnostics/source_trace.md
 M reports/diagnostics/validation_statistics.md
 M reports/diagnostics/validation_trace.md
 M reports/discovery/accepted_urls.md
 M reports/discovery/adaptive_budget.md
 M reports/discovery/discovery_capacity.md
 M reports/discovery/environment_audit.md
 M reports/discovery/hard_limit_audit.md
 M reports/discovery/provider_audit.md
 M reports/discovery/provider_exhaustion.md
 M reports/discovery/provider_health.md
 M reports/discovery/provider_ranking.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/provider_yield.md
 M reports/discovery/query_statistics.md
 M reports/discovery/rejected_urls.md
 M reports/discovery/reputation_scores.md
 M reports/discovery/throughput_analysis.md
 M reports/discovery/trusted_source_usage.md
 M reports/fulltext/acquisition_success.md
 M reports/fulltext/content_richness.md
 M reports/fulltext/doi_resolution.md
 M reports/fulltext/fallback_chain.md
 M reports/fulltext/fulltext_statistics.md
 M reports/fulltext/knowledge_gain_projection.md
 M reports/fulltext/publisher_resolution.md
 M reports/fulltext/repository_statistics.md
 M reports/fulltext/representation_quality.md
 M reports/fulltext/validation_before_after.md
 M reports/manufacturing/factory_economics.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/knowledge_universe.md
 M reports/manufacturing/production_capacity.md
 M reports/manufacturing/scheduler_decisions.md
 M reports/performance/api_statistics.md
 M reports/performance/auto_publish.md
 M reports/performance/cache_statistics.md
 M reports/performance/connector_performance.md
 M reports/performance/connector_ranking.md
 M reports/performance/crawler_statistics.md
 M reports/performance/download_statistics.md
 M reports/performance/extraction_statistics.md
 M reports/performance/factory_capacity.md
 M reports/performance/pipeline_bottleneck.md
 M reports/performance/production_capacity.md
 M reports/performance/queue_efficiency.md
 M reports/performance/session_efficiency.md
 M reports/performance/source_efficiency.md
 M reports/performance/source_ranking.md
 M reports/performance/stage_timings.md
 M reports/performance/throughput.md
 M reports/performance/throughput_report.md
 M reports/performance/worker_utilization.md
 M reports/production/candidate_pipeline.md
 M reports/production/connector_summary.md
 M reports/production/document_pipeline.md
 M reports/production/evidence_trace.md
 M reports/production/production_trace.md
 M reports/production/publish_pipeline.md
 M reports/production/runtime_statistics.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-7833BB.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-29CE5A.json
?? reports/production/production_trace_SES-20260711-7833BB.json
?? reports/production/sessions/SES-20260711-7833BB/
```

### diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/daily_2026-07-11.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-11.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
domains/business_development/business_signal_library.csv
reports/diagnostics/candidate_lifecycle.md
reports/diagnostics/candidate_root_cause.md
reports/diagnostics/dataset_validation_summary.md
reports/diagnostics/document_trace.md
reports/diagnostics/extraction_trace.md
reports/diagnostics/false_negative_analysis.md
reports/diagnostics/integrity_trace.md
reports/diagnostics/knowledge_gap_trace.md
reports/diagnostics/mission_trace.md
reports/diagnostics/publish_trace.md
reports/diagnostics/publisher_trace.md
reports/diagnostics/root_cause_analysis.md
reports/diagnostics/rule_impact.md
reports/diagnostics/scheduler_trace.md
reports/diagnostics/session_trace.md
reports/diagnostics/source_trace.md
reports/diagnostics/validation_statistics.md
reports/diagnostics/validation_trace.md
reports/discovery/accepted_urls.md
reports/discovery/adaptive_budget.md
reports/discovery/discovery_capacity.md
reports/discovery/environment_audit.md
reports/discovery/hard_limit_audit.md
reports/discovery/provider_audit.md
reports/discovery/provider_exhaustion.md
reports/discovery/provider_health.md
reports/discovery/provider_ranking.md
reports/discovery/provider_statistics.md
reports/discovery/provider_yield.md
reports/discovery/query_statistics.md
reports/discovery/rejected_urls.md
reports/discovery/reputation_scores.md
reports/discovery/throughput_analysis.md
reports/discovery/trusted_source_usage.md
reports/fulltext/acquisition_success.md
reports/fulltext/content_richness.md
reports/fulltext/doi_resolution.md
reports/fulltext/fallback_chain.md
reports/fulltext/fulltext_statistics.md
reports/fulltext/knowledge_gain_projection.md
reports/fulltext/publisher_resolution.md
reports/fulltext/repository_statistics.md
reports/fulltext/representation_quality.md
reports/fulltext/validation_before_after.md
reports/manufacturing/factory_economics.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/knowledge_universe.md
reports/manufacturing/production_capacity.md
reports/manufacturing/scheduler_decisions.md
reports/performance/api_statistics.md
reports/performance/auto_publish.md
reports/performance/cache_statistics.md
reports/performance/connector_performance.md
reports/performance/connector_ranking.md
reports/performance/crawler_statistics.md
reports/performance/download_statistics.md
reports/performance/extraction_statistics.md
reports/performance/factory_capacity.md
reports/performance/pipeline_bottleneck.md
reports/performance/production_capacity.md
reports/performance/queue_efficiency.md
reports/performance/session_efficiency.md
reports/performance/source_efficiency.md
reports/performance/source_ranking.md
reports/performance/stage_timings.md
reports/performance/throughput.md
reports/performance/throughput_report.md
reports/performance/worker_utilization.md
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
 .../learning/state/acquisition_performance.json    |  457 ++-
 automation/learning/state/current_snapshot.json    |    6 +-
 automation/learning/state/daily_2026-07-11.json    |    4 +-
 automation/learning/state/discovery_analytics.json | 3366 ++++++--------------
 automation/learning/state/learning_journal.jsonl   |  456 +++
 automation/learning/state/live_activity.json       |   45 +-
 automation/learning/state/manufacturing_state.json |  339 +-
 automation/learning/state/production_trace.json    | 2323 +++++++++++++-
 automation/learning/state/snapshot_2026-07-11.json |    6 +-
 automation/learning/state/source_health.json       |   86 +-
 automation/learning/state/source_performance.json  |   78 +-
 automation/sessions/index.json                     |   58 +-
 .../business_signal_library.csv                    |    5 +
 reports/diagnostics/candidate_lifecycle.md         |   18 +-
 reports/diagnostics/candidate_root_cause.md        |   43 +-
 reports/diagnostics/dataset_validation_summary.md  |    4 +-
 reports/diagnostics/document_trace.md              |  183 +-
 reports/diagnostics/extraction_trace.md            |   10 +-
 reports/diagnostics/false_negative_analysis.md     |   10 +-
 reports/diagnostics/integrity_trace.md             |  270 +-
 reports/diagnostics/knowledge_gap_trace.md         |    6 +-
 reports/diagnostics/mission_trace.md               |    2 +-
 reports/diagnostics/publish_trace.md               |   18 +-
 reports/diagnostics/publisher_trace.md             |   10 +-
 reports/diagnostics/root_cause_analysis.md         |   42 +-
 reports/diagnostics/rule_impact.md                 |    5 +-
 reports/diagnostics/scheduler_trace.md             |    8 +-
 reports/diagnostics/session_trace.md               |   50 +-
 reports/diagnostics/source_trace.md                |   30 +-
 reports/diagnostics/validation_statistics.md       |   10 +-
 reports/diagnostics/validation_trace.md            |  156 +-
 reports/discovery/accepted_urls.md                 |  230 +-
 reports/discovery/adaptive_budget.md               |   14 +-
 reports/discovery/discovery_capacity.md            |    8 +-
 reports/discovery/environment_audit.md             |    2 +-
 reports/discovery/hard_limit_audit.md              |   43 +-
 reports/discovery/provider_audit.md                |   38 +-
 reports/discovery/provider_exhaustion.md           |   22 +-
 reports/discovery/provider_health.md               |   14 +-
 reports/discovery/provider_ranking.md              |   20 +-
 reports/discovery/provider_statistics.md           |   36 +-
 reports/discovery/provider_yield.md                |   14 +-
 reports/discovery/query_statistics.md              |  114 +-
 reports/discovery/rejected_urls.md                 |   58 +-
 reports/discovery/reputation_scores.md             |   14 +-
 reports/discovery/throughput_analysis.md           |   16 +-
 reports/discovery/trusted_source_usage.md          |   22 +-
 reports/fulltext/acquisition_success.md            |   92 +-
 reports/fulltext/content_richness.md               |   10 +-
 reports/fulltext/doi_resolution.md                 |   12 +-
 reports/fulltext/fallback_chain.md                 |    2 +-
 reports/fulltext/fulltext_statistics.md            |   14 +-
 reports/fulltext/knowledge_gain_projection.md      |   16 +-
 reports/fulltext/publisher_resolution.md           |    6 +-
 reports/fulltext/repository_statistics.md          |    6 +-
 reports/fulltext/representation_quality.md         |   10 +-
 reports/fulltext/validation_before_after.md        |   14 +-
 reports/manufacturing/factory_economics.md         |   32 +-
 reports/manufacturing/growth_velocity.md           |   50 +-
 reports/manufacturing/knowledge_gap.md             |    4 +-
 reports/manufacturing/knowledge_universe.md        |    2 +-
 reports/manufacturing/production_capacity.md       |   20 +-
 reports/manufacturing/scheduler_decisions.md       |    2 +-
 reports/performance/api_statistics.md              |   14 +-
 reports/performance/auto_publish.md                |    8 +-
 reports/performance/cache_statistics.md            |    4 +-
 reports/performance/connector_performance.md       |   16 +-
 reports/performance/connector_ranking.md           |   16 +-
 reports/performance/crawler_statistics.md          |   55 +-
 reports/performance/download_statistics.md         |   22 +-
 reports/performance/extraction_statistics.md       |   41 +-
 reports/performance/factory_capacity.md            |   20 +-
 reports/performance/pipeline_bottleneck.md         |   44 +-
 reports/performance/production_capacity.md         |   12 +-
 reports/performance/queue_efficiency.md            |   14 +-
 reports/performance/session_efficiency.md          |    6 +-
 reports/performance/source_efficiency.md           |   16 +-
 reports/performance/source_ranking.md              |   35 +-
 reports/performance/stage_timings.md               |   12 +-
 reports/performance/throughput.md                  |   18 +-
 reports/performance/throughput_report.md           |   18 +-
 reports/performance/worker_utilization.md          |   14 +-
 reports/production/candidate_pipeline.md           |   24 +-
 reports/production/connector_summary.md            |   72 +-
 reports/production/document_pipeline.md            |  183 +-
 reports/production/evidence_trace.md               |   52 +-
 reports/production/production_trace.md             |   38 +-
 reports/production/publish_pipeline.md             |   20 +-
 reports/production/runtime_statistics.md           |   56 +-
 reports/reliability/git_worktree_trace.md          |   23 +
 reports/reliability/writer_finalize.json           |    4 +-
 91 files changed, 5636 insertions(+), 4282 deletions(-)
```

## pre_acquire

- **time:** 2026-07-11T17:38:48Z
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

- **time:** 2026-07-11T18:00:48Z
- **dirty_count:** 98

### status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/daily_2026-07-11.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-11.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M domains/business_development/industry_library.csv
 M reports/diagnostics/candidate_lifecycle.md
 M reports/diagnostics/candidate_root_cause.md
 M reports/diagnostics/dataset_validation_summary.md
 M reports/diagnostics/document_trace.md
 M reports/diagnostics/extraction_trace.md
 M reports/diagnostics/false_negative_analysis.md
 M reports/diagnostics/integrity_trace.md
 M reports/diagnostics/knowledge_gap_trace.md
 M reports/diagnostics/mission_trace.md
 M reports/diagnostics/publish_trace.md
 M reports/diagnostics/publisher_trace.md
 M reports/diagnostics/root_cause_analysis.md
 M reports/diagnostics/rule_impact.md
 M reports/diagnostics/scheduler_trace.md
 M reports/diagnostics/session_trace.md
 M reports/diagnostics/source_trace.md
 M reports/diagnostics/validation_statistics.md
 M reports/diagnostics/validation_trace.md
 M reports/discovery/accepted_urls.md
 M reports/discovery/adaptive_budget.md
 M reports/discovery/discovery_capacity.md
 M reports/discovery/environment_audit.md
 M reports/discovery/hard_limit_audit.md
 M reports/discovery/provider_audit.md
 M reports/discovery/provider_exhaustion.md
 M reports/discovery/provider_health.md
 M reports/discovery/provider_ranking.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/provider_yield.md
 M reports/discovery/query_statistics.md
 M reports/discovery/rejected_urls.md
 M reports/discovery/reputation_scores.md
 M reports/discovery/throughput_analysis.md
 M reports/discovery/trusted_source_usage.md
 M reports/enterprise/coverage_by_function.md
 M reports/enterprise/enterprise_state.json
 M reports/enterprise/production_distribution.md
 M reports/fulltext/acquisition_success.md
 M reports/fulltext/content_richness.md
 M reports/fulltext/doi_resolution.md
 M reports/fulltext/fallback_chain.md
 M reports/fulltext/fulltext_statistics.md
 M reports/fulltext/knowledge_gain_projection.md
 M reports/fulltext/publisher_resolution.md
 M reports/fulltext/repository_statistics.md
 M reports/fulltext/representation_quality.md
 M reports/fulltext/validation_before_after.md
 M reports/manufacturing/factory_economics.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/knowledge_universe.md
 M reports/manufacturing/production_capacity.md
 M reports/performance/api_statistics.md
 M reports/performance/auto_publish.md
 M reports/performance/cache_statistics.md
 M reports/performance/connector_performance.md
 M reports/performance/connector_ranking.md
 M reports/performance/crawler_statistics.md
 M reports/performance/download_statistics.md
 M reports/performance/extraction_statistics.md
 M reports/performance/factory_capacity.md
 M reports/performance/pipeline_bottleneck.md
 M reports/performance/production_capacity.md
 M reports/performance/queue_efficiency.md
 M reports/performance/session_efficiency.md
 M reports/performance/source_efficiency.md
 M reports/performance/source_ranking.md
 M reports/performance/stage_timings.md
 M reports/performance/throughput.md
 M reports/performance/throughput_report.md
 M reports/performance/worker_utilization.md
 M reports/production/candidate_pipeline.md
 M reports/production/connector_summary.md
 M reports/production/document_pipeline.md
 M reports/production/evidence_trace.md
 M reports/production/production_trace.md
 M reports/production/publish_pipeline.md
 M reports/production/runtime_statistics.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-DA29BA.jsonl
?? automation/queue/publish/CAND-E9B6307893CE.json
?? automation/sessions/2026-07-11/SESSION-20260711-41DBF5.json
?? reports/production/production_trace_SES-20260711-DA29BA.json
?? reports/production/sessions/SES-20260711-DA29BA/
```

### diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/daily_2026-07-11.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-11.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
domains/business_development/industry_library.csv
reports/diagnostics/candidate_lifecycle.md
reports/diagnostics/candidate_root_cause.md
reports/diagnostics/dataset_validation_summary.md
reports/diagnostics/document_trace.md
reports/diagnostics/extraction_trace.md
reports/diagnostics/false_negative_analysis.md
reports/diagnostics/integrity_trace.md
reports/diagnostics/knowledge_gap_trace.md
reports/diagnostics/mission_trace.md
reports/diagnostics/publish_trace.md
reports/diagnostics/publisher_trace.md
reports/diagnostics/root_cause_analysis.md
reports/diagnostics/rule_impact.md
reports/diagnostics/scheduler_trace.md
reports/diagnostics/session_trace.md
reports/diagnostics/source_trace.md
reports/diagnostics/validation_statistics.md
reports/diagnostics/validation_trace.md
reports/discovery/accepted_urls.md
reports/discovery/adaptive_budget.md
reports/discovery/discovery_capacity.md
reports/discovery/environment_audit.md
reports/discovery/hard_limit_audit.md
reports/discovery/provider_audit.md
reports/discovery/provider_exhaustion.md
reports/discovery/provider_health.md
reports/discovery/provider_ranking.md
reports/discovery/provider_statistics.md
reports/discovery/provider_yield.md
reports/discovery/query_statistics.md
reports/discovery/rejected_urls.md
reports/discovery/reputation_scores.md
reports/discovery/throughput_analysis.md
reports/discovery/trusted_source_usage.md
reports/enterprise/coverage_by_function.md
reports/enterprise/enterprise_state.json
reports/enterprise/production_distribution.md
reports/fulltext/acquisition_success.md
reports/fulltext/content_richness.md
reports/fulltext/doi_resolution.md
reports/fulltext/fallback_chain.md
reports/fulltext/fulltext_statistics.md
reports/fulltext/knowledge_gain_projection.md
reports/fulltext/publisher_resolution.md
reports/fulltext/repository_statistics.md
reports/fulltext/representation_quality.md
reports/fulltext/validation_before_after.md
reports/manufacturing/factory_economics.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/knowledge_universe.md
reports/manufacturing/production_capacity.md
reports/performance/api_statistics.md
reports/performance/auto_publish.md
reports/performance/cache_statistics.md
reports/performance/connector_performance.md
reports/performance/connector_ranking.md
reports/performance/crawler_statistics.md
reports/performance/download_statistics.md
reports/performance/extraction_statistics.md
reports/performance/factory_capacity.md
reports/performance/pipeline_bottleneck.md
reports/performance/production_capacity.md
reports/performance/queue_efficiency.md
reports/performance/session_efficiency.md
reports/performance/source_efficiency.md
reports/performance/source_ranking.md
reports/performance/stage_timings.md
reports/performance/throughput.md
reports/performance/throughput_report.md
reports/performance/worker_utilization.md
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
 .../learning/state/acquisition_performance.json    |  479 ++--
 automation/learning/state/current_snapshot.json    |    6 +-
 automation/learning/state/daily_2026-07-11.json    |    4 +-
 automation/learning/state/discovery_analytics.json | 1485 +++++++-----
 automation/learning/state/learning_journal.jsonl   |  446 ++++
 automation/learning/state/live_activity.json       |   10 +-
 automation/learning/state/manufacturing_state.json |  362 +--
 automation/learning/state/production_trace.json    | 2354 +++++++++-----------
 automation/learning/state/snapshot_2026-07-11.json |    6 +-
 automation/learning/state/source_health.json       |   82 +-
 automation/learning/state/source_performance.json  |   86 +-
 automation/sessions/index.json                     |   30 +-
 domains/business_development/industry_library.csv  |    2 +
 reports/diagnostics/candidate_lifecycle.md         |   16 +-
 reports/diagnostics/candidate_root_cause.md        |   42 +-
 reports/diagnostics/dataset_validation_summary.md  |    4 +-
 reports/diagnostics/document_trace.md              |  155 +-
 reports/diagnostics/extraction_trace.md            |   10 +-
 reports/diagnostics/false_negative_analysis.md     |   12 +-
 reports/diagnostics/integrity_trace.md             |  246 +-
 reports/diagnostics/knowledge_gap_trace.md         |    6 +-
 reports/diagnostics/mission_trace.md               |    4 +-
 reports/diagnostics/publish_trace.md               |   16 +-
 reports/diagnostics/publisher_trace.md             |   10 +-
 reports/diagnostics/root_cause_analysis.md         |   32 +-
 reports/diagnostics/rule_impact.md                 |    6 +-
 reports/diagnostics/scheduler_trace.md             |   10 +-
 reports/diagnostics/session_trace.md               |   50 +-
 reports/diagnostics/source_trace.md                |   30 +-
 reports/diagnostics/validation_statistics.md       |    8 +-
 reports/diagnostics/validation_trace.md            |  162 +-
 reports/discovery/accepted_urls.md                 |  221 +-
 reports/discovery/adaptive_budget.md               |   28 +-
 reports/discovery/discovery_capacity.md            |   12 +-
 reports/discovery/environment_audit.md             |    2 +-
 reports/discovery/hard_limit_audit.md              |   16 +-
 reports/discovery/provider_audit.md                |   12 +-
 reports/discovery/provider_exhaustion.md           |    8 +-
 reports/discovery/provider_health.md               |    4 +-
 reports/discovery/provider_ranking.md              |   10 +-
 reports/discovery/provider_statistics.md           |   20 +-
 reports/discovery/provider_yield.md                |   10 +-
 reports/discovery/query_statistics.md              |   66 +-
 reports/discovery/rejected_urls.md                 |   55 +-
 reports/discovery/reputation_scores.md             |   35 +-
 reports/discovery/throughput_analysis.md           |   10 +-
 reports/discovery/trusted_source_usage.md          |   24 +-
 reports/enterprise/coverage_by_function.md         |    2 +-
 reports/enterprise/enterprise_state.json           |   20 +-
 reports/enterprise/production_distribution.md      |   12 +-
 reports/fulltext/acquisition_success.md            |   86 +-
 reports/fulltext/content_richness.md               |   10 +-
 reports/fulltext/doi_resolution.md                 |   10 +-
 reports/fulltext/fallback_chain.md                 |    2 +-
 reports/fulltext/fulltext_statistics.md            |   14 +-
 reports/fulltext/knowledge_gain_projection.md      |   16 +-
 reports/fulltext/publisher_resolution.md           |    6 +-
 reports/fulltext/repository_statistics.md          |    6 +-
 reports/fulltext/representation_quality.md         |   10 +-
 reports/fulltext/validation_before_after.md        |   14 +-
 reports/manufacturing/factory_economics.md         |   30 +-
 reports/manufacturing/growth_velocity.md           |   48 +-
 reports/manufacturing/knowledge_gap.md             |    4 +-
 reports/manufacturing/knowledge_universe.md        |    2 +-
 reports/manufacturing/production_capacity.md       |   20 +-
 reports/performance/api_statistics.md              |   14 +-
 reports/performance/auto_publish.md                |    2 +-
 reports/performance/cache_statistics.md            |    4 +-
 reports/performance/connector_performance.md       |   16 +-
 reports/performance/connector_ranking.md           |   16 +-
 reports/performance/crawler_statistics.md          |   51 +-
 reports/performance/download_statistics.md         |   20 +-
 reports/performance/extraction_statistics.md       |   37 +-
 reports/performance/factory_capacity.md            |   22 +-
 reports/performance/pipeline_bottleneck.md         |   50 +-
 reports/performance/production_capacity.md         |   16 +-
 reports/performance/queue_efficiency.md            |   10 +-
 reports/performance/session_efficiency.md          |   14 +-
 reports/performance/source_efficiency.md           |   16 +-
 reports/performance/source_ranking.md              |   35 +-
 reports/performance/stage_timings.md               |   12 +-
 reports/performance/throughput.md                  |   16 +-
 reports/performance/throughput_report.md           |   20 +-
 reports/performance/worker_utilization.md          |   10 +-
 reports/production/candidate_pipeline.md           |   24 +-
 reports/production/connector_summary.md            |   38 +-
 reports/production/document_pipeline.md            |  155 +-
 reports/production/evidence_trace.md               |   60 +-
 reports/production/production_trace.md             |   44 +-
 reports/production/publish_pipeline.md             |   14 +-
 reports/production/runtime_statistics.md           |   56 +-
 reports/reliability/git_worktree_trace.md          |   23 +
 reports/reliability/writer_finalize.json           |    2 +-
 93 files changed, 4187 insertions(+), 3626 deletions(-)
```

## pre_acquire

- **time:** 2026-07-11T18:43:36Z
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

- **time:** 2026-07-11T18:55:53Z
- **dirty_count:** 91

### status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-11.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M reports/diagnostics/candidate_lifecycle.md
 M reports/diagnostics/candidate_root_cause.md
 M reports/diagnostics/dataset_validation_summary.md
 M reports/diagnostics/document_trace.md
 M reports/diagnostics/extraction_trace.md
 M reports/diagnostics/false_negative_analysis.md
 M reports/diagnostics/integrity_trace.md
 M reports/diagnostics/knowledge_gap_trace.md
 M reports/diagnostics/mission_trace.md
 M reports/diagnostics/publish_trace.md
 M reports/diagnostics/publisher_trace.md
 M reports/diagnostics/root_cause_analysis.md
 M reports/diagnostics/rule_impact.md
 M reports/diagnostics/scheduler_trace.md
 M reports/diagnostics/session_trace.md
 M reports/diagnostics/source_trace.md
 M reports/diagnostics/validation_statistics.md
 M reports/diagnostics/validation_trace.md
 M reports/discovery/accepted_urls.md
 M reports/discovery/adaptive_budget.md
 M reports/discovery/discovery_capacity.md
 M reports/discovery/environment_audit.md
 M reports/discovery/hard_limit_audit.md
 M reports/discovery/provider_audit.md
 M reports/discovery/provider_exhaustion.md
 M reports/discovery/provider_health.md
 M reports/discovery/provider_ranking.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/provider_yield.md
 M reports/discovery/query_statistics.md
 M reports/discovery/rejected_urls.md
 M reports/discovery/reputation_scores.md
 M reports/discovery/throughput_analysis.md
 M reports/discovery/trusted_source_usage.md
 M reports/fulltext/acquisition_success.md
 M reports/fulltext/content_richness.md
 M reports/fulltext/doi_resolution.md
 M reports/fulltext/fallback_chain.md
 M reports/fulltext/fulltext_statistics.md
 M reports/fulltext/knowledge_gain_projection.md
 M reports/fulltext/publisher_resolution.md
 M reports/fulltext/repository_statistics.md
 M reports/fulltext/representation_quality.md
 M reports/fulltext/validation_before_after.md
 M reports/manufacturing/factory_economics.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/production_capacity.md
 M reports/performance/api_statistics.md
 M reports/performance/auto_publish.md
 M reports/performance/cache_statistics.md
 M reports/performance/connector_performance.md
 M reports/performance/connector_ranking.md
 M reports/performance/crawler_statistics.md
 M reports/performance/download_statistics.md
 M reports/performance/extraction_statistics.md
 M reports/performance/factory_capacity.md
 M reports/performance/pipeline_bottleneck.md
 M reports/performance/production_capacity.md
 M reports/performance/queue_efficiency.md
 M reports/performance/session_efficiency.md
 M reports/performance/source_efficiency.md
 M reports/performance/source_ranking.md
 M reports/performance/stage_timings.md
 M reports/performance/throughput.md
 M reports/performance/throughput_report.md
 M reports/performance/worker_utilization.md
 M reports/production/candidate_pipeline.md
 M reports/production/connector_summary.md
 M reports/production/document_pipeline.md
 M reports/production/evidence_trace.md
 M reports/production/production_trace.md
 M reports/production/publish_pipeline.md
 M reports/production/runtime_statistics.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-1C026A.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-9942B1.json
?? reports/production/production_trace_SES-20260711-1C026A.json
?? reports/production/sessions/SES-20260711-1C026A/
```

### diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-11.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
reports/diagnostics/candidate_lifecycle.md
reports/diagnostics/candidate_root_cause.md
reports/diagnostics/dataset_validation_summary.md
reports/diagnostics/document_trace.md
reports/diagnostics/extraction_trace.md
reports/diagnostics/false_negative_analysis.md
reports/diagnostics/integrity_trace.md
reports/diagnostics/knowledge_gap_trace.md
reports/diagnostics/mission_trace.md
reports/diagnostics/publish_trace.md
reports/diagnostics/publisher_trace.md
reports/diagnostics/root_cause_analysis.md
reports/diagnostics/rule_impact.md
reports/diagnostics/scheduler_trace.md
reports/diagnostics/session_trace.md
reports/diagnostics/source_trace.md
reports/diagnostics/validation_statistics.md
reports/diagnostics/validation_trace.md
reports/discovery/accepted_urls.md
reports/discovery/adaptive_budget.md
reports/discovery/discovery_capacity.md
reports/discovery/environment_audit.md
reports/discovery/hard_limit_audit.md
reports/discovery/provider_audit.md
reports/discovery/provider_exhaustion.md
reports/discovery/provider_health.md
reports/discovery/provider_ranking.md
reports/discovery/provider_statistics.md
reports/discovery/provider_yield.md
reports/discovery/query_statistics.md
reports/discovery/rejected_urls.md
reports/discovery/reputation_scores.md
reports/discovery/throughput_analysis.md
reports/discovery/trusted_source_usage.md
reports/fulltext/acquisition_success.md
reports/fulltext/content_richness.md
reports/fulltext/doi_resolution.md
reports/fulltext/fallback_chain.md
reports/fulltext/fulltext_statistics.md
reports/fulltext/knowledge_gain_projection.md
reports/fulltext/publisher_resolution.md
reports/fulltext/repository_statistics.md
reports/fulltext/representation_quality.md
reports/fulltext/validation_before_after.md
reports/manufacturing/factory_economics.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/production_capacity.md
reports/performance/api_statistics.md
reports/performance/auto_publish.md
reports/performance/cache_statistics.md
reports/performance/connector_performance.md
reports/performance/connector_ranking.md
reports/performance/crawler_statistics.md
reports/performance/download_statistics.md
reports/performance/extraction_statistics.md
reports/performance/factory_capacity.md
reports/performance/pipeline_bottleneck.md
reports/performance/production_capacity.md
reports/performance/queue_efficiency.md
reports/performance/session_efficiency.md
reports/performance/source_efficiency.md
reports/performance/source_ranking.md
reports/performance/stage_timings.md
reports/performance/throughput.md
reports/performance/throughput_report.md
reports/performance/worker_utilization.md
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
 .../learning/state/acquisition_performance.json    |  411 ++--
 automation/learning/state/current_snapshot.json    |    2 +-
 automation/learning/state/discovery_analytics.json | 1406 ++++---------
 automation/learning/state/learning_journal.jsonl   |  388 ++++
 automation/learning/state/live_activity.json       |   10 +-
 automation/learning/state/manufacturing_state.json |  244 ++-
 automation/learning/state/production_trace.json    | 2096 +++++++++-----------
 automation/learning/state/snapshot_2026-07-11.json |    2 +-
 automation/learning/state/source_health.json       |    2 +-
 automation/learning/state/source_performance.json  |   78 +-
 automation/sessions/index.json                     |   30 +-
 reports/diagnostics/candidate_lifecycle.md         |   17 +-
 reports/diagnostics/candidate_root_cause.md        |   40 +-
 reports/diagnostics/dataset_validation_summary.md  |    4 +-
 reports/diagnostics/document_trace.md              |  159 +-
 reports/diagnostics/extraction_trace.md            |    9 +-
 reports/diagnostics/false_negative_analysis.md     |    8 +-
 reports/diagnostics/integrity_trace.md             |  183 +-
 reports/diagnostics/knowledge_gap_trace.md         |    2 +-
 reports/diagnostics/mission_trace.md               |    2 +-
 reports/diagnostics/publish_trace.md               |   17 +-
 reports/diagnostics/publisher_trace.md             |    9 +-
 reports/diagnostics/root_cause_analysis.md         |   46 +-
 reports/diagnostics/rule_impact.md                 |    5 +-
 reports/diagnostics/scheduler_trace.md             |    8 +-
 reports/diagnostics/session_trace.md               |   54 +-
 reports/diagnostics/source_trace.md                |   30 +-
 reports/diagnostics/validation_statistics.md       |   10 +-
 reports/diagnostics/validation_trace.md            |   96 +-
 reports/discovery/accepted_urls.md                 |  260 +--
 reports/discovery/adaptive_budget.md               |   12 +-
 reports/discovery/discovery_capacity.md            |    4 +-
 reports/discovery/environment_audit.md             |    2 +-
 reports/discovery/hard_limit_audit.md              |    4 +-
 reports/discovery/provider_audit.md                |   12 +-
 reports/discovery/provider_exhaustion.md           |    8 +-
 reports/discovery/provider_health.md               |    4 +-
 reports/discovery/provider_ranking.md              |   10 +-
 reports/discovery/provider_statistics.md           |   26 +-
 reports/discovery/provider_yield.md                |   10 +-
 reports/discovery/query_statistics.md              |   65 +-
 reports/discovery/rejected_urls.md                 |   52 +-
 reports/discovery/reputation_scores.md             |   14 +-
 reports/discovery/throughput_analysis.md           |   12 +-
 reports/discovery/trusted_source_usage.md          |   19 +-
 reports/fulltext/acquisition_success.md            |   82 +-
 reports/fulltext/content_richness.md               |   10 +-
 reports/fulltext/doi_resolution.md                 |   14 +-
 reports/fulltext/fallback_chain.md                 |    2 +-
 reports/fulltext/fulltext_statistics.md            |   16 +-
 reports/fulltext/knowledge_gain_projection.md      |   16 +-
 reports/fulltext/publisher_resolution.md           |    4 +-
 reports/fulltext/repository_statistics.md          |    4 +-
 reports/fulltext/representation_quality.md         |   10 +-
 reports/fulltext/validation_before_after.md        |   14 +-
 reports/manufacturing/factory_economics.md         |   28 +-
 reports/manufacturing/growth_velocity.md           |   36 +-
 reports/manufacturing/knowledge_gap.md             |    2 +-
 reports/manufacturing/production_capacity.md       |   14 +-
 reports/performance/api_statistics.md              |   14 +-
 reports/performance/auto_publish.md                |    8 +-
 reports/performance/cache_statistics.md            |    4 +-
 reports/performance/connector_performance.md       |   16 +-
 reports/performance/connector_ranking.md           |   16 +-
 reports/performance/crawler_statistics.md          |   58 +-
 reports/performance/download_statistics.md         |   28 +-
 reports/performance/extraction_statistics.md       |   28 +-
 reports/performance/factory_capacity.md            |   24 +-
 reports/performance/pipeline_bottleneck.md         |   48 +-
 reports/performance/production_capacity.md         |   16 +-
 reports/performance/queue_efficiency.md            |   14 +-
 reports/performance/session_efficiency.md          |   12 +-
 reports/performance/source_efficiency.md           |   16 +-
 reports/performance/source_ranking.md              |   14 +-
 reports/performance/stage_timings.md               |   12 +-
 reports/performance/throughput.md                  |   18 +-
 reports/performance/throughput_report.md           |   20 +-
 reports/performance/worker_utilization.md          |   14 +-
 reports/production/candidate_pipeline.md           |   25 +-
 reports/production/connector_summary.md            |   76 +-
 reports/production/document_pipeline.md            |  155 +-
 reports/production/evidence_trace.md               |   26 +-
 reports/production/production_trace.md             |   46 +-
 reports/production/publish_pipeline.md             |   20 +-
 reports/production/runtime_statistics.md           |   64 +-
 reports/reliability/git_worktree_trace.md          |   23 +
 reports/reliability/writer_finalize.json           |    2 +-
 87 files changed, 3172 insertions(+), 3779 deletions(-)
```

## pre_acquire

- **time:** 2026-07-11T19:07:37Z
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

- **time:** 2026-07-11T19:28:15Z
- **dirty_count:** 95

### status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/daily_2026-07-11.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-11.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M domains/business_development/business_signal_library.csv
 M reports/diagnostics/candidate_lifecycle.md
 M reports/diagnostics/candidate_root_cause.md
 M reports/diagnostics/dataset_validation_summary.md
 M reports/diagnostics/document_trace.md
 M reports/diagnostics/extraction_trace.md
 M reports/diagnostics/false_negative_analysis.md
 M reports/diagnostics/integrity_trace.md
 M reports/diagnostics/knowledge_gap_trace.md
 M reports/diagnostics/mission_trace.md
 M reports/diagnostics/publish_trace.md
 M reports/diagnostics/publisher_trace.md
 M reports/diagnostics/root_cause_analysis.md
 M reports/diagnostics/rule_impact.md
 M reports/diagnostics/scheduler_trace.md
 M reports/diagnostics/session_trace.md
 M reports/diagnostics/source_trace.md
 M reports/diagnostics/validation_statistics.md
 M reports/diagnostics/validation_trace.md
 M reports/discovery/accepted_urls.md
 M reports/discovery/adaptive_budget.md
 M reports/discovery/discovery_capacity.md
 M reports/discovery/environment_audit.md
 M reports/discovery/hard_limit_audit.md
 M reports/discovery/provider_audit.md
 M reports/discovery/provider_exhaustion.md
 M reports/discovery/provider_health.md
 M reports/discovery/provider_ranking.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/provider_yield.md
 M reports/discovery/query_statistics.md
 M reports/discovery/rejected_urls.md
 M reports/discovery/reputation_scores.md
 M reports/discovery/throughput_analysis.md
 M reports/discovery/trusted_source_usage.md
 M reports/fulltext/acquisition_success.md
 M reports/fulltext/content_richness.md
 M reports/fulltext/doi_resolution.md
 M reports/fulltext/fallback_chain.md
 M reports/fulltext/fulltext_statistics.md
 M reports/fulltext/knowledge_gain_projection.md
 M reports/fulltext/publisher_resolution.md
 M reports/fulltext/repository_statistics.md
 M reports/fulltext/representation_quality.md
 M reports/fulltext/validation_before_after.md
 M reports/manufacturing/factory_economics.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/knowledge_universe.md
 M reports/manufacturing/production_capacity.md
 M reports/manufacturing/scheduler_decisions.md
 M reports/performance/api_statistics.md
 M reports/performance/auto_publish.md
 M reports/performance/cache_statistics.md
 M reports/performance/connector_performance.md
 M reports/performance/connector_ranking.md
 M reports/performance/crawler_statistics.md
 M reports/performance/download_statistics.md
 M reports/performance/extraction_statistics.md
 M reports/performance/factory_capacity.md
 M reports/performance/pipeline_bottleneck.md
 M reports/performance/production_capacity.md
 M reports/performance/queue_efficiency.md
 M reports/performance/session_efficiency.md
 M reports/performance/source_efficiency.md
 M reports/performance/source_ranking.md
 M reports/performance/stage_timings.md
 M reports/performance/throughput.md
 M reports/performance/throughput_report.md
 M reports/performance/worker_utilization.md
 M reports/production/candidate_pipeline.md
 M reports/production/connector_summary.md
 M reports/production/document_pipeline.md
 M reports/production/evidence_trace.md
 M reports/production/production_trace.md
 M reports/production/publish_pipeline.md
 M reports/production/runtime_statistics.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-FA8B7C.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-FC647C.json
?? reports/production/production_trace_SES-20260711-FA8B7C.json
?? reports/production/sessions/SES-20260711-FA8B7C/
```

### diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/daily_2026-07-11.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-11.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
domains/business_development/business_signal_library.csv
reports/diagnostics/candidate_lifecycle.md
reports/diagnostics/candidate_root_cause.md
reports/diagnostics/dataset_validation_summary.md
reports/diagnostics/document_trace.md
reports/diagnostics/extraction_trace.md
reports/diagnostics/false_negative_analysis.md
reports/diagnostics/integrity_trace.md
reports/diagnostics/knowledge_gap_trace.md
reports/diagnostics/mission_trace.md
reports/diagnostics/publish_trace.md
reports/diagnostics/publisher_trace.md
reports/diagnostics/root_cause_analysis.md
reports/diagnostics/rule_impact.md
reports/diagnostics/scheduler_trace.md
reports/diagnostics/session_trace.md
reports/diagnostics/source_trace.md
reports/diagnostics/validation_statistics.md
reports/diagnostics/validation_trace.md
reports/discovery/accepted_urls.md
reports/discovery/adaptive_budget.md
reports/discovery/discovery_capacity.md
reports/discovery/environment_audit.md
reports/discovery/hard_limit_audit.md
reports/discovery/provider_audit.md
reports/discovery/provider_exhaustion.md
reports/discovery/provider_health.md
reports/discovery/provider_ranking.md
reports/discovery/provider_statistics.md
reports/discovery/provider_yield.md
reports/discovery/query_statistics.md
reports/discovery/rejected_urls.md
reports/discovery/reputation_scores.md
reports/discovery/throughput_analysis.md
reports/discovery/trusted_source_usage.md
reports/fulltext/acquisition_success.md
reports/fulltext/content_richness.md
reports/fulltext/doi_resolution.md
reports/fulltext/fallback_chain.md
reports/fulltext/fulltext_statistics.md
reports/fulltext/knowledge_gain_projection.md
reports/fulltext/publisher_resolution.md
reports/fulltext/repository_statistics.md
reports/fulltext/representation_quality.md
reports/fulltext/validation_before_after.md
reports/manufacturing/factory_economics.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/knowledge_universe.md
reports/manufacturing/production_capacity.md
reports/manufacturing/scheduler_decisions.md
reports/performance/api_statistics.md
reports/performance/auto_publish.md
reports/performance/cache_statistics.md
reports/performance/connector_performance.md
reports/performance/connector_ranking.md
reports/performance/crawler_statistics.md
reports/performance/download_statistics.md
reports/performance/extraction_statistics.md
reports/performance/factory_capacity.md
reports/performance/pipeline_bottleneck.md
reports/performance/production_capacity.md
reports/performance/queue_efficiency.md
reports/performance/session_efficiency.md
reports/performance/source_efficiency.md
reports/performance/source_ranking.md
reports/performance/stage_timings.md
reports/performance/throughput.md
reports/performance/throughput_report.md
reports/performance/worker_utilization.md
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
 .../learning/state/acquisition_performance.json    |  474 ++--
 automation/learning/state/current_snapshot.json    |    6 +-
 automation/learning/state/daily_2026-07-11.json    |    4 +-
 automation/learning/state/discovery_analytics.json | 1067 +++++----
 automation/learning/state/learning_journal.jsonl   |  493 +++++
 automation/learning/state/live_activity.json       |   10 +-
 automation/learning/state/manufacturing_state.json |  346 +--
 automation/learning/state/production_trace.json    | 2266 ++++++++++++--------
 automation/learning/state/snapshot_2026-07-11.json |    6 +-
 automation/learning/state/source_health.json       |   72 +-
 automation/learning/state/source_performance.json  |   78 +-
 automation/sessions/index.json                     |   30 +-
 .../business_signal_library.csv                    |    5 +
 reports/diagnostics/candidate_lifecycle.md         |   19 +-
 reports/diagnostics/candidate_root_cause.md        |   44 +-
 reports/diagnostics/dataset_validation_summary.md  |    4 +-
 reports/diagnostics/document_trace.md              |  169 +-
 reports/diagnostics/extraction_trace.md            |   11 +-
 reports/diagnostics/false_negative_analysis.md     |   10 +-
 reports/diagnostics/integrity_trace.md             |  263 +--
 reports/diagnostics/knowledge_gap_trace.md         |    6 +-
 reports/diagnostics/mission_trace.md               |    2 +-
 reports/diagnostics/publish_trace.md               |   19 +-
 reports/diagnostics/publisher_trace.md             |   11 +-
 reports/diagnostics/root_cause_analysis.md         |   46 +-
 reports/diagnostics/rule_impact.md                 |    5 +-
 reports/diagnostics/scheduler_trace.md             |    8 +-
 reports/diagnostics/session_trace.md               |   54 +-
 reports/diagnostics/source_trace.md                |   30 +-
 reports/diagnostics/validation_statistics.md       |   10 +-
 reports/diagnostics/validation_trace.md            |  178 +-
 reports/discovery/accepted_urls.md                 |  202 +-
 reports/discovery/adaptive_budget.md               |   28 +-
 reports/discovery/discovery_capacity.md            |   12 +-
 reports/discovery/environment_audit.md             |    2 +-
 reports/discovery/hard_limit_audit.md              |    4 +-
 reports/discovery/provider_audit.md                |   10 +-
 reports/discovery/provider_exhaustion.md           |    8 +-
 reports/discovery/provider_health.md               |    4 +-
 reports/discovery/provider_ranking.md              |    8 +-
 reports/discovery/provider_statistics.md           |   26 +-
 reports/discovery/provider_yield.md                |    8 +-
 reports/discovery/query_statistics.md              |   65 +-
 reports/discovery/rejected_urls.md                 |   33 +-
 reports/discovery/reputation_scores.md             |   35 +-
 reports/discovery/throughput_analysis.md           |   12 +-
 reports/discovery/trusted_source_usage.md          |   23 +-
 reports/fulltext/acquisition_success.md            |   84 +-
 reports/fulltext/content_richness.md               |   10 +-
 reports/fulltext/doi_resolution.md                 |   14 +-
 reports/fulltext/fallback_chain.md                 |    2 +-
 reports/fulltext/fulltext_statistics.md            |   16 +-
 reports/fulltext/knowledge_gain_projection.md      |   16 +-
 reports/fulltext/publisher_resolution.md           |    6 +-
 reports/fulltext/repository_statistics.md          |    6 +-
 reports/fulltext/representation_quality.md         |    8 +-
 reports/fulltext/validation_before_after.md        |   14 +-
 reports/manufacturing/factory_economics.md         |   30 +-
 reports/manufacturing/growth_velocity.md           |   48 +-
 reports/manufacturing/knowledge_gap.md             |    4 +-
 reports/manufacturing/knowledge_universe.md        |    2 +-
 reports/manufacturing/production_capacity.md       |   20 +-
 reports/manufacturing/scheduler_decisions.md       |    2 +-
 reports/performance/api_statistics.md              |   14 +-
 reports/performance/auto_publish.md                |    8 +-
 reports/performance/cache_statistics.md            |    4 +-
 reports/performance/connector_performance.md       |   16 +-
 reports/performance/connector_ranking.md           |   16 +-
 reports/performance/crawler_statistics.md          |   67 +-
 reports/performance/download_statistics.md         |   28 +-
 reports/performance/extraction_statistics.md       |   41 +-
 reports/performance/factory_capacity.md            |   20 +-
 reports/performance/pipeline_bottleneck.md         |   44 +-
 reports/performance/production_capacity.md         |   12 +-
 reports/performance/queue_efficiency.md            |   14 +-
 reports/performance/session_efficiency.md          |    6 +-
 reports/performance/source_efficiency.md           |   16 +-
 reports/performance/source_ranking.md              |   35 +-
 reports/performance/stage_timings.md               |   12 +-
 reports/performance/throughput.md                  |   18 +-
 reports/performance/throughput_report.md           |   18 +-
 reports/performance/worker_utilization.md          |   14 +-
 reports/production/candidate_pipeline.md           |   29 +-
 reports/production/connector_summary.md            |   70 +-
 reports/production/document_pipeline.md            |  165 +-
 reports/production/evidence_trace.md               |   52 +-
 reports/production/production_trace.md             |   44 +-
 reports/production/publish_pipeline.md             |   20 +-
 reports/production/runtime_statistics.md           |   62 +-
 reports/reliability/git_worktree_trace.md          |   23 +
 reports/reliability/writer_finalize.json           |    2 +-
 91 files changed, 4428 insertions(+), 2950 deletions(-)
```

## pre_acquire

- **time:** 2026-07-11T20:51:06Z
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

- **time:** 2026-07-11T21:10:32Z
- **dirty_count:** 94

### status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/daily_2026-07-11.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-11.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M domains/business_development/business_signal_library.csv
 M reports/diagnostics/candidate_lifecycle.md
 M reports/diagnostics/candidate_root_cause.md
 M reports/diagnostics/dataset_validation_summary.md
 M reports/diagnostics/document_trace.md
 M reports/diagnostics/extraction_trace.md
 M reports/diagnostics/false_negative_analysis.md
 M reports/diagnostics/integrity_trace.md
 M reports/diagnostics/knowledge_gap_trace.md
 M reports/diagnostics/mission_trace.md
 M reports/diagnostics/publish_trace.md
 M reports/diagnostics/publisher_trace.md
 M reports/diagnostics/root_cause_analysis.md
 M reports/diagnostics/rule_impact.md
 M reports/diagnostics/scheduler_trace.md
 M reports/diagnostics/session_trace.md
 M reports/diagnostics/source_trace.md
 M reports/diagnostics/validation_statistics.md
 M reports/diagnostics/validation_trace.md
 M reports/discovery/accepted_urls.md
 M reports/discovery/adaptive_budget.md
 M reports/discovery/discovery_capacity.md
 M reports/discovery/environment_audit.md
 M reports/discovery/hard_limit_audit.md
 M reports/discovery/provider_audit.md
 M reports/discovery/provider_exhaustion.md
 M reports/discovery/provider_health.md
 M reports/discovery/provider_ranking.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/provider_yield.md
 M reports/discovery/query_statistics.md
 M reports/discovery/rejected_urls.md
 M reports/discovery/reputation_scores.md
 M reports/discovery/throughput_analysis.md
 M reports/discovery/trusted_source_usage.md
 M reports/fulltext/acquisition_success.md
 M reports/fulltext/content_richness.md
 M reports/fulltext/doi_resolution.md
 M reports/fulltext/fallback_chain.md
 M reports/fulltext/fulltext_statistics.md
 M reports/fulltext/knowledge_gain_projection.md
 M reports/fulltext/publisher_resolution.md
 M reports/fulltext/repository_statistics.md
 M reports/fulltext/representation_quality.md
 M reports/fulltext/validation_before_after.md
 M reports/manufacturing/factory_economics.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/knowledge_universe.md
 M reports/manufacturing/production_capacity.md
 M reports/manufacturing/scheduler_decisions.md
 M reports/performance/api_statistics.md
 M reports/performance/cache_statistics.md
 M reports/performance/connector_performance.md
 M reports/performance/connector_ranking.md
 M reports/performance/crawler_statistics.md
 M reports/performance/download_statistics.md
 M reports/performance/extraction_statistics.md
 M reports/performance/factory_capacity.md
 M reports/performance/pipeline_bottleneck.md
 M reports/performance/production_capacity.md
 M reports/performance/queue_efficiency.md
 M reports/performance/session_efficiency.md
 M reports/performance/source_efficiency.md
 M reports/performance/source_ranking.md
 M reports/performance/stage_timings.md
 M reports/performance/throughput.md
 M reports/performance/throughput_report.md
 M reports/performance/worker_utilization.md
 M reports/production/candidate_pipeline.md
 M reports/production/connector_summary.md
 M reports/production/document_pipeline.md
 M reports/production/evidence_trace.md
 M reports/production/production_trace.md
 M reports/production/publish_pipeline.md
 M reports/production/runtime_statistics.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-AB2D95.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-EDE650.json
?? reports/production/production_trace_SES-20260711-AB2D95.json
?? reports/production/sessions/SES-20260711-AB2D95/
```

### diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/daily_2026-07-11.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-11.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
domains/business_development/business_signal_library.csv
reports/diagnostics/candidate_lifecycle.md
reports/diagnostics/candidate_root_cause.md
reports/diagnostics/dataset_validation_summary.md
reports/diagnostics/document_trace.md
reports/diagnostics/extraction_trace.md
reports/diagnostics/false_negative_analysis.md
reports/diagnostics/integrity_trace.md
reports/diagnostics/knowledge_gap_trace.md
reports/diagnostics/mission_trace.md
reports/diagnostics/publish_trace.md
reports/diagnostics/publisher_trace.md
reports/diagnostics/root_cause_analysis.md
reports/diagnostics/rule_impact.md
reports/diagnostics/scheduler_trace.md
reports/diagnostics/session_trace.md
reports/diagnostics/source_trace.md
reports/diagnostics/validation_statistics.md
reports/diagnostics/validation_trace.md
reports/discovery/accepted_urls.md
reports/discovery/adaptive_budget.md
reports/discovery/discovery_capacity.md
reports/discovery/environment_audit.md
reports/discovery/hard_limit_audit.md
reports/discovery/provider_audit.md
reports/discovery/provider_exhaustion.md
reports/discovery/provider_health.md
reports/discovery/provider_ranking.md
reports/discovery/provider_statistics.md
reports/discovery/provider_yield.md
reports/discovery/query_statistics.md
reports/discovery/rejected_urls.md
reports/discovery/reputation_scores.md
reports/discovery/throughput_analysis.md
reports/discovery/trusted_source_usage.md
reports/fulltext/acquisition_success.md
reports/fulltext/content_richness.md
reports/fulltext/doi_resolution.md
reports/fulltext/fallback_chain.md
reports/fulltext/fulltext_statistics.md
reports/fulltext/knowledge_gain_projection.md
reports/fulltext/publisher_resolution.md
reports/fulltext/repository_statistics.md
reports/fulltext/representation_quality.md
reports/fulltext/validation_before_after.md
reports/manufacturing/factory_economics.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/knowledge_universe.md
reports/manufacturing/production_capacity.md
reports/manufacturing/scheduler_decisions.md
reports/performance/api_statistics.md
reports/performance/cache_statistics.md
reports/performance/connector_performance.md
reports/performance/connector_ranking.md
reports/performance/crawler_statistics.md
reports/performance/download_statistics.md
reports/performance/extraction_statistics.md
reports/performance/factory_capacity.md
reports/performance/pipeline_bottleneck.md
reports/performance/production_capacity.md
reports/performance/queue_efficiency.md
reports/performance/session_efficiency.md
reports/performance/source_efficiency.md
reports/performance/source_ranking.md
reports/performance/stage_timings.md
reports/performance/throughput.md
reports/performance/throughput_report.md
reports/performance/worker_utilization.md
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
 .../learning/state/acquisition_performance.json    |  294 +--
 automation/learning/state/current_snapshot.json    |    6 +-
 automation/learning/state/daily_2026-07-11.json    |    4 +-
 automation/learning/state/discovery_analytics.json |  856 +++++--
 automation/learning/state/learning_journal.jsonl   |  631 ++++++
 automation/learning/state/live_activity.json       |    8 +-
 automation/learning/state/manufacturing_state.json |  297 ++-
 automation/learning/state/production_trace.json    | 2392 +++++++++++++-------
 automation/learning/state/snapshot_2026-07-11.json |    6 +-
 automation/learning/state/source_health.json       |   86 +-
 automation/learning/state/source_performance.json  |   78 +-
 automation/sessions/index.json                     |   30 +-
 .../business_signal_library.csv                    |    5 +
 reports/diagnostics/candidate_lifecycle.md         |   16 +-
 reports/diagnostics/candidate_root_cause.md        |   32 +-
 reports/diagnostics/dataset_validation_summary.md  |    4 +-
 reports/diagnostics/document_trace.md              |  132 +-
 reports/diagnostics/extraction_trace.md            |   12 +-
 reports/diagnostics/false_negative_analysis.md     |   12 +-
 reports/diagnostics/integrity_trace.md             |  116 +-
 reports/diagnostics/knowledge_gap_trace.md         |    6 +-
 reports/diagnostics/mission_trace.md               |    2 +-
 reports/diagnostics/publish_trace.md               |   12 +-
 reports/diagnostics/publisher_trace.md             |   12 +-
 reports/diagnostics/root_cause_analysis.md         |   16 +-
 reports/diagnostics/rule_impact.md                 |    6 +-
 reports/diagnostics/scheduler_trace.md             |    8 +-
 reports/diagnostics/session_trace.md               |   28 +-
 reports/diagnostics/source_trace.md                |   30 +-
 reports/diagnostics/validation_statistics.md       |    2 +-
 reports/diagnostics/validation_trace.md            |  124 +-
 reports/discovery/accepted_urls.md                 |  122 +-
 reports/discovery/adaptive_budget.md               |    2 +-
 reports/discovery/discovery_capacity.md            |    2 +-
 reports/discovery/environment_audit.md             |    2 +-
 reports/discovery/hard_limit_audit.md              |    4 +-
 reports/discovery/provider_audit.md                |    8 +-
 reports/discovery/provider_exhaustion.md           |    6 +-
 reports/discovery/provider_health.md               |    4 +-
 reports/discovery/provider_ranking.md              |    6 +-
 reports/discovery/provider_statistics.md           |   20 +-
 reports/discovery/provider_yield.md                |    6 +-
 reports/discovery/query_statistics.md              |   36 +-
 reports/discovery/rejected_urls.md                 |   25 +
 reports/discovery/reputation_scores.md             |    6 +-
 reports/discovery/throughput_analysis.md           |   10 +-
 reports/discovery/trusted_source_usage.md          |   10 +-
 reports/fulltext/acquisition_success.md            |   50 +-
 reports/fulltext/content_richness.md               |   10 +-
 reports/fulltext/doi_resolution.md                 |   14 +-
 reports/fulltext/fallback_chain.md                 |    2 +-
 reports/fulltext/fulltext_statistics.md            |   16 +-
 reports/fulltext/knowledge_gain_projection.md      |   16 +-
 reports/fulltext/publisher_resolution.md           |    6 +-
 reports/fulltext/repository_statistics.md          |    6 +-
 reports/fulltext/representation_quality.md         |   10 +-
 reports/fulltext/validation_before_after.md        |   14 +-
 reports/manufacturing/factory_economics.md         |   28 +-
 reports/manufacturing/growth_velocity.md           |   46 +-
 reports/manufacturing/knowledge_gap.md             |    4 +-
 reports/manufacturing/knowledge_universe.md        |    2 +-
 reports/manufacturing/production_capacity.md       |   20 +-
 reports/manufacturing/scheduler_decisions.md       |    2 +-
 reports/performance/api_statistics.md              |   14 +-
 reports/performance/cache_statistics.md            |    4 +-
 reports/performance/connector_performance.md       |   16 +-
 reports/performance/connector_ranking.md           |   16 +-
 reports/performance/crawler_statistics.md          |   56 +-
 reports/performance/download_statistics.md         |   26 +-
 reports/performance/extraction_statistics.md       |   26 +-
 reports/performance/factory_capacity.md            |   20 +-
 reports/performance/pipeline_bottleneck.md         |   48 +-
 reports/performance/production_capacity.md         |   16 +-
 reports/performance/queue_efficiency.md            |    4 +-
 reports/performance/session_efficiency.md          |   14 +-
 reports/performance/source_efficiency.md           |   16 +-
 reports/performance/source_ranking.md              |    6 +-
 reports/performance/stage_timings.md               |   12 +-
 reports/performance/throughput.md                  |   16 +-
 reports/performance/throughput_report.md           |   18 +-
 reports/performance/worker_utilization.md          |   10 +-
 reports/production/candidate_pipeline.md           |   12 +-
 reports/production/connector_summary.md            |   34 +-
 reports/production/document_pipeline.md            |  128 +-
 reports/production/evidence_trace.md               |   50 +-
 reports/production/production_trace.md             |   34 +-
 reports/production/publish_pipeline.md             |    2 +-
 reports/production/runtime_statistics.md           |   34 +-
 reports/reliability/git_worktree_trace.md          |   23 +
 reports/reliability/writer_finalize.json           |    2 +-
 90 files changed, 4223 insertions(+), 2212 deletions(-)
```

## pre_acquire

- **time:** 2026-07-11T21:51:33Z
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

- **time:** 2026-07-11T22:15:38Z
- **dirty_count:** 94

### status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/daily_2026-07-11.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-11.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M domains/business_development/business_signal_library.csv
 M reports/diagnostics/candidate_lifecycle.md
 M reports/diagnostics/candidate_root_cause.md
 M reports/diagnostics/dataset_validation_summary.md
 M reports/diagnostics/document_trace.md
 M reports/diagnostics/extraction_trace.md
 M reports/diagnostics/false_negative_analysis.md
 M reports/diagnostics/integrity_trace.md
 M reports/diagnostics/knowledge_gap_trace.md
 M reports/diagnostics/mission_trace.md
 M reports/diagnostics/publish_trace.md
 M reports/diagnostics/publisher_trace.md
 M reports/diagnostics/root_cause_analysis.md
 M reports/diagnostics/rule_impact.md
 M reports/diagnostics/scheduler_trace.md
 M reports/diagnostics/session_trace.md
 M reports/diagnostics/source_trace.md
 M reports/diagnostics/validation_statistics.md
 M reports/diagnostics/validation_trace.md
 M reports/discovery/accepted_urls.md
 M reports/discovery/adaptive_budget.md
 M reports/discovery/discovery_capacity.md
 M reports/discovery/environment_audit.md
 M reports/discovery/hard_limit_audit.md
 M reports/discovery/provider_audit.md
 M reports/discovery/provider_exhaustion.md
 M reports/discovery/provider_health.md
 M reports/discovery/provider_ranking.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/provider_yield.md
 M reports/discovery/query_statistics.md
 M reports/discovery/rejected_urls.md
 M reports/discovery/reputation_scores.md
 M reports/discovery/throughput_analysis.md
 M reports/discovery/trusted_source_usage.md
 M reports/fulltext/acquisition_success.md
 M reports/fulltext/content_richness.md
 M reports/fulltext/doi_resolution.md
 M reports/fulltext/fallback_chain.md
 M reports/fulltext/fulltext_statistics.md
 M reports/fulltext/knowledge_gain_projection.md
 M reports/fulltext/publisher_resolution.md
 M reports/fulltext/repository_statistics.md
 M reports/fulltext/representation_quality.md
 M reports/fulltext/validation_before_after.md
 M reports/manufacturing/factory_economics.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/knowledge_universe.md
 M reports/manufacturing/production_capacity.md
 M reports/manufacturing/scheduler_decisions.md
 M reports/performance/api_statistics.md
 M reports/performance/cache_statistics.md
 M reports/performance/connector_performance.md
 M reports/performance/connector_ranking.md
 M reports/performance/crawler_statistics.md
 M reports/performance/download_statistics.md
 M reports/performance/extraction_statistics.md
 M reports/performance/factory_capacity.md
 M reports/performance/pipeline_bottleneck.md
 M reports/performance/production_capacity.md
 M reports/performance/queue_efficiency.md
 M reports/performance/session_efficiency.md
 M reports/performance/source_efficiency.md
 M reports/performance/source_ranking.md
 M reports/performance/stage_timings.md
 M reports/performance/throughput.md
 M reports/performance/throughput_report.md
 M reports/performance/worker_utilization.md
 M reports/production/candidate_pipeline.md
 M reports/production/connector_summary.md
 M reports/production/document_pipeline.md
 M reports/production/evidence_trace.md
 M reports/production/production_trace.md
 M reports/production/publish_pipeline.md
 M reports/production/runtime_statistics.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-D442E3.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-4D5D42.json
?? reports/production/production_trace_SES-20260711-D442E3.json
?? reports/production/sessions/SES-20260711-D442E3/
```

### diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/daily_2026-07-11.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-11.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
domains/business_development/business_signal_library.csv
reports/diagnostics/candidate_lifecycle.md
reports/diagnostics/candidate_root_cause.md
reports/diagnostics/dataset_validation_summary.md
reports/diagnostics/document_trace.md
reports/diagnostics/extraction_trace.md
reports/diagnostics/false_negative_analysis.md
reports/diagnostics/integrity_trace.md
reports/diagnostics/knowledge_gap_trace.md
reports/diagnostics/mission_trace.md
reports/diagnostics/publish_trace.md
reports/diagnostics/publisher_trace.md
reports/diagnostics/root_cause_analysis.md
reports/diagnostics/rule_impact.md
reports/diagnostics/scheduler_trace.md
reports/diagnostics/session_trace.md
reports/diagnostics/source_trace.md
reports/diagnostics/validation_statistics.md
reports/diagnostics/validation_trace.md
reports/discovery/accepted_urls.md
reports/discovery/adaptive_budget.md
reports/discovery/discovery_capacity.md
reports/discovery/environment_audit.md
reports/discovery/hard_limit_audit.md
reports/discovery/provider_audit.md
reports/discovery/provider_exhaustion.md
reports/discovery/provider_health.md
reports/discovery/provider_ranking.md
reports/discovery/provider_statistics.md
reports/discovery/provider_yield.md
reports/discovery/query_statistics.md
reports/discovery/rejected_urls.md
reports/discovery/reputation_scores.md
reports/discovery/throughput_analysis.md
reports/discovery/trusted_source_usage.md
reports/fulltext/acquisition_success.md
reports/fulltext/content_richness.md
reports/fulltext/doi_resolution.md
reports/fulltext/fallback_chain.md
reports/fulltext/fulltext_statistics.md
reports/fulltext/knowledge_gain_projection.md
reports/fulltext/publisher_resolution.md
reports/fulltext/repository_statistics.md
reports/fulltext/representation_quality.md
reports/fulltext/validation_before_after.md
reports/manufacturing/factory_economics.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/knowledge_universe.md
reports/manufacturing/production_capacity.md
reports/manufacturing/scheduler_decisions.md
reports/performance/api_statistics.md
reports/performance/cache_statistics.md
reports/performance/connector_performance.md
reports/performance/connector_ranking.md
reports/performance/crawler_statistics.md
reports/performance/download_statistics.md
reports/performance/extraction_statistics.md
reports/performance/factory_capacity.md
reports/performance/pipeline_bottleneck.md
reports/performance/production_capacity.md
reports/performance/queue_efficiency.md
reports/performance/session_efficiency.md
reports/performance/source_efficiency.md
reports/performance/source_ranking.md
reports/performance/stage_timings.md
reports/performance/throughput.md
reports/performance/throughput_report.md
reports/performance/worker_utilization.md
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
 .../learning/state/acquisition_performance.json    |  298 +--
 automation/learning/state/current_snapshot.json    |    6 +-
 automation/learning/state/daily_2026-07-11.json    |    4 +-
 automation/learning/state/discovery_analytics.json |  698 +++----
 automation/learning/state/learning_journal.jsonl   |  582 ++++++
 automation/learning/state/live_activity.json       |    8 +-
 automation/learning/state/manufacturing_state.json |  308 +--
 automation/learning/state/production_trace.json    | 2122 +++++++++++---------
 automation/learning/state/snapshot_2026-07-11.json |    6 +-
 automation/learning/state/source_health.json       |   86 +-
 automation/learning/state/source_performance.json  |   96 +-
 automation/sessions/index.json                     |   58 +-
 .../business_signal_library.csv                    |    5 +
 reports/diagnostics/candidate_lifecycle.md         |   16 +-
 reports/diagnostics/candidate_root_cause.md        |   32 +-
 reports/diagnostics/dataset_validation_summary.md  |    4 +-
 reports/diagnostics/document_trace.md              |  125 +-
 reports/diagnostics/extraction_trace.md            |   12 +-
 reports/diagnostics/false_negative_analysis.md     |   12 +-
 reports/diagnostics/integrity_trace.md             |  116 +-
 reports/diagnostics/knowledge_gap_trace.md         |    6 +-
 reports/diagnostics/mission_trace.md               |    2 +-
 reports/diagnostics/publish_trace.md               |   12 +-
 reports/diagnostics/publisher_trace.md             |   12 +-
 reports/diagnostics/root_cause_analysis.md         |   16 +-
 reports/diagnostics/rule_impact.md                 |    6 +-
 reports/diagnostics/scheduler_trace.md             |    8 +-
 reports/diagnostics/session_trace.md               |   28 +-
 reports/diagnostics/source_trace.md                |   30 +-
 reports/diagnostics/validation_statistics.md       |    2 +-
 reports/diagnostics/validation_trace.md            |  124 +-
 reports/discovery/accepted_urls.md                 |  125 +-
 reports/discovery/adaptive_budget.md               |    2 +-
 reports/discovery/discovery_capacity.md            |    2 +-
 reports/discovery/environment_audit.md             |    2 +-
 reports/discovery/hard_limit_audit.md              |   16 +-
 reports/discovery/provider_audit.md                |    8 +-
 reports/discovery/provider_exhaustion.md           |    4 +-
 reports/discovery/provider_health.md               |    4 +-
 reports/discovery/provider_ranking.md              |    6 +-
 reports/discovery/provider_statistics.md           |   20 +-
 reports/discovery/provider_yield.md                |    6 +-
 reports/discovery/query_statistics.md              |   42 +-
 reports/discovery/rejected_urls.md                 |    7 +-
 reports/discovery/reputation_scores.md             |    8 +-
 reports/discovery/throughput_analysis.md           |   10 +-
 reports/discovery/trusted_source_usage.md          |    8 +-
 reports/fulltext/acquisition_success.md            |   56 +-
 reports/fulltext/content_richness.md               |   10 +-
 reports/fulltext/doi_resolution.md                 |    8 +-
 reports/fulltext/fallback_chain.md                 |    2 +-
 reports/fulltext/fulltext_statistics.md            |   16 +-
 reports/fulltext/knowledge_gain_projection.md      |   16 +-
 reports/fulltext/publisher_resolution.md           |    6 +-
 reports/fulltext/repository_statistics.md          |    6 +-
 reports/fulltext/representation_quality.md         |   10 +-
 reports/fulltext/validation_before_after.md        |   14 +-
 reports/manufacturing/factory_economics.md         |   38 +-
 reports/manufacturing/growth_velocity.md           |   40 +-
 reports/manufacturing/knowledge_gap.md             |    4 +-
 reports/manufacturing/knowledge_universe.md        |    2 +-
 reports/manufacturing/production_capacity.md       |   18 +-
 reports/manufacturing/scheduler_decisions.md       |    2 +-
 reports/performance/api_statistics.md              |   14 +-
 reports/performance/cache_statistics.md            |    4 +-
 reports/performance/connector_performance.md       |   16 +-
 reports/performance/connector_ranking.md           |   16 +-
 reports/performance/crawler_statistics.md          |   56 +-
 reports/performance/download_statistics.md         |   26 +-
 reports/performance/extraction_statistics.md       |   26 +-
 reports/performance/factory_capacity.md            |   18 +-
 reports/performance/pipeline_bottleneck.md         |   48 +-
 reports/performance/production_capacity.md         |   16 +-
 reports/performance/queue_efficiency.md            |    4 +-
 reports/performance/session_efficiency.md          |   12 +-
 reports/performance/source_efficiency.md           |   16 +-
 reports/performance/source_ranking.md              |    8 +-
 reports/performance/stage_timings.md               |   12 +-
 reports/performance/throughput.md                  |   16 +-
 reports/performance/throughput_report.md           |   18 +-
 reports/performance/worker_utilization.md          |   10 +-
 reports/production/candidate_pipeline.md           |   12 +-
 reports/production/connector_summary.md            |   22 +-
 reports/production/document_pipeline.md            |  127 +-
 reports/production/evidence_trace.md               |   38 +-
 reports/production/production_trace.md             |   32 +-
 reports/production/publish_pipeline.md             |    2 +-
 reports/production/runtime_statistics.md           |   32 +-
 reports/reliability/git_worktree_trace.md          |   23 +
 reports/reliability/writer_finalize.json           |    2 +-
 90 files changed, 3321 insertions(+), 2663 deletions(-)
```

