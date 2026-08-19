# Production Trace

**Generated:** 2026-08-19T07:58:17+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260819-D97818`
**Session ID:** `SES-20260819-D19791`
**Started:** 2026-08-19T07:40:38+00:00
**Finished:** 2026-08-19T07:58:17+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6219.1 | 77 | 0 | — |
| document_discovery | completed | 6219.3 | 77 | 0 | — |
| document_download | completed | 310984.4 | 42 | 0 | — |
| extraction | completed | 31.7 | 0 | 5 | — |
| candidate_validation | completed | 13.5 | 0 | 5 | — |
| publish_queue | completed | 13.5 | 0 | 5 | — |
| append_dataset | completed | 23.3 | 0 | 5 | — |
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
