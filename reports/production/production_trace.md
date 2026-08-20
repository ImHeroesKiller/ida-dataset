# Production Trace

**Generated:** 2026-08-20T16:55:41+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260820-CAEE4F`
**Session ID:** `SES-20260820-105549`
**Started:** 2026-08-20T16:37:36+00:00
**Finished:** 2026-08-20T16:55:41+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6260.6 | 77 | 0 | — |
| document_discovery | completed | 6260.7 | 77 | 0 | — |
| document_download | completed | 336740.7 | 42 | 0 | — |
| extraction | completed | 37.6 | 0 | 5 | — |
| candidate_validation | completed | 13.3 | 0 | 5 | — |
| publish_queue | completed | 13.3 | 0 | 5 | — |
| append_dataset | completed | 15.4 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.4 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
