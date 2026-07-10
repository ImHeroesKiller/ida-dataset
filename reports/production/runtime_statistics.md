# Runtime Statistics

**Session:** `SES-20260710-B37525`
**Mission:** Expand Outsourcing Industry Indonesia
**Total stage time (ms):** 19474.7

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 0.9 | completed |
| source_discovery | 1.1 | completed |
| connector | 7301.3 | completed |
| document_discovery | 7301.7 | completed |
| document_download | 4829.0 | completed |
| extraction | 20.6 | completed |
| candidate_validation | 6.6 | completed |
| publish_queue | 6.5 | completed |
| append_dataset | 6.3 | completed |
| export | 0.3 | skipped |
| git_commit | 0.2 | skipped |
| push | 0.2 | skipped |

## Counters

```json
{
  "summary": {
    "connectors_ok": 7,
    "connectors_failed": 0,
    "documents_discovered": 12,
    "documents_downloaded": 5,
    "documents_failed": 0,
    "documents_duplicates": 1,
    "candidates_extracted": 3,
    "candidates_validated": 3,
    "candidates_rejected": 0,
    "rows_published": 3,
    "rows_duplicate": 0
  },
  "publish": {
    "extracted": 3,
    "validated": 3,
    "rejected": 0,
    "queued": 3,
    "published": 3,
    "skipped": 0,
    "duplicate": 0,
    "by_dataset": {
      "business_signal_library": 3
    },
    "balance_ok": true
  },
  "document_queue": {
    "queued": 0,
    "processing": 0,
    "completed": 5,
    "failed": 0,
    "duplicates": 1
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
