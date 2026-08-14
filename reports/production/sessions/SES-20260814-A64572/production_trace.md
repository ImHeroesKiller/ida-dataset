# Production Trace

**Generated:** 2026-08-14T15:06:53+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260814-E0D1E9`
**Session ID:** `SES-20260814-A64572`
**Started:** 2026-08-14T14:53:43+00:00
**Finished:** 2026-08-14T15:06:53+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6202.4 | 77 | 0 | — |
| document_discovery | completed | 6202.5 | 77 | 0 | — |
| document_download | completed | 40391.1 | 42 | 0 | — |
| extraction | completed | 25.4 | 0 | 5 | — |
| candidate_validation | completed | 8.6 | 0 | 5 | — |
| publish_queue | completed | 8.6 | 0 | 5 | — |
| append_dataset | completed | 23.3 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
| git_commit | skipped | 0.6 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
