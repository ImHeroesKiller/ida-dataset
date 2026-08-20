# Production Trace

**Generated:** 2026-08-20T14:07:34+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260820-3A137E`
**Session ID:** `SES-20260820-35DADC`
**Started:** 2026-08-20T13:49:20+00:00
**Finished:** 2026-08-20T14:07:34+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.1 | 0 | 0 | — |
| connector | completed | 6431.2 | 75 | 0 | — |
| document_discovery | completed | 6431.4 | 75 | 0 | — |
| document_download | completed | 339061.2 | 42 | 0 | — |
| extraction | completed | 34.1 | 0 | 5 | — |
| candidate_validation | completed | 16.0 | 0 | 5 | — |
| publish_queue | completed | 16.0 | 0 | 5 | — |
| append_dataset | completed | 23.9 | 0 | 5 | — |
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
