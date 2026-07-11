# Runtime Statistics

**Session:** `SES-20260711-C77248`
**Mission:** Bootstrap BPO Services Indonesia — continuous knowledge manufacturing for service_library (gap_score=112.922, universe_remaining=49935, mode=BOOTSTRAP)
**Total stage time (ms):** 46884.4

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 0.9 | completed |
| source_discovery | 2.7 | completed |
| connector | 6218.8 | completed |
| document_discovery | 6218.9 | completed |
| document_download | 34390.3 | completed |
| extraction | 30.7 | completed |
| candidate_validation | 6.7 | completed |
| publish_queue | 6.7 | completed |
| append_dataset | 7.7 | completed |
| export | 0.3 | skipped |
| git_commit | 0.4 | skipped |
| push | 0.3 | skipped |

## Counters

```json
{
  "summary": {
    "connectors_ok": 7,
    "connectors_failed": 0,
    "documents_discovered": 11,
    "documents_downloaded": 11,
    "documents_failed": 0,
    "documents_duplicates": 3,
    "candidates_extracted": 5,
    "candidates_validated": 5,
    "candidates_rejected": 0,
    "rows_published": 5,
    "rows_duplicate": 0
  },
  "publish": {
    "extracted": 5,
    "validated": 5,
    "rejected": 0,
    "queued": 5,
    "published": 5,
    "skipped": 0,
    "duplicate": 0,
    "by_dataset": {
      "business_signal_library": 5
    },
    "balance_ok": true
  },
  "document_queue": {
    "queued": 0,
    "processing": 0,
    "completed": 11,
    "failed": 0,
    "duplicates": 3
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
