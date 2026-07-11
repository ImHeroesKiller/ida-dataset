# Runtime Statistics

**Session:** `SES-20260711-7833BB`
**Mission:** Expand company profile, product and solution for outsourcing company in indonesia
**Total stage time (ms):** 1705125.5

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 0.9 | completed |
| source_discovery | 3.0 | completed |
| connector | 97806.1 | completed |
| document_discovery | 97806.2 | completed |
| document_download | 1509355.9 | completed |
| extraction | 93.4 | completed |
| candidate_validation | 6.5 | completed |
| publish_queue | 6.5 | completed |
| append_dataset | 46.1 | completed |
| export | 0.3 | skipped |
| git_commit | 0.3 | skipped |
| push | 0.3 | skipped |

## Counters

```json
{
  "summary": {
    "connectors_ok": 7,
    "connectors_failed": 0,
    "documents_discovered": 21,
    "documents_downloaded": 95,
    "documents_failed": 0,
    "documents_duplicates": 56,
    "candidates_extracted": 5,
    "candidates_validated": 5,
    "candidates_rejected": 0,
    "rows_published": 5,
    "rows_duplicate": 0
  },
  "publish": {
    "extracted": 5,
    "validated": 5,
    "rejected": 0,
    "queued": 5,
    "published": 5,
    "skipped": 0,
    "duplicate": 0,
    "by_dataset": {
      "business_signal_library": 5
    },
    "balance_ok": true
  },
  "document_queue": {
    "queued": 0,
    "processing": 0,
    "completed": 95,
    "failed": 0,
    "duplicates": 56
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
