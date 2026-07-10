# Runtime Statistics

**Session:** `SES-PERF-002`
**Mission:** Expand Outsourcing Industry Indonesia
**Total stage time (ms):** 5198.0

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 0.2 | completed |
| source_discovery | 0.9 | completed |
| connector | 9.1 | completed |
| document_discovery | 9.3 | completed |
| document_download | 5151.8 | completed |
| extraction | 17.9 | completed |
| candidate_validation | 2.5 | completed |
| publish_queue | 2.6 | completed |
| append_dataset | 2.8 | completed |
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
    "documents_downloaded": 2,
    "documents_failed": 0,
    "documents_duplicates": 6,
    "candidates_extracted": 2,
    "candidates_validated": 2,
    "candidates_rejected": 0,
    "rows_published": 2,
    "rows_duplicate": 0
  },
  "publish": {
    "extracted": 2,
    "validated": 2,
    "rejected": 0,
    "queued": 2,
    "published": 2,
    "skipped": 0,
    "duplicate": 0,
    "by_dataset": {
      "business_signal_library": 2
    },
    "balance_ok": true
  },
  "document_queue": {
    "queued": 0,
    "processing": 0,
    "completed": 2,
    "failed": 0,
    "duplicates": 6
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
