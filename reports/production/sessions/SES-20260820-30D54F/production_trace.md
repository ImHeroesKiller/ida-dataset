# Production Trace

**Generated:** 2026-08-20T19:00:07+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260820-651E50`
**Session ID:** `SES-20260820-30D54F`
**Started:** 2026-08-20T18:41:28+00:00
**Finished:** 2026-08-20T19:00:07+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.2 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6216.8 | 77 | 0 | — |
| document_discovery | completed | 6216.9 | 77 | 0 | — |
| document_download | completed | 378762.8 | 42 | 0 | — |
| extraction | completed | 34.9 | 0 | 5 | — |
| candidate_validation | completed | 16.0 | 0 | 5 | — |
| publish_queue | completed | 16.1 | 0 | 5 | — |
| append_dataset | completed | 23.9 | 0 | 5 | — |
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
