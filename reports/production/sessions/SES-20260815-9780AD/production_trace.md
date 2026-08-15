# Production Trace

**Generated:** 2026-08-15T13:41:20+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260815-4E2CAC`
**Session ID:** `SES-20260815-9780AD`
**Started:** 2026-08-15T13:32:13+00:00
**Finished:** 2026-08-15T13:41:20+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.6 | 0 | 0 | — |
| source_discovery | completed | 2.2 | 0 | 0 | — |
| connector | completed | 6205.4 | 73 | 0 | — |
| document_discovery | completed | 6205.5 | 73 | 0 | — |
| document_download | completed | 38199.6 | 42 | 0 | — |
| extraction | completed | 25.5 | 0 | 5 | — |
| candidate_validation | completed | 9.3 | 0 | 5 | — |
| publish_queue | completed | 9.3 | 0 | 5 | — |
| append_dataset | completed | 12.6 | 0 | 5 | — |
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
