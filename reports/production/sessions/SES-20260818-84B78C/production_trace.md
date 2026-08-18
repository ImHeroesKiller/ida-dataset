# Production Trace

**Generated:** 2026-08-18T21:37:11+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260818-4C4B89`
**Session ID:** `SES-20260818-84B78C`
**Started:** 2026-08-18T21:27:13+00:00
**Finished:** 2026-08-18T21:37:11+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.8 | 0 | 0 | — |
| source_discovery | completed | 2.6 | 0 | 0 | — |
| connector | completed | 6289.7 | 23 | 0 | — |
| document_discovery | completed | 6290.5 | 23 | 0 | — |
| document_download | completed | 35481.4 | 11 | 0 | — |
| extraction | completed | 25.2 | 0 | 5 | — |
| candidate_validation | completed | 14.9 | 0 | 5 | — |
| publish_queue | completed | 14.9 | 0 | 5 | — |
| append_dataset | completed | 7.9 | 0 | 5 | — |
| export | skipped | 0.2 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **11**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
