# Production Trace

**Generated:** 2026-08-20T17:49:19+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260820-B74693`
**Session ID:** `SES-20260820-147AE2`
**Started:** 2026-08-20T17:31:14+00:00
**Finished:** 2026-08-20T17:49:19+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6196.1 | 47 | 0 | — |
| document_discovery | completed | 6196.2 | 47 | 0 | — |
| document_download | completed | 339230.9 | 31 | 0 | — |
| extraction | completed | 33.8 | 0 | 5 | — |
| candidate_validation | completed | 15.9 | 0 | 5 | — |
| publish_queue | completed | 15.9 | 0 | 5 | — |
| append_dataset | completed | 19.5 | 0 | 5 | — |
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
