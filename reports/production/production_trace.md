# Production Trace

**Generated:** 2026-08-22T04:52:33+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260822-411E4F`
**Session ID:** `SES-20260822-48EFBE`
**Started:** 2026-08-22T04:34:56+00:00
**Finished:** 2026-08-22T04:52:33+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.7 | 0 | 0 | — |
| source_discovery | completed | 2.2 | 0 | 0 | — |
| connector | completed | 6138.1 | 47 | 0 | — |
| document_discovery | completed | 6138.2 | 47 | 0 | — |
| document_download | completed | 309882.2 | 31 | 0 | — |
| extraction | completed | 51.8 | 0 | 5 | — |
| candidate_validation | completed | 14.0 | 0 | 5 | — |
| publish_queue | completed | 14.0 | 0 | 5 | — |
| append_dataset | completed | 14.5 | 0 | 5 | — |
| export | skipped | 0.2 | 0 | 0 | — |
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
