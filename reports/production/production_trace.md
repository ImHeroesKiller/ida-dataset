# Production Trace

**Generated:** 2026-08-17T09:57:13+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260817-514E77`
**Session ID:** `SES-20260817-D36273`
**Started:** 2026-08-17T09:43:26+00:00
**Finished:** 2026-08-17T09:57:13+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6194.5 | 77 | 0 | — |
| document_discovery | completed | 6194.6 | 77 | 0 | — |
| document_download | completed | 76058.7 | 42 | 0 | — |
| extraction | completed | 29.1 | 0 | 5 | — |
| candidate_validation | completed | 11.6 | 0 | 5 | — |
| publish_queue | completed | 11.7 | 0 | 5 | — |
| append_dataset | completed | 23.8 | 0 | 5 | — |
| export | skipped | 1.2 | 0 | 0 | — |
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
