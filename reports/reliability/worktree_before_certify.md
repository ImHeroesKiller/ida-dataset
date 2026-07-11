# worktree_before_certify.md

- **time:** 2026-07-11T04:49:47Z

## git status --porcelain=v1

```
 M automation/learning/state/acquisition_performance.json
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/snapshot_2026-07-11.json
 M automation/learning/state/source_health.json
 M automation/learning/state/source_performance.json
 M automation/sessions/index.json
 M reports/discovery/provider_health.md
 M reports/discovery/provider_statistics.md
 M reports/discovery/query_statistics.md
 M reports/discovery/reputation_scores.md
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
 M reports/reliability/worktree_before_sync.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-784A5F.jsonl
?? automation/queue/publish/CAND-7528E4183942.json
?? automation/queue/publish/CAND-D03DE2F0A439.json
?? automation/queue/publish/CAND-F04B1DEAECD0.json
?? automation/sessions/2026-07-11/SESSION-20260711-6BC023.json
?? reports/production/production_trace_SES-20260711-784A5F.json
?? reports/production/sessions/SES-20260711-784A5F/
```

## git diff --name-only

```
automation/learning/state/acquisition_performance.json
automation/learning/state/current_snapshot.json
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/production_trace.json
automation/learning/state/snapshot_2026-07-11.json
automation/learning/state/source_health.json
automation/learning/state/source_performance.json
automation/sessions/index.json
reports/discovery/provider_health.md
reports/discovery/provider_statistics.md
reports/discovery/query_statistics.md
reports/discovery/reputation_scores.md
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
reports/reliability/worktree_before_sync.md
reports/reliability/writer_finalize.json
```

## git diff --stat

```
 .../learning/state/acquisition_performance.json    | 132 +++----
 automation/learning/state/current_snapshot.json    |   2 +-
 automation/learning/state/discovery_analytics.json |  76 ++--
 automation/learning/state/learning_journal.jsonl   |  63 ++++
 automation/learning/state/live_activity.json       |  10 +-
 automation/learning/state/production_trace.json    | 404 +++++++++------------
 automation/learning/state/snapshot_2026-07-11.json |   2 +-
 automation/learning/state/source_health.json       |   2 +-
 automation/learning/state/source_performance.json  |  62 ++--
 automation/sessions/index.json                     |  30 +-
 reports/discovery/provider_health.md               |   2 +-
 reports/discovery/provider_statistics.md           |  10 +-
 reports/discovery/query_statistics.md              |  46 +--
 reports/discovery/reputation_scores.md             |   8 +-
 reports/performance/api_statistics.md              |  14 +-
 reports/performance/cache_statistics.md            |   4 +-
 reports/performance/connector_performance.md       |  16 +-
 reports/performance/crawler_statistics.md          |  32 +-
 reports/performance/download_statistics.md         |  20 +-
 reports/performance/source_ranking.md              |   8 +-
 reports/performance/throughput.md                  |  14 +-
 reports/production/candidate_pipeline.md           |  10 +-
 reports/production/connector_summary.md            |  50 +--
 reports/production/document_pipeline.md            |  14 +-
 reports/production/evidence_trace.md               |  32 +-
 reports/production/production_trace.md             |  34 +-
 reports/production/publish_pipeline.md             |  14 +-
 reports/production/runtime_statistics.md           |  44 ++-
 reports/reliability/git_worktree_trace.md          | 141 +++++++
 reports/reliability/worktree_before_sync.md        | 108 +++---
 reports/reliability/writer_finalize.json           |   2 +-
 31 files changed, 771 insertions(+), 635 deletions(-)
```

## git diff --cached --name-only

```
(empty)
```
