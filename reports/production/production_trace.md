# Production Trace

**Generated:** 2026-08-22T07:00:25+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260822-131A31`
**Session ID:** `SES-20260822-F94F64`
**Started:** 2026-08-22T06:42:27+00:00
**Finished:** 2026-08-22T07:00:25+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.8 | 0 | 0 | — |
| connector | completed | 6205.7 | 73 | 0 | — |
| document_discovery | completed | 6206.0 | 73 | 0 | — |
| document_download | completed | 323536.5 | 42 | 0 | — |
| extraction | completed | 35.2 | 0 | 5 | — |
| candidate_validation | completed | 15.5 | 0 | 5 | — |
| publish_queue | completed | 15.5 | 0 | 5 | — |
| append_dataset | completed | 15.7 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
