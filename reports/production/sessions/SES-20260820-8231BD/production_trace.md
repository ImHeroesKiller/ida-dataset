# Production Trace

**Generated:** 2026-08-20T23:45:12+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260820-B4BAC5`
**Session ID:** `SES-20260820-8231BD`
**Started:** 2026-08-20T23:27:08+00:00
**Finished:** 2026-08-20T23:45:12+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.6 | 0 | 0 | — |
| source_discovery | completed | 54.6 | 0 | 0 | — |
| connector | completed | 6222.1 | 47 | 0 | — |
| document_discovery | completed | 6222.2 | 47 | 0 | — |
| document_download | completed | 334039.4 | 31 | 0 | — |
| extraction | completed | 27.4 | 0 | 5 | — |
| candidate_validation | completed | 80.5 | 0 | 5 | — |
| publish_queue | completed | 85.8 | 0 | 5 | — |
| append_dataset | completed | 12.0 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
