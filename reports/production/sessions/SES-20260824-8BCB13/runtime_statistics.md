# Runtime Statistics

**Session:** `SES-20260824-8BCB13`
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Total stage time (ms):** 354837.6

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 1.0 | completed |
| source_discovery | 3.0 | completed |
| connector | 6227.0 | completed |
| document_discovery | 6227.2 | completed |
| document_download | 342275.2 | completed |
| extraction | 39.7 | completed |
| candidate_validation | 20.7 | completed |
| publish_queue | 20.7 | completed |
| append_dataset | 22.1 | completed |
| export | 0.4 | skipped |
| git_commit | 0.3 | skipped |
| push | 0.3 | skipped |

## Counters

```json
{
  "summary": {
    "connectors_ok": 7,
    "connectors_failed": 0,
    "documents_discovered": 11,
    "documents_downloaded": 42,
    "documents_failed": 0,
    "documents_duplicates": 31,
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
    "completed": 42,
    "failed": 0,
    "duplicates": 31
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
