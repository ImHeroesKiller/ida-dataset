# Production Trace

**Generated:** 2026-08-14T18:07:52+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260814-F69227`
**Session ID:** `SES-20260814-3CC70B`
**Started:** 2026-08-14T17:54:41+00:00
**Finished:** 2026-08-14T18:07:52+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6227.8 | 77 | 0 | — |
| document_discovery | completed | 6227.9 | 77 | 0 | — |
| document_download | completed | 46822.0 | 42 | 0 | — |
| extraction | completed | 25.2 | 0 | 5 | — |
| candidate_validation | completed | 8.0 | 0 | 5 | — |
| publish_queue | completed | 7.9 | 0 | 5 | — |
| append_dataset | completed | 22.3 | 0 | 5 | — |
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
