# Production Trace

**Generated:** 2026-08-21T14:05:03+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260821-E08005`
**Session ID:** `SES-20260821-A4AC3C`
**Started:** 2026-08-21T13:47:19+00:00
**Finished:** 2026-08-21T14:05:03+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.2 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6149.0 | 75 | 0 | — |
| document_discovery | completed | 6149.1 | 75 | 0 | — |
| document_download | completed | 314065.2 | 42 | 0 | — |
| extraction | completed | 35.2 | 0 | 5 | — |
| candidate_validation | completed | 17.1 | 0 | 5 | — |
| publish_queue | completed | 17.1 | 0 | 5 | — |
| append_dataset | completed | 23.7 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
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
