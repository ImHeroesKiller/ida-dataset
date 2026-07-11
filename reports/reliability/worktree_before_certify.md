# worktree_before_certify.md

- **time:** 2026-07-11T15:34:45Z

## git status --porcelain=v1

```
 M automation/learning/state/discovery_analytics.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M automation/learning/state/source_performance.json
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
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/production_capacity.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/worktree_before_sync.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-C15C23.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-211F6B.json
```

## git diff --name-only

```
automation/learning/state/discovery_analytics.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
automation/learning/state/source_performance.json
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
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/production_capacity.md
reports/reliability/git_worktree_trace.md
reports/reliability/worktree_before_sync.md
reports/reliability/writer_finalize.json
```

## git diff --stat

```
 automation/learning/state/discovery_analytics.json | 2826 ++++++++++++--------
 automation/learning/state/learning_journal.jsonl   |  398 +++
 automation/learning/state/live_activity.json       |   45 +-
 automation/learning/state/manufacturing_state.json |    8 +-
 automation/learning/state/production_trace.json    | 2032 +-------------
 automation/learning/state/source_performance.json  |   66 +-
 reports/discovery/accepted_urls.md                 |  396 +--
 reports/discovery/adaptive_budget.md               |   28 +-
 reports/discovery/discovery_capacity.md            |   12 +-
 reports/discovery/environment_audit.md             |    2 +-
 reports/discovery/hard_limit_audit.md              |    5 +-
 reports/discovery/provider_audit.md                |   12 +-
 reports/discovery/provider_exhaustion.md           |   10 +-
 reports/discovery/provider_health.md               |    6 +-
 reports/discovery/provider_ranking.md              |   12 +-
 reports/discovery/provider_statistics.md           |   26 +-
 reports/discovery/provider_yield.md                |   10 +-
 reports/discovery/query_statistics.md              |  162 +-
 reports/discovery/rejected_urls.md                 |  126 +-
 reports/discovery/reputation_scores.md             |   35 +-
 reports/discovery/throughput_analysis.md           |   14 +-
 reports/discovery/trusted_source_usage.md          |   27 +-
 reports/manufacturing/growth_velocity.md           |    4 +-
 reports/manufacturing/knowledge_gap.md             |    2 +-
 reports/manufacturing/production_capacity.md       |    2 +-
 reports/reliability/git_worktree_trace.md          |  127 +
 reports/reliability/worktree_before_sync.md        |  290 +-
 reports/reliability/writer_finalize.json           |    4 +-
 28 files changed, 2949 insertions(+), 3738 deletions(-)
```

## git diff --cached --name-only

```
(empty)
```
