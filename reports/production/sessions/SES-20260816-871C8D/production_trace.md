# Production Trace

**Generated:** 2026-08-16T20:35:24+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260816-D87BB2`
**Session ID:** `SES-20260816-871C8D`
**Started:** 2026-08-16T20:24:16+00:00
**Finished:** 2026-08-16T20:35:24+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6214.1 | 23 | 0 | — |
| document_discovery | completed | 6214.2 | 23 | 0 | — |
| document_download | completed | 98845.9 | 11 | 0 | — |
| extraction | completed | 25.7 | 0 | 5 | — |
| candidate_validation | completed | 10.4 | 0 | 5 | — |
| publish_queue | completed | 10.5 | 0 | 5 | — |
| append_dataset | completed | 10.2 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
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
