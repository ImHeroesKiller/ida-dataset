# Worktree Before Sync

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

## git diff --stat

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
 reports/reliability/git_worktree_trace.md          | 252 ++++++
 reports/reliability/writer_finalize.json           |   4 +-
 68 files changed, 2511 insertions(+), 1350 deletions(-)
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
	modified:   automation/learning/state/daily_2026-07-11.json
	modified:   automation/learning/state/discovery_analytics.json
	modified:   automation/learning/state/learning_journal.jsonl
	modified:   automation/learning/state/live_activity.json
	modified:   automation/learning/state/manufacturing_state.json
	modified:   automation/learning/state/production_trace.json
	modified:   automation/learning/state/snapshot_2026-07-11.json
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
	modified:   reports/discovery/provider_health.md
	modified:   reports/discovery/provider_statistics.md
	modified:   reports/discovery/query_statistics.md
	modified:   reports/discovery/reputation_scores.md
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
	automation/learning/state/sessions/SES-20260711-5BAD14.jsonl
	automation/sessions/2026-07-11/SESSION-20260711-C6CDF9.json
	reports/production/production_trace_SES-20260711-5BAD14.json
	reports/production/sessions/SES-20260711-5BAD14/

no changes added to commit (use "git add" and/or "git commit -a")
```
