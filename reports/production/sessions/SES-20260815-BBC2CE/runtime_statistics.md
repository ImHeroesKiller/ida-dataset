# Runtime Statistics

**Session:** `SES-20260815-BBC2CE`
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Total stage time (ms):** 55002.5

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 0.9 | completed |
| source_discovery | 2.9 | completed |
| connector | 6146.3 | completed |
| document_discovery | 6146.5 | completed |
| document_download | 42640.5 | completed |
| extraction | 25.9 | completed |
| candidate_validation | 8.8 | completed |
| publish_queue | 8.8 | completed |
| append_dataset | 21.0 | completed |
| export | 0.3 | skipped |
| git_commit | 0.3 | skipped |
| push | 0.3 | skipped |

## Counters

```json
{
  "summary": {
    "connectors_ok": 7,
    "connectors_failed": 0,
    "documents_discovered": 11,
    "documents_downloaded": 39,
    "documents_failed": 0,
    "documents_duplicates": 24,
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
    "completed": 39,
    "failed": 0,
    "duplicates": 24
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
