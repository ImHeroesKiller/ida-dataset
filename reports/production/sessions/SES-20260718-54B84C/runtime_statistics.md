# Runtime Statistics

**Session:** `SES-20260718-54B84C`
**Mission:** corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_library across enterprise function Corporate Governance (function_gap=58.4; not BD-only); dataset_gap=112.922; mode=BOOTSTRAP
**Total stage time (ms):** 324366.6

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 0.6 | completed |
| source_discovery | 39.8 | completed |
| connector | 94137.1 | completed |
| document_discovery | 94137.2 | completed |
| document_download | 135973.1 | completed |
| extraction | 53.5 | completed |
| candidate_validation | 5.9 | completed |
| publish_queue | 5.9 | completed |
| append_dataset | 12.4 | completed |
| export | 0.3 | skipped |
| git_commit | 0.2 | skipped |
| push | 0.6 | skipped |

## Counters

```json
{
  "summary": {
    "connectors_ok": 7,
    "connectors_failed": 0,
    "documents_discovered": 31,
    "documents_downloaded": 27,
    "documents_failed": 0,
    "documents_duplicates": 20,
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
    "completed": 27,
    "failed": 0,
    "duplicates": 20
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
