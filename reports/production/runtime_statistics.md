# Runtime Statistics

**Session:** `SES-20260815-D5C99B`
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Total stage time (ms):** 55734.0

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 0.6 | completed |
| source_discovery | 2.2 | completed |
| connector | 6157.6 | completed |
| document_discovery | 6157.7 | completed |
| document_download | 43373.2 | completed |
| extraction | 19.7 | completed |
| candidate_validation | 5.7 | completed |
| publish_queue | 5.7 | completed |
| append_dataset | 10.9 | completed |
| export | 0.3 | skipped |
| git_commit | 0.2 | skipped |
| push | 0.2 | skipped |

## Counters

```json
{
  "summary": {
    "connectors_ok": 7,
    "connectors_failed": 0,
    "documents_discovered": 11,
    "documents_downloaded": 34,
    "documents_failed": 0,
    "documents_duplicates": 19,
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
    "completed": 34,
    "failed": 0,
    "duplicates": 19
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
