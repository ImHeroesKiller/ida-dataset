# Production Trace

**Generated:** 2026-08-23T22:41:28+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260823-36FE53`
**Session ID:** `SES-20260823-0FAB01`
**Started:** 2026-08-23T22:23:55+00:00
**Finished:** 2026-08-23T22:41:28+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6192.0 | 47 | 0 | — |
| document_discovery | completed | 6192.1 | 47 | 0 | — |
| document_download | completed | 304190.2 | 31 | 0 | — |
| extraction | completed | 37.8 | 0 | 5 | — |
| candidate_validation | completed | 19.7 | 0 | 5 | — |
| publish_queue | completed | 19.7 | 0 | 5 | — |
| append_dataset | completed | 18.9 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.7 | 0 | 0 | — |
| push | skipped | 0.4 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
