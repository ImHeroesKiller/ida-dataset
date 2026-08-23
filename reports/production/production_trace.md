# Production Trace

**Generated:** 2026-08-23T07:01:31+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260823-73A055`
**Session ID:** `SES-20260823-45F9D3`
**Started:** 2026-08-23T06:42:57+00:00
**Finished:** 2026-08-23T07:01:31+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 0.7 | 0 | 0 | — |
| source_discovery | completed | 2.3 | 0 | 0 | — |
| connector | completed | 6160.4 | 43 | 0 | — |
| document_discovery | completed | 6160.5 | 43 | 0 | — |
| document_download | completed | 361425.1 | 31 | 0 | — |
| extraction | completed | 28.5 | 0 | 5 | — |
| candidate_validation | completed | 15.0 | 0 | 5 | — |
| publish_queue | completed | 15.1 | 0 | 5 | — |
| append_dataset | completed | 13.8 | 0 | 5 | — |
| export | skipped | 0.2 | 0 | 0 | — |
| git_commit | skipped | 0.2 | 0 | 0 | — |
| push | skipped | 0.2 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
