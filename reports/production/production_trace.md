# Production Trace

**Generated:** 2026-08-19T17:47:28+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260819-9C5975`
**Session ID:** `SES-20260819-BA4D84`
**Started:** 2026-08-19T17:29:34+00:00
**Finished:** 2026-08-19T17:47:28+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6204.4 | 40 | 0 | — |
| document_discovery | completed | 6204.6 | 40 | 0 | — |
| document_download | completed | 322332.6 | 31 | 0 | — |
| extraction | completed | 33.1 | 0 | 5 | — |
| candidate_validation | completed | 15.0 | 0 | 5 | — |
| publish_queue | completed | 15.0 | 0 | 5 | — |
| append_dataset | completed | 18.0 | 0 | 5 | — |
| export | skipped | 0.5 | 0 | 0 | — |
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
