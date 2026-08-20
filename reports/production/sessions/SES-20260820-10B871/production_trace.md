# Production Trace

**Generated:** 2026-08-20T04:56:45+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260820-A69EDF`
**Session ID:** `SES-20260820-10B871`
**Started:** 2026-08-20T04:39:07+00:00
**Finished:** 2026-08-20T04:56:45+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.6 | 0 | 0 | — |
| source_discovery | completed | 2.1 | 0 | 0 | — |
| connector | completed | 6147.7 | 75 | 0 | — |
| document_discovery | completed | 6147.8 | 75 | 0 | — |
| document_download | completed | 310629.4 | 42 | 0 | — |
| extraction | completed | 26.1 | 0 | 5 | — |
| candidate_validation | completed | 15.7 | 0 | 5 | — |
| publish_queue | completed | 15.8 | 0 | 5 | — |
| append_dataset | completed | 12.7 | 0 | 5 | — |
| export | skipped | 7.2 | 0 | 0 | — |
| git_commit | skipped | 0.4 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
