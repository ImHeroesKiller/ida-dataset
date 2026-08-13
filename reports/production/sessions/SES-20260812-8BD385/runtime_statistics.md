# Runtime Statistics

**Session:** `SES-20260812-8BD385`
**Mission:** corporate finance — industry knowledge for Finance — continuous knowledge manufacturing for industry_library across enterprise function Finance (function_gap=59.5; not BD-only); dataset_gap=125.25; mode=BOOTSTRAP
**Total stage time (ms):** 538192.7

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 0.9 | completed |
| source_discovery | 2.7 | completed |
| connector | 93833.2 | completed |
| document_discovery | 93833.4 | completed |
| document_download | 350339.4 | completed |
| extraction | 86.0 | completed |
| candidate_validation | 31.0 | completed |
| publish_queue | 31.0 | completed |
| append_dataset | 34.2 | completed |
| export | 0.3 | skipped |
| git_commit | 0.3 | skipped |
| push | 0.3 | skipped |

## Counters

```json
{
  "summary": {
    "connectors_ok": 7,
    "connectors_failed": 0,
    "documents_discovered": 31,
    "documents_downloaded": 51,
    "documents_failed": 0,
    "documents_duplicates": 16,
    "candidates_extracted": 40,
    "candidates_validated": 14,
    "candidates_rejected": 26,
    "rows_published": 14,
    "rows_duplicate": 0
  },
  "publish": {
    "extracted": 40,
    "validated": 14,
    "rejected": 26,
    "queued": 40,
    "published": 14,
    "skipped": 0,
    "duplicate": 0,
    "by_dataset": {
      "industry_library": 14
    },
    "balance_ok": true
  },
  "document_queue": {
    "queued": 0,
    "processing": 0,
    "completed": 51,
    "failed": 0,
    "duplicates": 16
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
