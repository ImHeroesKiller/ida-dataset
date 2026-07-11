# Production Trace

**Generated:** 2026-07-11T17:59:27+00:00
**Mission:** Expand Industry Library
**Mission ID:** `MIS-20260711-CF302E`
**Session ID:** `SES-20260711-DA29BA`
**Started:** 2026-07-11T17:38:49+00:00
**Finished:** 2026-07-11T17:59:27+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.6 | 0 | 0 | — |
| connector | completed | 94110.2 | 204 | 0 | — |
| document_discovery | completed | 94110.4 | 204 | 0 | — |
| document_download | completed | 370722.2 | 90 | 0 | — |
| extraction | completed | 89.8 | 0 | 3 | — |
| candidate_validation | completed | 4.3 | 0 | 2 | — |
| publish_queue | completed | 4.4 | 0 | 3 | — |
| append_dataset | completed | 36.5 | 0 | 2 | — |
| export | skipped | 0.2 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **28**
- Documents downloaded: **90**
- Candidates extracted: **3**
- Candidates validated: **2**
- Candidates rejected: **1**
- Rows published: **2**
- Duplicates: **0**
