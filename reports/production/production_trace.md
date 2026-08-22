# Production Trace

**Generated:** 2026-08-22T15:40:13+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260822-FC782A`
**Session ID:** `SES-20260822-1D7D5A`
**Started:** 2026-08-22T15:22:43+00:00
**Finished:** 2026-08-22T15:40:13+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.8 | 0 | 0 | — |
| source_discovery | completed | 2.3 | 0 | 0 | — |
| connector | completed | 6136.2 | 77 | 0 | — |
| document_discovery | completed | 6136.3 | 77 | 0 | — |
| document_download | completed | 310318.1 | 42 | 0 | — |
| extraction | completed | 29.7 | 0 | 5 | — |
| candidate_validation | completed | 14.6 | 0 | 5 | — |
| publish_queue | completed | 14.6 | 0 | 5 | — |
| append_dataset | completed | 17.2 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
