# Runtime Statistics

**Session:** `SES-20260719-7860C3`
**Mission:** corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_library across enterprise function Corporate Governance (function_gap=58.4; not BD-only); dataset_gap=112.922; mode=BOOTSTRAP
**Total stage time (ms):** 452659.1

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 0.8 | completed |
| source_discovery | 2.3 | completed |
| connector | 93999.6 | completed |
| document_discovery | 93999.7 | completed |
| document_download | 264539.2 | completed |
| extraction | 71.1 | completed |
| candidate_validation | 8.1 | completed |
| publish_queue | 8.1 | completed |
| append_dataset | 29.5 | completed |
| export | 0.3 | skipped |
| git_commit | 0.2 | skipped |
| push | 0.2 | skipped |

## Counters

```json
{
  "summary": {
    "connectors_ok": 7,
    "connectors_failed": 0,
    "documents_discovered": 31,
    "documents_downloaded": 50,
    "documents_failed": 0,
    "documents_duplicates": 17,
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
    "completed": 50,
    "failed": 0,
    "duplicates": 17
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
