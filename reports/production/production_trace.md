# Production Trace

**Generated:** 2026-08-15T06:51:37+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260815-ACC0FA`
**Session ID:** `SES-20260815-A4FD0A`
**Started:** 2026-08-15T06:40:27+00:00
**Finished:** 2026-08-15T06:51:37+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.4 | 0 | 0 | — |
| connector | completed | 6175.0 | 79 | 0 | — |
| document_discovery | completed | 6175.1 | 79 | 0 | — |
| document_download | completed | 43240.1 | 42 | 0 | — |
| extraction | completed | 26.2 | 0 | 5 | — |
| candidate_validation | completed | 9.2 | 0 | 5 | — |
| publish_queue | completed | 9.2 | 0 | 5 | — |
| append_dataset | completed | 23.4 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
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
