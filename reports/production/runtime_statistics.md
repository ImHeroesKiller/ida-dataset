# Runtime Statistics

**Session:** `SES-20260712-277571`
**Mission:** corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_library across enterprise function Corporate Governance (function_gap=58.4; not BD-only); dataset_gap=112.922; mode=BOOTSTRAP
**Total stage time (ms):** 672570.4

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 0.5 | completed |
| source_discovery | 1.8 | completed |
| connector | 94240.7 | completed |
| document_discovery | 94241.0 | completed |
| document_download | 483987.6 | completed |
| extraction | 54.3 | completed |
| candidate_validation | 2.2 | completed |
| publish_queue | 2.3 | completed |
| append_dataset | 37.5 | completed |
| export | 0.2 | skipped |
| git_commit | 2.1 | skipped |
| push | 0.2 | skipped |

## Counters

```json
{
  "summary": {
    "connectors_ok": 7,
    "connectors_failed": 0,
    "documents_discovered": 31,
    "documents_downloaded": 133,
    "documents_failed": 0,
    "documents_duplicates": 101,
    "candidates_extracted": 1,
    "candidates_validated": 1,
    "candidates_rejected": 0,
    "rows_published": 1,
    "rows_duplicate": 0
  },
  "publish": {
    "extracted": 1,
    "validated": 1,
    "rejected": 0,
    "queued": 1,
    "published": 1,
    "skipped": 0,
    "duplicate": 0,
    "by_dataset": {
      "industry_library": 1
    },
    "balance_ok": true
  },
  "document_queue": {
    "queued": 0,
    "processing": 0,
    "completed": 133,
    "failed": 0,
    "duplicates": 101
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
