# worktree_before_certify.md

- **time:** 2026-07-11T08:15:01Z

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
 M reports/reliability/worktree_before_sync.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-D73A0C.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-F61AC8.json
?? reports/performance/auto_publish.md
?? reports/performance/extraction_statistics.md
?? reports/performance/stage_timings.md
?? reports/production/production_trace_SES-20260711-D73A0C.json
?? reports/production/sessions/SES-20260711-D73A0C/
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
reports/reliability/worktree_before_sync.md
reports/reliability/writer_finalize.json
```

## git diff --stat

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
 reports/reliability/git_worktree_trace.md          | 201 ++++++
 reports/reliability/worktree_before_sync.md        | 158 +++-
 reports/reliability/writer_finalize.json           |   4 +-
 51 files changed, 2302 insertions(+), 1188 deletions(-)
```

## git diff --cached --name-only

```
(empty)
```
