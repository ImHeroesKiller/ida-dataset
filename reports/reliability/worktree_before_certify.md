# worktree_before_certify.md

- **time:** 2026-07-11T14:35:48Z

## git status --porcelain=v1

```
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M reports/manufacturing/knowledge_gap.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/worktree_before_sync.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260711-C22382.jsonl
?? automation/sessions/2026-07-11/SESSION-20260711-F6132B.json
```

## git diff --name-only

```
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/production_trace.json
reports/manufacturing/knowledge_gap.md
reports/reliability/git_worktree_trace.md
reports/reliability/worktree_before_sync.md
reports/reliability/writer_finalize.json
```

## git diff --stat

```
 automation/learning/state/learning_journal.jsonl   |   22 +
 automation/learning/state/live_activity.json       |   45 +-
 automation/learning/state/manufacturing_state.json |    4 +-
 automation/learning/state/production_trace.json    | 2083 +-------------------
 reports/manufacturing/knowledge_gap.md             |    2 +-
 reports/reliability/git_worktree_trace.md          |   67 +
 reports/reliability/worktree_before_sync.md        |  344 +---
 reports/reliability/writer_finalize.json           |    4 +-
 8 files changed, 164 insertions(+), 2407 deletions(-)
```

## git diff --cached --name-only

```
(empty)
```
