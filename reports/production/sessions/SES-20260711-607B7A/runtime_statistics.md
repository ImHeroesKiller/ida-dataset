# Runtime Statistics

**Session:** `SES-20260711-607B7A`
**Mission:** corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_library across enterprise function Corporate Governance (function_gap=58.4; not BD-only); dataset_gap=112.922; mode=BOOTSTRAP
**Total stage time (ms):** 1451701.2

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 1.3 | completed |
| source_discovery | 2.9 | completed |
| connector | 94176.1 | completed |
| document_discovery | 94176.2 | completed |
| document_download | 1263152.2 | completed |
| extraction | 61.2 | completed |
| candidate_validation | 5.3 | completed |
| publish_queue | 5.3 | completed |
| append_dataset | 119.7 | completed |
| export | 0.4 | skipped |
| git_commit | 0.3 | skipped |
| push | 0.3 | skipped |

## Counters

```json
{
  "summary": {
    "connectors_ok": 7,
    "connectors_failed": 0,
    "documents_discovered": 31,
    "documents_downloaded": 277,
    "documents_failed": 0,
    "documents_duplicates": 223,
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
      "industry_library": 2
    },
    "balance_ok": true
  },
  "document_queue": {
    "queued": 0,
    "processing": 0,
    "completed": 277,
    "failed": 0,
    "duplicates": 223
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
