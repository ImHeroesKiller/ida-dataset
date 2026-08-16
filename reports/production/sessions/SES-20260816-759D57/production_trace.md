# Production Trace

**Generated:** 2026-08-16T22:36:07+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260816-CAF316`
**Session ID:** `SES-20260816-759D57`
**Started:** 2026-08-16T22:22:17+00:00
**Finished:** 2026-08-16T22:36:07+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.8 | 0 | 0 | — |
| source_discovery | completed | 2.3 | 0 | 0 | — |
| connector | completed | 6148.6 | 77 | 0 | — |
| document_discovery | completed | 6148.7 | 77 | 0 | — |
| document_download | completed | 97103.1 | 42 | 0 | — |
| extraction | completed | 24.7 | 0 | 5 | — |
| candidate_validation | completed | 8.3 | 0 | 5 | — |
| publish_queue | completed | 8.3 | 0 | 5 | — |
| append_dataset | completed | 16.9 | 0 | 5 | — |
| export | skipped | 0.2 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
