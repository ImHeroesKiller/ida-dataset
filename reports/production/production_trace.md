# Production Trace

**Generated:** 2026-08-18T20:37:52+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260818-A96426`
**Session ID:** `SES-20260818-82D07C`
**Started:** 2026-08-18T20:26:34+00:00
**Finished:** 2026-08-18T20:37:52+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.8 | 0 | 0 | — |
| source_discovery | completed | 2.3 | 0 | 0 | — |
| connector | completed | 6137.5 | 23 | 0 | — |
| document_discovery | completed | 6137.6 | 23 | 0 | — |
| document_download | completed | 35361.2 | 11 | 0 | — |
| extraction | completed | 22.5 | 0 | 5 | — |
| candidate_validation | completed | 10.5 | 0 | 5 | — |
| publish_queue | completed | 10.4 | 0 | 5 | — |
| append_dataset | completed | 7.8 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
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
