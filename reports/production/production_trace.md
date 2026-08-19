# Production Trace

**Generated:** 2026-08-19T04:07:31+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260819-9F372F`
**Session ID:** `SES-20260819-3C2ECC`
**Started:** 2026-08-19T03:53:52+00:00
**Finished:** 2026-08-19T04:07:31+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6181.5 | 73 | 0 | — |
| document_discovery | completed | 6181.6 | 73 | 0 | — |
| document_download | completed | 305876.4 | 42 | 0 | — |
| extraction | completed | 31.6 | 0 | 5 | — |
| candidate_validation | completed | 13.4 | 0 | 5 | — |
| publish_queue | completed | 13.4 | 0 | 5 | — |
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
