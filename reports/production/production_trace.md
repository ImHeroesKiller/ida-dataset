# Production Trace

**Generated:** 2026-08-14T20:04:28+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260814-022E70`
**Session ID:** `SES-20260814-2C3B90`
**Started:** 2026-08-14T19:50:30+00:00
**Finished:** 2026-08-14T20:04:28+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.9 | 0 | 0 | — |
| source_discovery | completed | 2.9 | 0 | 0 | — |
| connector | completed | 6160.8 | 77 | 0 | — |
| document_discovery | completed | 6161.0 | 77 | 0 | — |
| document_download | completed | 93897.2 | 42 | 0 | — |
| extraction | completed | 25.5 | 0 | 5 | — |
| candidate_validation | completed | 20.1 | 0 | 5 | — |
| publish_queue | completed | 20.1 | 0 | 5 | — |
| append_dataset | completed | 23.6 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.4 | 0 | 0 | — |
| push | skipped | 0.4 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
