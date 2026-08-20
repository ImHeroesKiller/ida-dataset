# Production Trace

**Generated:** 2026-08-20T20:47:52+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260820-76B297`
**Session ID:** `SES-20260820-95F136`
**Started:** 2026-08-20T20:30:08+00:00
**Finished:** 2026-08-20T20:47:52+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.5 | 0 | 0 | — |
| source_discovery | completed | 2.0 | 0 | 0 | — |
| connector | completed | 6187.9 | 77 | 0 | — |
| document_discovery | completed | 6188.0 | 77 | 0 | — |
| document_download | completed | 316255.6 | 42 | 0 | — |
| extraction | completed | 21.0 | 0 | 5 | — |
| candidate_validation | completed | 8.2 | 0 | 5 | — |
| publish_queue | completed | 8.3 | 0 | 5 | — |
| append_dataset | completed | 10.7 | 0 | 5 | — |
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
