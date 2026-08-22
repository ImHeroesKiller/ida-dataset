# Production Trace

**Generated:** 2026-08-22T10:43:13+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260822-3C6B36`
**Session ID:** `SES-20260822-16F81D`
**Started:** 2026-08-22T10:25:30+00:00
**Finished:** 2026-08-22T10:43:13+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.8 | 0 | 0 | — |
| source_discovery | completed | 2.7 | 0 | 0 | — |
| connector | completed | 6145.0 | 77 | 0 | — |
| document_discovery | completed | 6145.1 | 77 | 0 | — |
| document_download | completed | 318414.3 | 42 | 0 | — |
| extraction | completed | 36.0 | 0 | 5 | — |
| candidate_validation | completed | 17.7 | 0 | 5 | — |
| publish_queue | completed | 17.7 | 0 | 5 | — |
| append_dataset | completed | 23.3 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
