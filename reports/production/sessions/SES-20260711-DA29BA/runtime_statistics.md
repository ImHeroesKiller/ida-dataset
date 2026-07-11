# Runtime Statistics

**Session:** `SES-20260711-DA29BA`
**Mission:** Expand Industry Library
**Total stage time (ms):** 559082.0

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 0.9 | completed |
| source_discovery | 2.6 | completed |
| connector | 94110.2 | completed |
| document_discovery | 94110.4 | completed |
| document_download | 370722.2 | completed |
| extraction | 89.8 | completed |
| candidate_validation | 4.3 | completed |
| publish_queue | 4.4 | completed |
| append_dataset | 36.5 | completed |
| export | 0.2 | skipped |
| git_commit | 0.2 | skipped |
| push | 0.3 | skipped |

## Counters

```json
{
  "summary": {
    "connectors_ok": 7,
    "connectors_failed": 0,
    "documents_discovered": 28,
    "documents_downloaded": 90,
    "documents_failed": 0,
    "documents_duplicates": 60,
    "candidates_extracted": 3,
    "candidates_validated": 2,
    "candidates_rejected": 1,
    "rows_published": 2,
    "rows_duplicate": 0
  },
  "publish": {
    "extracted": 3,
    "validated": 2,
    "rejected": 1,
    "queued": 3,
    "published": 2,
    "skipped": 0,
    "duplicate": 0,
    "by_dataset": {
      "industry_library": 2
    },
    "balance_ok": true
  },
  "document_queue": {
    "queued": 0,
    "processing": 0,
    "completed": 90,
    "failed": 0,
    "duplicates": 60
  },
  "exports": {
    "jsonl": false,
    "openai": false,
    "huggingface": false,
    "notes": [
      "Export packaging runs in dedicated export CI job"
    ]
  },
  "git": {
    "commit": false,
    "push": false,
    "notes": [
      "Git commit/push performed by learning CI after session"
    ]
  }
}
```
