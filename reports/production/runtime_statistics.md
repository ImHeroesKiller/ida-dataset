# Runtime Statistics

**Session:** `SES-20260819-814EF9`
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Total stage time (ms):** 321914.4

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 0.5 | completed |
| source_discovery | 2.2 | completed |
| connector | 6238.3 | completed |
| document_discovery | 6242.0 | completed |
| document_download | 309370.5 | completed |
| extraction | 24.4 | completed |
| candidate_validation | 10.5 | completed |
| publish_queue | 10.5 | completed |
| append_dataset | 12.5 | completed |
| export | 2.6 | skipped |
| git_commit | 0.2 | skipped |
| push | 0.2 | skipped |

## Counters

```json
{
  "summary": {
    "connectors_ok": 7,
    "connectors_failed": 0,
    "documents_discovered": 11,
    "documents_downloaded": 42,
    "documents_failed": 0,
    "documents_duplicates": 35,
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
    "duplicates": 35
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
