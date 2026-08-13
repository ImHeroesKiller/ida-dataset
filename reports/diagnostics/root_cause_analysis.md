# Root Cause Analysis

**Generated:** 2026-08-13T00:05:10+00:00
**Session:** `SESSION-20260812-299AA2`
**Mission:** `MIS-20260812-BB1FF2`

> Diagnostics only. No fixes. Evidence only.

## Why no new rows?

Latest evidence shows published=14; zero-row claim may refer to a later window.

## Exactly which stage stopped production?

**`none (production produced rows)`**

## What condition caused it?

**`rows_published`**

## What module decided it?

**`append path succeeded`**

## What evidence proves it?

- published=14
- extracted=40
- discovered=31 downloaded=51 duplicates=16

## Metrics snapshot

```json
{
  "documents_discovered": 31,
  "documents_downloaded": 51,
  "documents_duplicates": 16,
  "candidates_extracted": 40,
  "candidates_rejected": 26,
  "rows_published": 14,
  "dry_run": false,
  "fingerprint_urls_known": 67,
  "selected_dataset": "industry_library"
}
```

## Findings
### Finding 1

Session published rows; if overnight gap exists, examine later sessions.

- `published=14`
- `extracted=40`
- `discovered=31 downloaded=51 duplicates=16`

### Finding 2

Mission selection outcome (context).

- `selected_dataset=industry_library`
- `score=1904.83`
- `reason=mode=BOOTSTRAP · gap_score=87.823 · stretch_cov=0.3% · priority=100 · deps_met · sources=13 · continuous=true`
- `instruction=procurement — industry knowledge for Procurement — continuous knowledge manufacturing for industry_library across enterprise function Procurement (function_gap=59.0; not BD-only); dataset_gap=87.823; mode=BOOTSTRAP`
