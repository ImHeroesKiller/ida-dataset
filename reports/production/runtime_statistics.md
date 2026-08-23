# Runtime Statistics

**Session:** `SES-20260823-D61F66`
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Total stage time (ms):** 321271.4

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 0.9 | completed |
| source_discovery | 2.8 | completed |
| connector | 6204.7 | completed |
| document_discovery | 6204.9 | completed |
| document_download | 308763.2 | completed |
| extraction | 36.7 | completed |
| candidate_validation | 19.2 | completed |
| publish_queue | 19.1 | completed |
| append_dataset | 18.8 | completed |
| export | 0.4 | skipped |
| git_commit | 0.4 | skipped |
| push | 0.3 | skipped |

## Counters

```json
{
  "summary": {
    "connectors_ok": 7,
    "connectors_failed": 0,
    "documents_discovered": 11,
    "documents_downloaded": 31,
    "documents_failed": 0,
    "documents_duplicates": 12,
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
    "completed": 31,
    "failed": 0,
    "duplicates": 12
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
