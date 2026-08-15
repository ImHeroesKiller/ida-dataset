# Production Trace

**Generated:** 2026-08-15T09:41:43+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260815-B5CDB5`
**Session ID:** `SES-20260815-4F8CD6`
**Started:** 2026-08-15T09:27:48+00:00
**Finished:** 2026-08-15T09:41:43+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6361.8 | 43 | 0 | — |
| document_discovery | completed | 6361.9 | 43 | 0 | — |
| document_download | completed | 80459.0 | 31 | 0 | — |
| extraction | completed | 24.9 | 0 | 5 | — |
| candidate_validation | completed | 9.2 | 0 | 5 | — |
| publish_queue | completed | 9.2 | 0 | 5 | — |
| append_dataset | completed | 17.6 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 1.8 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
