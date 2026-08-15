# Production Trace

**Generated:** 2026-08-15T16:37:38+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260815-D7B9B5`
**Session ID:** `SES-20260815-F84088`
**Started:** 2026-08-15T16:26:31+00:00
**Finished:** 2026-08-15T16:37:38+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6184.7 | 73 | 0 | — |
| document_discovery | completed | 6184.9 | 73 | 0 | — |
| document_download | completed | 37559.9 | 42 | 0 | — |
| extraction | completed | 26.5 | 0 | 5 | — |
| candidate_validation | completed | 8.8 | 0 | 5 | — |
| publish_queue | completed | 9.0 | 0 | 5 | — |
| append_dataset | completed | 22.2 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
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
