# Worktree Before Sync

## git status --porcelain=v1

```
 M automation/learning/state/current_snapshot.json
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/snapshot_2026-08-13.json
 M automation/learning/state/source_health.json
 M automation/sessions/index.json
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/production_capacity.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260813-98427C.jsonl
?? automation/sessions/2026-08-13/SESSION-20260813-2C36C4.json
```

## git diff --name-only

```
automation/learning/state/current_snapshot.json
automation/learning/state/learning_journal.jsonl
automation/learning/state/live_activity.json
automation/learning/state/manufacturing_state.json
automation/learning/state/snapshot_2026-08-13.json
automation/learning/state/source_health.json
automation/sessions/index.json
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/production_capacity.md
reports/reliability/git_worktree_trace.md
reports/reliability/writer_finalize.json
```

## git diff --stat

```
 automation/learning/state/current_snapshot.json    |  2 +-
 automation/learning/state/learning_journal.jsonl   | 10 +++
 automation/learning/state/live_activity.json       | 18 ++---
 automation/learning/state/manufacturing_state.json | 12 ++--
 automation/learning/state/snapshot_2026-08-13.json |  2 +-
 automation/learning/state/source_health.json       |  2 +-
 automation/sessions/index.json                     | 58 +++++++--------
 reports/manufacturing/growth_velocity.md           | 10 +--
 reports/manufacturing/knowledge_gap.md             |  2 +-
 reports/manufacturing/production_capacity.md       |  2 +-
 reports/reliability/git_worktree_trace.md          | 82 ++++++++++++++++++++++
 reports/reliability/writer_finalize.json           |  2 +-
 12 files changed, 147 insertions(+), 55 deletions(-)
```

## git status

```
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   automation/learning/state/current_snapshot.json
	modified:   automation/learning/state/learning_journal.jsonl
	modified:   automation/learning/state/live_activity.json
	modified:   automation/learning/state/manufacturing_state.json
	modified:   automation/learning/state/snapshot_2026-08-13.json
	modified:   automation/learning/state/source_health.json
	modified:   automation/sessions/index.json
	modified:   reports/manufacturing/growth_velocity.md
	modified:   reports/manufacturing/knowledge_gap.md
	modified:   reports/manufacturing/production_capacity.md
	modified:   reports/reliability/git_worktree_trace.md
	modified:   reports/reliability/writer_finalize.json

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	automation/learning/state/sessions/SES-20260813-98427C.jsonl
	automation/sessions/2026-08-13/SESSION-20260813-2C36C4.json

no changes added to commit (use "git add" and/or "git commit -a")
```
