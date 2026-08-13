# Runtime Statistics

**Session:** `SES-20260813-C27354`
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Total stage time (ms):** 91722.7

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 1.1 | completed |
| source_discovery | 3.0 | completed |
| connector | 6193.4 | completed |
| document_discovery | 6193.6 | completed |
| document_download | 79270.9 | completed |
| extraction | 24.1 | completed |
| candidate_validation | 8.0 | completed |
| publish_queue | 8.0 | completed |
| append_dataset | 19.6 | completed |
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
    "documents_downloaded": 31,
    "documents_failed": 0,
    "documents_duplicates": 15,
    "candidates_extracted": 7,
    "candidates_validated": 4,
    "candidates_rejected": 3,
    "rows_published": 4,
    "rows_duplicate": 0
  },
  "publish": {
    "extracted": 7,
    "validated": 4,
    "rejected": 3,
    "queued": 7,
    "published": 4,
    "skipped": 0,
    "duplicate": 0,
    "by_dataset": {
      "industry_library": 4
    },
    "balance_ok": true
  },
  "document_queue": {
    "queued": 0,
    "processing": 0,
    "completed": 31,
    "failed": 0,
    "duplicates": 15
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
