# Root Cause Analysis

**Generated:** 2026-08-13T02:17:58+00:00
**Session:** `SESSION-20260813-F331BD`
**Mission:** `MIS-20260813-3FFF19`

> Diagnostics only. No fixes. Evidence only.

## Why no new rows?

Latest evidence shows published=1; zero-row claim may refer to a later window.

## Exactly which stage stopped production?

**`none (production produced rows)`**

## What condition caused it?

**`rows_published`**

## What module decided it?

**`append path succeeded`**

## What evidence proves it?

- published=1
- extracted=1
- discovered=11 downloaded=42 duplicates=38

## Metrics snapshot

```json
{
  "documents_discovered": 11,
  "documents_downloaded": 42,
  "documents_duplicates": 38,
  "candidates_extracted": 1,
  "candidates_rejected": 0,
  "rows_published": 1,
  "dry_run": false,
  "fingerprint_urls_known": 73,
  "selected_dataset": "industry_library"
}
```

## Findings
### Finding 1

Session published rows; if overnight gap exists, examine later sessions.

- `published=1`
- `extracted=1`
- `discovered=11 downloaded=42 duplicates=38`

### Finding 2

Mission selection outcome (context).

- `selected_dataset=industry_library`
- `score=908.1`
- `reason=mode=BOOTSTRAP · gap_score=0.0 · stretch_cov=0.4% · priority=100 · deps_met · sources=13 · continuous=true`
- `instruction=Produce Industry Dataset — expand industry_library toward product target`
