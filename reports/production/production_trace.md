# Production Trace

**Generated:** 2026-08-18T09:45:12+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260818-99A1C3`
**Session ID:** `SES-20260818-1E0714`
**Started:** 2026-08-18T09:35:51+00:00
**Finished:** 2026-08-18T09:45:12+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.3 | 0 | 0 | — |
| connector | completed | 6164.3 | 73 | 0 | — |
| document_discovery | completed | 6164.4 | 73 | 0 | — |
| document_download | completed | 41733.7 | 42 | 0 | — |
| extraction | completed | 34.9 | 0 | 5 | — |
| candidate_validation | completed | 15.0 | 0 | 5 | — |
| publish_queue | completed | 15.0 | 0 | 5 | — |
| append_dataset | completed | 25.3 | 0 | 5 | — |
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
