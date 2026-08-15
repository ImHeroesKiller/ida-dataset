# Production Trace

**Generated:** 2026-08-15T01:32:19+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260815-1A427F`
**Session ID:** `SES-20260815-2F8C44`
**Started:** 2026-08-15T01:19:06+00:00
**Finished:** 2026-08-15T01:32:19+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.7 | 0 | 0 | — |
| connector | completed | 6233.0 | 77 | 0 | — |
| document_discovery | completed | 6233.2 | 77 | 0 | — |
| document_download | completed | 53501.5 | 42 | 0 | — |
| extraction | completed | 25.2 | 0 | 5 | — |
| candidate_validation | completed | 8.6 | 0 | 5 | — |
| publish_queue | completed | 8.6 | 0 | 5 | — |
| append_dataset | completed | 23.1 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.5 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
