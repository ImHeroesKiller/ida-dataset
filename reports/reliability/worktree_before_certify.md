# worktree_before_certify.md

- **time:** 2026-07-11T00:14:22Z

## git status --porcelain=v1

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
 M reports/reliability/worktree_before_sync.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-D98C8B.jsonl
?? automation/sessions/2026-07-11/
?? reports/production/production_trace_SES-20260711-D98C8B.json
?? reports/production/sessions/SES-20260711-D98C8B/
```

## git diff --name-only

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
reports/reliability/worktree_before_sync.md
reports/reliability/writer_finalize.json
```

## git diff --stat

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
 reports/reliability/git_worktree_trace.md          | 162 +++++++++++++++
 reports/reliability/worktree_before_sync.md        |  62 +++---
 reports/reliability/writer_finalize.json           |   2 +-
 39 files changed, 730 insertions(+), 464 deletions(-)
```

## git diff --cached --name-only

```
(empty)
```
