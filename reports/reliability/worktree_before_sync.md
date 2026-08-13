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
 M reports/enterprise/coverage_by_function.md
 M reports/enterprise/dataset_function_matrix.md
 M reports/enterprise/enterprise_state.json
 M reports/enterprise/knowledge_gap_by_function.md
 M reports/enterprise/production_distribution.md
 M reports/manufacturing/continuous_production.md
 M reports/manufacturing/growth_velocity.md
 M reports/manufacturing/knowledge_gap.md
 M reports/manufacturing/knowledge_universe.md
 M reports/manufacturing/scheduler_decisions.md
 M reports/reliability/git_worktree_trace.md
 M reports/reliability/writer_finalize.json
?? automation/learning/state/sessions/SES-20260813-0BD3E5.jsonl
?? automation/sessions/2026-08-13/
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
reports/enterprise/coverage_by_function.md
reports/enterprise/dataset_function_matrix.md
reports/enterprise/enterprise_state.json
reports/enterprise/knowledge_gap_by_function.md
reports/enterprise/production_distribution.md
reports/manufacturing/continuous_production.md
reports/manufacturing/growth_velocity.md
reports/manufacturing/knowledge_gap.md
reports/manufacturing/knowledge_universe.md
reports/manufacturing/scheduler_decisions.md
reports/reliability/git_worktree_trace.md
reports/reliability/writer_finalize.json
```

## git diff --stat

```
 automation/learning/state/current_snapshot.json    |   75 +-
 automation/learning/state/learning_journal.jsonl   |   10 +
 automation/learning/state/live_activity.json       |   34 +-
 automation/learning/state/manufacturing_state.json | 2666 ++++++++++----------
 automation/learning/state/snapshot_2026-08-13.json |   75 +-
 automation/learning/state/source_health.json       |    2 +-
 automation/sessions/index.json                     |   58 +-
 reports/enterprise/coverage_by_function.md         |   88 +-
 reports/enterprise/dataset_function_matrix.md      |   46 +-
 reports/enterprise/enterprise_state.json           | 1450 +++++------
 reports/enterprise/knowledge_gap_by_function.md    |   78 +-
 reports/enterprise/production_distribution.md      |   94 +-
 reports/manufacturing/continuous_production.md     |    4 +-
 reports/manufacturing/growth_velocity.md           |    2 +-
 reports/manufacturing/knowledge_gap.md             |   34 +-
 reports/manufacturing/knowledge_universe.md        |   32 +-
 reports/manufacturing/scheduler_decisions.md       |   16 +-
 reports/reliability/git_worktree_trace.md          |  103 +
 reports/reliability/writer_finalize.json           |    4 +-
 19 files changed, 2515 insertions(+), 2356 deletions(-)
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
	modified:   reports/enterprise/coverage_by_function.md
	modified:   reports/enterprise/dataset_function_matrix.md
	modified:   reports/enterprise/enterprise_state.json
	modified:   reports/enterprise/knowledge_gap_by_function.md
	modified:   reports/enterprise/production_distribution.md
	modified:   reports/manufacturing/continuous_production.md
	modified:   reports/manufacturing/growth_velocity.md
	modified:   reports/manufacturing/knowledge_gap.md
	modified:   reports/manufacturing/knowledge_universe.md
	modified:   reports/manufacturing/scheduler_decisions.md
	modified:   reports/reliability/git_worktree_trace.md
	modified:   reports/reliability/writer_finalize.json

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	automation/learning/state/sessions/SES-20260813-0BD3E5.jsonl
	automation/sessions/2026-08-13/

no changes added to commit (use "git add" and/or "git commit -a")
```
