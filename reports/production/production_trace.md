# Production Trace

**Generated:** 2026-08-19T13:09:58+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260819-8ECBF6`
**Session ID:** `SES-20260819-667595`
**Started:** 2026-08-19T12:51:37+00:00
**Finished:** 2026-08-19T13:09:58+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6254.2 | 77 | 0 | — |
| document_discovery | completed | 6254.3 | 77 | 0 | — |
| document_download | completed | 348442.3 | 42 | 0 | — |
| extraction | completed | 74.5 | 0 | 5 | — |
| candidate_validation | completed | 37.9 | 0 | 5 | — |
| publish_queue | completed | 37.9 | 0 | 5 | — |
| append_dataset | completed | 37.1 | 0 | 5 | — |
| export | skipped | 0.9 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
