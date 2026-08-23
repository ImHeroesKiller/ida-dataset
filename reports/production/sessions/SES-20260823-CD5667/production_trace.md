# Production Trace

**Generated:** 2026-08-23T09:47:44+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260823-0DB2AD`
**Session ID:** `SES-20260823-CD5667`
**Started:** 2026-08-23T09:30:09+00:00
**Finished:** 2026-08-23T09:47:44+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6214.9 | 47 | 0 | — |
| document_discovery | completed | 6215.1 | 47 | 0 | — |
| document_download | completed | 308216.9 | 31 | 0 | — |
| extraction | completed | 38.0 | 0 | 5 | — |
| candidate_validation | completed | 22.9 | 0 | 5 | — |
| publish_queue | completed | 23.0 | 0 | 5 | — |
| append_dataset | completed | 18.7 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
