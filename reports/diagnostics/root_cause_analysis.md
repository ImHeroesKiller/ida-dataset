# Root Cause Analysis

**Generated:** 2026-07-11T18:00:48+00:00
**Session:** `SESSION-20260711-41DBF5`
**Mission:** `MIS-20260711-CF302E`

> Diagnostics only. No fixes. Evidence only.

## Why no new rows?

Latest evidence shows published=2; zero-row claim may refer to a later window.

## Exactly which stage stopped production?

**`none (production produced rows)`**

## What condition caused it?

**`rows_published`**

## What module decided it?

**`append path succeeded`**

## What evidence proves it?

- published=2
- extracted=3
- discovered=28 downloaded=90 duplicates=60

## Metrics snapshot

```json
{
  "documents_discovered": 28,
  "documents_downloaded": 90,
  "documents_duplicates": 60,
  "candidates_extracted": 3,
  "candidates_rejected": 1,
  "rows_published": 2,
  "dry_run": false,
  "fingerprint_urls_known": 148,
  "selected_dataset": "service_library"
}
```

## Findings
### Finding 1

Session published rows; if overnight gap exists, examine later sessions.

- `published=2`
- `extracted=3`
- `discovered=28 downloaded=90 duplicates=60`

### Finding 2

Mission selection outcome (context).

- `selected_dataset=service_library`
- `score=2137.87`
- `reason=mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · sources=13 · continuous=true`
- `instruction=corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_library across enterprise function Corporate Governance (function_gap=58.4; not BD-only); dataset_gap=112.922; mode=BOOTSTRAP`
