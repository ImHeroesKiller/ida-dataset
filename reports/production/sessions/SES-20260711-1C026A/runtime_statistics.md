# Runtime Statistics

**Session:** `SES-20260711-1C026A`
**Mission:** Expand Industry Library — factory learn cycle
**Total stage time (ms):** 173813.6

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 1.1 | completed |
| source_discovery | 3.2 | completed |
| connector | 6137.2 | completed |
| document_discovery | 6137.3 | completed |
| document_download | 161423.7 | completed |
| extraction | 68.6 | completed |
| candidate_validation | 1.5 | completed |
| publish_queue | 1.5 | completed |
| append_dataset | 38.6 | completed |
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
    "documents_downloaded": 73,
    "documents_failed": 0,
    "documents_duplicates": 59,
    "candidates_extracted": 4,
    "candidates_validated": 4,
    "candidates_rejected": 4,
    "rows_published": 0,
    "rows_duplicate": 0
  },
  "publish": {
    "extracted": 4,
    "validated": 4,
    "rejected": 4,
    "queued": 4,
    "published": 0,
    "skipped": 4,
    "duplicate": 0,
    "by_dataset": {},
    "balance_ok": false
  },
  "document_queue": {
    "queued": 0,
    "processing": 0,
    "completed": 73,
    "failed": 0,
    "duplicates": 59
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
