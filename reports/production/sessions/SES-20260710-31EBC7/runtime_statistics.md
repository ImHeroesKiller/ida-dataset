# Runtime Statistics

**Session:** `SES-20260710-31EBC7`
**Mission:** Bootstrap Buyer Persona Library — continuous knowledge manufacturing for buyer_persona_library (gap_score=142.5, universe_remaining=5000, mode=BOOTSTRAP)
**Total stage time (ms):** 47796.6

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 1.1 | completed |
| source_discovery | 2.7 | completed |
| connector | 6206.7 | completed |
| document_discovery | 6206.9 | completed |
| document_download | 35345.8 | completed |
| extraction | 19.0 | completed |
| candidate_validation | 4.8 | completed |
| publish_queue | 4.8 | completed |
| append_dataset | 3.9 | completed |
| export | 0.3 | skipped |
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
    "candidates_extracted": 3,
    "candidates_validated": 3,
    "candidates_rejected": 0,
    "rows_published": 3,
    "rows_duplicate": 0
  },
  "publish": {
    "extracted": 3,
    "validated": 3,
    "rejected": 0,
    "queued": 3,
    "published": 3,
    "skipped": 0,
    "duplicate": 0,
    "by_dataset": {
      "business_signal_library": 3
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
