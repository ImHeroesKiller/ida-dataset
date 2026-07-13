# Root Cause Analysis

**Generated:** 2026-07-13T16:55:52+00:00
**Session:** `SESSION-20260713-AA142C`
**Mission:** `MIS-20260713-0C2CB5`

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
- discovered=31 downloaded=95 duplicates=82

## Metrics snapshot

```json
{
  "documents_discovered": 31,
  "documents_downloaded": 95,
  "documents_duplicates": 82,
  "candidates_extracted": 1,
  "candidates_rejected": 0,
  "rows_published": 1,
  "dry_run": false,
  "fingerprint_urls_known": 177,
  "selected_dataset": "service_library"
}
```

## Findings
### Finding 1

Session published rows; if overnight gap exists, examine later sessions.

- `published=1`
- `extracted=1`
- `discovered=31 downloaded=95 duplicates=82`

### Finding 2

Mission selection outcome (context).

- `selected_dataset=service_library`
- `score=2137.87`
- `reason=mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · sources=13 · continuous=true`
- `instruction=corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_library across enterprise function Corporate Governance (function_gap=58.4; not BD-only); dataset_gap=112.922; mode=BOOTSTRAP`
