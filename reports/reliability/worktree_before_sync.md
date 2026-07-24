# Worktree Before Sync

## git status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/daily_2026-07-24.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-24.json
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
?? automation/learning/state/sessions/SES-20260724-0CC2BD.jsonl
?? automation/sessions/2026-07-24/SESSION-20260724-A6E0FB.json
?? reports/production/production_trace_SES-20260724-0CC2BD.json
?? reports/production/sessions/SES-20260724-0CC2BD/
```

## git diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/daily_2026-07-24.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-24.json
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

## git diff --stat

```
 .../learning/state/acquisition_performance.json    | 208 +++---
 automation/learning/state/current_snapshot.json    |   6 +-
 automation/learning/state/daily_2026-07-24.json    |   4 +-
 automation/learning/state/discovery_analytics.json | 568 +++++++++++++--
 automation/learning/state/learning_journal.jsonl   | 311 +++++++++
 automation/learning/state/live_activity.json       |   8 +-
 automation/learning/state/manufacturing_state.json | 242 +++----
 automation/learning/state/production_trace.json    | 758 +++++++++++++--------
 automation/learning/state/snapshot_2026-07-24.json |   6 +-
 automation/learning/state/source_health.json       |  72 +-
 automation/learning/state/source_performance.json  |  72 +-
 automation/sessions/index.json                     |  58 +-
 .../business_signal_library.csv                    |   5 +
 reports/diagnostics/candidate_lifecycle.md         |  16 +-
 reports/diagnostics/candidate_root_cause.md        |  32 +-
 reports/diagnostics/dataset_validation_summary.md  |   4 +-
 reports/diagnostics/document_trace.md              |  33 +-
 reports/diagnostics/extraction_trace.md            |  12 +-
 reports/diagnostics/false_negative_analysis.md     |  12 +-
 reports/diagnostics/integrity_trace.md             | 116 ++--
 reports/diagnostics/knowledge_gap_trace.md         |   6 +-
 reports/diagnostics/mission_trace.md               |   2 +-
 reports/diagnostics/publish_trace.md               |  12 +-
 reports/diagnostics/publisher_trace.md             |  12 +-
 reports/diagnostics/root_cause_analysis.md         |  16 +-
 reports/diagnostics/rule_impact.md                 |   2 +-
 reports/diagnostics/scheduler_trace.md             |   8 +-
 reports/diagnostics/session_trace.md               |  28 +-
 reports/diagnostics/source_trace.md                |  30 +-
 reports/diagnostics/validation_statistics.md       |   2 +-
 reports/diagnostics/validation_trace.md            | 128 ++--
 reports/discovery/accepted_urls.md                 |  30 +
 reports/discovery/adaptive_budget.md               |   2 +-
 reports/discovery/discovery_capacity.md            |   2 +-
 reports/discovery/environment_audit.md             |   2 +-
 reports/discovery/hard_limit_audit.md              |  16 +-
 reports/discovery/provider_audit.md                |   8 +-
 reports/discovery/provider_exhaustion.md           |   4 +-
 reports/discovery/provider_health.md               |   4 +-
 reports/discovery/provider_ranking.md              |   6 +-
 reports/discovery/provider_statistics.md           |  20 +-
 reports/discovery/provider_yield.md                |   4 +-
 reports/discovery/query_statistics.md              |  26 +-
 reports/discovery/rejected_urls.md                 |  50 ++
 reports/discovery/reputation_scores.md             |   4 +-
 reports/discovery/throughput_analysis.md           |  10 +-
 reports/discovery/trusted_source_usage.md          |   2 +
 reports/fulltext/acquisition_success.md            |  28 +-
 reports/fulltext/content_richness.md               |  10 +-
 reports/fulltext/doi_resolution.md                 |   4 +-
 reports/fulltext/fallback_chain.md                 |   2 +-
 reports/fulltext/fulltext_statistics.md            |  14 +-
 reports/fulltext/knowledge_gain_projection.md      |  14 +-
 reports/fulltext/publisher_resolution.md           |   4 +-
 reports/fulltext/repository_statistics.md          |   2 +-
 reports/fulltext/representation_quality.md         |   8 +-
 reports/fulltext/validation_before_after.md        |  12 +-
 reports/manufacturing/factory_economics.md         |  28 +-
 reports/manufacturing/growth_velocity.md           |  28 +-
 reports/manufacturing/knowledge_gap.md             |   4 +-
 reports/manufacturing/knowledge_universe.md        |   2 +-
 reports/manufacturing/production_capacity.md       |  14 +-
 reports/manufacturing/scheduler_decisions.md       |   2 +-
 reports/performance/api_statistics.md              |  14 +-
 reports/performance/cache_statistics.md            |   4 +-
 reports/performance/connector_performance.md       |  16 +-
 reports/performance/connector_ranking.md           |  16 +-
 reports/performance/crawler_statistics.md          |  54 +-
 reports/performance/download_statistics.md         |  26 +-
 reports/performance/extraction_statistics.md       |  24 +-
 reports/performance/factory_capacity.md            |  16 +-
 reports/performance/pipeline_bottleneck.md         |  44 +-
 reports/performance/production_capacity.md         |  16 +-
 reports/performance/queue_efficiency.md            |   4 +-
 reports/performance/session_efficiency.md          |  12 +-
 reports/performance/source_efficiency.md           |  16 +-
 reports/performance/source_ranking.md              |   4 +-
 reports/performance/stage_timings.md               |  12 +-
 reports/performance/throughput.md                  |  14 +-
 reports/performance/throughput_report.md           |  18 +-
 reports/performance/worker_utilization.md          |   6 +-
 reports/production/candidate_pipeline.md           |  12 +-
 reports/production/connector_summary.md            |  22 +-
 reports/production/document_pipeline.md            |  29 +-
 reports/production/evidence_trace.md               |  22 +-
 reports/production/production_trace.md             |  32 +-
 reports/production/publish_pipeline.md             |   2 +-
 reports/production/runtime_statistics.md           |  32 +-
 reports/reliability/git_worktree_trace.md          | 318 +++++++++
 reports/reliability/writer_finalize.json           |   2 +-
 90 files changed, 2681 insertions(+), 1261 deletions(-)
```

## git status

```
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   automation/learning/state/acquisition_performance.json
	modified:   automation/learning/state/current_snapshot.json
	modified:   automation/learning/state/daily_2026-07-24.json
	modified:   automation/learning/state/discovery_analytics.json
	modified:   automation/learning/state/learning_journal.jsonl
	modified:   automation/learning/state/live_activity.json
	modified:   automation/learning/state/manufacturing_state.json
	modified:   automation/learning/state/production_trace.json
	modified:   automation/learning/state/snapshot_2026-07-24.json
	modified:   automation/learning/state/source_health.json
	modified:   automation/learning/state/source_performance.json
	modified:   automation/sessions/index.json
	modified:   domains/business_development/business_signal_library.csv
	modified:   reports/diagnostics/candidate_lifecycle.md
	modified:   reports/diagnostics/candidate_root_cause.md
	modified:   reports/diagnostics/dataset_validation_summary.md
	modified:   reports/diagnostics/document_trace.md
	modified:   reports/diagnostics/extraction_trace.md
	modified:   reports/diagnostics/false_negative_analysis.md
	modified:   reports/diagnostics/integrity_trace.md
	modified:   reports/diagnostics/knowledge_gap_trace.md
	modified:   reports/diagnostics/mission_trace.md
	modified:   reports/diagnostics/publish_trace.md
	modified:   reports/diagnostics/publisher_trace.md
	modified:   reports/diagnostics/root_cause_analysis.md
	modified:   reports/diagnostics/rule_impact.md
	modified:   reports/diagnostics/scheduler_trace.md
	modified:   reports/diagnostics/session_trace.md
	modified:   reports/diagnostics/source_trace.md
	modified:   reports/diagnostics/validation_statistics.md
	modified:   reports/diagnostics/validation_trace.md
	modified:   reports/discovery/accepted_urls.md
	modified:   reports/discovery/adaptive_budget.md
	modified:   reports/discovery/discovery_capacity.md
	modified:   reports/discovery/environment_audit.md
	modified:   reports/discovery/hard_limit_audit.md
	modified:   reports/discovery/provider_audit.md
	modified:   reports/discovery/provider_exhaustion.md
	modified:   reports/discovery/provider_health.md
	modified:   reports/discovery/provider_ranking.md
	modified:   reports/discovery/provider_statistics.md
	modified:   reports/discovery/provider_yield.md
	modified:   reports/discovery/query_statistics.md
	modified:   reports/discovery/rejected_urls.md
	modified:   reports/discovery/reputation_scores.md
	modified:   reports/discovery/throughput_analysis.md
	modified:   reports/discovery/trusted_source_usage.md
	modified:   reports/fulltext/acquisition_success.md
	modified:   reports/fulltext/content_richness.md
	modified:   reports/fulltext/doi_resolution.md
	modified:   reports/fulltext/fallback_chain.md
	modified:   reports/fulltext/fulltext_statistics.md
	modified:   reports/fulltext/knowledge_gain_projection.md
	modified:   reports/fulltext/publisher_resolution.md
	modified:   reports/fulltext/repository_statistics.md
	modified:   reports/fulltext/representation_quality.md
	modified:   reports/fulltext/validation_before_after.md
	modified:   reports/manufacturing/factory_economics.md
	modified:   reports/manufacturing/growth_velocity.md
	modified:   reports/manufacturing/knowledge_gap.md
	modified:   reports/manufacturing/knowledge_universe.md
	modified:   reports/manufacturing/production_capacity.md
	modified:   reports/manufacturing/scheduler_decisions.md
	modified:   reports/performance/api_statistics.md
	modified:   reports/performance/cache_statistics.md
	modified:   reports/performance/connector_performance.md
	modified:   reports/performance/connector_ranking.md
	modified:   reports/performance/crawler_statistics.md
	modified:   reports/performance/download_statistics.md
	modified:   reports/performance/extraction_statistics.md
	modified:   reports/performance/factory_capacity.md
	modified:   reports/performance/pipeline_bottleneck.md
	modified:   reports/performance/production_capacity.md
	modified:   reports/performance/queue_efficiency.md
	modified:   reports/performance/session_efficiency.md
	modified:   reports/performance/source_efficiency.md
	modified:   reports/performance/source_ranking.md
	modified:   reports/performance/stage_timings.md
	modified:   reports/performance/throughput.md
	modified:   reports/performance/throughput_report.md
	modified:   reports/performance/worker_utilization.md
	modified:   reports/production/candidate_pipeline.md
	modified:   reports/production/connector_summary.md
	modified:   reports/production/document_pipeline.md
	modified:   reports/production/evidence_trace.md
	modified:   reports/production/production_trace.md
	modified:   reports/production/publish_pipeline.md
	modified:   reports/production/runtime_statistics.md
	modified:   reports/reliability/git_worktree_trace.md
	modified:   reports/reliability/writer_finalize.json

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	automation/learning/state/sessions/SES-20260724-0CC2BD.jsonl
	automation/sessions/2026-07-24/SESSION-20260724-A6E0FB.json
	reports/production/production_trace_SES-20260724-0CC2BD.json
	reports/production/sessions/SES-20260724-0CC2BD/

no changes added to commit (use "git add" and/or "git commit -a")
```
