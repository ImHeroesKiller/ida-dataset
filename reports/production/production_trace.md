# Production Trace

**Generated:** 2026-08-18T16:43:27+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260818-F4C198`
**Session ID:** `SES-20260818-4BB8D5`
**Started:** 2026-08-18T16:34:02+00:00
**Finished:** 2026-08-18T16:43:27+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6223.5 | 53 | 0 | — |
| document_discovery | completed | 6223.6 | 53 | 0 | — |
| document_download | completed | 35493.8 | 34 | 0 | — |
| extraction | completed | 30.4 | 0 | 5 | — |
| candidate_validation | completed | 13.2 | 0 | 5 | — |
| publish_queue | completed | 13.2 | 0 | 5 | — |
| append_dataset | completed | 19.7 | 0 | 5 | — |
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
