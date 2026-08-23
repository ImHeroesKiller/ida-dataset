# Production Trace

**Generated:** 2026-08-23T07:52:28+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260823-C49A92`
**Session ID:** `SES-20260823-6698F6`
**Started:** 2026-08-23T07:34:54+00:00
**Finished:** 2026-08-23T07:52:28+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6170.8 | 77 | 0 | — |
| document_discovery | completed | 6171.0 | 77 | 0 | — |
| document_download | completed | 308911.2 | 42 | 0 | — |
| extraction | completed | 38.5 | 0 | 5 | — |
| candidate_validation | completed | 19.8 | 0 | 5 | — |
| publish_queue | completed | 19.9 | 0 | 5 | — |
| append_dataset | completed | 24.1 | 0 | 5 | — |
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
