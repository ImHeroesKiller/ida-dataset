# Production Trace

**Generated:** 2026-08-24T03:22:57+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260824-179641`
**Session ID:** `SES-20260824-827AD2`
**Started:** 2026-08-24T03:05:18+00:00
**Finished:** 2026-08-24T03:22:57+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.5 | 0 | 0 | — |
| source_discovery | completed | 1.9 | 0 | 0 | — |
| connector | completed | 6231.8 | 43 | 0 | — |
| document_discovery | completed | 6231.9 | 43 | 0 | — |
| document_download | completed | 306521.8 | 31 | 0 | — |
| extraction | completed | 24.6 | 0 | 5 | — |
| candidate_validation | completed | 11.3 | 0 | 5 | — |
| publish_queue | completed | 11.4 | 0 | 5 | — |
| append_dataset | completed | 9.6 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
| git_commit | skipped | 40.0 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
