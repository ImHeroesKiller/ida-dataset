# Production Trace

**Generated:** 2026-08-15T15:31:54+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260815-36C9CE`
**Session ID:** `SES-20260815-8EBD2A`
**Started:** 2026-08-15T15:22:27+00:00
**Finished:** 2026-08-15T15:31:54+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.2 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6214.7 | 73 | 0 | — |
| document_discovery | completed | 6214.8 | 73 | 0 | — |
| document_download | completed | 45665.4 | 42 | 0 | — |
| extraction | completed | 26.2 | 0 | 5 | — |
| candidate_validation | completed | 9.0 | 0 | 5 | — |
| publish_queue | completed | 9.1 | 0 | 5 | — |
| append_dataset | completed | 23.2 | 0 | 5 | — |
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
