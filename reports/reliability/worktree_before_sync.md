# Worktree Before Sync

## git status --porcelain=v1

```
 M automation/learning/state/learning_journal.jsonl
 M automation/learning/state/live_activity.json
 M automation/learning/state/manufacturing_state.json
 M automation/learning/state/production_trace.json
 M reports/manufacturing/knowledge_gap.md
 M reports/reliability/git_worktree_trace.md
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
 reports/reliability/writer_finalize.json           |    4 +-
 7 files changed, 154 insertions(+), 2073 deletions(-)
```

## git status

```
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   automation/learning/state/learning_journal.jsonl
	modified:   automation/learning/state/live_activity.json
	modified:   automation/learning/state/manufacturing_state.json
	modified:   automation/learning/state/production_trace.json
	modified:   reports/manufacturing/knowledge_gap.md
	modified:   reports/reliability/git_worktree_trace.md
	modified:   reports/reliability/writer_finalize.json

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	automation/learning/state/sessions/SES-20260711-C22382.jsonl
	automation/sessions/2026-07-11/SESSION-20260711-F6132B.json

no changes added to commit (use "git add" and/or "git commit -a")
```
