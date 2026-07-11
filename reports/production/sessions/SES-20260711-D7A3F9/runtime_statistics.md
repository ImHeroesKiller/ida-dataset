# Runtime Statistics

**Session:** `SES-20260711-D7A3F9`
**Mission:** Expand Industry Library — factory learn cycle
**Total stage time (ms):** 51847.2

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 0.9 | completed |
| source_discovery | 2.8 | completed |
| connector | 6206.6 | completed |
| document_discovery | 6206.8 | completed |
| document_download | 39365.8 | completed |
| extraction | 35.0 | completed |
| candidate_validation | 1.4 | completed |
| publish_queue | 1.4 | completed |
| append_dataset | 25.6 | completed |
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
    "documents_downloaded": 61,
    "documents_failed": 0,
    "documents_duplicates": 56,
    "candidates_extracted": 2,
    "candidates_validated": 2,
    "candidates_rejected": 2,
    "rows_published": 0,
    "rows_duplicate": 0
  },
  "publish": {
    "extracted": 2,
    "validated": 2,
    "rejected": 2,
    "queued": 2,
    "published": 0,
    "skipped": 2,
    "duplicate": 0,
    "by_dataset": {},
    "balance_ok": false
  },
  "document_queue": {
    "queued": 0,
    "processing": 0,
    "completed": 61,
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
