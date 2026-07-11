# Runtime Statistics

**Session:** `SES-20260711-AE4E77`
**Mission:** Expand Industry Library — factory learn cycle
**Total stage time (ms):** 121047.7

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 1.1 | completed |
| source_discovery | 2.8 | completed |
| connector | 6177.9 | completed |
| document_discovery | 6178.0 | completed |
| document_download | 108575.1 | completed |
| extraction | 63.4 | completed |
| candidate_validation | 1.4 | completed |
| publish_queue | 1.4 | completed |
| append_dataset | 45.5 | completed |
| export | 0.4 | skipped |
| git_commit | 0.4 | skipped |
| push | 0.3 | skipped |

## Counters

```json
{
  "summary": {
    "connectors_ok": 7,
    "connectors_failed": 0,
    "documents_discovered": 21,
    "documents_downloaded": 86,
    "documents_failed": 0,
    "documents_duplicates": 64,
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
    "completed": 86,
    "failed": 0,
    "duplicates": 64
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
