# Production Trace

**Generated:** 2026-08-18T14:46:24+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260818-B1A1BA`
**Session ID:** `SES-20260818-205FD5`
**Started:** 2026-08-18T14:36:05+00:00
**Finished:** 2026-08-18T14:46:24+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6196.7 | 53 | 0 | — |
| document_discovery | completed | 6196.9 | 53 | 0 | — |
| document_download | completed | 66670.3 | 34 | 0 | — |
| extraction | completed | 30.6 | 0 | 5 | — |
| candidate_validation | completed | 13.2 | 0 | 5 | — |
| publish_queue | completed | 13.2 | 0 | 5 | — |
| append_dataset | completed | 19.0 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **34**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
