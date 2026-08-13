# Production Trace

**Generated:** 2026-08-13T12:02:14+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260813-583473`
**Session ID:** `SES-20260813-1730EE`
**Started:** 2026-08-13T11:49:00+00:00
**Finished:** 2026-08-13T12:02:14+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.1 | 0 | 0 | — |
| source_discovery | completed | 3.2 | 0 | 0 | — |
| connector | completed | 6237.1 | 74 | 0 | — |
| document_discovery | completed | 6237.2 | 74 | 0 | — |
| document_download | completed | 38831.5 | 42 | 0 | — |
| extraction | completed | 25.8 | 0 | 5 | — |
| candidate_validation | completed | 7.0 | 0 | 5 | — |
| publish_queue | completed | 7.0 | 0 | 5 | — |
| append_dataset | completed | 24.1 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
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
