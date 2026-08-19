# Production Trace

**Generated:** 2026-08-19T15:51:34+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260819-63E5A9`
**Session ID:** `SES-20260819-A565F5`
**Started:** 2026-08-19T15:34:03+00:00
**Finished:** 2026-08-19T15:51:34+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6203.3 | 77 | 0 | — |
| document_discovery | completed | 6203.4 | 77 | 0 | — |
| document_download | completed | 308842.3 | 42 | 0 | — |
| extraction | completed | 32.7 | 0 | 5 | — |
| candidate_validation | completed | 14.2 | 0 | 5 | — |
| publish_queue | completed | 14.2 | 0 | 5 | — |
| append_dataset | completed | 23.2 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.4 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
