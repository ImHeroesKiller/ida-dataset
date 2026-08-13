# Runtime Statistics

**Session:** `SES-20260813-620086`
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Total stage time (ms):** 94188.8

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 0.7 | completed |
| source_discovery | 2.3 | completed |
| connector | 6153.7 | completed |
| document_discovery | 6153.8 | completed |
| document_download | 81842.4 | completed |
| extraction | 13.7 | completed |
| candidate_validation | 2.3 | completed |
| publish_queue | 2.3 | completed |
| append_dataset | 17.0 | completed |
| export | 0.2 | skipped |
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
    "documents_duplicates": 38,
    "candidates_extracted": 1,
    "candidates_validated": 1,
    "candidates_rejected": 0,
    "rows_published": 1,
    "rows_duplicate": 0
  },
  "publish": {
    "extracted": 1,
    "validated": 1,
    "rejected": 0,
    "queued": 1,
    "published": 1,
    "skipped": 0,
    "duplicate": 0,
    "by_dataset": {
      "industry_library": 1
    },
    "balance_ok": true
  },
  "document_queue": {
    "queued": 0,
    "processing": 0,
    "completed": 42,
    "failed": 0,
    "duplicates": 38
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
