# Production Trace

**Generated:** 2026-08-20T01:37:08+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260820-F611B6`
**Session ID:** `SES-20260820-44717F`
**Started:** 2026-08-20T01:18:45+00:00
**Finished:** 2026-08-20T01:37:08+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.8 | 0 | 0 | — |
| source_discovery | completed | 2.5 | 0 | 0 | — |
| connector | completed | 6155.0 | 47 | 0 | — |
| document_discovery | completed | 6155.1 | 47 | 0 | — |
| document_download | completed | 354925.2 | 31 | 0 | — |
| extraction | completed | 25.4 | 0 | 5 | — |
| candidate_validation | completed | 13.0 | 0 | 5 | — |
| publish_queue | completed | 13.1 | 0 | 5 | — |
| append_dataset | completed | 14.0 | 0 | 5 | — |
| export | skipped | 0.2 | 0 | 0 | — |
| git_commit | skipped | 0.6 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
