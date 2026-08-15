# Production Trace

**Generated:** 2026-08-15T14:33:58+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260815-0E8B10`
**Session ID:** `SES-20260815-D5C99B`
**Started:** 2026-08-15T14:24:26+00:00
**Finished:** 2026-08-15T14:33:58+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.6 | 0 | 0 | — |
| source_discovery | completed | 2.2 | 0 | 0 | — |
| connector | completed | 6157.6 | 53 | 0 | — |
| document_discovery | completed | 6157.7 | 53 | 0 | — |
| document_download | completed | 43373.2 | 34 | 0 | — |
| extraction | completed | 19.7 | 0 | 5 | — |
| candidate_validation | completed | 5.7 | 0 | 5 | — |
| publish_queue | completed | 5.7 | 0 | 5 | — |
| append_dataset | completed | 10.9 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **34**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
