# Runtime Statistics

**Session:** `SES-20260711-BAFFD0`
**Mission:** Expand Industry Library — factory learn cycle
**Total stage time (ms):** 125023.4

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 0.9 | completed |
| source_discovery | 2.9 | completed |
| connector | 6180.0 | completed |
| document_discovery | 6180.2 | completed |
| document_download | 112546.0 | completed |
| extraction | 67.7 | completed |
| candidate_validation | 1.4 | completed |
| publish_queue | 1.4 | completed |
| append_dataset | 42.0 | completed |
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
    "documents_downloaded": 82,
    "documents_failed": 0,
    "documents_duplicates": 68,
    "candidates_extracted": 3,
    "candidates_validated": 3,
    "candidates_rejected": 3,
    "rows_published": 0,
    "rows_duplicate": 0
  },
  "publish": {
    "extracted": 3,
    "validated": 3,
    "rejected": 3,
    "queued": 3,
    "published": 0,
    "skipped": 3,
    "duplicate": 0,
    "by_dataset": {},
    "balance_ok": false
  },
  "document_queue": {
    "queued": 0,
    "processing": 0,
    "completed": 82,
    "failed": 0,
    "duplicates": 68
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
