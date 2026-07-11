# worktree_before_certify.md

- **time:** 2026-07-11T12:22:40Z

## git status --porcelain=v1

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
 M reports/reliability/worktree_before_sync.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-D7A3F9.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-B8F6DE.json
?? reports/production/production_trace_SES-20260711-D7A3F9.json
?? reports/production/sessions/SES-20260711-D7A3F9/
```

## git diff --name-only

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
reports/reliability/worktree_before_sync.md
reports/reliability/writer_finalize.json
```

## git diff --stat

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
 reports/reliability/git_worktree_trace.md          |  285 ++
 reports/reliability/worktree_before_sync.md        |  210 +-
 reports/reliability/writer_finalize.json           |    4 +-
 80 files changed, 5012 insertions(+), 4244 deletions(-)
```

## git diff --cached --name-only

```
(empty)
```
