# Production Trace

**Generated:** 2026-08-15T08:44:07+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260815-20E7A0`
**Session ID:** `SES-20260815-507300`
**Started:** 2026-08-15T08:31:05+00:00
**Finished:** 2026-08-15T08:44:07+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6254.9 | 77 | 0 | — |
| document_discovery | completed | 6255.1 | 77 | 0 | — |
| document_download | completed | 44464.6 | 42 | 0 | — |
| extraction | completed | 24.3 | 0 | 5 | — |
| candidate_validation | completed | 7.2 | 0 | 5 | — |
| publish_queue | completed | 7.2 | 0 | 5 | — |
| append_dataset | completed | 16.0 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
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
