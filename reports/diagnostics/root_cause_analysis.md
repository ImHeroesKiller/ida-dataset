# Root Cause Analysis

**Generated:** 2026-08-13T00:38:59+00:00
**Session:** `SESSION-20260813-EFF8A4`
**Mission:** `Batch-001`

> Diagnostics only. No fixes. Evidence only.

## Why no new rows?

Production stopped or yielded zero published rows at stage `connector_calls / document_discovery` due to condition `no_documents_discovered`.

## Exactly which stage stopped production?

**`connector_calls / document_discovery`**

## What condition caused it?

**`no_documents_discovered`**

## What module decided it?

**`automation/acquisition/pipeline.py connector search + discovery layer`**

## What evidence proves it?

- documents_discovered=0
- connectors=[('Crossref', 'ok', 10), ('OpenAlex', 'no_updates', 0), ('World Bank', 'ok', 1), ('OECD', 'no_updates', 0), ('Asian Development Bank', 'no_updates', 0), ('Kemenperin', 'no_updates', 0), ('BPS Indonesia', 'no_updates', 0)]

## Metrics snapshot

```json
{
  "documents_discovered": 0,
  "documents_downloaded": 0,
  "documents_duplicates": 0,
  "candidates_extracted": 0,
  "candidates_rejected": 0,
  "rows_published": 0,
  "dry_run": false,
  "fingerprint_urls_known": 0,
  "selected_dataset": "industry_library"
}
```

## Findings
### Finding 1

Discovery found zero documents.

- `documents_discovered=0`
- `connectors=[('Crossref', 'ok', 10), ('OpenAlex', 'no_updates', 0), ('World Bank', 'ok', 1), ('OECD', 'no_updates', 0), ('Asian Development Bank', 'no_updates', 0), ('Kemenperin', 'no_updates', 0), ('BPS Indonesia', 'no_updates', 0)]`

### Finding 2

Mission selection outcome (context).

- `selected_dataset=industry_library`
- `score=908.6`
- `reason=mode=BOOTSTRAP · gap_score=0.0 · stretch_cov=0.3% · priority=100 · deps_met · sources=13 · continuous=true`
- `instruction=Produce Industry Dataset — expand industry_library toward product target`

## Failed stages (from execution trace)

```json
[
  {
    "stage": "end_session",
    "status": "failed",
    "duration_ms": null,
    "documents": null,
    "rows": null,
    "meta": {
      "duration_seconds": 518.0,
      "dry_run": false
    },
    "errors": [],
    "evidence": "prioritize_search_results() got an unexpected keyword argument 'dataset'"
  }
]
```
