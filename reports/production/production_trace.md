# Production Trace

**Generated:** 2026-08-21T16:55:21+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260821-137340`
**Session ID:** `SES-20260821-7F3319`
**Started:** 2026-08-21T16:36:37+00:00
**Finished:** 2026-08-21T16:55:21+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.5 | 0 | 0 | — |
| connector | completed | 6239.9 | 75 | 0 | — |
| document_discovery | completed | 6240.0 | 75 | 0 | — |
| document_download | completed | 366687.5 | 42 | 0 | — |
| extraction | completed | 31.2 | 0 | 5 | — |
| candidate_validation | completed | 13.5 | 0 | 5 | — |
| publish_queue | completed | 13.5 | 0 | 5 | — |
| append_dataset | completed | 17.0 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
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
