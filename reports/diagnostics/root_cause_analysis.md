# Root Cause Analysis

**Generated:** 2026-07-11T14:18:19+00:00
**Session:** `SESSION-20260711-610B3E`
**Mission:** `MIS-20260711-E0F5D5`

> Diagnostics only. No fixes. Evidence only.

## Why no new rows?

Production stopped or yielded zero published rows at stage `publish` due to condition `session_dry_run_true`.

## Exactly which stage stopped production?

**`publish`**

## What condition caused it?

**`session_dry_run_true`**

## What module decided it?

**`automation/ci/learning_session.py (dry_run / publish flags)`**

## What evidence proves it?

- session.dry_run=True
- knowledge_added=0
- extracted=3 rejected=3
- summary=Session completed · published=0 extracted=3 validated=3 rejected=3 docs=86 entity=— · dry_run

## Metrics snapshot

```json
{
  "documents_discovered": 21,
  "documents_downloaded": 86,
  "documents_duplicates": 64,
  "candidates_extracted": 3,
  "candidates_rejected": 3,
  "rows_published": 0,
  "dry_run": true,
  "fingerprint_urls_known": 146,
  "selected_dataset": "service_library"
}
```

## Findings
### Finding 1

No rows published because session ran with dry_run.

- `session.dry_run=True`
- `knowledge_added=0`
- `extracted=3 rejected=3`
- `summary=Session completed · published=0 extracted=3 validated=3 rejected=3 docs=86 entity=— · dry_run`

### Finding 2

Mission selection outcome (context).

- `selected_dataset=service_library`
- `score=2137.87`
- `reason=mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · sources=13 · continuous=true`
- `instruction=corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_library across enterprise function Corporate Governance (function_gap=58.4; not BD-only); dataset_gap=112.922; mode=BOOTSTRAP`
