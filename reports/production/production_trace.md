# Production Trace

**Generated:** 2026-08-19T14:04:07+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260819-05FD4B`
**Session ID:** `SES-20260819-0F6047`
**Started:** 2026-08-19T13:46:28+00:00
**Finished:** 2026-08-19T14:04:07+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6205.2 | 74 | 0 | — |
| document_discovery | completed | 6205.4 | 74 | 0 | — |
| document_download | completed | 309275.3 | 42 | 0 | — |
| extraction | completed | 33.0 | 0 | 5 | — |
| candidate_validation | completed | 14.5 | 0 | 5 | — |
| publish_queue | completed | 14.5 | 0 | 5 | — |
| append_dataset | completed | 23.7 | 0 | 5 | — |
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
