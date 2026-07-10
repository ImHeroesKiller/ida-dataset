# Runtime Statistics

**Session:** `SES-20260710-725C07`
**Mission:** Bootstrap Buyer Persona Library — continuous knowledge manufacturing for buyer_persona_library (gap_score=142.5, universe_remaining=5000, mode=BOOTSTRAP)
**Total stage time (ms):** 47581.0

## Stage durations

| Stage | ms | Status |
|-------|---:|--------|
| mission | 0.7 | completed |
| source_discovery | 2.2 | completed |
| connector | 6146.1 | completed |
| document_discovery | 6146.2 | completed |
| document_download | 35260.5 | completed |
| extraction | 15.2 | completed |
| candidate_validation | 3.3 | completed |
| publish_queue | 3.3 | completed |
| append_dataset | 2.9 | completed |
| export | 0.2 | skipped |
| git_commit | 0.2 | skipped |
| push | 0.2 | skipped |

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
