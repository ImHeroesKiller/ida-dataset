# Runtime Statistics

**Session:** `SES-20260728-AF397C`
**Mission:** corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_library across enterprise function Corporate Governance (function_gap=58.4; not BD-only); dataset_gap=112.922; mode=BOOTSTRAP
**Total stage time (ms):** 414556.8

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 1.2 | completed |
| source_discovery | 3.1 | completed |
| connector | 94103.8 | completed |
| document_discovery | 94104.0 | completed |
| document_download | 226196.3 | completed |
| extraction | 99.9 | completed |
| candidate_validation | 5.5 | completed |
| publish_queue | 5.4 | completed |
| append_dataset | 36.7 | completed |
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
