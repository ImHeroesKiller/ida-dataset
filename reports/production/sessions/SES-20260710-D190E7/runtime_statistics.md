# Runtime Statistics

**Session:** `SES-20260710-D190E7`
**Mission:** Bootstrap Buyer Persona Library — continuous knowledge manufacturing for buyer_persona_library (gap_score=142.5, universe_remaining=5000, mode=BOOTSTRAP)
**Total stage time (ms):** 48195.0

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 1.0 | completed |
| source_discovery | 2.7 | completed |
| connector | 6180.7 | completed |
| document_discovery | 6180.8 | completed |
| document_download | 35800.5 | completed |
| extraction | 16.2 | completed |
| candidate_validation | 4.1 | completed |
| publish_queue | 4.2 | completed |
| append_dataset | 3.8 | completed |
| export | 0.4 | skipped |
| git_commit | 0.3 | skipped |
| push | 0.3 | skipped |

## Counters

```json
{
  "summary": {
    "connectors_ok": 7,
    "connectors_failed": 0,
    "documents_discovered": 6,
    "documents_downloaded": 5,
    "documents_failed": 0,
    "documents_duplicates": 3,
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
    "completed": 5,
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
