# Production Trace

**Generated:** 2026-08-15T12:49:47+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260815-743B9B`
**Session ID:** `SES-20260815-F41A5D`
**Started:** 2026-08-15T12:40:08+00:00
**Finished:** 2026-08-15T12:49:47+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.7 | 0 | 0 | — |
| connector | completed | 6216.3 | 73 | 0 | — |
| document_discovery | completed | 6216.4 | 73 | 0 | — |
| document_download | completed | 50864.7 | 42 | 0 | — |
| extraction | completed | 26.3 | 0 | 5 | — |
| candidate_validation | completed | 9.1 | 0 | 5 | — |
| publish_queue | completed | 9.1 | 0 | 5 | — |
| append_dataset | completed | 23.3 | 0 | 5 | — |
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
