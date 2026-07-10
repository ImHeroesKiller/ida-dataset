# Worktree Before Sync

## git status --porcelain=v1

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

## git diff --name-only

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

## git diff --stat

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
 reports/reliability/git_worktree_trace.md          | 162 +++++++++++
 reports/reliability/writer_finalize.json           |   2 +-
 38 files changed, 760 insertions(+), 494 deletions(-)
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
	modified:   automation/learning/state/daily_2026-07-10.json
	modified:   automation/learning/state/discovery_analytics.json
	modified:   automation/learning/state/learning_journal.jsonl
	modified:   automation/learning/state/live_activity.json
	modified:   automation/learning/state/manufacturing_state.json
	modified:   automation/learning/state/production_trace.json
	modified:   automation/learning/state/snapshot_2026-07-10.json
	modified:   automation/learning/state/source_health.json
	modified:   automation/learning/state/source_performance.json
	modified:   automation/sessions/index.json
	modified:   domains/business_development/business_signal_library.csv
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
	modified:   reports/performance/connector_performance.md
	modified:   reports/performance/crawler_statistics.md
	modified:   reports/performance/download_statistics.md
	modified:   reports/performance/source_ranking.md
	modified:   reports/performance/throughput.md
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
	automation/learning/state/sessions/SES-20260710-725C07.jsonl
	automation/sessions/2026-07-10/SESSION-20260710-E077DD.json
	reports/production/production_trace_SES-20260710-725C07.json
	reports/production/sessions/SES-20260710-725C07/

no changes added to commit (use "git add" and/or "git commit -a")
```
