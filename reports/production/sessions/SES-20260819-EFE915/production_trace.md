# Production Trace

**Generated:** 2026-08-19T22:53:30+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260819-D6EBB4`
**Session ID:** `SES-20260819-EFE915`
**Started:** 2026-08-19T22:27:34+00:00
**Finished:** 2026-08-19T22:53:30+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6199.8 | 75 | 0 | — |
| document_discovery | completed | 6199.9 | 75 | 0 | — |
| document_download | completed | 806610.2 | 54 | 0 | — |
| extraction | completed | 33.8 | 0 | 5 | — |
| candidate_validation | completed | 14.9 | 0 | 5 | — |
| publish_queue | completed | 14.8 | 0 | 5 | — |
| append_dataset | completed | 29.1 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **54**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
