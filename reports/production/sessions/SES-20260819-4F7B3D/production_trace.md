# Production Trace

**Generated:** 2026-08-19T20:49:09+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260819-8DB403`
**Session ID:** `SES-20260819-4F7B3D`
**Started:** 2026-08-19T20:31:17+00:00
**Finished:** 2026-08-19T20:49:09+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.2 | 0 | 0 | — |
| connector | completed | 6142.8 | 40 | 0 | — |
| document_discovery | completed | 6142.9 | 40 | 0 | — |
| document_download | completed | 316919.8 | 31 | 0 | — |
| extraction | completed | 32.3 | 0 | 5 | — |
| candidate_validation | completed | 15.2 | 0 | 5 | — |
| publish_queue | completed | 15.2 | 0 | 5 | — |
| append_dataset | completed | 18.2 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
