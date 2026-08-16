# Production Trace

**Generated:** 2026-08-16T23:35:31+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260816-9BE4E6`
**Session ID:** `SES-20260816-C8B198`
**Started:** 2026-08-16T23:21:32+00:00
**Finished:** 2026-08-16T23:35:31+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.8 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6198.8 | 47 | 0 | — |
| document_discovery | completed | 6198.9 | 47 | 0 | — |
| document_download | completed | 94393.6 | 31 | 0 | — |
| extraction | completed | 28.4 | 0 | 5 | — |
| candidate_validation | completed | 11.1 | 0 | 5 | — |
| publish_queue | completed | 11.1 | 0 | 5 | — |
| append_dataset | completed | 18.9 | 0 | 5 | — |
| export | skipped | 1.4 | 0 | 0 | — |
| git_commit | skipped | 1.1 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
