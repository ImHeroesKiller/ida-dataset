# Production Trace

**Generated:** 2026-08-24T10:55:53+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260824-2CA3AA`
**Session ID:** `SES-20260824-394568`
**Started:** 2026-08-24T10:39:09+00:00
**Finished:** 2026-08-24T10:55:53+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.8 | 0 | 0 | — |
| source_discovery | completed | 2.3 | 0 | 0 | — |
| connector | completed | 6168.9 | 73 | 0 | — |
| document_discovery | completed | 6169.0 | 73 | 0 | — |
| document_download | completed | 311067.7 | 42 | 0 | — |
| extraction | completed | 30.8 | 0 | 5 | — |
| candidate_validation | completed | 96.4 | 0 | 5 | — |
| publish_queue | completed | 96.4 | 0 | 5 | — |
| append_dataset | completed | 17.6 | 0 | 5 | — |
| export | skipped | 0.2 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
