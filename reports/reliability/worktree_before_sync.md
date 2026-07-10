# Worktree Before Sync

## git status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-10.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M reports/discovery/provider_health.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/query_statistics.md
 M reports/discovery/trusted_source_usage.md
 M reports/performance/api_statistics.md
 M reports/performance/cache_statistics.md
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
?? automation/learning/state/sessions/SES-20260710-88FC2E.jsonl
?? automation/queue/publish/CAND-94B9A207CDEE.json
?? automation/queue/publish/CAND-95C824E2F514.json
?? automation/queue/publish/CAND-AB5E38F39855.json
?? automation/sessions/2026-07-10/SESSION-20260710-005543.json
?? reports/production/production_trace_SES-20260710-88FC2E.json
?? reports/production/sessions/SES-20260710-88FC2E/
```

## git diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-10.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
reports/discovery/provider_health.md
reports/discovery/provider_statistics.md
reports/discovery/query_statistics.md
reports/discovery/trusted_source_usage.md
reports/performance/api_statistics.md
reports/performance/cache_statistics.md
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
 .../learning/state/acquisition_performance.json    | 199 +++++----
 automation/learning/state/current_snapshot.json    |   6 +-
 automation/learning/state/discovery_analytics.json |  96 +++--
 automation/learning/state/learning_journal.jsonl   |  63 +++
 automation/learning/state/live_activity.json       |  10 +-
 automation/learning/state/production_trace.json    | 474 +++++++++++----------
 automation/learning/state/snapshot_2026-07-10.json |   6 +-
 automation/learning/state/source_health.json       |  50 +--
 automation/learning/state/source_performance.json  |  62 +--
 automation/sessions/index.json                     |  30 +-
 reports/discovery/provider_health.md               |   2 +-
 reports/discovery/provider_statistics.md           |  12 +-
 reports/discovery/query_statistics.md              |  46 +-
 reports/discovery/trusted_source_usage.md          |   6 +-
 reports/performance/api_statistics.md              |  14 +-
 reports/performance/cache_statistics.md            |   4 +-
 reports/performance/connector_performance.md       |  16 +-
 reports/performance/crawler_statistics.md          |  26 +-
 reports/performance/download_statistics.md         |  18 +-
 reports/performance/source_ranking.md              |  12 +-
 reports/performance/throughput.md                  |  18 +-
 reports/production/candidate_pipeline.md           |   9 +-
 reports/production/connector_summary.md            |  64 +--
 reports/production/document_pipeline.md            |  13 +-
 reports/production/evidence_trace.md               |  22 +-
 reports/production/production_trace.md             |  42 +-
 reports/production/publish_pipeline.md             |  20 +-
 reports/production/runtime_statistics.md           |  60 ++-
 reports/reliability/git_worktree_trace.md          | 141 ++++++
 reports/reliability/writer_finalize.json           |   2 +-
 30 files changed, 898 insertions(+), 645 deletions(-)
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
	modified:   automation/learning/state/production_trace.json
	modified:   automation/learning/state/snapshot_2026-07-10.json
	modified:   automation/learning/state/source_health.json
	modified:   automation/learning/state/source_performance.json
	modified:   automation/sessions/index.json
	modified:   reports/discovery/provider_health.md
	modified:   reports/discovery/provider_statistics.md
	modified:   reports/discovery/query_statistics.md
	modified:   reports/discovery/trusted_source_usage.md
	modified:   reports/performance/api_statistics.md
	modified:   reports/performance/cache_statistics.md
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
	automation/learning/state/sessions/SES-20260710-88FC2E.jsonl
	automation/queue/publish/CAND-94B9A207CDEE.json
	automation/queue/publish/CAND-95C824E2F514.json
	automation/queue/publish/CAND-AB5E38F39855.json
	automation/sessions/2026-07-10/SESSION-20260710-005543.json
	reports/production/production_trace_SES-20260710-88FC2E.json
	reports/production/sessions/SES-20260710-88FC2E/

no changes added to commit (use "git add" and/or "git commit -a")
```
