# Production Trace

**Generated:** 2026-08-19T18:56:49+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260819-87F27E`
**Session ID:** `SES-20260819-E8C6A0`
**Started:** 2026-08-19T18:38:57+00:00
**Finished:** 2026-08-19T18:56:49+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.8 | 0 | 0 | — |
| source_discovery | completed | 3.0 | 0 | 0 | — |
| connector | completed | 6219.3 | 73 | 0 | — |
| document_discovery | completed | 6219.3 | 73 | 0 | — |
| document_download | completed | 320453.9 | 42 | 0 | — |
| extraction | completed | 32.5 | 0 | 5 | — |
| candidate_validation | completed | 15.8 | 0 | 5 | — |
| publish_queue | completed | 15.8 | 0 | 5 | — |
| append_dataset | completed | 23.5 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
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
