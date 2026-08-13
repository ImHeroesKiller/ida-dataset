# worktree_before_certify.md

- **time:** 2026-08-13T00:39:09Z

## git status --porcelain=v1

```
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-08-13.json
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
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/worktree_before_sync.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260813-A45A75.jsonl
?? automation/sessions/2026-08-13/SESSION-20260813-EFF8A4.json
```

## git diff --name-only

```
automation/learning/state/current_snapshot.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-08-13.json
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
reports/reliability/git_worktree_trace.md
reports/reliability/worktree_before_sync.md
reports/reliability/writer_finalize.json
```

## git diff --stat

```
 automation/learning/state/current_snapshot.json    |    2 +-
 automation/learning/state/discovery_analytics.json |  554 +++--
 automation/learning/state/learning_journal.jsonl   |   34 +
 automation/learning/state/live_activity.json       |   24 +-
 automation/learning/state/manufacturing_state.json |   82 +-
 automation/learning/state/production_trace.json    | 2314 +-------------------
 automation/learning/state/snapshot_2026-08-13.json |    2 +-
 automation/learning/state/source_health.json       |    2 +-
 automation/learning/state/source_performance.json  |   58 +-
 automation/sessions/index.json                     |   58 +-
 reports/diagnostics/candidate_lifecycle.md         |   29 +-
 reports/diagnostics/candidate_root_cause.md        |   59 +-
 reports/diagnostics/dataset_validation_summary.md  |    5 +-
 reports/diagnostics/document_trace.md              |   62 +-
 reports/diagnostics/extraction_trace.md            |   43 +-
 reports/diagnostics/false_negative_analysis.md     |   18 +-
 reports/diagnostics/integrity_trace.md             | 1215 +++-------
 reports/diagnostics/knowledge_gap_trace.md         |   38 +-
 reports/diagnostics/mission_trace.md               |   38 +-
 reports/diagnostics/publish_trace.md               |   49 +-
 reports/diagnostics/publisher_trace.md             |   75 +-
 reports/diagnostics/root_cause_analysis.md         |   66 +-
 reports/diagnostics/rule_impact.md                 |    6 +-
 reports/diagnostics/scheduler_trace.md             |   40 +-
 reports/diagnostics/session_trace.md               |   64 +-
 reports/diagnostics/source_trace.md                |   30 +-
 reports/diagnostics/validation_statistics.md       |   10 +-
 reports/diagnostics/validation_trace.md            |  506 ++---
 reports/discovery/accepted_urls.md                 |   34 +-
 reports/discovery/adaptive_budget.md               |   20 +-
 reports/discovery/discovery_capacity.md            |    8 +-
 reports/discovery/environment_audit.md             |    2 +-
 reports/discovery/hard_limit_audit.md              |  139 +-
 reports/discovery/provider_audit.md                |   10 +-
 reports/discovery/provider_exhaustion.md           |    6 +-
 reports/discovery/provider_health.md               |    4 +-
 reports/discovery/provider_ranking.md              |    8 +-
 reports/discovery/provider_statistics.md           |   24 +-
 reports/discovery/provider_yield.md                |    6 +-
 reports/discovery/query_statistics.md              |   45 +-
 reports/discovery/rejected_urls.md                 |   38 +-
 reports/discovery/reputation_scores.md             |   10 +-
 reports/discovery/throughput_analysis.md           |   12 +-
 reports/discovery/trusted_source_usage.md          |   10 +-
 reports/manufacturing/factory_economics.md         |   14 +-
 reports/manufacturing/growth_velocity.md           |   12 +-
 reports/manufacturing/knowledge_gap.md             |    4 +-
 reports/manufacturing/knowledge_universe.md        |    2 +-
 reports/manufacturing/production_capacity.md       |    4 +-
 reports/reliability/git_worktree_trace.md          |  199 ++
 reports/reliability/worktree_before_sync.md        |  190 +-
 reports/reliability/writer_finalize.json           |    4 +-
 52 files changed, 1994 insertions(+), 4294 deletions(-)
```

## git diff --cached --name-only

```
(empty)
```
