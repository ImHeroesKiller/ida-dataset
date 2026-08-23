# Production Trace

**Generated:** 2026-08-23T04:57:00+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260823-F12803`
**Session ID:** `SES-20260823-50A9C8`
**Started:** 2026-08-23T04:39:21+00:00
**Finished:** 2026-08-23T04:57:00+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.8 | 0 | 0 | — |
| source_discovery | completed | 2.5 | 0 | 0 | — |
| connector | completed | 6229.4 | 77 | 0 | — |
| document_discovery | completed | 6229.5 | 77 | 0 | — |
| document_download | completed | 310059.9 | 42 | 0 | — |
| extraction | completed | 30.1 | 0 | 5 | — |
| candidate_validation | completed | 18.5 | 0 | 5 | — |
| publish_queue | completed | 18.5 | 0 | 5 | — |
| append_dataset | completed | 13.4 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **42**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
