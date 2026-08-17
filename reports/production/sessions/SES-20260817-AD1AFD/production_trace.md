# Production Trace

**Generated:** 2026-08-17T18:54:36+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260817-4C36E8`
**Session ID:** `SES-20260817-AD1AFD`
**Started:** 2026-08-17T18:41:24+00:00
**Finished:** 2026-08-17T18:54:36+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6200.5 | 75 | 0 | — |
| document_discovery | completed | 6200.6 | 75 | 0 | — |
| document_download | completed | 40691.0 | 42 | 0 | — |
| extraction | completed | 28.8 | 0 | 5 | — |
| candidate_validation | completed | 13.3 | 0 | 5 | — |
| publish_queue | completed | 13.3 | 0 | 5 | — |
| append_dataset | completed | 22.9 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.4 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
