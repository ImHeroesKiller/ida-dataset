# Production Trace

**Generated:** 2026-08-24T05:57:24+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260824-068712`
**Session ID:** `SES-20260824-226B0C`
**Started:** 2026-08-24T05:39:43+00:00
**Finished:** 2026-08-24T05:57:24+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6220.5 | 75 | 0 | — |
| document_discovery | completed | 6220.6 | 75 | 0 | — |
| document_download | completed | 307683.5 | 42 | 0 | — |
| extraction | completed | 38.8 | 0 | 5 | — |
| candidate_validation | completed | 19.8 | 0 | 5 | — |
| publish_queue | completed | 19.8 | 0 | 5 | — |
| append_dataset | completed | 23.4 | 0 | 5 | — |
| export | skipped | 0.5 | 0 | 0 | — |
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
