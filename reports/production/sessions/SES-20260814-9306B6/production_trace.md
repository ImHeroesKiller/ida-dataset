# Production Trace

**Generated:** 2026-08-14T16:07:46+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260814-E2281A`
**Session ID:** `SES-20260814-9306B6`
**Started:** 2026-08-14T15:54:01+00:00
**Finished:** 2026-08-14T16:07:46+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6206.6 | 25 | 0 | — |
| document_discovery | completed | 6206.7 | 25 | 0 | — |
| document_download | completed | 70280.4 | 11 | 0 | — |
| extraction | completed | 22.3 | 0 | 5 | — |
| candidate_validation | completed | 7.6 | 0 | 5 | — |
| publish_queue | completed | 7.6 | 0 | 5 | — |
| append_dataset | completed | 10.1 | 0 | 5 | — |
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
