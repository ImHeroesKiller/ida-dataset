# Worktree Before Sync

## git status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
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
 M reports/enterprise/dataset_function_matrix.md
 M reports/enterprise/enterprise_state.json
 M reports/enterprise/knowledge_gap_by_function.md
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
?? automation/learning/state/daily_2026-08-13.json
?? automation/learning/state/sessions/SES-20260812-8BD385.jsonl
?? automation/learning/state/snapshot_2026-08-13.json
?? automation/queue/publish/CAND-14C0396A9DC4.json
?? automation/queue/publish/CAND-198A3C192524.json
?? automation/queue/publish/CAND-21EFE6035AB9.json
?? automation/queue/publish/CAND-29E5FA722096.json
?? automation/queue/publish/CAND-4AF10225EB6B.json
?? automation/queue/publish/CAND-4D31A7BF92F6.json
?? automation/queue/publish/CAND-4D7BD598AB16.json
?? automation/queue/publish/CAND-59B49A1A8F1F.json
?? automation/queue/publish/CAND-61FC37838342.json
?? automation/queue/publish/CAND-64F739498BDB.json
?? automation/queue/publish/CAND-6A30FDEFF5EF.json
?? automation/queue/publish/CAND-6ACEF72974C4.json
?? automation/queue/publish/CAND-6ADD53D8E489.json
?? automation/queue/publish/CAND-7DDE5E598B3B.json
?? automation/queue/publish/CAND-8B66153B6B79.json
?? automation/queue/publish/CAND-8E0287DD32BE.json
?? automation/queue/publish/CAND-924C6F41A07B.json
?? automation/queue/publish/CAND-933FD0411EAD.json
?? automation/queue/publish/CAND-9DFB1CD280F2.json
?? automation/queue/publish/CAND-A794C3DE0ED1.json
?? automation/queue/publish/CAND-AB49E874BE64.json
?? automation/queue/publish/CAND-BA8A78824279.json
?? automation/queue/publish/CAND-C0DEF0FB996B.json
?? automation/queue/publish/CAND-E1882A3C114F.json
?? automation/queue/publish/CAND-EFE423B30DA3.json
?? automation/queue/publish/CAND-FD9FB8F20088.json
?? automation/sessions/2026-08-12/SESSION-20260812-299AA2.json
?? reports/production/production_trace_SES-20260812-8BD385.json
?? reports/production/sessions/SES-20260812-8BD385/
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
reports/enterprise/dataset_function_matrix.md
reports/enterprise/enterprise_state.json
reports/enterprise/knowledge_gap_by_function.md
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

## git diff --stat

```
 .../learning/state/acquisition_performance.json    |  598 +++--
 automation/learning/state/current_snapshot.json    |    8 +-
 automation/learning/state/discovery_analytics.json |  675 +----
 automation/learning/state/learning_journal.jsonl   |  316 +++
 automation/learning/state/live_activity.json       |   10 +-
 automation/learning/state/manufacturing_state.json | 1452 +++++-----
 automation/learning/state/production_trace.json    | 2239 ++++++++++------
 automation/learning/state/source_health.json       |  106 +-
 automation/learning/state/source_performance.json  |   76 +-
 automation/sessions/index.json                     |   58 +-
 domains/business_development/industry_library.csv  |   14 +
 reports/diagnostics/candidate_lifecycle.md         |   53 +-
 reports/diagnostics/candidate_root_cause.md        |  116 +-
 reports/diagnostics/dataset_validation_summary.md  |    4 +-
 reports/diagnostics/document_trace.md              |   83 +-
 reports/diagnostics/extraction_trace.md            |   47 +-
 reports/diagnostics/false_negative_analysis.md     |   49 +-
 reports/diagnostics/integrity_trace.md             | 2765 +++++++++++++++++++-
 reports/diagnostics/knowledge_gap_trace.md         |   12 +-
 reports/diagnostics/mission_trace.md               |   38 +-
 reports/diagnostics/publish_trace.md               |   53 +-
 reports/diagnostics/publisher_trace.md             |   47 +-
 reports/diagnostics/root_cause_analysis.md         |   42 +-
 reports/diagnostics/rule_impact.md                 |    6 +-
 reports/diagnostics/scheduler_trace.md             |   46 +-
 reports/diagnostics/session_trace.md               |   54 +-
 reports/diagnostics/source_trace.md                |   32 +-
 reports/diagnostics/validation_statistics.md       |    8 +-
 reports/diagnostics/validation_trace.md            | 1014 ++++++-
 reports/discovery/accepted_urls.md                 |   30 -
 reports/discovery/adaptive_budget.md               |   22 +-
 reports/discovery/discovery_capacity.md            |    8 +-
 reports/discovery/environment_audit.md             |    2 +-
 reports/discovery/hard_limit_audit.md              |  126 +-
 reports/discovery/provider_audit.md                |    8 +-
 reports/discovery/provider_exhaustion.md           |    6 +-
 reports/discovery/provider_health.md               |    4 +-
 reports/discovery/provider_ranking.md              |    6 +-
 reports/discovery/provider_statistics.md           |   26 +-
 reports/discovery/provider_yield.md                |    6 +-
 reports/discovery/query_statistics.md              |   51 +-
 reports/discovery/rejected_urls.md                 |   30 -
 reports/discovery/reputation_scores.md             |   35 +-
 reports/discovery/throughput_analysis.md           |   12 +-
 reports/discovery/trusted_source_usage.md          |    8 +-
 reports/enterprise/coverage_by_function.md         |   80 +-
 reports/enterprise/dataset_function_matrix.md      |    8 +-
 reports/enterprise/enterprise_state.json           |  764 +++---
 reports/enterprise/knowledge_gap_by_function.md    |   74 +-
 reports/enterprise/production_distribution.md      |   92 +-
 reports/fulltext/acquisition_success.md            |   46 +-
 reports/fulltext/content_richness.md               |   10 +-
 reports/fulltext/doi_resolution.md                 |   12 +-
 reports/fulltext/fallback_chain.md                 |    2 +-
 reports/fulltext/fulltext_statistics.md            |   16 +-
 reports/fulltext/knowledge_gain_projection.md      |   16 +-
 reports/fulltext/publisher_resolution.md           |    4 +-
 reports/fulltext/repository_statistics.md          |    4 +-
 reports/fulltext/representation_quality.md         |   10 +-
 reports/fulltext/validation_before_after.md        |   14 +-
 reports/manufacturing/factory_economics.md         |   30 +-
 reports/manufacturing/growth_velocity.md           |   48 +-
 reports/manufacturing/knowledge_gap.md             |    8 +-
 reports/manufacturing/knowledge_universe.md        |    6 +-
 reports/manufacturing/production_capacity.md       |   20 +-
 reports/manufacturing/scheduler_decisions.md       |   12 +-
 reports/performance/api_statistics.md              |   14 +-
 reports/performance/auto_publish.md                |    2 +-
 reports/performance/cache_statistics.md            |    4 +-
 reports/performance/connector_performance.md       |   16 +-
 reports/performance/connector_ranking.md           |   16 +-
 reports/performance/crawler_statistics.md          |   65 +-
 reports/performance/download_statistics.md         |   26 +-
 reports/performance/extraction_statistics.md       |   41 +-
 reports/performance/factory_capacity.md            |   14 +-
 reports/performance/pipeline_bottleneck.md         |   38 +-
 reports/performance/production_capacity.md         |   12 +-
 reports/performance/queue_efficiency.md            |   12 +-
 reports/performance/session_efficiency.md          |   10 +-
 reports/performance/source_efficiency.md           |   16 +-
 reports/performance/source_ranking.md              |   35 +-
 reports/performance/stage_timings.md               |   12 +-
 reports/performance/throughput.md                  |   18 +-
 reports/performance/throughput_report.md           |   18 +-
 reports/performance/worker_utilization.md          |    6 +-
 reports/production/candidate_pipeline.md           |  209 +-
 reports/production/connector_summary.md            |   38 +-
 reports/production/document_pipeline.md            |   79 +-
 reports/production/evidence_trace.md               |  192 +-
 reports/production/production_trace.md             |   44 +-
 reports/production/publish_pipeline.md             |   14 +-
 reports/production/runtime_statistics.md           |   56 +-
 reports/reliability/git_worktree_trace.md          |  358 +++
 reports/reliability/writer_finalize.json           |    4 +-
 94 files changed, 8982 insertions(+), 4064 deletions(-)
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
	modified:   automation/learning/state/discovery_analytics.json
	modified:   automation/learning/state/learning_journal.jsonl
	modified:   automation/learning/state/live_activity.json
	modified:   automation/learning/state/manufacturing_state.json
	modified:   automation/learning/state/production_trace.json
	modified:   automation/learning/state/source_health.json
	modified:   automation/learning/state/source_performance.json
	modified:   automation/sessions/index.json
	modified:   domains/business_development/industry_library.csv
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
	modified:   reports/enterprise/coverage_by_function.md
	modified:   reports/enterprise/dataset_function_matrix.md
	modified:   reports/enterprise/enterprise_state.json
	modified:   reports/enterprise/knowledge_gap_by_function.md
	modified:   reports/enterprise/production_distribution.md
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
	modified:   reports/performance/auto_publish.md
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
	automation/learning/state/daily_2026-08-13.json
	automation/learning/state/sessions/SES-20260812-8BD385.jsonl
	automation/learning/state/snapshot_2026-08-13.json
	automation/queue/publish/CAND-14C0396A9DC4.json
	automation/queue/publish/CAND-198A3C192524.json
	automation/queue/publish/CAND-21EFE6035AB9.json
	automation/queue/publish/CAND-29E5FA722096.json
	automation/queue/publish/CAND-4AF10225EB6B.json
	automation/queue/publish/CAND-4D31A7BF92F6.json
	automation/queue/publish/CAND-4D7BD598AB16.json
	automation/queue/publish/CAND-59B49A1A8F1F.json
	automation/queue/publish/CAND-61FC37838342.json
	automation/queue/publish/CAND-64F739498BDB.json
	automation/queue/publish/CAND-6A30FDEFF5EF.json
	automation/queue/publish/CAND-6ACEF72974C4.json
	automation/queue/publish/CAND-6ADD53D8E489.json
	automation/queue/publish/CAND-7DDE5E598B3B.json
	automation/queue/publish/CAND-8B66153B6B79.json
	automation/queue/publish/CAND-8E0287DD32BE.json
	automation/queue/publish/CAND-924C6F41A07B.json
	automation/queue/publish/CAND-933FD0411EAD.json
	automation/queue/publish/CAND-9DFB1CD280F2.json
	automation/queue/publish/CAND-A794C3DE0ED1.json
	automation/queue/publish/CAND-AB49E874BE64.json
	automation/queue/publish/CAND-BA8A78824279.json
	automation/queue/publish/CAND-C0DEF0FB996B.json
	automation/queue/publish/CAND-E1882A3C114F.json
	automation/queue/publish/CAND-EFE423B30DA3.json
	automation/queue/publish/CAND-FD9FB8F20088.json
	automation/sessions/2026-08-12/SESSION-20260812-299AA2.json
	reports/production/production_trace_SES-20260812-8BD385.json
	reports/production/sessions/SES-20260812-8BD385/

no changes added to commit (use "git add" and/or "git commit -a")
```
