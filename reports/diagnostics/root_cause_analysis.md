# Root Cause Analysis

**Generated:** 2026-08-14T20:46:11+00:00
**Session:** `SESSION-20260814-8A298D`
**Mission:** `MIS-20260814-32F73A`

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
- discovered=11 downloaded=31 duplicates=16

## Metrics snapshot

```json
{
  "documents_discovered": 11,
  "documents_downloaded": 31,
  "documents_duplicates": 16,
  "candidates_extracted": 5,
  "candidates_rejected": 0,
  "rows_published": 5,
  "dry_run": false,
  "fingerprint_urls_known": 47,
  "selected_dataset": "industry_library"
}
```

## Findings
### Finding 1

Session published rows; if overnight gap exists, examine later sessions.

- `published=5`
- `extracted=5`
- `discovered=11 downloaded=31 duplicates=16`

### Finding 2

Mission selection outcome (context).

- `selected_dataset=industry_library`
- `score=908.1`
- `reason=mode=BOOTSTRAP · gap_score=0.0 · stretch_cov=0.4% · priority=100 · deps_met · sources=13 · continuous=true`
- `instruction=Produce Industry Dataset — expand industry_library toward product target`
