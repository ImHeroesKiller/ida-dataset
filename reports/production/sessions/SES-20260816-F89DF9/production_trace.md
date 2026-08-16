# Production Trace

**Generated:** 2026-08-16T21:32:08+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260816-FC27EB`
**Session ID:** `SES-20260816-F89DF9`
**Started:** 2026-08-16T21:21:44+00:00
**Finished:** 2026-08-16T21:32:08+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6147.0 | 73 | 0 | — |
| document_discovery | completed | 6147.2 | 73 | 0 | — |
| document_download | completed | 98722.6 | 42 | 0 | — |
| extraction | completed | 28.9 | 0 | 5 | — |
| candidate_validation | completed | 11.0 | 0 | 5 | — |
| publish_queue | completed | 11.0 | 0 | 5 | — |
| append_dataset | completed | 31.7 | 0 | 5 | — |
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
