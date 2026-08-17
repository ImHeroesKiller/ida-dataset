# Production Trace

**Generated:** 2026-08-17T03:15:40+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260817-C3EF76`
**Session ID:** `SES-20260817-FAACD3`
**Started:** 2026-08-17T03:01:37+00:00
**Finished:** 2026-08-17T03:15:40+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6227.6 | 77 | 0 | — |
| document_discovery | completed | 6227.7 | 77 | 0 | — |
| document_download | completed | 103984.2 | 42 | 0 | — |
| extraction | completed | 28.5 | 0 | 5 | — |
| candidate_validation | completed | 11.2 | 0 | 5 | — |
| publish_queue | completed | 11.2 | 0 | 5 | — |
| append_dataset | completed | 23.1 | 0 | 5 | — |
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
