# Runtime Statistics

**Session:** `SES-PERF-001`
**Mission:** Expand Outsourcing Industry Indonesia
**Total stage time (ms):** 9069.2

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 0.4 | completed |
| source_discovery | 1.3 | completed |
| connector | 3172.0 | completed |
| document_discovery | 3172.5 | completed |
| document_download | 2690.8 | completed |
| extraction | 19.3 | completed |
| candidate_validation | 2.9 | completed |
| publish_queue | 2.8 | completed |
| append_dataset | 6.3 | completed |
| export | 0.3 | skipped |
| git_commit | 0.3 | skipped |
| push | 0.3 | skipped |

## Counters

```json
{
  "summary": {
    "connectors_ok": 7,
    "connectors_failed": 0,
    "documents_discovered": 10,
    "documents_downloaded": 4,
    "documents_failed": 0,
    "documents_duplicates": 0,
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
    "completed": 4,
    "failed": 0,
    "duplicates": 0
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
