# Production Trace

**Generated:** 2026-08-24T09:09:08+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260824-87AC4A`
**Session ID:** `SES-20260824-8BCB13`
**Started:** 2026-08-24T08:50:48+00:00
**Finished:** 2026-08-24T09:09:08+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6227.0 | 73 | 0 | — |
| document_discovery | completed | 6227.2 | 73 | 0 | — |
| document_download | completed | 342275.2 | 42 | 0 | — |
| extraction | completed | 39.7 | 0 | 5 | — |
| candidate_validation | completed | 20.7 | 0 | 5 | — |
| publish_queue | completed | 20.7 | 0 | 5 | — |
| append_dataset | completed | 22.1 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
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
