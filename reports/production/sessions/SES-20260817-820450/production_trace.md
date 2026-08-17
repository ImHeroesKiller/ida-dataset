# Production Trace

**Generated:** 2026-08-17T04:57:02+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260817-482CEF`
**Session ID:** `SES-20260817-820450`
**Started:** 2026-08-17T04:43:22+00:00
**Finished:** 2026-08-17T04:57:02+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 2.7 | 0 | 0 | — |
| connector | completed | 6239.2 | 77 | 0 | — |
| document_discovery | completed | 6239.3 | 77 | 0 | — |
| document_download | completed | 84446.8 | 42 | 0 | — |
| extraction | completed | 26.6 | 0 | 5 | — |
| candidate_validation | completed | 9.5 | 0 | 5 | — |
| publish_queue | completed | 9.5 | 0 | 5 | — |
| append_dataset | completed | 15.1 | 0 | 5 | — |
| export | skipped | 0.4 | 0 | 0 | — |
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
