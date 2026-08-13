# Production Trace

**Generated:** 2026-08-13T08:36:06+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260813-656EC6`
**Session ID:** `SES-20260813-3F9DFD`
**Started:** 2026-08-13T08:22:34+00:00
**Finished:** 2026-08-13T08:36:06+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6201.8 | 75 | 0 | — |
| document_discovery | completed | 6202.0 | 75 | 0 | — |
| document_download | completed | 37970.0 | 42 | 0 | — |
| extraction | completed | 24.6 | 0 | 5 | — |
| candidate_validation | completed | 10.5 | 0 | 5 | — |
| publish_queue | completed | 10.5 | 0 | 5 | — |
| append_dataset | completed | 23.8 | 0 | 5 | — |
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
