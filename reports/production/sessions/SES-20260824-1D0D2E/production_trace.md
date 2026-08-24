# Production Trace

**Generated:** 2026-08-24T14:11:49+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260824-0373F8`
**Session ID:** `SES-20260824-1D0D2E`
**Started:** 2026-08-24T13:53:54+00:00
**Finished:** 2026-08-24T14:11:49+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6201.9 | 77 | 0 | — |
| document_discovery | completed | 6202.0 | 77 | 0 | — |
| document_download | completed | 319841.7 | 42 | 0 | — |
| extraction | completed | 39.9 | 0 | 5 | — |
| candidate_validation | completed | 20.5 | 0 | 5 | — |
| publish_queue | completed | 20.5 | 0 | 5 | — |
| append_dataset | completed | 23.6 | 0 | 5 | — |
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
