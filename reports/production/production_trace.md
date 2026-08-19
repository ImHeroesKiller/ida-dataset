# Production Trace

**Generated:** 2026-08-19T21:45:57+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260819-E8F0CA`
**Session ID:** `SES-20260819-4EDB2F`
**Started:** 2026-08-19T21:28:16+00:00
**Finished:** 2026-08-19T21:45:57+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6227.2 | 40 | 0 | — |
| document_discovery | completed | 6227.4 | 40 | 0 | — |
| document_download | completed | 309048.9 | 31 | 0 | — |
| extraction | completed | 32.7 | 0 | 5 | — |
| candidate_validation | completed | 14.6 | 0 | 5 | — |
| publish_queue | completed | 14.5 | 0 | 5 | — |
| append_dataset | completed | 19.0 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
