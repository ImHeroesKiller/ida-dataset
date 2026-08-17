# Production Trace

**Generated:** 2026-08-17T19:42:54+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260817-E5CAD6`
**Session ID:** `SES-20260817-5C955E`
**Started:** 2026-08-17T19:29:49+00:00
**Finished:** 2026-08-17T19:42:54+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.2 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6227.6 | 77 | 0 | — |
| document_discovery | completed | 6227.7 | 77 | 0 | — |
| document_download | completed | 36788.3 | 42 | 0 | — |
| extraction | completed | 30.1 | 0 | 5 | — |
| candidate_validation | completed | 12.1 | 0 | 5 | — |
| publish_queue | completed | 12.1 | 0 | 5 | — |
| append_dataset | completed | 23.3 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
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
