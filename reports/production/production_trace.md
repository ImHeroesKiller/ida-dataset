# Production Trace

**Generated:** 2026-08-20T07:07:15+00:00
**Mission:** Produce Industry Dataset — expand industry_library toward product target
**Mission ID:** `MIS-20260820-668F7A`
**Session ID:** `SES-20260820-8936FC`
**Started:** 2026-08-20T06:49:34+00:00
**Finished:** 2026-08-20T07:07:15+00:00

## Pipeline timeline

| Stage | Status | Duration (ms) | Docs | Rows | Errors |
|-------|--------|--------------:|-----:|-----:|--------|
| mission | completed | 1.0 | 0 | 0 | — |
| source_discovery | completed | 3.1 | 0 | 0 | — |
| connector | completed | 6190.8 | 45 | 0 | — |
| document_discovery | completed | 6190.9 | 45 | 0 | — |
| document_download | completed | 307752.3 | 31 | 0 | — |
| extraction | completed | 32.7 | 0 | 5 | — |
| candidate_validation | completed | 15.3 | 0 | 5 | — |
| publish_queue | completed | 15.3 | 0 | 5 | — |
| append_dataset | completed | 17.8 | 0 | 5 | — |
| export | skipped | 0.3 | 0 | 0 | — |
| git_commit | skipped | 0.3 | 0 | 0 | — |
| push | skipped | 0.3 | 0 | 0 | — |

## Summary

- Documents discovered: **11**
- Documents downloaded: **31**
- Candidates extracted: **5**
- Candidates validated: **5**
- Candidates rejected: **0**
- Rows published: **5**
- Duplicates: **0**
