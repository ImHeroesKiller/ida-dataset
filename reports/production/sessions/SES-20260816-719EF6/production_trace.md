# Production Trace

**Generated:** 2026-08-16T08:45:51+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260816-CD4093`
**Session ID:** `SES-20260816-719EF6`
**Started:** 2026-08-16T08:31:47+00:00
**Finished:** 2026-08-16T08:45:51+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.5 | 0 | 0 | — |
| connector | completed | 6177.3 | 27 | 0 | — |
| document_discovery | completed | 6177.5 | 27 | 0 | — |
| document_download | completed | 99693.5 | 11 | 0 | — |
| extraction | completed | 22.6 | 0 | 5 | — |
| candidate_validation | completed | 7.7 | 0 | 5 | — |
| publish_queue | completed | 7.8 | 0 | 5 | — |
| append_dataset | completed | 8.0 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **11**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
