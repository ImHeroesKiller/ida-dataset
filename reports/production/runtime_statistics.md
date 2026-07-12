# Runtime Statistics

**Session:** `SES-20260712-CB8076`
**Mission:** Expand Industry Library — factory learn cycle
**Total stage time (ms):** 142180.4

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 0.8 | completed |
| source_discovery | 2.4 | completed |
| connector | 6154.6 | completed |
| document_discovery | 6154.7 | completed |
| document_download | 129777.6 | completed |
| extraction | 54.7 | completed |
| candidate_validation | 1.1 | completed |
| publish_queue | 1.1 | completed |
| append_dataset | 32.6 | completed |
| export | 0.3 | skipped |
| git_commit | 0.2 | skipped |
| push | 0.3 | skipped |

## Counters

```json
{
  "summary": {
    "connectors_ok": 7,
    "connectors_failed": 0,
    "documents_discovered": 21,
    "documents_downloaded": 83,
    "documents_failed": 0,
    "documents_duplicates": 67,
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
    "completed": 83,
    "failed": 0,
    "duplicates": 67
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
