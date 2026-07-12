# Root Cause Analysis

**Generated:** 2026-07-12T18:23:54+00:00
**Session:** `SESSION-20260712-B8F796`
**Mission:** `MIS-20260712-4F53B0`

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
- discovered=31 downloaded=133 duplicates=101

## Metrics snapshot

```json
{
  "documents_discovered": 31,
  "documents_downloaded": 133,
  "documents_duplicates": 101,
  "candidates_extracted": 1,
  "candidates_rejected": 0,
  "rows_published": 1,
  "dry_run": false,
  "fingerprint_urls_known": 232,
  "selected_dataset": "service_library"
}
```

## Findings
### Finding 1

Session published rows; if overnight gap exists, examine later sessions.

- `published=1`
- `extracted=1`
- `discovered=31 downloaded=133 duplicates=101`

### Finding 2

Mission selection outcome (context).

- `selected_dataset=service_library`
- `score=2137.87`
- `reason=mode=BOOTSTRAP · gap_score=112.922 · stretch_cov=0.1% · priority=95 · deps_met · sources=13 · continuous=true`
- `instruction=corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_library across enterprise function Corporate Governance (function_gap=58.4; not BD-only); dataset_gap=112.922; mode=BOOTSTRAP`
