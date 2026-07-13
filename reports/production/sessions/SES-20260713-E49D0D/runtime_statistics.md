# Runtime Statistics

**Session:** `SES-20260713-E49D0D`
**Mission:** corporate governance — service knowledge for Corporate Governance — continuous knowledge manufacturing for service_library across enterprise function Corporate Governance (function_gap=58.4; not BD-only); dataset_gap=112.922; mode=BOOTSTRAP
**Total stage time (ms):** 402518.4

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 1.2 | completed |
| source_discovery | 2.8 | completed |
| connector | 94016.6 | completed |
| document_discovery | 94016.8 | completed |
| document_download | 214326.9 | completed |
| extraction | 90.2 | completed |
| candidate_validation | 4.3 | completed |
| publish_queue | 4.3 | completed |
| append_dataset | 54.3 | completed |
| export | 0.3 | skipped |
| git_commit | 0.3 | skipped |
| push | 0.4 | skipped |

## Counters

```json
{
  "summary": {
    "connectors_ok": 7,
    "connectors_failed": 0,
    "documents_discovered": 31,
    "documents_downloaded": 95,
    "documents_failed": 0,
    "documents_duplicates": 82,
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
    "completed": 95,
    "failed": 0,
    "duplicates": 82
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
