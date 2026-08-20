# Production Trace

**Generated:** 2026-08-20T10:46:47+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260820-F6965C`
**Session ID:** `SES-20260820-A1B323`
**Started:** 2026-08-20T10:32:44+00:00
**Finished:** 2026-08-20T10:46:47+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6221.6 | 73 | 0 | — |
| document_discovery | completed | 6221.8 | 73 | 0 | — |
| document_download | completed | 331935.8 | 42 | 0 | — |
| extraction | completed | 33.5 | 0 | 5 | — |
| candidate_validation | completed | 15.7 | 0 | 5 | — |
| publish_queue | completed | 15.8 | 0 | 5 | — |
| append_dataset | completed | 23.4 | 0 | 5 | — |
| export | skipped | 0.8 | 0 | 0 | — |
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
