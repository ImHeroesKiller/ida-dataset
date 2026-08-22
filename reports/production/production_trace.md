# Production Trace

**Generated:** 2026-08-22T01:36:10+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260822-3B3992`
**Session ID:** `SES-20260822-C93B2F`
**Started:** 2026-08-22T01:18:01+00:00
**Finished:** 2026-08-22T01:36:10+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.5 | 0 | 0 | — |
| source_discovery | completed | 1.9 | 0 | 0 | — |
| connector | completed | 6259.4 | 45 | 0 | — |
| document_discovery | completed | 6259.5 | 45 | 0 | — |
| document_download | completed | 335883.1 | 31 | 0 | — |
| extraction | completed | 225.9 | 0 | 5 | — |
| candidate_validation | completed | 9.9 | 0 | 5 | — |
| publish_queue | completed | 10.1 | 0 | 5 | — |
| append_dataset | completed | 9.2 | 0 | 5 | — |
| export | skipped | 0.5 | 0 | 0 | — |
| git_commit | skipped | 0.4 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
