# Production Trace

**Generated:** 2026-08-21T09:00:09+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260821-FE6A00`
**Session ID:** `SES-20260821-C258E8`
**Started:** 2026-08-21T08:42:28+00:00
**Finished:** 2026-08-21T09:00:09+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.3 | 0 | 0 | — |
| connector | completed | 6158.0 | 76 | 0 | — |
| document_discovery | completed | 6158.1 | 76 | 0 | — |
| document_download | completed | 311825.1 | 42 | 0 | — |
| extraction | completed | 35.3 | 0 | 5 | — |
| candidate_validation | completed | 16.9 | 0 | 5 | — |
| publish_queue | completed | 16.9 | 0 | 5 | — |
| append_dataset | completed | 22.6 | 0 | 5 | — |
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
