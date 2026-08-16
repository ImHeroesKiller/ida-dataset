# Production Trace

**Generated:** 2026-08-16T06:55:41+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260816-C88FE8`
**Session ID:** `SES-20260816-C252A8`
**Started:** 2026-08-16T06:41:46+00:00
**Finished:** 2026-08-16T06:55:41+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6199.2 | 27 | 0 | — |
| document_discovery | completed | 6199.4 | 27 | 0 | — |
| document_download | completed | 95730.3 | 11 | 0 | — |
| extraction | completed | 24.6 | 0 | 5 | — |
| candidate_validation | completed | 9.8 | 0 | 5 | — |
| publish_queue | completed | 9.8 | 0 | 5 | — |
| append_dataset | completed | 9.9 | 0 | 5 | — |
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
