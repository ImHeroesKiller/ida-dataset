# Runtime Statistics

**Session:** `SES-20260710-88FC2E`
**Mission:** Expand Industry Library — factory learn cycle
**Total stage time (ms):** 61542.6

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 1.0 | completed |
| source_discovery | 2.7 | completed |
| connector | 6206.3 | completed |
| document_discovery | 6206.5 | completed |
| document_download | 49103.1 | completed |
| extraction | 15.4 | completed |
| candidate_validation | 1.6 | completed |
| publish_queue | 1.7 | completed |
| append_dataset | 3.4 | completed |
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
    "documents_downloaded": 5,
    "documents_failed": 0,
    "documents_duplicates": 1,
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
    "completed": 5,
    "failed": 0,
    "duplicates": 1
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
