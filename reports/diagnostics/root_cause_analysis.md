# Root Cause Analysis

**Generated:** 2026-08-13T01:08:35+00:00
**Session:** `SESSION-20260813-D1D658`
**Mission:** `MIS-20260813-E95C7C`

> Diagnostics only. No fixes. Evidence only.

## Why no new rows?

Latest evidence shows published=4; zero-row claim may refer to a later window.

## Exactly which stage stopped production?

**`none (production produced rows)`**

## What condition caused it?

**`rows_published`**

## What module decided it?

**`append path succeeded`**

## What evidence proves it?

- published=4
- extracted=7
- discovered=11 downloaded=31 duplicates=15

## Metrics snapshot

```json
{
  "documents_discovered": 11,
  "documents_downloaded": 31,
  "documents_duplicates": 15,
  "candidates_extracted": 7,
  "candidates_rejected": 3,
  "rows_published": 4,
  "dry_run": false,
  "fingerprint_urls_known": 46,
  "selected_dataset": "industry_library"
}
```

## Findings
### Finding 1

Session published rows; if overnight gap exists, examine later sessions.

- `published=4`
- `extracted=7`
- `discovered=11 downloaded=31 duplicates=15`

### Finding 2

Mission selection outcome (context).

- `selected_dataset=industry_library`
- `score=908.2`
- `reason=mode=BOOTSTRAP · gap_score=0.0 · stretch_cov=0.4% · priority=100 · deps_met · sources=13 · continuous=true`
- `instruction=Produce Industry Dataset — expand industry_library toward product target`
