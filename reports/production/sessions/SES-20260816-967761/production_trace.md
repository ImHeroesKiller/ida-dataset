# Production Trace

**Generated:** 2026-08-16T09:43:05+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260816-EF2E16`
**Session ID:** `SES-20260816-967761`
**Started:** 2026-08-16T09:29:02+00:00
**Finished:** 2026-08-16T09:43:05+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 3.1 | 0 | 0 | — |
| connector | completed | 6207.0 | 27 | 0 | — |
| document_discovery | completed | 6207.1 | 27 | 0 | — |
| document_download | completed | 99525.1 | 11 | 0 | — |
| extraction | completed | 25.3 | 0 | 5 | — |
| candidate_validation | completed | 10.1 | 0 | 5 | — |
| publish_queue | completed | 10.1 | 0 | 5 | — |
| append_dataset | completed | 10.3 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **11**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
