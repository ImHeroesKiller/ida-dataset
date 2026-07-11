# worktree_before_certify.md

- **time:** 2026-07-11T08:32:16Z

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
 M reports/reliability/worktree_before_sync.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-C77248.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-642972.json
?? reports/production/production_trace_SES-20260711-C77248.json
?? reports/production/sessions/SES-20260711-C77248/
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
reports/reliability/worktree_before_sync.md
reports/reliability/writer_finalize.json
```

## git diff --stat

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
 reports/reliability/git_worktree_trace.md          | 195 ++++++++++++
 reports/reliability/worktree_before_sync.md        | 116 ++++---
 reports/reliability/writer_finalize.json           |   2 +-
 50 files changed, 1065 insertions(+), 758 deletions(-)
```

## git diff --cached --name-only

```
(empty)
```
