# Production Trace

**Generated:** 2026-08-13T22:00:43+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260813-A3195B`
**Session ID:** `SES-20260813-6B6A93`
**Started:** 2026-08-13T21:47:43+00:00
**Finished:** 2026-08-13T22:00:43+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6142.1 | 77 | 0 | — |
| document_discovery | completed | 6142.2 | 77 | 0 | — |
| document_download | completed | 40522.5 | 42 | 0 | — |
| extraction | completed | 24.0 | 0 | 5 | — |
| candidate_validation | completed | 7.1 | 0 | 5 | — |
| publish_queue | completed | 7.0 | 0 | 5 | — |
| append_dataset | completed | 22.1 | 0 | 5 | — |
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
