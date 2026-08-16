# Production Trace

**Generated:** 2026-08-16T15:37:36+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260816-1817C6`
**Session ID:** `SES-20260816-BEAB5E`
**Started:** 2026-08-16T15:23:30+00:00
**Finished:** 2026-08-16T15:37:36+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.1 | 0 | 0 | — |
| connector | completed | 6224.9 | 47 | 0 | — |
| document_discovery | completed | 6225.0 | 47 | 0 | — |
| document_download | completed | 98836.7 | 31 | 0 | — |
| extraction | completed | 27.3 | 0 | 5 | — |
| candidate_validation | completed | 10.5 | 0 | 5 | — |
| publish_queue | completed | 10.5 | 0 | 5 | — |
| append_dataset | completed | 17.9 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
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
