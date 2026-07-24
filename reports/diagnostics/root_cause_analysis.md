# Root Cause Analysis

**Generated:** 2026-07-24T12:46:40+00:00
**Session:** `SESSION-20260724-A7B211`
**Mission:** `MIS-20260724-3ADCA5`

> Diagnostics only. No fixes. Evidence only.

## Why no new rows?

Latest evidence shows published=5; zero-row claim may refer to a later window.

## Exactly which stage stopped production?

**`none (production produced rows)`**

## What condition caused it?

**`rows_published`**

## What module decided it?

**`append path succeeded`**

## What evidence proves it?

- published=5
- extracted=5
- discovered=31 downloaded=62 duplicates=35

## Metrics snapshot

```json
{
  "documents_discovered": 31,
  "documents_downloaded": 62,
  "documents_duplicates": 35,
  "candidates_extracted": 5,
  "candidates_rejected": 0,
  "rows_published": 5,
  "dry_run": false,
  "fingerprint_urls_known": 90,
  "selected_dataset": "service_library"
}
```

## Findings
### Finding 1

Session published rows; if overnight gap exists, examine later sessions.

- `published=5`
- `extracted=5`
- `discovered=31 downloaded=62 duplicates=35`

### Finding 2

Mission selection outcome (context).

- `selected_dataset=service_library`
- `score=2137.87`
- `reason=mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · sources=13 · continuous=true`
- `instruction=corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_library across enterprise function Corporate Governance (function_gap=58.4; not BD-only); dataset_gap=112.922; mode=BOOTSTRAP`
