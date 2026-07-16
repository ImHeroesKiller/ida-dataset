# worktree_before_certify.md

- **time:** 2026-07-16T08:42:32Z

## git status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/daily_2026-07-16.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-16.json
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
 M reports/reliability/worktree_before_sync.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260716-905D1C.jsonl
?? automation/sessions/2026-07-16/SESSION-20260716-27E30C.json
?? reports/production/production_trace_SES-20260716-905D1C.json
?? reports/production/sessions/SES-20260716-905D1C/
```

## git diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/daily_2026-07-16.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-16.json
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
reports/reliability/worktree_before_sync.md
reports/reliability/writer_finalize.json
```

## git diff --stat

```
 .../learning/state/acquisition_performance.json    |  212 ++--
 automation/learning/state/current_snapshot.json    |    6 +-
 automation/learning/state/daily_2026-07-16.json    |    4 +-
 automation/learning/state/discovery_analytics.json |  448 +-------
 automation/learning/state/learning_journal.jsonl   |  247 +++++
 automation/learning/state/live_activity.json       |    8 +-
 automation/learning/state/manufacturing_state.json |  261 ++---
 automation/learning/state/production_trace.json    | 1080 ++++++--------------
 automation/learning/state/snapshot_2026-07-16.json |    6 +-
 automation/learning/state/source_health.json       |   58 +-
 automation/learning/state/source_performance.json  |   74 +-
 automation/sessions/index.json                     |   58 +-
 .../business_signal_library.csv                    |    5 +
 reports/diagnostics/candidate_lifecycle.md         |   16 +-
 reports/diagnostics/candidate_root_cause.md        |   32 +-
 reports/diagnostics/dataset_validation_summary.md  |    4 +-
 reports/diagnostics/document_trace.md              |   51 +-
 reports/diagnostics/extraction_trace.md            |   12 +-
 reports/diagnostics/false_negative_analysis.md     |   12 +-
 reports/diagnostics/integrity_trace.md             |  116 +--
 reports/diagnostics/knowledge_gap_trace.md         |    6 +-
 reports/diagnostics/mission_trace.md               |    2 +-
 reports/diagnostics/publish_trace.md               |   12 +-
 reports/diagnostics/publisher_trace.md             |   12 +-
 reports/diagnostics/root_cause_analysis.md         |   16 +-
 reports/diagnostics/rule_impact.md                 |    2 +-
 reports/diagnostics/scheduler_trace.md             |    8 +-
 reports/diagnostics/session_trace.md               |   28 +-
 reports/diagnostics/source_trace.md                |   30 +-
 reports/diagnostics/validation_statistics.md       |    2 +-
 reports/diagnostics/validation_trace.md            |  128 +--
 reports/discovery/accepted_urls.md                 |   30 -
 reports/discovery/adaptive_budget.md               |    2 +-
 reports/discovery/discovery_capacity.md            |    2 +-
 reports/discovery/environment_audit.md             |    2 +-
 reports/discovery/hard_limit_audit.md              |  162 +--
 reports/discovery/provider_audit.md                |    8 +-
 reports/discovery/provider_exhaustion.md           |    4 +-
 reports/discovery/provider_health.md               |    4 +-
 reports/discovery/provider_ranking.md              |    6 +-
 reports/discovery/provider_statistics.md           |   20 +-
 reports/discovery/provider_yield.md                |    4 +-
 reports/discovery/query_statistics.md              |   26 +-
 reports/discovery/rejected_urls.md                 |   30 -
 reports/discovery/reputation_scores.md             |    4 +-
 reports/discovery/throughput_analysis.md           |   10 +-
 reports/discovery/trusted_source_usage.md          |    2 -
 reports/fulltext/acquisition_success.md            |   36 +-
 reports/fulltext/content_richness.md               |   10 +-
 reports/fulltext/doi_resolution.md                 |    8 +-
 reports/fulltext/fallback_chain.md                 |    2 +-
 reports/fulltext/fulltext_statistics.md            |   16 +-
 reports/fulltext/knowledge_gain_projection.md      |   16 +-
 reports/fulltext/publisher_resolution.md           |    6 +-
 reports/fulltext/repository_statistics.md          |    4 +-
 reports/fulltext/representation_quality.md         |   10 +-
 reports/fulltext/validation_before_after.md        |   14 +-
 reports/manufacturing/factory_economics.md         |   28 +-
 reports/manufacturing/growth_velocity.md           |   36 +-
 reports/manufacturing/knowledge_gap.md             |    4 +-
 reports/manufacturing/knowledge_universe.md        |    2 +-
 reports/manufacturing/production_capacity.md       |   18 +-
 reports/manufacturing/scheduler_decisions.md       |    2 +-
 reports/performance/api_statistics.md              |   14 +-
 reports/performance/cache_statistics.md            |    4 +-
 reports/performance/connector_performance.md       |   16 +-
 reports/performance/connector_ranking.md           |   16 +-
 reports/performance/crawler_statistics.md          |   52 +-
 reports/performance/download_statistics.md         |   24 +-
 reports/performance/extraction_statistics.md       |   24 +-
 reports/performance/factory_capacity.md            |   16 +-
 reports/performance/pipeline_bottleneck.md         |   44 +-
 reports/performance/production_capacity.md         |   16 +-
 reports/performance/queue_efficiency.md            |    4 +-
 reports/performance/session_efficiency.md          |   12 +-
 reports/performance/source_efficiency.md           |   16 +-
 reports/performance/source_ranking.md              |    4 +-
 reports/performance/stage_timings.md               |   12 +-
 reports/performance/throughput.md                  |   14 +-
 reports/performance/throughput_report.md           |   18 +-
 reports/performance/worker_utilization.md          |    6 +-
 reports/production/candidate_pipeline.md           |   12 +-
 reports/production/connector_summary.md            |   44 +-
 reports/production/document_pipeline.md            |   49 +-
 reports/production/evidence_trace.md               |   24 +-
 reports/production/production_trace.md             |   36 +-
 reports/production/publish_pipeline.md             |    2 +-
 reports/production/runtime_statistics.md           |   36 +-
 reports/reliability/git_worktree_trace.md          |  318 ++++++
 reports/reliability/worktree_before_sync.md        |   86 +-
 reports/reliability/writer_finalize.json           |    2 +-
 91 files changed, 2045 insertions(+), 2360 deletions(-)
```

## git diff --cached --name-only

```
(empty)
```
