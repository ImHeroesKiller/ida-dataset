# Production Trace

**Generated:** 2026-08-19T07:04:57+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260819-568761`
**Session ID:** `SES-20260819-BD99C2`
**Started:** 2026-08-19T06:47:16+00:00
**Finished:** 2026-08-19T07:04:57+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.6 | 0 | 0 | — |
| source_discovery | completed | 2.2 | 0 | 0 | — |
| connector | completed | 6228.2 | 47 | 0 | — |
| document_discovery | completed | 6228.3 | 47 | 0 | — |
| document_download | completed | 312956.3 | 31 | 0 | — |
| extraction | completed | 23.4 | 0 | 5 | — |
| candidate_validation | completed | 9.4 | 0 | 5 | — |
| publish_queue | completed | 9.4 | 0 | 5 | — |
| append_dataset | completed | 10.4 | 0 | 5 | — |
| export | skipped | 0.2 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
